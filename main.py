def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    book_words = get_book_words(text)
    print(f"{book_words} words found in the document\n")
    #print(file_contents)
    
    count_characters = get_count_characters(text)
    #print(count_characters)

    char_list = [{"character": char, "count": count} for char, count in count_characters.items()]
    char_list.sort(key=lambda x: x["count"], reverse=True)

    
    for entry in char_list:
        print(f"The '{entry['character']}' character was found {entry['count']} times")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_book_words(file_contents):
    words = file_contents.split()
    return len(words)

def get_count_characters(file_contents):
    char_count = {}
    lowered_string = file_contents.lower()
    
    for character in lowered_string:
        if character.isalpha():
            if character in char_count:
                char_count[character] += 1
            else:
                char_count[character] = 1
        
    


    return char_count


    

main()
