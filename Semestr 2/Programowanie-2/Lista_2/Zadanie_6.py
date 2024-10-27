def math_operation(text: str):
    """
    :param text: łańcuch znaków (działanie matematyczne)
    :return: słupek z wykonanym działaniem
    """
    # Tworzy listę z zadanego łąńcucha znaków
    math_list = list(text)
    for i in range(len(math_list)):
        # jeśli natrafilmy na znak + lub -
        if math_list[i] in ['+', '-']:
            first_digit = ""
            # pierwsza liczba jako zmienna typu str
            first_digit = first_digit.join(math_list[0:i])
            last_digit = ""
            # analogicznie do pierwszej liczby zmienna typu str
            last_digit = last_digit.join(math_list[i+1:len(math_list)])
            # if dla dodawania
            if math_list[i] == '+':
                # wynik suny dwóch liczb
                result = int(first_digit) + int(last_digit)
            # dla odejmowania mamy
            else:
                # wynik różnicy dwóch liczb
                result = int(first_digit) - int(last_digit)
            # w przypadku, kiedy pierwsza liczba składa się z tej samej bądź większej ilości cyfr co druga liczba
            if len(first_digit) >= len(last_digit):
                # przerwa przed drugą liczbą
                space_between_1 = ' ' * (1 + len(first_digit) - len(last_digit))
                floor = '_' * (2 + len(first_digit))
                # przerwa przed wynikiem
                space_between_2 = ' ' * (len(floor) - len(str(result)))
                return ('  ' + first_digit + "\n" + math_list[i] + space_between_1 + last_digit + "\n" + floor + "\n" + space_between_2 + str(result))
            # przypadek, kiedy druga liczba składa się z większej ilości cyfr niż pierwsza liczba
            else:
                # przerwa przed pierwszą liczbą
                space_between_1 = ' ' * (2 + len(last_digit) - len(first_digit))
                floor = '_' * (2 + len(last_digit))
                # przerwa przed wynikiem
                space_between_2 = ' ' * (len(floor) - len(str(result)))
                return (space_between_1 + first_digit + "\n" + math_list[i] + ' ' + last_digit + "\n" + floor + "\n" + space_between_2 + str(result))
        # dla mnożenia mamy
        elif math_list[i] == '*':
            first_digit = ""
            first_digit = first_digit.join(math_list[0:i])
            last_digit = ""
            last_digit = last_digit.join(math_list[i + 1:len(math_list)])
            # wynik mnożenia dwóch liczb
            result = int(first_digit) * int(last_digit)

            # przezrwa przed pierwszą cyfrą
            space_between_1 = ' ' * (len(str(result)) - len(first_digit) + 2)
            # przezrwa przed drugą cyfrą
            space_between_2 = ' ' * (len(str(result)) - len(last_digit) + 1)
            floor = '_' * (2 + len(str(result)))
            return (space_between_1 + first_digit + "\n" + math_list[i]
                    + space_between_2 + last_digit + "\n" + floor + "\n" + "  " + str(result))

if __name__ == '__main__':
    print(math_operation('123*9999') + '\n')
    print(math_operation('123-9999') + '\n')
    print(math_operation('1224757+9999'))