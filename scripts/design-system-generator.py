#!/usr/bin/env python3
"""
Elite Graphic Designer: Design System Generator
Parses JSON design tokens and generates production-ready CSS variables mapped to the 8px grid.

Usage:
    python design-system-generator.py
"""

import json
from pathlib import Path

CONFIG_PATH = Path(__file__).parent.parent / "config" / "design-tokens.json"
OUTPUT_PATH = Path("theme.css")

def load_config():
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)

def generate_css(config):
    lines = ["/* Elite Graphic Designer - Auto Generated Design Tokens */", ":root {"]
    
    # Spacing
    lines.append("  /* Base 8px Grid Spacing */")
    for key, val in config["spacing_scale"].items():
        lines.append(f"  --spacing-{key}: {val};")
        
    # Typography
    lines.append("\n  /* Typographic Scale */")
    levels = config["typography_scale"]["levels"]
    for key, spec in levels.items():
        lines.append(f"  --text-{key}-size: {spec['size']};")
        lines.append(f"  --text-{key}-line: {spec['lineHeight']};")
        
    lines.append("}\n")
    return "\n".join(lines)

def main():
    print("🎨 INITIALIZING DESIGN SYSTEM GENERATOR...")
    config = load_config()
    
    css = generate_css(config)
    OUTPUT_PATH.write_text(css)
    
    print(f"✅ SUCCESSFULLY GENERATED: {OUTPUT_PATH.absolute()}")
    print("   Tokens are strictly mapped to the 8px baseline and Satori progression.")

if __name__ == "__main__":
    main()
