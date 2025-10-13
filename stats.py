def count_words(text: str):
    return len(text.split())

def get_unique_char(text: str):
    words = text.split()
    struc = {}
    for word in words:
        for char in word:
            if char.lower() not in struc:
                struc.update({f"{char.lower()}": 0})
            struc[char.lower()] += 1 

    return struc

def sort_on(items):
    return items["num"]

def sort_dict(charachters: dict):
    new = []
    for key, value in charachters.items():
        new.append({"char": key, "num": value})

    new.sort(reverse=True, key=sort_on)
    return new

