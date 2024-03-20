class InputUtils:
    @staticmethod
    def input_alphabet(previous: list = None) -> list | None:

        input_phrase = "Введите пожалуйста алфавит через пробел(пример: 'a b c)': " \
            if previous is None \
            else f"Введите пожалуйста алфавит через пробел(пример: 'a b c')(Предыдущий '{' '.join(previous)}'): "

        while True:
            try:
                alphabet = input(input_phrase).split()
            except KeyboardInterrupt:
                return None
            error = False

            if not alphabet:
                return None

            if len(alphabet) < 2:
                print("Вы ввели недопустимый алфавит. Длина алфавита должна быть не меньше 2.")
                continue

            j = 0
            for i in alphabet:
                if i in alphabet[j + 1:]:
                    print("Вы ввели недопустимый алфавит. В веденном алфавите есть повторяющийся символ.")
                    error = True
                    break

                if len(i) != 1:
                    error = True
                    print("Вы ввели недопустимый алфавит. Скорее всего вы ввели двойной символ")
                    break

                j += 1

            if error:
                continue
            break

        return alphabet

    @staticmethod
    def get_number() -> int | None:
        while True:
            try:
                number = input("Видете целое число - Лексико Графический Номер (или Enter для выхода): ")
                if number == "":
                    return None
                number = int(number)
            except KeyboardInterrupt:
                return None
            except ValueError:
                print("Вы ввели не число. Повторите ввод.")
                continue
            if number < 0:
                print("Вы ввели число меньше 0. (Лексико Графический номер не может быть отрицательным")
                continue

            return number

    @staticmethod
    def get_word(alphabet: list) -> str | None:
        while True:

            error = False
            try:
                word = input("Введите слово (или Enter для выхода): ")
            except KeyboardInterrupt:
                return None
            if len(word) == 0:
                return ""
            for i in word:
                if i not in alphabet:
                    print("Вы ввели слово, буквы которого нет в заданном алфавите.")
                    error = True
                    break
            if error:
                continue

            return word

    @staticmethod
    def goto_main_menu():
        try:
            input("Нажмите Enter для возврата в главное меню. ")
        except KeyboardInterrupt:
            pass

