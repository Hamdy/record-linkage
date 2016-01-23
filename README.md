# record-linkage
A simple application that does [record linkage](https://en.wikipedia.org/wiki/Record_linkage) on 2 data sources
- data/products.txt
 - ```{"product_name":"blah","manufacturer":"blah","model":"blah"}```
- data/listings.txt
 - ```{"title":"blah","manufacturer":"blah","currency":"blah","price":""}```

Final result is data/result.txt with product as key and all its listings as value

## Usage
```python main.py```
