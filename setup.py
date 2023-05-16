from cx_Freeze import setup, Executable

base = None

executables = [Executable("fileremover.py", base=base)]

packages = []
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="File Remover",
    options=options,
    version="1.0.1",
    description=' This is a simple script that removes files from a directory based on the extension of the file.',
    executables=executables
)
