from zxcvbn import zxcvbn

def analyze_password(password):
    result = zxcvbn(password)
    print(f"\nPassword Score (0–4): {result['score']}")
    print("Feedback:")
    for suggestion in result['feedback']['suggestions']:
        print(f"- {suggestion}")

def get_user_inputs():
    inputs = []
    inputs.append(input("Enter your name: "))
    inputs.append(input("Enter your pet's name: "))
    inputs.append(input("Enter your birth year: "))
    inputs.append(input("Enter a favorite word: "))
    return inputs

def generate_wordlist(user_inputs):
    common_patterns = ['', '123', '!', '@', '#', '2024']
    leet = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$'}

    wordlist = set()

    for item in user_inputs:
        for pattern in common_patterns:
            wordlist.add(item + pattern)
            wordlist.add(item.lower() + pattern)
            wordlist.add(item.upper() + pattern)
            wordlist.add(item.capitalize() + pattern)
        
        # Leetspeak version
        leet_word = ''.join(leet.get(c, c) for c in item.lower())
        wordlist.add(leet_word)

    return list(wordlist)

def export_wordlist(wordlist, filename='custom_wordlist.txt'):
    with open(filename, 'w') as f:
        for word in wordlist:
            f.write(word + '\n')
    print(f"\n✅ Wordlist saved as {filename}")

def main():
    print("=== Password Strength Analyzer ===")
    password = input("Enter a password to analyze: ")
    analyze_password(password)

    print("\n=== Custom Wordlist Generator ===")
    inputs = get_user_inputs()
    wordlist = generate_wordlist(inputs)
    export_wordlist(wordlist)

if __name__ == "__main__":
    main()
