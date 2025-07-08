# JSON Formatter

A simple, fast, and reliable Python utility for formatting, validating, and minifying JSON data.

## 🚀 Quick Reference

| What you want to do | Command |
|---------------------|---------|
| Format my JSON file | `python3 json_formatter.py myfile.json` |
| Save formatted version | `python3 json_formatter.py myfile.json -o clean.json` |
| Use 2-space indents | `python3 json_formatter.py myfile.json -i 2` |
| Sort keys A-Z | `python3 json_formatter.py myfile.json --sort-keys` |
| Make it compact | `python3 json_formatter.py myfile.json -m` |
| Just check if valid | `python3 json_formatter.py myfile.json -v` |

💡 **Put your JSON files in the same folder as `json_formatter.py`**

## Features

- ✅ Format JSON with customizable indentation
- ✅ Validate JSON syntax
- ✅ Minify JSON (remove whitespace)
- ✅ Sort keys alphabetically (optional)
- ✅ Handle Unicode characters properly
- ✅ Command-line interface
- ✅ Python API for programmatic use
- ✅ Comprehensive error handling

## Installation

Clone this repository:

```bash
git clone <your-repo-url>
cd json-formatter
```

No additional dependencies required - uses only Python standard library.

## Quick Start Guide

### Step 1: Place Your JSON File

Put your JSON file in the same folder as `json_formatter.py`. For example:
- Save your JSON as `my_data.json` in the project folder
- Or use any of the included sample files: `portfolio.json`, `sample.json`

### Step 2: Format Your JSON

Open terminal/command prompt in the project folder and run:

```bash
# Format your JSON file (displays result in terminal)
python3 json_formatter.py my_data.json

# Save formatted JSON to a new file
python3 json_formatter.py my_data.json -o my_data_formatted.json
```

### Step 3: Check Your Results
- **Terminal output**: See formatted JSON immediately
- **New file**: Find your formatted JSON in `my_data_formatted.json`

## Usage Options

### 📁 Where to Put Your JSON Files
```
json-formatter/
├── json_formatter.py          ← The formatter tool
├── my_data.json              ← PUT YOUR JSON HERE
├── portfolio.json            ← Sample file (already included)
├── sample.json               ← Sample file (already included)
└── my_data_formatted.json    ← Output will be created here
```

### 🔧 Formatting Commands

**Basic formatting** (4-space indentation):
```bash
python3 json_formatter.py my_data.json
```

**Custom indentation** (2 spaces):
```bash
python3 json_formatter.py my_data.json -i 2
```

**Save to new file**:
```bash
python3 json_formatter.py my_data.json -o formatted_output.json
```

**Sort keys alphabetically**:
```bash
python3 json_formatter.py my_data.json --sort-keys
```

**Minify JSON** (remove all spaces):
```bash
python3 json_formatter.py my_data.json -m
```

**Just validate** (check if JSON is valid):
```bash
python3 json_formatter.py my_data.json -v
```

### 📝 Real Examples with Included Files

Try these commands with the sample files:

```bash
# Format the portfolio example
python3 json_formatter.py portfolio.json

# Create a minified version
python3 json_formatter.py portfolio.json -m -o portfolio_mini.json

# Format with 2-space indentation and sorted keys
python3 json_formatter.py sample.json -i 2 --sort-keys -o sample_clean.json
```

### 🎯 Complete Walkthrough Example

**Step 1**: Look at the messy JSON file:
```bash
cat example_messy.json
```
Shows: `{"name":"Alice Smith","age":28,"city":"New York"...}`

**Step 2**: Format it beautifully:
```bash
python3 json_formatter.py example_messy.json -o example_clean.json
```

**Step 3**: See the beautiful result:
```bash
cat example_clean.json
```
Shows:
```json
{
    "name": "Alice Smith",
    "age": 28,
    "city": "New York",
    "hobbies": [
        "reading",
        "hiking", 
        "coding"
    ],
    "contact": {
        "email": "alice@example.com",
        "phone": "555-1234"
    },
    "active": true
}
```

### Python API

```python
from json_formatter import JSONFormatter

# Create formatter instance
formatter = JSONFormatter(indent=4, sort_keys=True)

# Format JSON string
json_string = '{"name":"John","age":30}'
formatted = formatter.format_string(json_string)
print(formatted)

# Format JSON file
formatter.format_file('input.json', 'output.json')

# Validate JSON
is_valid = formatter.validate('{"valid": "json"}')
print(is_valid)  # True

# Minify JSON
minified = formatter.minify('{\n  "name": "John"\n}')
print(minified)  # {"name":"John"}
```

## API Reference

### JSONFormatter Class

#### Constructor
```python
JSONFormatter(indent=4, sort_keys=False)
```
- `indent` (int): Number of spaces for indentation (default: 4)
- `sort_keys` (bool): Whether to sort keys alphabetically (default: False)

#### Methods

- `format_string(json_string: str) -> str`: Format a JSON string
- `format_file(input_path, output_path=None) -> str`: Format JSON from file
- `validate(json_string: str) -> bool`: Validate JSON syntax
- `minify(json_string: str) -> str`: Remove whitespace from JSON

## Examples

### Example 1: Basic Formatting
```python
from json_formatter import JSONFormatter

formatter = JSONFormatter()
ugly_json = '{"users":[{"name":"Alice","age":25},{"name":"Bob","age":30}]}'
pretty_json = formatter.format_string(ugly_json)
print(pretty_json)
```

Output:
```json
{
    "users": [
        {
            "name": "Alice",
            "age": 25
        },
        {
            "name": "Bob",
            "age": 30
        }
    ]
}
```

### Example 2: File Processing
```python
from json_formatter import JSONFormatter

formatter = JSONFormatter(indent=2, sort_keys=True)
formatter.format_file('messy.json', 'clean.json')
```

### Example 3: Validation
```python
from json_formatter import JSONFormatter

formatter = JSONFormatter()

valid_json = '{"status": "ok"}'
invalid_json = '{"status": ok}'

print(formatter.validate(valid_json))    # True
print(formatter.validate(invalid_json))  # False
```

## Troubleshooting

### Common Issues

**Q: "python: command not found"**
```bash
# Try python3 instead
python3 json_formatter.py my_data.json
```

**Q: "No such file or directory"**
```bash
# Make sure you're in the right folder
cd path/to/json-formatter
ls  # Should see json_formatter.py

# Make sure your JSON file exists
ls my_data.json  # Should show your file
```

**Q: "Invalid JSON" error**
- Check your JSON syntax at [jsonlint.com](https://jsonlint.com)
- Common issues: missing quotes, trailing commas, unescaped characters

**Q: Where do I find my formatted output?**
- Without `-o`: Output shows in terminal
- With `-o filename.json`: Creates new file in same folder

### File Locations
```
Your project folder/
├── json_formatter.py     ← The tool (don't move this)
├── YOUR_FILE.json       ← Put your JSON files here
├── output.json          ← Formatted files appear here
└── README.md           ← This documentation
```

## Testing

Run the test suite:
```bash
python -m unittest test_json_formatter.py
```

Run with verbose output:
```bash
python -m unittest test_json_formatter.py -v
```

## Error Handling

The formatter provides clear error messages for common issues:

- **Invalid JSON**: Detailed syntax error information
- **File not found**: Clear file path error messages
- **Permission errors**: Helpful file access error messages

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Commit your changes (`git commit -am 'Add new feature'`)
7. Push to the branch (`git push origin feature/new-feature`)
8. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Changelog

### v1.0.0
- Initial release
- Basic JSON formatting functionality
- Command-line interface
- Validation and minification features
- Comprehensive test suite