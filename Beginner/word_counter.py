def word_counter():

    text = input("Enter a sentence: ")

    numbers_of_words = len(text.split())

    print(f"Total number of words: {numbers_of_words}")

word_counter()