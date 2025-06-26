
import random

def get_prediction():
    number = random.randint(0, 9)
    color = "Green" if number in [1, 3, 7, 9] else "Red" if number in [2, 4, 6, 8] else "Violet"
    size = "Big" if number >= 5 else "Small"
    return {
        "number": number,
        "color": color,
        "size": size
    }
