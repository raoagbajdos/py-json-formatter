import unittest
import json
import tempfile
import os
from pathlib import Path
from json_formatter import JSONFormatter


class TestJSONFormatter(unittest.TestCase):
    """Test cases for the JSONFormatter class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.formatter = JSONFormatter()
        self.sample_json = '{"name": "John", "age": 30, "city": "New York"}'
        self.sample_dict = {"name": "John", "age": 30, "city": "New York"}
        self.invalid_json = '{"name": "John", "age": 30, "city":}'
    
    def test_format_string_valid_json(self):
        """Test formatting a valid JSON string."""
        result = self.formatter.format_string(self.sample_json)
        expected = json.dumps(self.sample_dict, indent=4, ensure_ascii=False)
        self.assertEqual(result, expected)
    
    def test_format_string_invalid_json(self):
        """Test formatting an invalid JSON string."""
        with self.assertRaises(json.JSONDecodeError):
            self.formatter.format_string(self.invalid_json)
    
    def test_format_string_with_sort_keys(self):
        """Test formatting with sorted keys."""
        formatter = JSONFormatter(sort_keys=True)
        result = formatter.format_string(self.sample_json)
        parsed = json.loads(result)
        keys = list(parsed.keys())
        self.assertEqual(keys, sorted(keys))
    
    def test_format_string_custom_indent(self):
        """Test formatting with custom indentation."""
        formatter = JSONFormatter(indent=2)
        result = formatter.format_string(self.sample_json)
        lines = result.split('\n')
        # Check that the first nested line has 2 spaces
        self.assertTrue(lines[1].startswith('  '))
    
    def test_validate_valid_json(self):
        """Test validation of valid JSON."""
        self.assertTrue(self.formatter.validate(self.sample_json))
    
    def test_validate_invalid_json(self):
        """Test validation of invalid JSON."""
        self.assertFalse(self.formatter.validate(self.invalid_json))
    
    def test_minify(self):
        """Test JSON minification."""
        formatted = json.dumps(self.sample_dict, indent=4)
        minified = self.formatter.minify(formatted)
        expected = json.dumps(self.sample_dict, separators=(',', ':'), ensure_ascii=False)
        self.assertEqual(minified, expected)
    
    def test_format_file(self):
        """Test formatting a JSON file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write(self.sample_json)
            temp_path = f.name
        
        try:
            result = self.formatter.format_file(temp_path)
            expected = json.dumps(self.sample_dict, indent=4, ensure_ascii=False)
            self.assertEqual(result, expected)
            
            # Check that the file was updated
            with open(temp_path, 'r') as f:
                file_content = f.read()
            self.assertEqual(file_content, expected)
        finally:
            os.unlink(temp_path)
    
    def test_format_file_with_output(self):
        """Test formatting a JSON file with separate output."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as input_f:
            input_f.write(self.sample_json)
            input_path = input_f.name
        
        with tempfile.NamedTemporaryFile(delete=False) as output_f:
            output_path = output_f.name
        
        try:
            result = self.formatter.format_file(input_path, output_path)
            expected = json.dumps(self.sample_dict, indent=4, ensure_ascii=False)
            self.assertEqual(result, expected)
            
            # Check that the output file has the formatted content
            with open(output_path, 'r') as f:
                file_content = f.read()
            self.assertEqual(file_content, expected)
            
            # Check that the input file is unchanged
            with open(input_path, 'r') as f:
                input_content = f.read()
            self.assertEqual(input_content, self.sample_json)
        finally:
            os.unlink(input_path)
            os.unlink(output_path)
    
    def test_format_file_not_found(self):
        """Test formatting a non-existent file."""
        with self.assertRaises(FileNotFoundError):
            self.formatter.format_file('/nonexistent/file.json')
    
    def test_unicode_handling(self):
        """Test handling of Unicode characters."""
        unicode_json = '{"message": "Hello 世界", "emoji": "🌍"}'
        result = self.formatter.format_string(unicode_json)
        self.assertIn('世界', result)
        self.assertIn('🌍', result)


if __name__ == '__main__':
    unittest.main()