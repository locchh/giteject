# giteject

**giteject** is a utility for recreating repository structures from [gitingest](https://github.com/cyclotruc/gitingest) analysis outputs. It reconstructs directories and files using the metadata and content provided by gitingest, helping you restore or inspect repository layouts with ease.

---

## 🔧 Features

* Parses gitingest output files
* Reconstructs original repository layout:

  * Automatically generates folder hierarchy
  * Restores file contents accurately
  * Preserves relative paths and file types
* Simple and intuitive command-line interface
* Lightweight and easy to integrate into workflows

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/giteject.git
cd giteject
pip install -r requirements.txt
```

---

## 🚀 Usage

### Step 1: Generate an analysis file with `gitingest`

```bash
gitingest https://github.com/user/repo -o repo_analysis.txt
```

### Step 2: Recreate the repository using `giteject`

```bash
python -m giteject.cli repo_analysis.txt /path/to/output/repo
```

The tool will:

* Create all directories as needed
* Write the content of each file to its correct location

---

## 📄 Input Format

giteject expects input files to follow the structure generated by gitingest, e.g.:

```
File: path/to/file1.txt
Content:
[contents of file1]

File: path/to/file2.py
Content:
[contents of file2]
```

Each file block starts with a `File:` line and includes the file content under a `Content:` header.

---

## 📚 Related Projects

* [gitingest](https://github.com/cyclotruc/gitingest) – Extracts file structure and contents from Git repositories
* [gitingest.com](https://gitingest.com) – Project homepage for gitingest (if active)
* [gitdiagram](https://github.com/ahmedkhaleel2004/gitdiagram) – Visualize code repositories as diagrams
* [gitdiagram.com](https://gitdiagram.com) – Gitdiagram web tool (if live)
* [deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open) – Open-source project for building wikis from code
* [deepwiki.com](https://deepwiki.com) – Website for DeepWiki project (if available)

---

## 📄 License

This project is licensed under the terms of the [LICENSE](LICENSE) file.
