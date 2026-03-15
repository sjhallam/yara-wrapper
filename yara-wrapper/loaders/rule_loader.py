import yara
from pathlib import Path

def load_rule(rule_path):
    if not Path(rule_path).exists():
        raise FileNotFoundError(f"Rule file not found: {rule_path}")
    
    try:
        compiled_rule = yara.compile(rule_path)
    except yara.SyntaxError as e:
        raise ValueError(f"Invalid YARA syntax in {rule_path}: {e}")
    
    return compiled_rule


def load_all_rules(directory_path):
    if not Path(directory_path).exists():
        raise FileNotFoundError(f"Directory not found: {directory_path}")
    
    files_found = Path(directory_path).glob("*.yar")
    rule_files = []
    
    for rule_file in files_found:
        rule_files.append(load_rule(rule_file))
    if not rule_files:
        raise FileNotFoundError(f"No .yar files found in: {directory_path}")
    
    return rule_files