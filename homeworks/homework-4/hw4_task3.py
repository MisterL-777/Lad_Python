# Палиндром

def is_palindrome(text: str) -> bool:
    cleaned = []
    for char in text.lower():
        if char.isalnum():
            cleaned.append(char)
    cleaned = "".join(cleaned)

    return cleaned == cleaned[::-1]

print(f"Это палидром? : {is_palindrome('А роза упала на лапу Азора')}")
print(f"Это палидром? : {is_palindrome('Привет')}")
