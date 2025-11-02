def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    dict_chars = {} 
    for char in text:        
        if char.isalpha():  
            char = char.lower()  
            if char in dict_chars:
                dict_chars[char]["nums"]  += 1
               
            else:
                dict_chars[char] = { "chars": char, "nums": 1 }
    return dict_chars

def sort_on(items):
    return items["nums"]

def sort_characters(dictionary):
    dictionary_list = list(dictionary.values())
    dictionary_list.sort(key=sort_on, reverse=True)
    return dictionary_list
