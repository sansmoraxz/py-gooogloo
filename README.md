# Py Gooogloo
Google search using RESTful APIs

## Usage Demo:

Search and display title and links
```python
>>> import gooogloo
>>> gse = gooogloo.GoogleSearch(api_key={Your API Key}, cx={Search Engine ID})
>>> reso = gse.search(q={search_string})
>>> for x in reso:
...   print(x['title'], x['link'])
```