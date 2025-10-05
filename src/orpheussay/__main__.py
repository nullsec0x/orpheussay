#!/usr/bin/env python3
import sys
import textwrap
import argparse

ORPHEUS_ART = r"""
          \
           \
            \  __
              / _)
     _.----._/ /
    /         /
 __/ (| | (  |
/__.-'|_|--|_|
"""

def create_bubble(text, width=40):
    """Create a speech bubble around the text"""
    wrapped_lines = textwrap.wrap(text, width=width)
    
    max_len = max(len(line) for line in wrapped_lines) if wrapped_lines else 0
    
    top_border = " " + "_" * (max_len + 2)
    
    bottom_border = " " + "-" * (max_len + 2)
    
    bubble_lines = []
    if len(wrapped_lines) == 1:
        bubble_lines.append(f"< {wrapped_lines[0]} >")
    else:
        for i, line in enumerate(wrapped_lines):
            padded_line = line.ljust(max_len)
            if i == 0:
                bubble_lines.append(f"/ {padded_line} \\")
            elif i == len(wrapped_lines) - 1:
                bubble_lines.append(f"\\ {padded_line} /")
            else:
                bubble_lines.append(f"| {padded_line} |")
    
    bubble = [top_border]
    bubble.extend(bubble_lines)
    bubble.append(bottom_border)
    
    return "\n".join(bubble)

def main():
    parser = argparse.ArgumentParser(description="Make Orpheus say something")
    parser.add_argument("message", nargs="*", help="The message for Orpheus to say")
    parser.add_argument("-w", "--width", type=int, default=40, help="Width of the speech bubble")
    
    args = parser.parse_args()
    
    if args.message:
        text = " ".join(args.message)
    elif not sys.stdin.isatty():
        text = sys.stdin.read().strip()
    else:
        parser.print_help()
        return
    
    bubble = create_bubble(text, args.width)
    print(bubble)
    print(ORPHEUS_ART)

if __name__ == "__main__":
    main()
