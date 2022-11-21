from operations import addition, subtraction, multiplication, division

def main():
    a = 9
    b = 7
    print("The results of applying the 4 fundamental operations are as follows:")
    print("Sumar:", addition.sumar(a, b))
    print("Restar:", subtraction.restar(a, b))
    print("Multiplicar:", multiplication.multiplicar(a, b))
    print("Dividir:", division.dividir(a, b))

if __name__ == "__main__":
    main()
