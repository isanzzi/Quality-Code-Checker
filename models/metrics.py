from dataclasses import dataclass, field
from typing import List

@dataclass
class MethodMetrics: 
    name: str
    line_number: int
    parameter_count: int = 0
    nesting_level: int = 0
    complexity: int = 1
    local_variable_count: int = 0
    method_call_count: int = 0 
    has_docstring: bool = False
    is_public: bool = False
    name_length: int = 0
    return_count: int = 0
    
    def __post_init__(self):
        self.name_length = len(self.name)

@dataclass
class VariableMetrics:
    name: str
    line_number: int
    name_length: int = 0
    is_constant: bool = False
    
    def __post_init__(self):
        self.name_length = len(self.name)

@dataclass
class ClassMetrics:
    name: str
    line_number: int
    method_count: int = 0
    attribute_count: int = 0
    name_length: int = 0
    
    def __post_init__(self):
        self.name_length = len(self.name)

@dataclass
class CodeMetrics:
    methods: List[MethodMetrics] = field(default_factory=list)
    classes: List[ClassMetrics] = field(default_factory=list)
    variables: List[VariableMetrics] = field(default_factory=list)