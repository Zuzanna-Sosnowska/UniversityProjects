import numpy as np


def IEEE_to_number(IEEE):
    mantissa = IEEE[9:]
    mantissa = 1 + (int(mantissa, 2) / 2**23)
    exponent = IEEE[1:9]
    exponent = binary_to_decimal1(exponent) - 127
    sighn = int(IEEE[0])
    return (-1)**sighn * np.power(2, exponent) * mantissa


def binary_to_decimal1(x):
    result = 0
    n = len(x)
    expon = 1
    for i in range(n):
        if x[n-1-i] == '1':
            result += expon
        expon *= 2
    return result


def binary_to_decimal2(x):
    return int(x, 2)


if __name__ == '__main__':
    IEEE = '00111111110110011001100110011001'
    x = IEEE_to_number(IEEE)
    print(x)

    # # Błąd bezwzględny
    # # 1.7 w pythonie zapisywane jest na 64 bitach, stąd różnica między wartością zapisaną w standardzie IEEE, a rzeczywistą
    # # wartością równą 1.7, jest w zaokrągleniu równa poniższej różnicy (64 bitowa reprezentacja dokładniej przybliża wartość 1.7)
    # error1 = np.abs(x - 1.7)
    # print(error1)
    #
    # # Błąd względny
    # error2 = error1 / 1.7
    # print(error2)
    #
    # print(1.7-np.float32(1.7))
