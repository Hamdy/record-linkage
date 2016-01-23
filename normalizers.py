class Normalizer(object):
    """
    Contains normalize() function that does
    text normalization
    """
    def normalize(self, string):
        """
        Normalizes a string
        """
        string = string.replace('_', ' ')
        string = set(string.split()) # remove duplicates
        string = ' '.join(string)
        return ''.join([e.lower() for e in string if e.isalnum() or e == ' '])