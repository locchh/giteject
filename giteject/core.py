"""Core functionality for creating repositories from gitingest output."""
import os
from pathlib import Path
from typing import List, Optional
import re

from .types import FileContent, RepoStructure

def parse_gitingest_output(content: str) -> RepoStructure:
    """
    Parse the output from gitingest and extract file information.
    
    Args:
        content: The content of the gitingest output file
        
    Returns:
        RepoStructure containing files and directories to create
    """
    files: List[FileContent] = []
    directories = set()
    
    # Pattern to match file sections in gitingest output
    file_pattern = r'File: ([^\n]+)\nContent:\n(.*?)(?=\nFile:|$)'
    
    # Find all file sections
    matches = re.finditer(file_pattern, content, re.DOTALL)
    
    for match in matches:
        path = match.group(1).strip()
        content = match.group(2).strip()
        
        # Add directory path to set
        dir_path = os.path.dirname(path)
        if dir_path:
            directories.add(dir_path)
            # Add parent directories as well
            while dir_path:
                dir_path = os.path.dirname(dir_path)
                if dir_path:
                    directories.add(dir_path)
        
        files.append(FileContent(path=path, content=content))
    
    return RepoStructure(
        files=files,
        directories=sorted(list(directories))
    )

def create_repository(output_path: str, structure: RepoStructure) -> None:
    """
    Create a repository structure from the parsed gitingest output.
    
    Args:
        output_path: Path where to create the repository
        structure: RepoStructure containing files and directories to create
    """
    # Create base directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    
    # Create all directories first
    for directory in structure.directories:
        dir_path = os.path.join(output_path, directory)
        os.makedirs(dir_path, exist_ok=True)
    
    # Create all files
    for file_info in structure.files:
        file_path = os.path.join(output_path, file_info.path)
        
        # Create parent directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Write file content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(file_info.content)