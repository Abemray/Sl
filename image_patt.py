import re

class ImagePatterns:
    def __init__(self):
        self.patterns = {
            'jpg': r'\b(?:jpg|jpeg)\b',
            'png': r'\bpng\b',
            'gif': r'\bgif\b',
            'bmp': r'\bbmp\b',
            'svg': r'\bsvg\b'
            # Add more patterns as needed
        }

    def find_images(self, text):
        images = {}
        for format, pattern in self.patterns.items():
            image_matches = re.findall(pattern, text, flags=re.IGNORECASE)
            if image_matches:
                images[format] = image_matches
        return images

# Example usage
if __name__ == "__main__":
    image_patterns = ImagePatterns()

    text = "Here are some images: cat.jpg, dog.png, nature.jpeg, sunset.svg."

    images = image_patterns.find_images(text)
    print("Images:", images)
