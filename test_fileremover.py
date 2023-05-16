import subprocess

def test_invalid_argument():
    # Test with an invalid argument
    result = subprocess.run(['python3', 'fileremover.py', '--z', '/mnt/d/Documents/Projets/file-sort/example_path'], capture_output=True, text=True)
    assert result.returncode == 1
    assert result.stderr == 'Error: unknown argument --z\n'

def test_missing_path():
    # Test without the --path argument
    result = subprocess.run(['python3', 'fileremover.py', '--view'], capture_output=True, text=True)
    assert result.returncode == 1
    assert result.stderr == 'Error: --path argument is required\n'

def test_missing_arguments():
    # Test without any argument
    result = subprocess.run(['python3', 'fileremover.py'], capture_output=True, text=True)
    assert result.returncode == 1
    assert result.stderr == 'Error: missing arguments\n'

def test_extension_no_dot():
    # test if the extension given has dot
    result = subprocess.run(['python3', 'fileremover.py','--path','/mnt/d/Documents/Projets/file-sort/example_path','--rm',' json'], capture_output=True, text=True)
    assert result.returncode == 1
    assert result.stderr == 'Error: the extension to remove don\'t start with a dot\n'
