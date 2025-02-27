"""
giteject - A tool for extracting and analyzing code repositories
"""

from .core import analyze_directory, analyze_repo
from .types import AnalysisResult

__version__ = "0.1.0"
__all__ = ["analyze_directory", "analyze_repo", "AnalysisResult"]
