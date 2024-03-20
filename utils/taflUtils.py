from .numberUtils import NumberUtils


class TAFLUtils:
    @staticmethod
    def get_number(word: str, alphabet: list[str]) -> int:
        print("\nАлфавит: " + ', '.join(alphabet))

        n = len(alphabet)
        k = len(word)

        print(f"{n=}, {k=}\n")
        formula = ""

        result = 0
        for i in range(1, k + 1):
            char = word[i - 1]
            result += (n ** (k - i)) * (alphabet.index(char) + 1)
            formula += f"{n}{NumberUtils.covert_number_to_degree(k - i)} * {alphabet.index(char) + 1} + "

        formula = formula[:-3] + f" = {result}"
        print(formula)

        return result

    @staticmethod
    def get_word(number: int, alphabet: list) -> str:
        print("\nАлфавит: " + ', '.join(alphabet))

        n = len(alphabet)

        if number <= n:
            if number == 0:
                return '*Пустой символ*'
            return alphabet[number - 1]

        print(f"{n=}, {number=}\n")
        formula_template = "({k}) * {n} + {remainder} "
        formula = formula_template
        left_part = ""

        char_index_list = []

        k = number
        while True:

            if k % n == 0:
                k = (k // n) - 1
                remainder = n
            else:
                remainder = k % n
                k = k // n

            char_index_list.append(remainder)
            if k > n:
                left_part += formula.format(k=k, n=n, remainder=remainder) + " = "
                formula = formula.format(k=formula_template, n=n, remainder=remainder)
            else:
                char_index_list.append(k)
                formula = formula.format(k=k, n=n, remainder=remainder)
                break

        char_index_list.reverse()

        print(number, " = ", left_part, formula)

        end_formula = ""
        word = ""

        k = len(char_index_list)
        for index in range(len(char_index_list)):
            i = char_index_list[index]
            word += alphabet[i - 1]
            k = k - 1
            end_formula += f"{n}{NumberUtils.covert_number_to_degree(k)} * {i} + "

        end_formula = end_formula[:-3]

        print(end_formula)
        print("\nИндекса букв в алфавите: ", ', '.join(map(str, char_index_list)))
        return word

