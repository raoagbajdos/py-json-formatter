#!/usr/bin/env python3
"""
JSON Formatter - A simple utility to format and validate JSON data.
"""

import json
import sys
import argparse
from typing import Union, Dict, List, Any
from pathlib import Path


class JSONFormatter:
    """A utility class for formatting and validating JSON data."""
    
    def __init__(self, indent: int = 4, sort_keys: bool = False):
        """
        Initialize the JSON formatter.
        
        Args:
            indent: Number of spaces for indentation (default: 4)
            sort_keys: Whether to sort keys alphabetically (default: False)
        """
        self.indent = indent
        self.sort_keys = sort_keys
    
    def format_string(self, json_string: str) -> str:
        """
        Format a JSON string.
        
        Args:
            json_string: Raw JSON string to format
            
        Returns:
            Formatted JSON string
            
        Raises:
            json.JSONDecodeError: If the input is not valid JSON
        """
        try:
            parsed = json.loads(json_string)
            return json.dumps(
                parsed, 
                indent=self.indent, 
                sort_keys=self.sort_keys,
                ensure_ascii=False
            )
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON: {e.msg}", e.doc, e.pos)
    
    def format_file(self, input_path: Union[str, Path], output_path: Union[str, Path] = None) -> str:
        """
        Format JSON from a file.
        
        Args:
            input_path: Path to input JSON file
            output_path: Path to output file (optional, overwrites input if not provided)
            
        Returns:
            Formatted JSON string
        """
        input_path = Path(input_path)
        
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")
        
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        formatted = self.format_string(content)
        
        if output_path:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(formatted)
        else:
            with open(input_path, 'w', encoding='utf-8') as f:
                f.write(formatted)
        
        return formatted
    
    def validate(self, json_string: str) -> bool:
        """
        Validate if a string is valid JSON.
        
        Args:
            json_string: String to validate
            
        Returns:
            True if valid JSON, False otherwise
        """
        try:
            json.loads(json_string)
            return True
        except json.JSONDecodeError:
            return False
    
    def minify(self, json_string: str) -> str:
        """
        Minify JSON by removing whitespace.
        
        Args:
            json_string: JSON string to minify
            
        Returns:
            Minified JSON string
        """
        parsed = json.loads(json_string)
        return json.dumps(parsed, separators=(',', ':'), ensure_ascii=False)


def main():
    """Command line interface for the JSON formatter."""
    parser = argparse.ArgumentParser(description='Format and validate JSON files')
    parser.add_argument('input', help='Input JSON file path')
    parser.add_argument('-o', '--output', help='Output file path (optional)')
    parser.add_argument('-i', '--indent', type=int, default=4, help='Indentation spaces (default: 4)')
    parser.add_argument('-s', '--sort-keys', action='store_true', help='Sort keys alphabetically')
    parser.add_argument('-m', '--minify', action='store_true', help='Minify JSON instead of formatting')
    parser.add_argument('-v', '--validate', action='store_true', help='Only validate JSON, don\'t format')
    
    args = parser.parse_args()
    
    formatter = JSONFormatter(indent=args.indent, sort_keys=args.sort_keys)
    
    try:
        if args.validate:
            with open(args.input, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if formatter.validate(content):
                print(f"✓ {args.input} is valid JSON")
                sys.exit(0)
            else:
                print(f"✗ {args.input} is not valid JSON")
                sys.exit(1)
        
        elif args.minify:
            with open(args.input, 'r', encoding='utf-8') as f:
                content = f.read()
            
            minified = formatter.minify(content)
            
            if args.output:
                with open(args.output, 'w', encoding='utf-8') as f:
                    f.write(minified)
                print(f"Minified JSON written to {args.output}")
            else:
                print(minified)
        
        else:
            formatted = formatter.format_file(args.input, args.output)
            if args.output:
                print(f"Formatted JSON written to {args.output}")
            else:
                print(f"Formatted {args.input}")
    
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()