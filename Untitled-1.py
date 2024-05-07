def check_even_odd():
    num = eval(input("Digite um número ou código Python: "))
    if num % 2 == 0:
        print(f"{num} é par.")
    else:
        print(f"{num} é ímpar.")

if __name__ == "__main__":
    check_even_odd()import os

def check_even_odd():
    num = eval(input("Digite um número ou código Python: "))
    if num % 2 == 0:
        print(f"{num} é par.")
    else:
        print(f"{num} é ímpar.")

def write_to_file():
    file = open("output.txt", "w")
    file.write("Este é um teste.")

def delete_file():
    os.remove("output.txt")

if __name__ == "__main__":
    check_even_odd()
    write_to_file()
    delete_file()