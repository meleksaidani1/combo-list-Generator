import itertools

def generate_combos(emails, passwords):
    combos = list(itertools.product(emails, passwords))
    return combos

def save_combos(combos, filename):
    with open(filename, 'w') as file:
        for combo in combos:
            file.write(f'{combo[0]}:{combo[1]}\n')

print("Combo List Generator")
print("Enter emails separated by spaces:")
emails = input().split()

print("Enter passwords separated by spaces:")
passwords = input().split()

combo_list = generate_combos(emails, passwords)

print(f"Generated {len(combo_list)} combos.")
filename = input("Enter a filename to save the combo list: ")

save_combos(combo_list, filename)
print(f"Combo list saved to {filename}.")
