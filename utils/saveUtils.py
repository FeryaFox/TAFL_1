class SaveUtils:
    @staticmethod
    def load_alphabet() -> list | None:
        try:
            with open('alphabet.txt', 'r', encoding="utf-8") as f:
                return f.read().split()
        except FileNotFoundError:
            return None

    @staticmethod
    def save_alphabet(alphabet: list) -> None:
        with open('alphabet.txt', 'w', encoding="utf-8") as f:
            f.write(' '.join(alphabet))
