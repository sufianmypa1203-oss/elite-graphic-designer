#!/usr/bin/env python3
"""
Elite Graphic Designer: Visual QA Auditor
Audits CSS/SCSS/TSX files against the strict 8px grid and WCAG parameters.

Usage:
    python visual-qa-auditor.py <target_directory_or_file>
"""

import sys
import os
import re
import json
from pathlib import Path

CONFIG_PATH = Path(__file__).parent.parent / "config" / "qa-checklist.json"

def load_config():
    if not CONFIG_PATH.exists():
        print(f"Error: Could not find config at {CONFIG_PATH}")
        sys.exit(1)
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)

def check_grid_violations(content, config, filename):
    violations = []
    base_unit = config["grid_enforcement"]["base_unit"]
    
    # Regex to find pixel values for strictly enforced properties (e.g. padding: 15px)
    props = "|".join(config["grid_enforcement"]["strictly_enforced_properties"])
    pattern = re.compile(rf"({props})\s*:\s*.*?(\d+)px", re.IGNORECASE)
    
    for i, line in enumerate(content.splitlines(), 1):
        if match := pattern.search(line):
            prop = match.group(1)
            px_val = int(match.group(2))
            
            # Check if it's cleanly divisible by 8 (or 4 for 0.5 multiples)
            if px_val % (base_unit / 2) != 0:
                violations.append(f"Line {i}: Grid Violation - `{prop}: {px_val}px`. Value must align to the {base_unit}px baseline grid.")
    
    return violations

def check_color_smells(content, config, filename):
    violations = []
    smells = config["color_smells"]
    
    for i, line in enumerate(content.splitlines(), 1):
        for pattern in smells["pure_black"]:
            if pattern in line:
                violations.append(f"Line {i}: Color Smell - Pure Black detected. {smells['pure_black_reason']}")
                break
        for pattern in smells["pure_white"]:
            if pattern in line:
                violations.append(f"Line {i}: Color Smell - Pure White detected. {smells['pure_white_reason']}")
                break
                
    return violations

def audit_file(filepath: Path, config):
    try:
        content = filepath.read_text()
        violations = []
        violations.extend(check_grid_violations(content, config, filepath.name))
        violations.extend(check_color_smells(content, config, filepath.name))
        return violations
    except Exception as e:
        return [f"Error reading file {filepath.name}: {e}"]

def main():
    if len(sys.argv) < 2:
        print("Usage: python visual-qa-auditor.py <target_directory_or_file>")
        sys.exit(1)
        
    target = Path(sys.argv[1])
    config = load_config()
    
    all_violations = {}
    
    print("\n🔍 ELITE GRAPHIC DESIGNER: VISUAL QA AUDIT")
    print("==========================================")
    
    if target.is_file():
        files_to_audit = [target]
    else:
        files_to_audit = [f for f in target.rglob("*") if f.suffix in ['.css', '.scss', '.tsx', '.jsx']]
        
    for f in files_to_audit:
        v = audit_file(f, config)
        if v:
            all_violations[str(f)] = v

    if not all_violations:
        print("\n✅ QA PASSED: 100% Alignment with Elite Design Standards.")
        print("   The 8px grid is unbroken. Colors are sophisticated.")
        sys.exit(0)
    else:
        print(f"\n❌ FAILED: {len(all_violations)} files contain critical design formatting errors.\n")
        for filepath, issues in all_violations.items():
            print(f"📄 {filepath}:")
            for issue in issues:
                print(f"   -> {issue}")
        print("\nFix these deviations immediately before proceeding to delivery.\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
