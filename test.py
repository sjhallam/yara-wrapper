import os
import psutil
from yara_wrapper.loaders.rule_loader import load_rule
from yara_wrapper.scanners.process_scanner import scan_process

# Load the rule
rule = load_rule("rules/test_rule.yar")

# Get current Python process PID
pid = os.getpid()
print(f"Scanning process: {pid}")

# Scan the process
results = scan_process(rule, pid)
print("Results:", results)