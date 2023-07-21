def is_balanced(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return "NO"
        else:
            stack.append(char)

    return "YES" if not stack else "NO"

def main():
    input_string = input("Masukkan tanda kurung: ")
    result = is_balanced(input_string)
    print(result)

if __name__ == "__main__":
    main()
