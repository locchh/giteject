# giteject

A tool for creating repositories from [gitingest](https://github.com/cyclotruc/gitingest) output. This tool helps you recreate a repository structure from gitingest's analysis output.

## Features

- Parse gitingest output files
- Recreate repository structure:
  - Automatically creates directory hierarchy
  - Preserves file content and structure
  - Maintains relative paths
- Simple command-line interface

## Installation

```bash
# Install requirements
pip install -r requirements.txt
```

## Usage

1. First, use gitingest to analyze a repository and save the output:
```bash
# Using gitingest
gitingest https://github.com/user/repo -o repo_analysis.txt
```

2. Then use giteject to create a new repository from the analysis:
```bash
# Create repository from gitingest output
python -m giteject.cli repo_analysis.txt /path/to/output/repo
```

## Input Format

The tool expects gitingest output in the following format:
```
File: path/to/file1.txt
Content:
[file content here]

File: path/to/file2.py
Content:
[file content here]
```

## License

See the [LICENSE](LICENSE) file for details.

## References

[gitingest](https://github.com/cyclotruc/gitingest)

[gitdiagram](https://github.com/ahmedkhaleel2004/gitdiagram)

[deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open)
