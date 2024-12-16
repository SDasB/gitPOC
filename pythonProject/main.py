import itertools

target_password = "ab89"
character_set = "ab89"
print(f"Password cracker 1234"+target_password)
for length in range(1,5):
    for combination in itertools.product(character_set, repeat=length):
        print(combination)
        guess = "".join(combination)
        if guess == target_password:
            print(f"Password cracked123: {guess}")
            break
