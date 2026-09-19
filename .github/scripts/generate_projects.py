#!/usr/bin/env python3
"""
Generate projects.svg from merged.json into output directory.
"""
import sys, os, json, shutil

def main():
    merged_path = sys.argv[1] if len(sys.argv) > 1 else "merged.json"
    out_dir = sys.argv[2] if len(sys.argv) > 2 else "out"
    os.makedirs(out_dir, exist_ok=True)

    # Use the pre-designed projects_dark.svg as projects.svg for the projects branch
    src_svg = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "projects_dark.svg")
    target_svg = os.path.join(out_dir, "projects.svg")

    if os.path.exists(src_svg):
        shutil.copyfile(src_svg, target_svg)
        print(f"Copied {src_svg} -> {target_svg}")
    else:
        print(f"Warning: {src_svg} not found", file=sys.stderr)

if __name__ == "__main__":
    main()
