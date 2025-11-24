class TextProcessor:

    def __init__(self):
        self.processed_texts = []
    
    def capitalize_text(self, text):
        """Szöveg nagybetűssé alakítása"""
        if not text:
            return ""
        return text.upper()
    
    def reverse_text(self, text):
        """Szöveg megfordítása"""
        if not text:
            return ""
        return text[::-1]
    
    def count_words(self, text):
        """Szavak számolása"""
        if not text:
            return 0
        return len(text.split())
    
    def is_palindrome(self, text):
        """Palindróma ellenőrzés (pl. "anna" -> True)"""
        if not text:
            return False
        cleaned = text.lower().replace(" ", "")
        return cleaned == cleaned[::-1]


    def remove_spaces(self, text):
        """Szóközök eltávolítása"""
        if not text:
            return ""
        return text.replace(" ", "")
    



