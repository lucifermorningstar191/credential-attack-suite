class DictionaryGenerator:

    def generate_dictionary(self, base_word, output_file):
        variations = [
            base_word,
            base_word.lower(),
            base_word.upper(),
            base_word.capitalize(),
            base_word + "123",
            base_word + "2024",
            base_word + "!",
            base_word + "@123"
        ]

        with open(output_file, "w") as file:
            for word in variations:
                file.write(word + "\n")
