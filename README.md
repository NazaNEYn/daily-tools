# Daily Tools

A collection of lightweight, dependency-free Python scripts designed to simplify common daily tasks. These scripts are easy to use, run in the terminal, and require only the Python standard library.

## Purpose

This repository provides practical tools for everyday file management and productivity tasks. Each script is standalone, simple, and focused on a single task to keep things efficient.

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Scripts

### rename_bulk.py

Bulk rename files in a directory with a custom prefix or timestamp.

**Usage:**
```bash
python rename_bulk.py
```

**Features:**
- Interactive prompts for directory and prefix selection
- Automatic timestamp generation if no prefix provided
- Validates directory existence before processing
- Reports number of files renamed

**Example:**
```
Enter folder path (leave blank for current directory): /path/to/files
Enter prefix (leave blank for timestamp): vacation_
Renamed 15 files with prefix 'vacation_' in '/path/to/files'
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your script following the established patterns
4. Test thoroughly
5. Submit a pull request

## License

MIT License - see LICENSE file for details (if applicable)