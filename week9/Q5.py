def find_max_alphabet_instances(file_path):

    alphabet_count = {}

    with open(file_path, 'r') as f:
        for line in f:
            for char in line:
                if char.isalpha():  
                    char = char.lower()  
                    alphabet_count[char] = alphabet_count.get(char, 0) + 1

    max_count = max(alphabet_count.values())

    max_alphabets = [char for char, count in alphabet_count.items() if count == max_count]

    print(f"Alphabets with the maximum occurrences {max_count} instances): {', '.join(max_alphabets)}")


file_path = 'ques5.txt'
find_max_alphabet_instances(file_path)
