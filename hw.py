def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
def square_numbers(numbers):
    return [num ** 2 for num in numbers]
def convert_to_uppercase(words):
    return [word.upper() for word in words]
def main():
    numbers = [1,2,3,4,5,6]
    words = ['hello', 'world']
    evens = get_even_numbers(numbers)
    squares = square_numbers(numbers)
    print("Squared numbers: ", squares)
    upper_words = convert_to_uppercase(words)
    print("Uppercase words: ", upper_words)
if __name__ == "__main__":
    main()
