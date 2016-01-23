import json

class Loader(object):
    """
    Load  data from text files into memory
    """
    def __init__(self, normalizer):
        self.normalizer = normalizer
        
    def _normalize_name(self, name, family, manufacturer):
        family = family.lower()
        manufacturer = manufacturer.lower()
        if family and family in name:
            name = name.replace(family, '')
        if manufacturer in name:
            name = name.replace(manufacturer, '')
        return name.strip()

    def _load(self, filename):
        result = {}
        with open('data/%s' % filename) as products:
            for line in products:
                line = json.loads(line)
                manufacturer = line['manufacturer'].lower()
                if not manufacturer in result:
                    result[manufacturer] = []
                # only listings
                if 'title' in line:
                    line['normalized_title'] = self.normalizer.normalize(line['title'])
                else: # only products
                    line['normalized_model'] = self.normalizer.normalize(line['model'])
                    line['info'] = self.normalizer.normalize('%s %s %s' % (line['product_name'],
                        line['model'], line.get('family', '')))
                    line['normalized_name'] = self.normalizer.normalize(line['product_name'])
                    line['normalized_name'] = self._normalize_name(line['normalized_name'], line.get('family', ''), line['manufacturer'])
                result[manufacturer].append(line)
        return result
    
    @property
    def products(self):
        """
        return dictionary of manufacturer as
        key and all its products as value
        there're extra 2 fields added to products
        normalized_model
        info : normalized string of product_name, model and family
        """
        return self._load('products.txt')
        
    @property
    def listings(self):
        """
        return dictionary of manufacturer as
        key and all its listings as value
        listings have title normalized
        """
        return self._load('listings.txt')