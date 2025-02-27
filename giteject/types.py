"""Types used throughout the giteject package."""
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class FileInfo:
    """Information about a single file."""
    path: str
    size: int
    token_count: Optional[int] = None
    content: Optional[str] = None

@dataclass
class AnalysisResult:
    """Result of analyzing a directory or repository."""
    files: List[FileInfo]
    total_size: int
    total_tokens: int
    structure: Dict[str, List[str]]  # Directory structure
    summary: str

@dataclass
class FileContent:
    """Information about a file from gitingest output."""
    path: str
    content: str

@dataclass
class RepoStructure:
    """Repository structure to be created."""
    files: List[FileContent]
    directories: List[str]
