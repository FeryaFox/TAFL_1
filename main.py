from utils import InputUtils, SaveUtils, TerminalUtils, TAFLUtils


def main():
    TerminalUtils.clear()
    alphabet = ""
    la = SaveUtils.load_alphabet()
    if la is None or la == []:
        alphabet = InputUtils.input_alphabet()
        SaveUtils.save_alphabet(alphabet)
        TerminalUtils.clear()
    else:
        print(f"Уже есть сохраненный алфавит '{' '.join(la)}'. Вы хотите использовать его?")

        menu_choice = TerminalUtils.get_choose(
            [
                "Да",
                "Нет"
            ],
            ignore_keyboard_interrupt=False
        )
        if menu_choice is None:
            TerminalUtils.clear()
            exit()
        TerminalUtils.clear()
        match menu_choice:
            case 0:
                alphabet = la
            case 1:
                alphabet = InputUtils.input_alphabet()
                if alphabet is None:
                    TerminalUtils.clear()
                    exit()
                SaveUtils.save_alphabet(alphabet)
                TerminalUtils.clear()

    while True:
        menu_choice = TerminalUtils.get_choose(
            [
                "Найти номер по слову",
                "Найти по слову номер",
                "Изменить алфавит",
                "Выйти"
            ],
            ignore_keyboard_interrupt=False
        )

        if menu_choice is None:
            TerminalUtils.clear()
            exit()
        TerminalUtils.clear()
        match menu_choice:
            case 0:
                word = InputUtils.get_word(alphabet)
                if word is None:
                    TerminalUtils.clear()
                    return None
                if word != "":
                    print("\nПолученный номер: ", TAFLUtils.get_number(word, alphabet), "\n")
                    InputUtils.goto_main_menu()
                TerminalUtils.clear()
            case 1:
                number = InputUtils.get_number()
                if number is None:
                    TerminalUtils.clear()
                    continue
                if number >= 0:
                    print("Полученное слово: ", TAFLUtils.get_word(number, alphabet), "\n")
                    InputUtils.goto_main_menu()
                TerminalUtils.clear()
            case 2:
                alphabet_temp = InputUtils.input_alphabet(alphabet)
                if alphabet_temp is None:
                    TerminalUtils.clear()
                    continue
                alphabet = alphabet_temp
                SaveUtils.save_alphabet(alphabet)
                TerminalUtils.clear()
            case 3:
                TerminalUtils.clear()
                exit()


if __name__ == "__main__":
    main()
