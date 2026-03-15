import yara
from pathlib import Path


def scan_file(rule, file_path):
    if not Path(file_path).exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        return rule.match(filepath=file_path)
    except Exception as e:
        raise RuntimeError(f"Error scanning file {file_path}: {e}")
    

def scan_directory(rule, directory_path):
    if not Path(directory_path).exists():
        raise FileNotFoundError(f"Directory not found: {directory_path}")
    
    files_found = Path(directory_path).glob("*")
    results = {}
    for file in files_found:
        if file.is_file():
            results[file] = scan_file(rule, file)
    return results