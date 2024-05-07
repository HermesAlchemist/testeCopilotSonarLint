def check_even_odd():
    num = eval(input("Digite um número ou código Python: "))
    if num % 2 == 0:
        print(f"{num} é par.")
    else:
        print(f"{num} é ímpar.")

if __name__ == "__main__":
    check_even_odd()