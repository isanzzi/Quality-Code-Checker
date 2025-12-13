import json
import os
import hashlib
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional

class SessionManager:
    """Manages analysis sessions with file tracking and auto-save"""
    
    def __init__(self, sessions_dir: str = "sessions"):
        self.sessions_dir = sessions_dir
        os.makedirs(sessions_dir, exist_ok=True)
    
    def create_session(self, name: str, rules_file: str, files: List[str], 
                      file_filters: Dict = None) -> Dict:
        """Create a new session"""
        session = {
            "name": name,
            "created_at": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat(),
            "rules_file": rules_file,
            "files": [],
            "file_filters": file_filters or {},
            "last_results": []
        }
        
        # Add files with their hash for change detection
        for file_path in files:
            if os.path.exists(file_path):
                session["files"].append({
                    "path": file_path,
                    "hash": self._get_file_hash(file_path),
                    "timestamp": os.path.getmtime(file_path),
                    "last_scanned": None
                })
        
        return session
    
    def save_session(self, session: Dict) -> str:
        """Save session to JSON file"""
        session["last_updated"] = datetime.now().isoformat()
        
        session_file = os.path.join(self.sessions_dir, f"{session['name']}.json")
        with open(session_file, 'w', encoding='utf-8') as f:
            json.dump(session, f, indent=2, ensure_ascii=False)
        
        return session_file
    
    def load_session(self, name: str) -> Optional[Dict]:
        """Load session from JSON file"""
        session_file = os.path.join(self.sessions_dir, f"{name}.json")
        
        if not os.path.exists(session_file):
            return None
        
        with open(session_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def list_sessions(self) -> List[str]:
        """List all available sessions"""
        sessions = []
        for file in os.listdir(self.sessions_dir):
            if file.endswith('.json'):
                sessions.append(file[:-5])  # Remove .json extension
        return sorted(sessions)
    
    def delete_session(self, name: str) -> bool:
        """Delete a session"""
        session_file = os.path.join(self.sessions_dir, f"{name}.json")
        if os.path.exists(session_file):
            os.remove(session_file)
            return True
        return False
    
    def get_changed_files(self, session: Dict) -> List[str]:
        """Get list of files that changed since last scan (optimized with timestamp check)"""
        changed_files = []
        
        for file_info in session.get("files", []):
            file_path = file_info["path"]
            
            if not os.path.exists(file_path):
                continue
            
            # Optimization: Check timestamp first (fast)
            stored_timestamp = file_info.get("timestamp")  # May be None for old sessions
            if stored_timestamp is not None:
                current_timestamp = os.path.getmtime(file_path)
                if current_timestamp == stored_timestamp and file_info["last_scanned"] is not None:
                    # Timestamp unchanged = file unchanged (skip expensive hash calculation)
                    continue
            
            # Timestamp changed or not available: Calculate hash (slower but accurate)
            current_hash = self._get_file_hash(file_path)
            
            # File changed or never scanned
            if current_hash != file_info["hash"] or file_info["last_scanned"] is None:
                changed_files.append(file_path)
        
        return changed_files
    
    def update_file_hash(self, session: Dict, file_path: str):
        """Update file hash and timestamp after scanning"""
        for file_info in session.get("files", []):
            if file_info["path"] == file_path:
                file_info["hash"] = self._get_file_hash(file_path)
                if os.path.exists(file_path):
                    file_info["timestamp"] = os.path.getmtime(file_path)
                file_info["last_scanned"] = datetime.now().isoformat()
                break
    
    def add_files_to_session(self, session: Dict, files: List[str]):
        """Add new files to existing session"""
        existing_paths = {f["path"] for f in session.get("files", [])}
        
        for file_path in files:
            if file_path not in existing_paths and os.path.exists(file_path):
                session["files"].append({
                    "path": file_path,
                    "hash": self._get_file_hash(file_path),
                    "timestamp": os.path.getmtime(file_path),
                    "last_scanned": None
                })
    
    def remove_file_from_session(self, session: Dict, file_path: str):
        """Remove file from session"""
        session["files"] = [f for f in session["files"] if f["path"] != file_path]
    
    def save_results(self, session: Dict, results: List[Dict]):
        """Save analysis results to session"""
        session["last_results"] = results
        session["last_analysis"] = datetime.now().isoformat()
        self.save_session(session)
    
    def _get_file_hash(self, file_path: str) -> str:
        """Calculate MD5 hash of file"""
        hasher = hashlib.md5()
        try:
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except Exception:
            return ""
