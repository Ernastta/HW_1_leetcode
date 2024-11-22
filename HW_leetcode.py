# Task 1. 796. Rotate String

def rotate_string(s, goal):

    if len(s) != len(goal):
        return False

    for _ in range(len(s)):
        if s == goal:
            return True
        s = s[1:] + s[0]  # Perform a shift

    return False

# Пример использования
s1 = "abcde"
goal1 = "cdeab"
print(f"'{s1}' can become '{goal1}': {rotate_string(s1, goal1)}")  # Output: True

s2 = "abcde"
goal2 = "abced"
print(f"'{s2}' can become '{goal2}': {rotate_string(s2, goal2)}")  # Output: False

s3 = "aa"
goal3 = "aa"
print(f"'{s3}' can become '{goal3}': {rotate_string(s3, goal3)}") # Output: True

s4 = ""
goal4 = ""
print(f"'{s4}' can become '{goal4}': {rotate_string(s4, goal4)}") # Output: True

s5 = "Aabcde"
goal5 = "abcdeA"
print(f"'{s5}' can become '{goal5}': {rotate_string(s5, goal5)}") # Output: True (case-sensitive comparison)



# Task 2. 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

def isPrefixOfWord(sentence: str, searchWord: str) -> int:
  
    words = sentence.split()
    for i, word in enumerate(words):
        if word.startswith(searchWord):
            return i + 1  # 1-indexed
    return -1

# Пример использования
sentence1 = "i love eating burger"
searchWord1 = "burg"
print(f"Example 1: {isPrefixOfWord(sentence1, searchWord1)}")  # Output: 4

sentence2 = "this problem is an easy problem"
searchWord2 = "pro"
print(f"Example 2: {isPrefixOfWord(sentence2, searchWord2)}")  # Output: 2

sentence3 = "i am tired"
searchWord3 = "you"
print(f"Example 3: {isPrefixOfWord(sentence3, searchWord3)}")  # Output: -1

sentence4 = "hello world"
searchWord4 = "wor"
print(f"Example 4: {isPrefixOfWord(sentence4, searchWord4)}") # Output: 2

sentence5 = "a"
searchWord5 = "a"
print(f"Example 5: {isPrefixOfWord(sentence5, searchWord5)}") #Output: 1


# Task 3. Password Generator

import random
import string

def generate_password(length):

    if length < 4:
        print("Длина пароля должна быть не меньше 4 символов.")
        return None

    all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    password = []

    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.digits))
    password.append(random.choice(string.punctuation))

    for i in range(length - 4):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    return "".join(password)


if __name__ == "__main__":
    try:
        password_length = int(input("Введите желаемую длину пароля: "))
        password = generate_password(password_length)
        if password:
            print("Сгенерированный пароль:", password)
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")
