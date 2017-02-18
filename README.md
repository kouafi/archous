# Archous
Archous is a lightweight Python script for archiving Internet links using JSON files. It supports classification by date, category, tags.

## Requierements
Python 3+

## Usage
### Default usage
To add a link your JSON file, just type
```
python archous.py -u http://example.com
```
### Add a category
```
python archous.py -u http://example.com -c website
```

### Download a link under HTML format
```
python archous.py -u http://example.com -D
```