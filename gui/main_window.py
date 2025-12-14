import sys
import os
import json
from pathlib import Path
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFileDialog, QListWidget, QTableWidget,
    QTableWidgetItem, QTabWidget, QTextEdit, QComboBox, QCheckBox,
    QProgressBar, QMessageBox, QSplitter, QHeaderView, QLineEdit,
    QDialog, QDialogButtonBox, QAbstractItemView, QListWidgetItem, QMenu
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QTimer, QSettings, QSize, QPoint
from PyQt6.QtGui import QFont, QColor, QTextCharFormat, QSyntaxHighlighter, QKeySequence, QShortcut, QAction, QPainter

from gui.styles import Styles
from gui.session_manager import SessionManager
from analyzer.dsl_parser import parse_dsl_file
from analyzer.java_analyzer import analyze_java_file
from analyzer.rule_evaluator import RuleEvaluator


class ToggleSwitch(QCheckBox):
    """Custom toggle switch widget"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(50, 24)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Colors
        if self.isChecked():
            bg_color = QColor("#2196F3")  # Blue when on
            circle_color = QColor("#FFFFFF")
        else:
            bg_color = QColor("#CCCCCC")  # Gray when off
            circle_color = QColor("#FFFFFF")
        
        # Draw background rounded rectangle
        painter.setBrush(bg_color)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(0, 0, 50, 24, 12, 12)
        
        # Draw circle
        circle_x = 28 if self.isChecked() else 2
        painter.setBrush(circle_color)
        painter.drawEllipse(circle_x, 2, 20, 20)


class AnalysisWorker(QThread):
    """Background worker for code analysis"""
    progress = pyqtSignal(str, int, int)  # file, current, total
    finished = pyqtSignal(list)  # violations
    error = pyqtSignal(str)  # error message
    
    def __init__(self, files, rules_file):
        super().__init__()
        self.files = files
        self.rules_file = rules_file
        self.is_running = True
        self._is_cancelled = False
    
    def run(self):
        try:
            # Load rules
            rules = parse_dsl_file(self.rules_file)
            all_violations = []
            
            # Analyze each file
            for i, file_path in enumerate(self.files):
                if not self.is_running or self._is_cancelled:
                    break
                
                self.progress.emit(file_path, i + 1, len(self.files))
                
                # Check file exists
                if not os.path.exists(file_path):
                    continue
                
                # Analyze file
                metrics = analyze_java_file(file_path)
                evaluator = RuleEvaluator(rules, metrics)
                violations = evaluator.evaluate_all()
                
                # Add file path to violations
                for violation in violations:
                    violation['file'] = file_path
                
                all_violations.extend(violations)
            
            if not self._is_cancelled:
                self.finished.emit(all_violations)
        
        except Exception as e:
            self.error.emit(str(e))
    
    def stop(self):
        """Stop the analysis"""
        self.is_running = False
        self._is_cancelled = True


class JavaSyntaxHighlighter(QSyntaxHighlighter):
    """Simple Java syntax highlighter"""
    
    def __init__(self, parent, theme='light'):
        super().__init__(parent)
        self.theme = theme
        self.setup_formats()
    
    def setup_formats(self):
        # Define colors based on theme
        if self.theme == 'light':
            keyword_color = QColor('#0000FF')
            string_color = QColor('#A31515')
            comment_color = QColor('#008000')
            number_color = QColor('#098658')
        else:
            keyword_color = QColor('#569CD6')
            string_color = QColor('#CE9178')
            comment_color = QColor('#6A9955')
            number_color = QColor('#B5CEA8')
        
        # Keyword format
        self.keyword_format = QTextCharFormat()
        self.keyword_format.setForeground(keyword_color)
        self.keyword_format.setFontWeight(QFont.Weight.Bold)
        
        # String format
        self.string_format = QTextCharFormat()
        self.string_format.setForeground(string_color)
        
        # Comment format
        self.comment_format = QTextCharFormat()
        self.comment_format.setForeground(comment_color)
        
        # Number format
        self.number_format = QTextCharFormat()
        self.number_format.setForeground(number_color)
        
        # Keywords
        self.keywords = [
            'abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch',
            'char', 'class', 'const', 'continue', 'default', 'do', 'double',
            'else', 'enum', 'extends', 'final', 'finally', 'float', 'for',
            'goto', 'if', 'implements', 'import', 'instanceof', 'int',
            'interface', 'long', 'native', 'new', 'package', 'private',
            'protected', 'public', 'return', 'short', 'static', 'strictfp',
            'super', 'switch', 'synchronized', 'this', 'throw', 'throws',
            'transient', 'try', 'void', 'volatile', 'while'
        ]
    
    def highlightBlock(self, text):
        # Highlight keywords
        for keyword in self.keywords:
            index = text.find(keyword)
            while index >= 0:
                # Check if it's a whole word
                if (index == 0 or not text[index-1].isalnum()) and \
                   (index + len(keyword) >= len(text) or not text[index + len(keyword)].isalnum()):
                    self.setFormat(index, len(keyword), self.keyword_format)
                index = text.find(keyword, index + 1)
        
        # Highlight strings
        string_index = text.find('"')
        while string_index >= 0:
            end_index = text.find('"', string_index + 1)
            if end_index == -1:
                length = len(text) - string_index
            else:
                length = end_index - string_index + 1
            self.setFormat(string_index, length, self.string_format)
            string_index = text.find('"', string_index + length)
        
        # Highlight single-line comments
        comment_index = text.find('//')
        if comment_index >= 0:
            self.setFormat(comment_index, len(text) - comment_index, self.comment_format)


class SessionDialog(QDialog):
    """Dialog for creating/loading sessions"""
    
    def __init__(self, session_manager, parent=None):
        super().__init__(parent)
        self.session_manager = session_manager
        self.selected_session = None
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Session Manager")
        self.setMinimumWidth(400)
        
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Manage Sessions")
        title.setProperty("class", "title")
        layout.addWidget(title)
        
        # Session list
        layout.addWidget(QLabel("Existing Sessions:"))
        self.session_list = QListWidget()
        self.refresh_sessions()
        self.session_list.itemDoubleClicked.connect(self.load_selected)
        layout.addWidget(self.session_list)
        
        # New session
        layout.addWidget(QLabel("Create New Session:"))
        self.new_session_input = QLineEdit()
        self.new_session_input.setPlaceholderText("Enter session name...")
        layout.addWidget(self.new_session_input)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        load_btn = QPushButton("Load")
        load_btn.clicked.connect(self.load_selected)
        button_layout.addWidget(load_btn)
        
        create_btn = QPushButton("Create")
        create_btn.clicked.connect(self.create_new)
        button_layout.addWidget(create_btn)
        
        delete_btn = QPushButton("Delete")
        delete_btn.setProperty("class", "danger")
        delete_btn.clicked.connect(self.delete_selected)
        button_layout.addWidget(delete_btn)
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setProperty("class", "secondary")
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def refresh_sessions(self):
        self.session_list.clear()
        sessions = self.session_manager.list_sessions()
        self.session_list.addItems(sessions)
    
    def load_selected(self):
        current_item = self.session_list.currentItem()
        if current_item:
            self.selected_session = current_item.text()
            self.accept()
    
    def create_new(self):
        name = self.new_session_input.text().strip()
        if name:
            self.selected_session = name
            self.accept()
    
    def delete_selected(self):
        current_item = self.session_list.currentItem()
        if current_item:
            reply = QMessageBox.question(
                self, "Confirm Delete",
                f"Delete session '{current_item.text()}'?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.Yes:
                self.session_manager.delete_session(current_item.text())
                self.refresh_sessions()


class MainWindow(QMainWindow):
    """Main GUI window"""
    
    def __init__(self):
        super().__init__()
        self.session_manager = SessionManager()
        self.current_session = None
        self.violations = []
        self.worker = None
        self.current_rules_file = ""
        
        # Settings for window state
        self.settings = QSettings("QualityCodeChecker", "MainWindow")
        
        # Undo/Redo stack for file operations
        self.undo_stack = []
        self.redo_stack = []
        
        # Detect system theme
        self.current_theme = self.detect_system_theme()
        
        self.init_ui()
        self.setup_shortcuts()
        self.auto_load_default_rules()
        self.restore_window_state()
        self.load_settings()
        self.apply_theme()
    
    def init_ui(self):
        self.setWindowTitle("Quality Code Checker")
        self.setMinimumSize(1200, 800)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Top bar (Session, Theme Toggle, Actions)
        top_bar = self.create_top_bar()
        main_layout.addLayout(top_bar)
        
        # Main content (Splitter with tabs and results)
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setChildrenCollapsible(False)  # Prevent collapsing panels
        
        # Left panel - Configuration tabs
        left_tabs = self.create_left_panel()
        left_tabs.setMinimumWidth(500)
        splitter.addWidget(left_tabs)
        
        # Right panel - Results and Preview
        right_tabs = self.create_right_panel()
        splitter.addWidget(right_tabs)
        
        # Set initial sizes - more space for file list
        splitter.setSizes([550, 650])
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 1)
        main_layout.addWidget(splitter)
        
        # Bottom bar (Progress and Summary)
        bottom_bar = self.create_bottom_bar()
        main_layout.addLayout(bottom_bar)
        
        # Status bar
        self.statusBar().showMessage("Ready")
    
    def create_top_bar(self):
        layout = QHBoxLayout()
        
        # Session controls
        session_btn = QPushButton("📁 Manage Sessions")
        session_btn.setToolTip("Create, load, or delete sessions")
        session_btn.clicked.connect(self.manage_sessions)
        layout.addWidget(session_btn)
        
        # Recent sessions dropdown
        self.recent_sessions_combo = QComboBox()
        self.recent_sessions_combo.setPlaceholderText("Recent Sessions")
        self.recent_sessions_combo.setMinimumWidth(150)
        self.recent_sessions_combo.activated.connect(self.load_recent_session)
        self.refresh_recent_sessions()
        layout.addWidget(self.recent_sessions_combo)
        
        self.save_session_btn = QPushButton("💾 Save Session")
        self.save_session_btn.setToolTip("Save current work to session")
        self.save_session_btn.clicked.connect(self.save_current_session)
        layout.addWidget(self.save_session_btn)
        
        self.session_label = QLabel("No session - click 'Save Session' to create one")
        self.session_label.setProperty("class", "subtitle")
        layout.addWidget(self.session_label)
        
        layout.addStretch()
        
        # Theme toggle with synced text
        theme_container = QHBoxLayout()
        self.theme_text_label = QLabel("☀️ Light Mode")
        theme_container.addWidget(self.theme_text_label)
        
        self.theme_toggle = ToggleSwitch()
        self.theme_toggle.setChecked(self.current_theme == 'dark')
        self.theme_toggle.setToolTip("Toggle theme (defaults to Windows system theme)")
        self.theme_toggle.stateChanged.connect(self.toggle_theme)
        theme_container.addWidget(self.theme_toggle)
        
        # Update text on startup
        self.update_theme_text()
        
        layout.addLayout(theme_container)
        
        return layout
    
    def create_left_panel(self):
        tabs = QTabWidget()
        
        # Files tab
        files_tab = QWidget()
        files_layout = QVBoxLayout(files_tab)
        
        files_layout.addWidget(QLabel("Java Files to Analyze:"))
        
        # Search bar for file list
        self.file_search = QLineEdit()
        self.file_search.setPlaceholderText("🔍 Search files...")
        self.file_search.textChanged.connect(self.filter_file_list)
        files_layout.addWidget(self.file_search)
        
        file_buttons = QHBoxLayout()
        add_file_btn = QPushButton("+ File")
        add_file_btn.clicked.connect(self.add_files)
        file_buttons.addWidget(add_file_btn)
        
        add_folder_btn = QPushButton("+ Folder")
        add_folder_btn.clicked.connect(self.add_folder)
        file_buttons.addWidget(add_folder_btn)
        
        remove_btn = QPushButton("- Remove")
        remove_btn.setProperty("class", "danger")
        remove_btn.clicked.connect(self.remove_selected_files)
        file_buttons.addWidget(remove_btn)
        
        remove_all_btn = QPushButton("🗑 Remove All")
        remove_all_btn.setProperty("class", "danger")
        remove_all_btn.clicked.connect(self.remove_all_files)
        file_buttons.addWidget(remove_all_btn)
        
        files_layout.addLayout(file_buttons)
        
        # Select/Deselect buttons
        select_buttons = QHBoxLayout()
        select_all_btn = QPushButton("☑ Select All")
        select_all_btn.clicked.connect(self.select_all_files)
        select_buttons.addWidget(select_all_btn)
        
        deselect_all_btn = QPushButton("☐ Deselect All")
        deselect_all_btn.clicked.connect(self.deselect_all_files)
        select_buttons.addWidget(deselect_all_btn)
        
        refresh_btn = QPushButton("🔄 Check Changes")
        refresh_btn.setToolTip("Check which files changed since last scan")
        refresh_btn.clicked.connect(self.check_file_changes)
        select_buttons.addWidget(refresh_btn)
        
        files_layout.addLayout(select_buttons)
        
        self.file_list = QListWidget()
        self.file_list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.file_list.itemDoubleClicked.connect(self.preview_file)  # Double-click preview
        self.file_list.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.file_list.customContextMenuRequested.connect(self.show_file_context_menu)
        self.file_list.setAcceptDrops(True)  # Enable drag-drop
        self.file_list.dragEnterEvent = self.file_list_drag_enter
        self.file_list.dropEvent = self.file_list_drop
        files_layout.addWidget(self.file_list)
        
        self.file_status_label = QLabel("Add files to start (checked files will be analyzed)")
        self.file_status_label.setProperty("class", "subtitle")
        files_layout.addWidget(self.file_status_label)
        
        files_layout.addWidget(QLabel("Exclude Extensions:"))
        self.exclude_ext_input = QLineEdit()
        self.exclude_ext_input.setPlaceholderText(".txt, .md, .xml")
        self.exclude_ext_input.setText(".txt, .md, .xml, .properties, .gradle")
        files_layout.addWidget(self.exclude_ext_input)
        
        files_layout.addWidget(QLabel("Exclude Folder Names:"))
        self.exclude_folder_input = QLineEdit()
        self.exclude_folder_input.setPlaceholderText("target, build, .git")
        self.exclude_folder_input.setText("target, build, .git, .idea, node_modules")
        files_layout.addWidget(self.exclude_folder_input)
        
        files_layout.addWidget(QLabel("Exclude File Patterns:"))
        self.exclude_file_pattern = QLineEdit()
        self.exclude_file_pattern.setPlaceholderText("*Test.java, *IT.java")
        files_layout.addWidget(self.exclude_file_pattern)
        
        apply_exclusions_btn = QPushButton("🔄 Apply Exclusions to Current Files")
        apply_exclusions_btn.setToolTip("Remove files matching exclusion patterns from the list")
        apply_exclusions_btn.clicked.connect(self.apply_exclusions_to_existing)
        files_layout.addWidget(apply_exclusions_btn)
        
        exclude_specific_layout = QHBoxLayout()
        files_layout.addWidget(QLabel("Exclude Specific Paths:"))
        
        self.excluded_paths_list = QListWidget()
        self.excluded_paths_list.setMaximumHeight(80)
        exclude_specific_layout.addWidget(self.excluded_paths_list)
        
        exclude_btn_layout = QVBoxLayout()
        add_exclude_file_btn = QPushButton("+ File")
        add_exclude_file_btn.clicked.connect(self.add_exclude_file)
        exclude_btn_layout.addWidget(add_exclude_file_btn)
        
        add_exclude_folder_btn = QPushButton("+ Folder")
        add_exclude_folder_btn.clicked.connect(self.add_exclude_folder)
        exclude_btn_layout.addWidget(add_exclude_folder_btn)
        
        remove_exclude_btn = QPushButton("- Remove")
        remove_exclude_btn.clicked.connect(self.remove_exclude_path)
        exclude_btn_layout.addWidget(remove_exclude_btn)
        
        exclude_specific_layout.addLayout(exclude_btn_layout)
        files_layout.addLayout(exclude_specific_layout)
        
        tabs.addTab(files_tab, "Files")
        
        # Rules tab
        rules_tab = QWidget()
        rules_layout = QVBoxLayout(rules_tab)
        
        rules_layout.addWidget(QLabel("DSL Rules Configuration:"))
        
        rules_btn_layout = QHBoxLayout()
        load_rules_btn = QPushButton("Load Rules File")
        load_rules_btn.clicked.connect(self.load_rules_file)
        rules_btn_layout.addWidget(load_rules_btn)
        
        save_rules_btn = QPushButton("Save Rules As...")
        save_rules_btn.setToolTip("Save rules to a new file")
        save_rules_btn.clicked.connect(self.save_rules_file)
        rules_btn_layout.addWidget(save_rules_btn)
        
        save_editor_btn = QPushButton("💾 Save Rule Editor")
        save_editor_btn.setToolTip("Save current editor content to loaded file")
        save_editor_btn.clicked.connect(self.save_rule_editor)
        rules_btn_layout.addWidget(save_editor_btn)
        
        rules_layout.addLayout(rules_btn_layout)
        
        self.rules_path_label = QLabel("No rules file loaded")
        self.rules_path_label.setProperty("class", "subtitle")
        rules_layout.addWidget(self.rules_path_label)
        
        rules_layout.addWidget(QLabel("Rules Editor:"))
        self.rules_editor = QTextEdit()
        self.rules_editor.setPlaceholderText("Load a DSL rules file or write rules here...")
        self.rules_editor.setFont(QFont("Consolas", 10))
        rules_layout.addWidget(self.rules_editor)
        
        tabs.addTab(rules_tab, "Rules")
        
        return tabs
    
    def create_right_panel(self):
        tabs = QTabWidget()
        
        # Results tab
        results_tab = QWidget()
        results_layout = QVBoxLayout(results_tab)
        
        # Filter controls
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel("Filter:"))
        
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["All", "Errors", "Warnings", "Info"])
        self.filter_combo.currentTextChanged.connect(self.filter_results)
        filter_layout.addWidget(self.filter_combo)
        
        filter_layout.addStretch()
        
        # Search in results
        self.result_search = QLineEdit()
        self.result_search.setPlaceholderText("🔍 Search results...")
        self.result_search.textChanged.connect(self.filter_results)
        filter_layout.addWidget(self.result_search)
        
        # Analyze and Cancel buttons
        self.analyze_btn = QPushButton("▶ Analyze")
        self.analyze_btn.clicked.connect(self.start_analysis)
        self.analyze_btn.setMinimumWidth(100)
        filter_layout.addWidget(self.analyze_btn)
        
        self.cancel_btn = QPushButton("⏸ Cancel")
        self.cancel_btn.clicked.connect(self.cancel_analysis)
        self.cancel_btn.setMinimumWidth(100)
        self.cancel_btn.setVisible(False)  # Hidden by default
        filter_layout.addWidget(self.cancel_btn)
        
        # Export buttons
        export_csv_btn = QPushButton("Export CSV")
        export_csv_btn.clicked.connect(lambda: self.export_results('csv'))
        filter_layout.addWidget(export_csv_btn)
        
        export_html_btn = QPushButton("Export HTML")
        export_html_btn.clicked.connect(lambda: self.export_results('html'))
        filter_layout.addWidget(export_html_btn)
        
        results_layout.addLayout(filter_layout)
        
        # Results table
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(6)
        self.results_table.setHorizontalHeaderLabels([
            "Severity", "Rule", "File", "Line", "Element", "Message"
        ])
        self.results_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        self.results_table.horizontalHeader().setStretchLastSection(True)
        self.results_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.results_table.itemSelectionChanged.connect(self.on_result_selected)
        results_layout.addWidget(self.results_table)
        
        tabs.addTab(results_tab, "Results")
        
        # Code Preview tab
        preview_tab = QWidget()
        preview_layout = QVBoxLayout(preview_tab)
        
        preview_layout.addWidget(QLabel("Source Code Preview:"))
        
        self.preview_path_label = QLabel("Select a violation to preview code")
        self.preview_path_label.setProperty("class", "subtitle")
        preview_layout.addWidget(self.preview_path_label)
        
        self.code_preview = QTextEdit()
        self.code_preview.setReadOnly(True)
        self.code_preview.setFont(QFont("Consolas", 10))
        self.code_preview.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        preview_layout.addWidget(self.code_preview)
        
        tabs.addTab(preview_tab, "Code Preview")
        
        return tabs
    
    def create_bottom_bar(self):
        layout = QHBoxLayout()
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar, 2)
        
        self.progress_label = QLabel("")
        self.progress_label.setVisible(False)
        layout.addWidget(self.progress_label, 1)
        
        # Summary
        self.summary_label = QLabel("Ready to analyze")
        layout.addWidget(self.summary_label, 1)
        
        self.error_label = QLabel("0 Errors")
        self.error_label.setProperty("severity", "error")
        layout.addWidget(self.error_label)
        
        self.warning_label = QLabel("0 Warnings")
        self.warning_label.setProperty("severity", "warning")
        layout.addWidget(self.warning_label)
        
        self.info_label = QLabel("0 Info")
        self.info_label.setProperty("severity", "info")
        layout.addWidget(self.info_label)
        
        return layout
    
    def toggle_theme(self):
        """Toggle between light and dark theme"""
        self.current_theme = 'dark' if self.theme_toggle.isChecked() else 'light'
        self.update_theme_text()
        self.apply_theme()
    
    def update_theme_text(self):
        """Update theme text label to match current theme"""
        if self.current_theme == 'dark':
            self.theme_text_label.setText("🌙 Dark Mode")
        else:
            self.theme_text_label.setText("☀️ Light Mode")
    
    def apply_theme(self):
        stylesheet = Styles.get_stylesheet(self.current_theme)
        self.setStyleSheet(stylesheet)
        
        # Update syntax highlighter if code preview has content
        if hasattr(self, 'code_preview'):
            self.syntax_highlighter = JavaSyntaxHighlighter(
                self.code_preview.document(), 
                self.current_theme
            )
    
    def manage_sessions(self):
        """
        Session workflow:
        - User can create new session or load existing
        - New session starts empty or with current files/rules
        - Loading session restores files, rules, and last results
        - All changes auto-save if session exists
        """
        dialog = SessionDialog(self.session_manager, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            session_name = dialog.selected_session
            
            if not session_name:
                return
            
            # Try to load existing session
            session = self.session_manager.load_session(session_name)
            
            if session:
                self.load_session(session)
            else:
                # Create new empty session
                files = [self.file_list.item(i).text() for i in range(self.file_list.count())]
                rules_file = self.current_session.get('rules_file', '') if self.current_session else ''
                
                self.current_session = self.session_manager.create_session(
                    name=session_name,
                    rules_file=rules_file,
                    files=files
                )
                self.session_manager.save_session(self.current_session)
                self.session_label.setText(f"Session: {session_name}")
                self.statusBar().showMessage(f"Created new session: {session_name}")
    
    def save_current_session(self):
        if self.current_session:
            self.update_session_data()
            self.session_manager.save_session(self.current_session)
            self.statusBar().showMessage(f"Session '{self.current_session['name']}' saved")
            QMessageBox.information(self, "Session Saved", 
                f"Session '{self.current_session['name']}' saved successfully!")
        else:
            # No session exists, prompt to create one
            name, ok = self._prompt_session_name()
            if ok and name:
                files = [self.file_list.item(i).text() for i in range(self.file_list.count())]
                
                self.current_session = self.session_manager.create_session(
                    name=name,
                    rules_file="",
                    files=files
                )
                self.update_session_data()
                self.session_manager.save_session(self.current_session)
                self.session_label.setText(f"Session: {name}")
                self.statusBar().showMessage(f"Created and saved session: {name}")
                QMessageBox.information(self, "Session Created", 
                    f"Session '{name}' created and saved!")
    
    def update_session_data(self):
        """Update current session with GUI state"""
        if not self.current_session:
            return
        
        # Update files list
        files = []
        for i in range(self.file_list.count()):
            file_path = self.file_list.item(i).text()
            
            # Remove status prefix if exists
            clean_path = file_path
            if clean_path.startswith(("✓ ", "⚠ ", "⚪ ")):
                clean_path = clean_path[2:]
            
            # Check if file already in session
            existing_file = next((f for f in self.current_session.get('files', []) 
                                if f['path'] == clean_path), None)
            if existing_file:
                files.append(existing_file)
            else:
                files.append({
                    "path": clean_path,
                    "hash": self.session_manager._get_file_hash(clean_path),
                    "last_scanned": None
                })
        
        self.current_session['files'] = files
        self.current_session['rules_file'] = getattr(self, 'current_rules_file', '')
        self.current_session['last_results'] = self.violations
    
    def _prompt_session_name(self):
        """Prompt user to enter session name"""
        from PyQt6.QtWidgets import QInputDialog
        return QInputDialog.getText(
            self, "Create Session", 
            "Enter session name:",
            QLineEdit.EchoMode.Normal
        )
    
    def load_session(self, session):
        self.current_session = session
        self.session_label.setText(f"Session: {session['name']}")
        
        # Load files
        self.file_list.clear()
        for file_info in session.get('files', []):
            self.file_list.addItem(file_info['path'])
        
        # Load rules
        rules_file = session.get('rules_file', '')
        self.current_rules_file = rules_file
        if rules_file and os.path.exists(rules_file):
            with open(rules_file, 'r', encoding='utf-8') as f:
                self.rules_editor.setPlainText(f.read())
            self.rules_path_label.setText(f"Loaded: {rules_file}")
        else:
            self.rules_editor.clear()
            self.rules_path_label.setText("No rules file loaded")
        
        # Load last results
        if session.get('last_results'):
            self.violations = session['last_results']
            self.display_results()
        
        # Check file changes
        self.check_file_changes()
        
        self.statusBar().showMessage(f"Loaded session: {session['name']}")
    
    def check_file_changes(self):
        """Check which files changed since last scan and update UI"""
        if not self.current_session:
            self.file_status_label.setText("No session - cannot track changes")
            return
        
        changed_files = self.session_manager.get_changed_files(self.current_session)
        total_files = self.file_list.count()
        
        if total_files == 0:
            self.file_status_label.setText("No files in session")
            return
        
        # Update file list display with status indicators
        for i in range(self.file_list.count()):
            item = self.file_list.item(i)
            file_path = item.text()
            
            # Remove any existing status prefix
            clean_path = file_path
            if clean_path.startswith("✓ ") or clean_path.startswith("⚠ ") or clean_path.startswith("⚪ "):
                clean_path = clean_path[2:]
            
            if clean_path in changed_files:
                item.setText(f"⚠ {clean_path}")
                item.setForeground(QColor("#FF9800"))  # Orange for changed
            else:
                # Check if file was ever scanned
                file_info = next((f for f in self.current_session.get('files', []) 
                                if f['path'] == clean_path), None)
                if file_info and file_info.get('last_scanned'):
                    item.setText(f"✓ {clean_path}")
                    item.setForeground(QColor("#4CAF50"))  # Green for unchanged
                else:
                    item.setText(f"⚪ {clean_path}")
                    item.setForeground(QColor("#757575"))  # Gray for not scanned
        
        # Update status label
        changed_count = len(changed_files)
        if changed_count > 0:
            self.file_status_label.setText(f"⚠ {changed_count} of {total_files} files changed since last scan")
        else:
            scanned_files = [f for f in self.current_session.get('files', []) 
                           if f.get('last_scanned')]
            if len(scanned_files) == total_files:
                self.file_status_label.setText(f"✓ All {total_files} files up to date")
            else:
                self.file_status_label.setText(f"⚪ {total_files - len(scanned_files)} files not yet scanned")
    
    def add_files(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Select Java Files", "", "Java Files (*.java)"
        )
        
        if files:
            self.add_files_to_list(files)
            self.statusBar().showMessage(f"Added {len(files)} file(s)")
    
    def add_exclude_file(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Select Files to Exclude", "", "All Files (*.*)"
        )
        
        for file in files:
            if file not in [self.excluded_paths_list.item(i).text() 
                          for i in range(self.excluded_paths_list.count())]:
                self.excluded_paths_list.addItem(file)
    
    def add_exclude_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder to Exclude")
        
        if folder:
            if folder not in [self.excluded_paths_list.item(i).text() 
                            for i in range(self.excluded_paths_list.count())]:
                self.excluded_paths_list.addItem(folder)
    
    def remove_exclude_path(self):
        for item in self.excluded_paths_list.selectedItems():
            self.excluded_paths_list.takeItem(self.excluded_paths_list.row(item))
    
    def add_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        
        if folder:
            # Get exclude patterns
            exclude_exts = [ext.strip() for ext in self.exclude_ext_input.text().split(',')]
            exclude_folder_names = [f.strip() for f in self.exclude_folder_input.text().split(',')]
            exclude_patterns = [p.strip() for p in self.exclude_file_pattern.text().split(',') if p.strip()]
            
            # Find all Java files
            excluded_paths = [self.excluded_paths_list.item(i).text() 
            for i in range(self.excluded_paths_list.count())]
            
            java_files = []
            for root, dirs, files in os.walk(folder):
                dirs[:] = [d for d in dirs if d not in exclude_folder_names]
                
                if root in excluded_paths:
                    continue
                
                skip_folder = False
                for excluded_path in excluded_paths:
                    if os.path.isdir(excluded_path) and root.startswith(excluded_path):
                        skip_folder = True
                        break
                
                if skip_folder:
                    continue
                
                for file in files:
                    if file.endswith('.java'):
                        file_path = os.path.join(root, file)
                        
                        if file_path in excluded_paths:
                            continue
                        
                        skip = False
                        
                        if any(file.endswith(ext) for ext in exclude_exts):
                            skip = True
                        
                        for pattern in exclude_patterns:
                            if pattern.startswith('*') and file.endswith(pattern[1:]):
                                skip = True
                            elif pattern.endswith('*') and file.startswith(pattern[:-1]):
                                skip = True
                            elif pattern in file:
                                skip = True
                        
                        if not skip:
                            java_files.append(file_path)
            
            added = 0
            for file in java_files:
                # Check if file already exists (remove status prefix for comparison)
                existing_files = []
                for i in range(self.file_list.count()):
                    item_text = self.file_list.item(i).text()
                    clean_text = item_text[2:] if item_text.startswith(("✓ ", "⚠ ", "⚪ ")) else item_text
                    existing_files.append(clean_text)
                
                if file not in existing_files:
                    item = QListWidgetItem(file)
                    item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
                    item.setCheckState(Qt.CheckState.Checked)  # Checked by default
                    self.file_list.addItem(item)
                    added += 1
            
            # Auto-save to session if exists
            if self.current_session:
                self.update_session_data()
                self.session_manager.save_session(self.current_session)
                self.check_file_changes()
            
            self.statusBar().showMessage(f"Added {added} file(s) from folder")
    
    def remove_selected_files(self):
        if not self.file_list.selectedItems():
            return
        
        self.save_undo_state()
        
        for item in self.file_list.selectedItems():
            self.file_list.takeItem(self.file_list.row(item))
        
        self.update_file_count_display()
        
        # Auto-save to session if exists
        if self.current_session:
            self.update_session_data()
            self.session_manager.save_session(self.current_session)
            self.check_file_changes()
    
    def load_rules_file(self):
        file, _ = QFileDialog.getOpenFileName(
            self, "Select DSL Rules File", "", "DSL Files (*.dsl);;All Files (*.*)"
        )
        
        if file:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.rules_editor.setPlainText(content)
            self.rules_path_label.setText(f"Loaded: {file}")
            self.current_rules_file = file
            
            # Auto-save to session if exists
            if self.current_session:
                self.current_session['rules_file'] = file
                self.session_manager.save_session(self.current_session)
    
    def save_rules_file(self):
        file, _ = QFileDialog.getSaveFileName(
            self, "Save DSL Rules File", "", "DSL Files (*.dsl)"
        )
        
        if file:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(self.rules_editor.toPlainText())
            
            self.rules_path_label.setText(f"Saved: {file}")
            self.statusBar().showMessage(f"Rules saved to {file}")
    
    def start_analysis(self):
        # Validate inputs
        if self.file_list.count() == 0:
            QMessageBox.warning(self, "No Files", "Please add Java files to analyze")
            return
        
        if not self.rules_editor.toPlainText().strip():
            QMessageBox.warning(self, "No Rules", "Please load or write DSL rules")
            return
        
        # Validate DSL syntax
        temp_rules = "temp_rules.dsl"
        try:
            with open(temp_rules, 'w', encoding='utf-8') as f:
                f.write(self.rules_editor.toPlainText())
            
            # Try to parse rules to validate syntax
            parse_dsl_file(temp_rules)
        except Exception as e:
            QMessageBox.critical(
                self, "Invalid DSL Syntax", 
                f"DSL rules contain syntax errors:\n\n{str(e)}\n\nPlease fix the rules before analyzing."
            )
            return
        
        # Get checked files to analyze
        files = []
        for i in range(self.file_list.count()):
            item = self.file_list.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                item_text = item.text()
                # Remove status prefix if exists
                clean_path = item_text[2:] if item_text.startswith(("✓ ", "⚠ ", "⚪ ")) else item_text
                
                # Check file exists
                if not os.path.exists(clean_path):
                    reply = QMessageBox.question(
                        self, "File Not Found",
                        f"File does not exist:\n{clean_path}\n\nRemove from list?",
                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                    )
                    if reply == QMessageBox.StandardButton.Yes:
                        self.file_list.takeItem(i)
                    continue
                
                files.append(clean_path)
        
        if len(files) == 0:
            QMessageBox.warning(self, "No Files Selected", "Please check at least one file to analyze")
            return
        
        # Check for changed files if session exists (smart re-scan)
        if self.current_session:
            changed_files = self.session_manager.get_changed_files(self.current_session)
            if changed_files and len(changed_files) < len(files):
                reply = QMessageBox.question(
                    self, "Smart Re-scan",
                    f"{len(changed_files)} of {len(files)} files changed.\n"
                    "Analyze only changed files?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                )
                if reply == QMessageBox.StandardButton.Yes:
                    files = changed_files
        
        # Start analysis
        self.analyze_btn.setEnabled(False)
        self.cancel_btn.setVisible(True)
        self.progress_bar.setVisible(True)
        self.progress_label.setVisible(True)
        self.progress_bar.setValue(0)
        
        self.worker = AnalysisWorker(files, temp_rules)
        self.worker.progress.connect(self.on_progress)
        self.worker.finished.connect(self.on_analysis_finished)
        self.worker.error.connect(self.on_analysis_error)
        self.worker.start()
    
    def on_progress(self, file, current, total):
        progress = int((current / total) * 100)
        self.progress_bar.setValue(progress)
        self.progress_label.setText(f"Analyzing {current}/{total}: {os.path.basename(file)}")
    
    def on_analysis_finished(self, violations):
        self.violations = violations
        self.display_results()
        
        # Update file hashes
        if self.current_session:
            for i in range(self.file_list.count()):
                item = self.file_list.item(i)
                if item.checkState() == Qt.CheckState.Checked:
                    item_text = item.text()
                    # Remove status prefix
                    clean_path = item_text[2:] if item_text.startswith(("✓ ", "⚠ ", "⚪ ")) else item_text
                    self.session_manager.update_file_hash(self.current_session, clean_path)
            
            self.session_manager.save_results(self.current_session, violations)
            self.check_file_changes()
        
        self.progress_bar.setVisible(False)
        self.progress_label.setVisible(False)
        self.analyze_btn.setEnabled(True)
        self.cancel_btn.setVisible(False)
        self.update_file_count_display()
        self.statusBar().showMessage(f"Analysis complete: {len(violations)} violations found")
    
    def on_analysis_error(self, error):
        QMessageBox.critical(self, "Analysis Error", f"Error during analysis:\n{error}")
        self.progress_bar.setVisible(False)
        self.progress_label.setVisible(False)
        self.analyze_btn.setEnabled(True)
        self.cancel_btn.setVisible(False)
        self.statusBar().showMessage("Analysis failed")
    
    def display_results(self):
        self.results_table.setRowCount(0)
        
        # Count by severity
        errors = sum(1 for v in self.violations if v['severity'] == 'error')
        warnings = sum(1 for v in self.violations if v['severity'] == 'warning')
        infos = sum(1 for v in self.violations if v['severity'] == 'info')
        
        # Update summary
        total_files = self.file_list.count()
        self.summary_label.setText(f"Analyzed {total_files} files - {len(self.violations)} violations")
        self.error_label.setText(f"{errors} Errors")
        self.warning_label.setText(f"{warnings} Warnings")
        self.info_label.setText(f"{infos} Info")
        
        # Filter violations by severity
        filter_text = self.filter_combo.currentText()
        filtered_violations = self.violations
        
        if filter_text != "All":
            severity_map = {"Errors": "error", "Warnings": "warning", "Info": "info"}
            filtered_violations = [
                v for v in self.violations 
                if v['severity'] == severity_map.get(filter_text, "")
            ]
        
        # Filter by search text
        search_text = self.result_search.text().lower()
        if search_text:
            filtered_violations = [
                v for v in filtered_violations
                if search_text in v['rule'].lower() or 
                   search_text in v['message'].lower() or
                   search_text in v['name'].lower() or
                   search_text in os.path.basename(v['file']).lower()
            ]
        
        # Display in table
        for violation in filtered_violations:
            row = self.results_table.rowCount()
            self.results_table.insertRow(row)
            
            # Severity
            severity_item = QTableWidgetItem(violation['severity'].upper())
            color = Styles.get_severity_color(violation['severity'], self.current_theme)
            severity_item.setForeground(QColor(color))
            self.results_table.setItem(row, 0, severity_item)
            
            # Rule
            self.results_table.setItem(row, 1, QTableWidgetItem(violation['rule']))
            
            # File (basename only)
            file_name = os.path.basename(violation['file'])
            self.results_table.setItem(row, 2, QTableWidgetItem(file_name))
            
            # Line
            self.results_table.setItem(row, 3, QTableWidgetItem(str(violation['line'])))
            
            # Element name
            self.results_table.setItem(row, 4, QTableWidgetItem(violation['name']))
            
            # Message
            self.results_table.setItem(row, 5, QTableWidgetItem(violation['message']))
        
        self.results_table.resizeColumnsToContents()
    
    def filter_results(self):
        self.display_results()
    
    def on_result_selected(self):
        selected = self.results_table.selectedItems()
        if not selected:
            return
        
        row = selected[0].row()
        
        # Get file and line
        file_name = self.results_table.item(row, 2).text()
        line_num = int(self.results_table.item(row, 3).text())
        
        # Find full file path
        file_path = None
        for v in self.violations:
            if os.path.basename(v['file']) == file_name:
                file_path = v['file']
                break
        
        if file_path and os.path.exists(file_path):
            self.show_code_preview(file_path, line_num)
    
    def show_code_preview(self, file_path, line_num):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Show context (10 lines before and after)
            start = max(0, line_num - 11)
            end = min(len(lines), line_num + 10)
            
            preview_text = ""
            for i in range(start, end):
                prefix = ">>> " if i == line_num - 1 else "    "
                preview_text += f"{prefix}{i+1:4d} | {lines[i]}"
            
            self.code_preview.setPlainText(preview_text)
            self.preview_path_label.setText(f"File: {file_path} (Line {line_num})")
            
            # Re-apply syntax highlighting
            self.syntax_highlighter = JavaSyntaxHighlighter(
                self.code_preview.document(), 
                self.current_theme
            )
        
        except Exception as e:
            self.code_preview.setPlainText(f"Error loading file: {e}")
    
    def export_results(self, format_type):
        if not self.violations:
            QMessageBox.warning(self, "No Results", "Run analysis first")
            return
        
        if format_type == 'csv':
            self.export_csv()
        elif format_type == 'html':
            self.export_html()
    
    def export_csv(self):
        file, _ = QFileDialog.getSaveFileName(
            self, "Export to CSV", "quality_report.csv", "CSV Files (*.csv)"
        )
        
        if file:
            import csv
            with open(file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Severity', 'Rule', 'File', 'Line', 'Element', 'Message'])
                
                for v in self.violations:
                    writer.writerow([
                        v['severity'],
                        v['rule'],
                        v['file'],
                        v['line'],
                        v['name'],
                        v['message']
                    ])
            
            self.statusBar().showMessage(f"Exported to {file}")
            QMessageBox.information(self, "Export Complete", f"Results exported to:\n{file}")
    
    def export_html(self):
        from gui.html_report import generate_html_report
        
        file = "quality_report.html"
        generate_html_report(self.violations, file)
        
        # Open in localhost
        import webbrowser
        import threading
        import http.server
        import socketserver
        
        PORT = 8000
        Handler = http.server.SimpleHTTPRequestHandler
        
        def start_server():
            with socketserver.TCPServer(("", PORT), Handler) as httpd:
                httpd.serve_forever()
        
        # Start server in background
        server_thread = threading.Thread(target=start_server, daemon=True)
        server_thread.start()
        
        # Open browser
        webbrowser.open(f"http://localhost:{PORT}/{file}")
        
        QMessageBox.information(
            self, "HTML Report",
            f"Report generated and opened in browser\nLocal server: http://localhost:{PORT}/{file}"
        )
    
    def update_theme_toggle_text(self):
        """Update theme toggle text with checkmark"""
        if self.theme_toggle.isChecked():
            self.theme_toggle.setText("✓ Enabled")
        else:
            self.theme_toggle.setText("Disabled")
    
    def auto_load_default_rules(self):
        """Auto-load examples/rules.dsl if exists"""
        default_rules = "examples/rules.dsl"
        if os.path.exists(default_rules):
            try:
                with open(default_rules, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.rules_editor.setPlainText(content)
                self.rules_path_label.setText(f"Auto-loaded: {default_rules}")
                self.current_rules_file = default_rules
            except Exception as e:
                pass
    
    def remove_all_files(self):
        """Remove all files from the list"""
        if self.file_list.count() == 0:
            return
        
        reply = QMessageBox.question(
            self, "Confirm Remove All",
            f"Remove all {self.file_list.count()} files?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.save_undo_state()
            self.file_list.clear()
            self.update_file_count_display()
            
            # Auto-save to session if exists
            if self.current_session:
                self.update_session_data()
                self.session_manager.save_session(self.current_session)
                self.check_file_changes()
            
            self.statusBar().showMessage("All files removed")
    
    def apply_exclusions_to_existing(self):
        """Apply exclusion patterns to already-added files"""
        if self.file_list.count() == 0:
            QMessageBox.information(self, "No Files", "No files in the list to filter")
            return
        
        # Get exclusion patterns
        exclude_exts = [ext.strip() for ext in self.exclude_ext_input.text().split(',') if ext.strip()]
        exclude_folders = [folder.strip() for folder in self.exclude_folder_input.text().split(',') if folder.strip()]
        exclude_patterns = [pat.strip() for pat in self.exclude_file_pattern.text().split(',') if pat.strip()]
        
        # Get specific excluded paths
        excluded_paths = []
        for i in range(self.excluded_paths_list.count()):
            excluded_paths.append(self.excluded_paths_list.item(i).text())
        
        # Check each file
        files_to_remove = []
        for i in range(self.file_list.count()):
            item_text = self.file_list.item(i).text()
            # Remove status prefix
            file_path = item_text[2:] if item_text.startswith(("✓ ", "⚠ ", "⚪ ")) else item_text
            file_name = os.path.basename(file_path)
            
            # Check if should be excluded
            should_exclude = False
            
            # Check specific paths
            if file_path in excluded_paths:
                should_exclude = True
            
            # Check extensions
            if any(file_name.endswith(ext) for ext in exclude_exts):
                should_exclude = True
            
            # Check folder names
            for folder in exclude_folders:
                if folder in file_path.split(os.sep):
                    should_exclude = True
                    break
            
            # Check patterns
            for pattern in exclude_patterns:
                if pattern.startswith('*') and file_name.endswith(pattern[1:]):
                    should_exclude = True
                elif pattern.endswith('*') and file_name.startswith(pattern[:-1]):
                    should_exclude = True
                elif pattern in file_name:
                    should_exclude = True
            
            if should_exclude:
                files_to_remove.append(i)
        
        # Remove files (in reverse order to maintain indices)
        removed_count = 0
        for i in reversed(files_to_remove):
            self.file_list.takeItem(i)
            removed_count += 1
        
        # Auto-save to session if exists
        if self.current_session:
            self.update_session_data()
            self.session_manager.save_session(self.current_session)
            self.check_file_changes()
        
        if removed_count > 0:
            self.statusBar().showMessage(f"Removed {removed_count} file(s) matching exclusion patterns")
            QMessageBox.information(
                self, "Exclusions Applied",
                f"Removed {removed_count} file(s) matching exclusion patterns"
            )
        else:
            self.statusBar().showMessage("No files matched exclusion patterns")
            QMessageBox.information(self, "Exclusions Applied", "No files matched exclusion patterns")
    
    def detect_system_theme(self):
        """Detect system dark/light mode (Windows 10/11)"""
        try:
            import winreg
            registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            key = winreg.OpenKey(registry, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
            value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
            winreg.CloseKey(key)
            return 'light' if value == 1 else 'dark'
        except:
            return 'light'  # Default to light
    
    def setup_shortcuts(self):
        """Setup keyboard shortcuts"""
        # Ctrl+A - Select all files
        QShortcut(QKeySequence("Ctrl+A"), self, self.select_all_files)
        
        # Delete - Remove selected files
        QShortcut(QKeySequence("Delete"), self, self.remove_selected_files)
        
        # F5 - Refresh/Check changes
        QShortcut(QKeySequence("F5"), self, self.check_file_changes)
        
        # Ctrl+S - Save session
        QShortcut(QKeySequence("Ctrl+S"), self, self.save_current_session)
        
        # Ctrl+O - Open/Manage sessions
        QShortcut(QKeySequence("Ctrl+O"), self, self.manage_sessions)
        
        # Ctrl+Z - Undo
        QShortcut(QKeySequence("Ctrl+Z"), self, self.undo_operation)
        
        # Ctrl+Y - Redo
        QShortcut(QKeySequence("Ctrl+Y"), self, self.redo_operation)
    
    def save_rule_editor(self):
        """Save current rule editor content to the loaded file"""
        if not self.current_rules_file:
            QMessageBox.warning(
                self, "No File Loaded",
                "Please load a rules file first, or use 'Save Rules As...' to create a new file"
            )
            return
        
        try:
            with open(self.current_rules_file, 'w', encoding='utf-8') as f:
                f.write(self.rules_editor.toPlainText())
            
            self.statusBar().showMessage(f"Saved to {self.current_rules_file}")
            QMessageBox.information(self, "Saved", f"Rules saved to:\n{self.current_rules_file}")
        except Exception as e:
            QMessageBox.critical(self, "Save Error", f"Failed to save:\n{str(e)}")
    
    def select_all_files(self):
        """Check all files in the list"""
        for i in range(self.file_list.count()):
            item = self.file_list.item(i)
            item.setCheckState(Qt.CheckState.Checked)
        self.update_file_count_display()
    
    def deselect_all_files(self):
        """Uncheck all files in the list"""
        for i in range(self.file_list.count()):
            item = self.file_list.item(i)
            item.setCheckState(Qt.CheckState.Unchecked)
        self.update_file_count_display()
    
    def cancel_analysis(self):
        """Cancel running analysis"""
        if self.worker and self.worker.isRunning():
            self.worker.stop()
            self.worker.wait()
            self.analyze_btn.setEnabled(True)
            self.cancel_btn.setVisible(False)
            self.progress_bar.setVisible(False)
            self.progress_label.setVisible(False)
            self.statusBar().showMessage("Analysis cancelled")
            QMessageBox.information(self, "Cancelled", "Analysis was cancelled")
    
    def filter_file_list(self):
        """Filter file list based on search text"""
        search_text = self.file_search.text().lower()
        
        for i in range(self.file_list.count()):
            item = self.file_list.item(i)
            item_text = item.text().lower()
            # Remove status prefix for search
            if item_text.startswith("✓ ") or item_text.startswith("⚠ ") or item_text.startswith("⚪ "):
                item_text = item_text[2:]
            
            # Show/hide based on match
            if search_text in item_text:
                item.setHidden(False)
            else:
                item.setHidden(True)
    
    def preview_file(self, item):
        """Preview file content when double-clicked"""
        file_path = item.text()
        # Remove status prefix
        if file_path.startswith(("✓ ", "⚠ ", "⚪ ")):
            file_path = file_path[2:]
        
        if not os.path.exists(file_path):
            QMessageBox.warning(self, "File Not Found", f"File does not exist:\n{file_path}")
            return
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.code_preview.setPlainText(content)
            self.preview_path_label.setText(f"Preview: {file_path}")
            self.syntax_highlighter = JavaSyntaxHighlighter(self.code_preview.document(), self.current_theme)
            self.statusBar().showMessage(f"Loaded: {os.path.basename(file_path)}")
        except Exception as e:
            QMessageBox.critical(self, "Read Error", f"Failed to read file:\n{str(e)}")
    
    def show_file_context_menu(self, position):
        """Show right-click context menu for file list"""
        item = self.file_list.itemAt(position)
        if not item:
            return
        
        menu = QMenu()
        
        # Check/Uncheck
        if item.checkState() == Qt.CheckState.Checked:
            uncheck_action = menu.addAction("⬜ Uncheck")
            uncheck_action.triggered.connect(lambda: item.setCheckState(Qt.CheckState.Unchecked))
        else:
            check_action = menu.addAction("☑ Check")
            check_action.triggered.connect(lambda: item.setCheckState(Qt.CheckState.Checked))
        
        menu.addSeparator()
        
        # Preview
        preview_action = menu.addAction("👁 Preview Code")
        preview_action.triggered.connect(lambda: self.preview_file(item))
        
        # Open in explorer
        open_folder_action = menu.addAction("📂 Open in Explorer")
        open_folder_action.triggered.connect(lambda: self.open_in_explorer(item))
        
        # Copy path
        copy_path_action = menu.addAction("📋 Copy Path")
        copy_path_action.triggered.connect(lambda: self.copy_file_path(item))
        
        menu.addSeparator()
        
        # Remove
        remove_action = menu.addAction("❌ Remove")
        remove_action.triggered.connect(lambda: self.file_list.takeItem(self.file_list.row(item)))
        
        menu.exec(self.file_list.mapToGlobal(position))
    
    def open_in_explorer(self, item):
        """Open file location in Windows Explorer"""
        file_path = item.text()
        if file_path.startswith(("✓ ", "⚠ ", "⚪ ")):
            file_path = file_path[2:]
        
        if os.path.exists(file_path):
            os.system(f'explorer /select,"{file_path}"')
    
    def copy_file_path(self, item):
        """Copy file path to clipboard"""
        file_path = item.text()
        if file_path.startswith(("✓ ", "⚠ ", "⚪ ")):
            file_path = file_path[2:]
        
        clipboard = QApplication.clipboard()
        clipboard.setText(file_path)
        self.statusBar().showMessage("Path copied to clipboard")
    
    def file_list_drag_enter(self, event):
        """Handle drag enter event"""
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    
    def file_list_drop(self, event):
        """Handle file drop event"""
        files = []
        for url in event.mimeData().urls():
            path = url.toLocalFile()
            if os.path.isfile(path) and path.endswith('.java'):
                files.append(path)
            elif os.path.isdir(path):
                # Add all Java files from directory
                for root, _, file_list in os.walk(path):
                    for file in file_list:
                        if file.endswith('.java'):
                            files.append(os.path.join(root, file))
        
        if files:
            self.add_files_to_list(files)
            self.statusBar().showMessage(f"Added {len(files)} file(s) via drag & drop")
    
    def add_files_to_list(self, files):
        """Add files to list with duplicate check"""
        # Get existing files
        existing_files = []
        for i in range(self.file_list.count()):
            item_text = self.file_list.item(i).text()
            clean_text = item_text[2:] if item_text.startswith(("✓ ", "⚠ ", "⚪ ")) else item_text
            existing_files.append(clean_text)
        
        # Save current state for undo
        self.save_undo_state()
        
        added = 0
        for file in files:
            if file not in existing_files:
                item = QListWidgetItem(file)
                item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
                item.setCheckState(Qt.CheckState.Checked)
                # Add tooltip with full path
                item.setToolTip(file)
                self.file_list.addItem(item)
                added += 1
        
        if added > 0:
            self.update_file_count_display()
            if self.current_session:
                self.update_session_data()
                self.session_manager.save_session(self.current_session)
    
    def update_file_count_display(self):
        """Update status bar with file count"""
        total = self.file_list.count()
        checked = sum(1 for i in range(total) if self.file_list.item(i).checkState() == Qt.CheckState.Checked)
        
        # Count changed files
        changed = 0
        if self.current_session:
            changed_files = self.session_manager.get_changed_files(self.current_session)
            changed = len(changed_files)
        
        if total == 0:
            self.file_status_label.setText("Add files to start")
        else:
            status_text = f"📁 {total} files total | ☑ {checked} checked"
            if changed > 0:
                status_text += f" | ⚠ {changed} changed"
            self.file_status_label.setText(status_text)
    
    def refresh_recent_sessions(self):
        """Refresh recent sessions dropdown"""
        self.recent_sessions_combo.clear()
        sessions = self.session_manager.list_sessions()
        
        # Get last 5 sessions
        recent = sessions[-5:] if len(sessions) > 5 else sessions
        self.recent_sessions_combo.addItems(recent)
    
    def load_recent_session(self):
        """Load selected recent session"""
        session_name = self.recent_sessions_combo.currentText()
        if session_name:
            self.load_session_by_name(session_name)
    
    def load_session_by_name(self, name):
        """Load session by name"""
        try:
            session = self.session_manager.load_session(name)
            if session:
                self.current_session = session
                self.session_label.setText(f"Session: {name}")
                
                # Load files
                self.file_list.clear()
                for file_info in session.get('files', []):
                    file_path = file_info['path']
                    if os.path.exists(file_path):
                        item = QListWidgetItem(file_path)
                        item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
                        item.setCheckState(Qt.CheckState.Checked)
                        item.setToolTip(file_path)
                        self.file_list.addItem(item)
                
                # Load rules if exists
                if session.get('rules_file') and os.path.exists(session['rules_file']):
                    self.load_rules_from_file(session['rules_file'])
                
                # Load file filters
                filters = session.get('file_filters', {})
                self.exclude_ext_input.setText(filters.get('exclude_ext', ''))
                self.exclude_folder_input.setText(filters.get('exclude_folder', ''))
                self.exclude_file_pattern.setText(filters.get('exclude_pattern', ''))
                
                self.check_file_changes()
                self.update_file_count_display()
                self.statusBar().showMessage(f"Loaded session: {name}")
        except Exception as e:
            QMessageBox.critical(self, "Load Error", f"Failed to load session:\n{str(e)}")
    

    
    def save_undo_state(self):
        """Save current state for undo"""
        state = {
            "files": [self.file_list.item(i).text() for i in range(self.file_list.count())]
        }
        self.undo_stack.append(state)
        # Limit undo stack to 20 items
        if len(self.undo_stack) > 20:
            self.undo_stack.pop(0)
        # Clear redo stack when new action is performed
        self.redo_stack.clear()
    
    def undo_operation(self):
        """Undo last file operation"""
        if not self.undo_stack:
            self.statusBar().showMessage("Nothing to undo")
            return
        
        # Save current state to redo
        current_state = {
            "files": [self.file_list.item(i).text() for i in range(self.file_list.count())]
        }
        self.redo_stack.append(current_state)
        
        # Restore previous state
        state = self.undo_stack.pop()
        self.file_list.clear()
        
        for file_path in state["files"]:
            item = QListWidgetItem(file_path)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Checked)
            item.setToolTip(file_path)
            self.file_list.addItem(item)
        
        self.update_file_count_display()
        self.statusBar().showMessage("Undo complete")
    
    def redo_operation(self):
        """Redo last undone operation"""
        if not self.redo_stack:
            self.statusBar().showMessage("Nothing to redo")
            return
        
        # Save current state to undo
        current_state = {
            "files": [self.file_list.item(i).text() for i in range(self.file_list.count())]
        }
        self.undo_stack.append(current_state)
        
        # Restore redo state
        state = self.redo_stack.pop()
        self.file_list.clear()
        
        for file_path in state["files"]:
            item = QListWidgetItem(file_path)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Checked)
            item.setToolTip(file_path)
            self.file_list.addItem(item)
        
        self.update_file_count_display()
        self.statusBar().showMessage("Redo complete")
    
    def restore_window_state(self):
        """Restore window size and position"""
        geometry = self.settings.value("geometry")
        if geometry:
            self.restoreGeometry(geometry)
        else:
            # Default size
            self.resize(1400, 900)
    
    def save_window_state(self):
        """Save window size and position"""
        self.settings.setValue("geometry", self.saveGeometry())
    
    def load_settings(self):
        """Load saved settings"""
        # Load exclude patterns
        exclude_ext = self.settings.value("exclude_extensions")
        if exclude_ext:
            self.exclude_ext_input.setText(exclude_ext)
        
        exclude_folders = self.settings.value("exclude_folders")
        if exclude_folders:
            self.exclude_folder_input.setText(exclude_folders)
        
        exclude_patterns = self.settings.value("exclude_patterns")
        if exclude_patterns:
            self.exclude_file_pattern.setText(exclude_patterns)
    
    def save_settings(self):
        """Save current settings"""
        self.settings.setValue("exclude_extensions", self.exclude_ext_input.text())
        self.settings.setValue("exclude_folders", self.exclude_folder_input.text())
        self.settings.setValue("exclude_patterns", self.exclude_file_pattern.text())
        self.save_window_state()
    
    def closeEvent(self, event):
        """Handle window close - save state"""
        self.save_settings()
        event.accept()
    
    def load_rules_from_file(self, file_path):
        """Helper to load rules from file path"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            self.rules_editor.setPlainText(content)
            self.rules_path_label.setText(f"Loaded: {file_path}")
            self.current_rules_file = file_path
        except Exception as e:
            pass


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Quality Code Checker")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
