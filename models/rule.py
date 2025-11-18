from dataclasses import dataclass
from typing import Any

@dataclass
class Rule:
    name: str
    target: str  # 'function', 'class', 'variable', 'import'
    condition: Any  # AST node dari condition	
    severity: str  # 'error', 'warning', 'info'
    message: str
    
    def __repr__(self):
        return f"Rule({self.name}, target={self.target}, severity={self.severity})"
