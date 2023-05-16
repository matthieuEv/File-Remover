# FileRemover
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/matthieuEv/File-Remover/python-app.yml?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/matthieuEv/File-Remover?style=for-the-badge)
## Description
This is a simple script that removes files from a directory based on the extension of the file.

## ⚠️ Disclamer
This program is not made to be usefull because there is already some tool built-in to do what my code does, like:
```bash
find <path> -type f -name "*.<extension>" -exec rm -f {} \;
```
or also: 
```bash
find /home/user/documents -type f \( -name "*.<extension>" -o -name "*.<extension>" \) -exec rm -f {} \;
``` 

FileRemover was made to improve my skills in python (learning how arguments work, make some recursive function...), learning how to make a good Readme and try to make a release of FileRemover. 
## Usage

First, download the script and put it wherever you want.

Then, you can use it with the following command:

```bash
python3 fileremover.py --path <path> <arguments>
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