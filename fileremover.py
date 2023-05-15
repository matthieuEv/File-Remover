import sys
from os import listdir, remove, walk
from os.path import isfile, join, isdir

class FileRemover:
    def __init__(self, path):
        self.path = path
        self.files_dict = self._get_files(self.path)

    def view_files(self):
        self._print_files(self.files_dict, 0)

    def _get_files(self, path):
        files_and_folders = {}
        for f in sorted(listdir(path)):
            subpath = join(path, f)
            if isdir(subpath):
                files_and_folders[f] = self._get_files(subpath)
            elif isfile(subpath):
                files_and_folders[f] = subpath
        return files_and_folders


    def _print_files(self, files_dict, level):
        for key in files_dict:
            print('├─' * level + key)
            value = files_dict[key]
            if isinstance(value, dict):
                self._print_files(value, level + 1)

    def remove_files(self, extensions):
        extensionsList = extensions.split(',')
        dict = self.files_dict
        for extension in extensionsList:
            allDirectoriesFiles = self._get_all_directories(dict)
            for dirfiles in allDirectoriesFiles:
                if dirfiles.endswith(extension):
                    remove(dirfiles)
                    print(dirfiles + " removed")

    def _get_all_directories(self, d):
        result = []
        for key, value in d.items():
            if isinstance(value, dict):
                result.extend(self._get_all_directories(value))
            else:
                result.append(value)
        return result


if __name__ == '__main__':
    if len(sys.argv) > 1:
        path = None
        extensions = []
        skip_next = False
        for i in range(1, len(sys.argv)):
            if skip_next:
                skip_next = False
                continue
            arg = sys.argv[i]
            if arg == "--path" and i+1 < len(sys.argv):
                path = sys.argv[i+1]
                skip_next = True
            elif arg == "--view":
                if path is None:
                    assert False, "Error: --path argument is required"
                print('\n')
                FileRemover = FileRemover(path)
                FileRemover.view_files()
                print('\n')
            elif (arg == "--rm" or arg == "--remove") and i+1 < len(sys.argv):
                if path is None:
                    assert False, "Error: --path argument is required"
                extensions = sys.argv[i+1]
                skip_next = True
                FileRemover = FileRemover(path)
                FileRemover.remove_files(extensions)
            else:
                print("Error: unknown argument " + arg, file=sys.stderr)
                sys.exit(1)
    else:
        assert False, "Error: no arguments provided"



