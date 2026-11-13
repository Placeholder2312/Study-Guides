#!/usr/bin/env python3
"""
BEEE Module 1 HTML Build Script
Converts the study guide markdown to the final HTML with DSGT visual style.
"""
import os
import sys
from pathlib import Path

def main():
    # The HTML is already hand-crafted and committed as beee/modules/module-1.html
    # This script exists for parity with the Maths project structure.
    # If you need to rebuild from markdown sources, implement conversion here.
    
    project_root = Path(__file__).parent.parent
    html_path = project_root / "modules" / "module-1.html"
    
    if html_path.exists():
        print(f"HTML already exists at {html_path}")
        print(f"Size: {html_path.stat().st_size:,} bytes")
    else:
        print(f"ERROR: {html_path} not found")
        sys.exit(1)

if __name__ == "__main__":
    main()