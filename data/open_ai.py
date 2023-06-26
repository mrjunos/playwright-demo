from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Message:
    role: str = ""
    content: Optional[str] = None
    name = Optional[str] = None
    function_call: Optional[str] = None

    def __post_init__(self):
        valid_roles = ['system', 'user', 'assistant', 'function']
        if self.role not in valid_roles:
            raise ValueError(f"Invalid role: {self.role}. Valid roles: {valid_roles}")


@dataclass
class Function:
    name: str = ""
    description: Optional[str] = None
    parameters: List[str] = field(default_factory=list)

    def __post_init__(self):
        if self.name is "":
            raise ValueError("Function name cannot be empty")


@dataclass
class Completion:
    model: str = ""
    messages: List[Message] = field(default_factory=Message)
    functions: Optional[List[Function]] = field(default_factory=Function)

    def __post_init__(self):
        if self.model is "":
            raise ValueError("Model cannot be empty")
