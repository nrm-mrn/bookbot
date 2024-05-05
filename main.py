def get_file_contents(filename):
    with open(f"books/{filename}.txt") as f:
        return f.read()
    
def get_words_count(string_to_count):
    return len(string_to_count.split())

def count_symbols(string_to_count):
    string_to_count = string_to_count.lower()
    library = {}
    for ch in string_to_count:
        if ch.isalpha():
            if ch in library:
                library[ch]+=1
            else:
                library[ch]=1
    return library

def generate_report(filename):
    text = get_file_contents(filename)
    words_count = get_words_count(text)
    library = count_symbols(text)
    list_library = []
    for symbol in library:
        list_library.append({"symbol": symbol, "num": library[symbol]})

    def sort_key(dict):
        return dict["num"]

    list_library.sort(reverse=True, key=sort_key)

    print(f"--- Begin report of the book {filename} ---\n\
          {words_count} words found in the book\n")
    for item in list_library:
        print(f"The {item["symbol"]} character was found {item["num"]} times")
    print("--- End of the Report ---")
    

def main():
    while True:
        try:
            book = input("type the name of the book to analyze\n\
The file should exist in ./books folder with txt extention!\n\
q for exit\n")
            if book == "q":
                break
            generate_report(book)
            break
        except FileNotFoundError:
            print("No file found, check again")

main()