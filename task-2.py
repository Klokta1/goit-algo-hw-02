from collections import deque

def is_palindrome(s):
    s = s.replace(" ", "").lower()

    char_deque = deque(s)

    while len(char_deque) > 1:
        left = char_deque.popleft()
        right = char_deque.pop()

        if left != right:
            return False

    return True

# Приклади рядків для тестування
test_cases = {
    "Abc cba": True,  # Парна кількість символів, паліндром
    "Race car": True, # Непарна кількість символів, паліндром
    "Hello": False   # Не паліндром
}

def test_palindromes():
    for test_string, expected in test_cases.items():
        result = is_palindrome(test_string)
        if result == expected:
            print(f"Тест для '{test_string}' пройдено.")
        else:
            print(f"Тест для '{test_string}' НЕ пройдено. Очікувалося: {expected}, отримано: {result}.")

test_palindromes()


