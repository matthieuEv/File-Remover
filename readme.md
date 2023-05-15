# FileRemover
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/matthieuEv/File-Remover/python-app.yml?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/matthieuEv/File-Remover?style=for-the-badge)
## Description
This is a simple script that removes files from a directory based on the extension of the file.

## Usage

First, download the script and put it wherever you want.

Then, you can use it with the following command:

```bash
python3 fileremover.py <arguments>
```

| Argument | Description | Needed |
| --- | --- | --- |
| --path | Absolute path of the directory to clean | ✅ |
| --rm </br>*-- remove* | Extension of the files to remove <br>If u want to remove multiple file, use "," between all extensions<br>*("all" delete all files but not the folders)* | ❌ |
| --view | Show all files and folders (can be put before and after to see the result) | ❌ |


## Example

```bash
python3 fileremover.py --path /home/user/Downloads --rm .pdf,.zip,.tar.gz --view
```
```bash
python3 fileremover.py --path /home/user/Downloads --view --rm all --view
```