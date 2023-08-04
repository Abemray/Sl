import re

class IgnoreSL:
    def __init__(self, ignore_optional_symbols=False):
        self.ignore_optional_symbols = ignore_optional_symbols
        self.symbol_pattern = r'[!@#$%^&*()\-_=+[\]{};:\'",.<>?/\\|`~]'
        
        self.optional_symbols = []
        
        self.image_pattern = r'\b(?:jpg|jpeg|png|gif)\b'

    def ignore_symbols(self, text):
        cleaned_text = re.sub(self.symbol_pattern, '', text)
        if self.ignore_optional_symbols:
            for optional_symbol in self.optional_symbols:
                cleaned_text = cleaned_text.replace(optional_symbol, '')
        return cleaned_text
    
    def add_optional_symbols(self, symbols):
        self.optional_symbols.extend(symbols)
    
    def remove_optional_symbols(self, symbols):
        for symbol in symbols:
            if symbol in self.optional_symbols:
                self.optional_symbols.remove(symbol)
    
    def find_images(self, text):
        image_matches = re.findall(self.image_pattern, text, flags=re.IGNORECASE)
        return image_matches

# Example usage
if __name__ == "__main__":
    ignore_sl = IgnoreSL(ignore_optional_symbols=True)
    ignore_sl.add_optional_symbols(['*', '_', ':'])

    text = "Hello! This is an example text with *symbols* and an image.jpg."

    cleaned_text = ignore_sl.ignore_symbols(text)
    print("Cleaned Text:", cleaned_text)

    images = ignore_sl.find_images(text)
    print("Images:", images)
