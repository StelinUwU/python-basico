import random
import string

def generate_password():
    uppercase = list(string.ascii_uppercase)
    lowercase = list(string.ascii_lowercase)
    numbers = list(string.digits)
    symbols = list(string.punctuation)
    characters = uppercase + lowercase + numbers + symbols
    size = int(input("Number of password characters: "))
    password = []
    for i in range(size):
        characters_random = random.choice(characters)
        password.append(characters_random)
    password = "".join(password)
    return password

    
def run():
    password = generate_password()
    print("Your new password is :" + password)

if __name__ == "__main__":
    run()
