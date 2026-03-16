import psutil
from pathlib import Path


def scan_process(rule, pid):
    if not psutil.pid_exists(pid):
        raise ProcessLookupError(f"Process not found: {pid}")
    
    results = {}
    with open(f"/proc/{pid}/maps", "r") as map:
        for line in map:
            split_map = line.split()
            if split_map[1].startswith("r"):
                address_range = split_map[0].split("-")
                region_size = int(address_range[1], 16) - int(address_range[0], 16)
                with open(f"/proc/{pid}/mem", "rb") as mem:
                    try:
                        mem.seek(int(address_range[0], 16))
                        matches = rule.match(data=mem.read(region_size))
                        if matches:
                            results[pid] = matches
                    except Exception:
                        continue
    return results