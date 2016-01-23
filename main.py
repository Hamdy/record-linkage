import json
from normalizers import Normalizer
from matchers import SimpleMatcher
from loaders import Loader

class Processor(object):
    def __init__(self, loader, matcher):
        self.products = loader.products
        self.listings = loader.listings
        self.matcher = matcher
    
    def _group_by_manufacturer(self):
        """
        Returns a dictionary with manufacturer as key
        and value as list of 2 lists
        first list is all products from products.txt for this manufacturer
        second value is all listings from listings.txt for this manufacturer
        """
        result = {}
        
        # process exactly matched manufacturer keys
        products_keys = self.products.keys()
        listings_keys = self.listings.keys()
        for k in listings_keys:
            for k2 in products_keys:
                if k2 in k.split():
                    if k2 not in result:
                        result[k2] = [[],[]]
                    result[k2][0].extend(self.products[k2])
                    result[k2][1].extend(self.listings[k])
        return result
    
    def match(self):
        """
        Giving products and listings for certain manufacturer
        do matching between products and related listings
        """
        result = {}
        manufact_groups = self._group_by_manufacturer()
        for _, v in manufact_groups.iteritems():
            products = v[0]
            listings = v[1]
            
            for p in products:
                name = p['product_name']
                if not name in result:
                    result[name] = []
                for item in listings:
                    if self.matcher.match(item['normalized_title'], p['normalized_model']) or\
                            self.matcher.match(item['normalized_title'], p['normalized_name']):
                        result[name].append(item)
                        
        return result

if __name__ == '__main__':
    loader = Loader(Normalizer())
    matcher = SimpleMatcher()
    processor = Processor(loader, matcher)
    matches = processor.match()
    with open('data/result.txt', 'w') as result:
        for k, v in matches.iteritems():
            # Some data cleaning
            for item in v:
                if 'normalized_title' in item:
                    item.pop('normalized_title')

            # Write cleaned data to disk
            line = json.dumps({k:v})
            result.write(line)
            result.write('\n')