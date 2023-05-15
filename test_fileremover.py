import subprocess

def test_invalid_argument():
    # Test with an invalid argument
    result = subprocess.run(['python3', 'fileremover.py', '--z', '/mnt/d/Documents/Projets/file-sort/example_path'], capture_output=True, text=True)
    assert result.returncode == 1
    assert result.stderr == 'Error: unknown argument --z\n'