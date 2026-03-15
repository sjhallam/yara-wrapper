from yara_wrapper.loaders.rule_loader import load_rule
from yara_wrapper.scanners.file_scanner import scan_file

# Load the rule
rule = load_rule("rules/test_rule.yar")

# Scan both files
malicious_result = scan_file(rule, "samples/malicious.txt")
clean_result = scan_file(rule, "samples/clean.txt")

# Print results
print("Malicious file:", malicious_result)
print("Clean file:", clean_result)