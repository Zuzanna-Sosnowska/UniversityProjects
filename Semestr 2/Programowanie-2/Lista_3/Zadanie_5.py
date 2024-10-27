def is_equation_right(equation):
    """
    :param equation: Równanie
    :return: Sprawdza, czy nawiasy w równaniu są prawidłowo użyte
    """
    # z równania zadanego jako argument tworzymy listę - str -> list
    list_from_equation = list(equation)
    # tworzymy pustą listę na nawiasy
    brackets_list = []
    # przechodzimy kolejno po każdym elemencie z listy
    for i in range(len(list_from_equation)):
        # jeśli napotkamy jeden z trezch typów nawiasów otwartych, to dodajemy go do listy na nawiasy
        if list_from_equation[i] == '(':
            brackets_list.append('(')
        elif list_from_equation[i] == '[':
            brackets_list.append('[')
        elif list_from_equation[i] == '{':
            brackets_list.append('{')
        elif list_from_equation[i] == '<':
            brackets_list.append('<')

        # jeśli na liście znajduje się nawias zamknięty, to sprawdzamy czy brackets_list jest pusta
        # (to oznacza, że przed nawiasem zamkniętym nie wystąpił żaden nawias otwarty, stąd wiemy, że
        # nawiasy są nieprawidłowe. Jeśli ostatnim elementem w brackets_list nie jest nawias pasujący do
        # nawiasu zamukającego, to oznacza to, że nawiasy są źle zagnieżdżone.
        elif list_from_equation[i] == ')':
            if brackets_list != [] and brackets_list[-1] == '(':
                # jeśli oba warunki zostały spełnione to usuwamy ostatni element (nawias) z brackets_list
                brackets_list.pop()
            else:
                return False

        elif list_from_equation[i] == ']':
            if brackets_list != [] and brackets_list[-1] == '[':
                brackets_list.pop()
            else:
                return False

        elif list_from_equation[i] == '}':
            if brackets_list != [] and brackets_list[-1] == '{':
                brackets_list.pop()
            else:
                return False

        elif list_from_equation[i] == '>':
            if brackets_list != [] and brackets_list[-1] == '<':
                brackets_list.pop()
            else:
                return False

    # jeśli końcowo lista nawiasów będzie pusta, to oznacza to, że nawiasy zostały prawidłowo zapisane w równaniu
    if not brackets_list:
        return True
    else:
        return False


print(is_equation_right('7*(-2+[-9*<12/8>*(1/2)/{9/[2/7]*(16/5)}])'))
print(is_equation_right('7*(-2-9*{)12/8}*(1/2)/{9/[2/7]*(16/5)}])'))
