from blessed import Terminal


def draw_dialpad():
    print(term.clear())
    print(term.move( 0, 0) + "_________________")
    print(term.move( 1, 0) + "Доступные символы")
    print(term.move( 2, 0) + "(Циферблат телефона)")
    print(term.move( 3, 0) + "+---+---+---")
    print(term.move( 4, 0) + "| 1 | 2 | 3 ")
    print(term.move( 5, 0) + "+---+---+---")
    print(term.move( 6, 0) + "| 4 | 5 | 6 ")
    print(term.move( 7, 0) + "+---+---+---")
    print(term.move( 8, 0) + "| 7 | 8 | 9 ")
    print(term.move( 9, 0) + "+---+---+---")
    print(term.move(10, 0) + "| + | 0 | <Enter> (Позвонить)")


def main():
    number = ""
    while True:
        draw_dialpad()
        print(term.move(11, 0) + "_________________" + "_" * len(number))
        print(term.move(12, 0) + "Набранный номер: " + number)
        key = term.inkey()
        if key.is_sequence:
            if key.name == "KEY_ENTER":
                if number:
                    print(term.clear())
                    print("Вызванный номер: " + number)
                    break
            elif key.name == "KEY_BACKSPACE":
                number = number[:-1]
        elif key.isprintable:
            if key == "+":
                number += "+"
            elif key.isdigit():
                number += key


if __name__ == "__main__":
    try:
        term = Terminal()
        with term.cbreak():
            main()
    except AttributeError as ae:
        print("Try opening terminal before the run...")
