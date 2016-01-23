class Matcher(object):
    """
    Parent class for all matchers
    Matchers are meant to tell whether
    2 strings are highly matched or not
    """
    
    def match(self, str1, str2):
        """
        @Overrideme
        """
        raise NotImplementedError()

class FuzzyMatcher(Matcher):
    """
    Uses fuzzywuzzy & python-Levenshtein
    This is generic matcher
    """
    THRESHOLD = 100
    
    def match(self, str1, str2):
        """
        2 strings are matched if their similarity
        >= THRESHOLD
        """
        from fuzzywuzzy import fuzz
        return fuzz.partial_ratio(str1, str2) >= self.THRESHOLD
    
class SimpleMatcher(Matcher):
    """
    Application specific matcher that checks if model in title
    """
    def match(self, title, model_or_name):
        splitted_title = title.split()
        # Check whole model name
        if model_or_name in splitted_title:
            return True
        #check parts of the model name
        for item in splitted_title:
            if model_or_name in item:
                return True
        return False