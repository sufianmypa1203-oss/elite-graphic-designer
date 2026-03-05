#!/usr/bin/env python3
"""
Elite Graphic Designer: Copy Flow Optimizer
Audits HTML/Markdown text configurations for typographic hierarchy and cognitive flow.

Usage:
    python copy-flow-optimizer.py <target_file.html>
"""

import sys
import json
import re
from pathlib import Path

CONFIG_PATH = Path(__file__).parent.parent / "config" / "copy-hierarchy-rules.json"

def load_config():
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)

def audit_file(filepath: Path, config):
    content = filepath.read_text()
    violations = []
    
    # Rule: Check if all caps has tracking (Basic heuristic check)
    if "text-transform: uppercase" in content.lower():
        if "letter-spacing" not in content.lower() and "tracking" not in content.lower():
            violations.append("Cognitive Flow: All-caps text detected without explicit tracking. Add at least 0.05em letter-spacing.")
            
    # Rule: Check line length on paragraphs (Basic estimation)
    paragraphs = re.findall(r'<p>(.*?)</p>', content, re.DOTALL)
    for i, p in enumerate(paragraphs, 1):
        char_count = len(re.sub('<[^<]+>', '', p).strip())
        if char_count > 0:
            if char_count < config["hierarchy_enforcement"]["optimal_line_length_min"] or char_count > config["hierarchy_enforcement"]["optimal_line_length_max"] * 4: # Assuming multi-line P tag
                violations.append(f"Typographical Error: Paragraph {i} may violate the 45-75 optimal line length measure. Character count: {char_count}")

    return violations

def main():
    if len(sys.argv) < 2:
        print("Usage: python copy-flow-optimizer.py <target_file.html>")
        sys.exit(1)
        
    target = Path(sys.argv[1])
    if not target.exists():
        print(f"File not found: {target}")
        sys.exit(1)
        
    config = load_config()
    print(f"\n📖 AUDITING TYPOGRAPHIC FLOW: {target.name}\n" + "="*50)
    
    issues = audit_file(target, config)
    
    if not issues:
        print("✅ PASSED: Cognitive flow and typographical hierarchy are optimal.")
        sys.exit(0)
    else:
        print("❌ FAILED: Suboptimal typographic rhythm detected:")
        for issue in issues:
            print(f"   - {issue}")
        sys.exit(1)

if __name__ == "__main__":
    main()
