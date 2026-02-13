from modules.hash_engine import HashEngine
from modules.attack_engine import AttackEngine
from modules.dictionary_generator import DictionaryGenerator
from modules.strength_analyzer import StrengthAnalyzer


def show_menu():
    print("\n===== Credential Attack Suite =====")
    print("1. Generate Hash")
    print("2. Dictionary Attack")
    print("3. Generate Dictionary")
    print("4. Analyze Password Strength")
    print("5. Exit")


def main():
    hash_engine = HashEngine()
    attack_engine = AttackEngine()
    dictionary_generator = DictionaryGenerator()
    strength_analyzer = StrengthAnalyzer()

    while True:
        show_menu()
        choice = input("Select option: ")

        if choice == "1":
            password = input("Enter password: ")
            algorithm = input("Enter algorithm (md5/sha1/sha256): ")
            result = hash_engine.generate_hash(password, algorithm)
            print("\nGenerated Hash:", result)

        elif choice == "2":
            target_hash = input("Enter target hash: ")
            wordlist_path = input("Enter wordlist path: ")
            algorithm = input("Enter algorithm (md5/sha1/sha256): ")

            result = attack_engine.dictionary_attack(
                target_hash,
                wordlist_path,
                algorithm
            )

            if result:
                print("\n[+] Password Found:", result)
            else:
                print("\n[-] Password Not Found")

        elif choice == "3":
            base_word = input("Enter base word: ")
            output_file = input("Enter output file name: ")
            dictionary_generator.generate_dictionary(base_word, output_file)
            print("\n[+] Dictionary Generated")

        elif choice == "4":
            password = input("Enter password to analyze: ")
            analysis = strength_analyzer.analyze_strength(password)

            print("\nPassword Strength Analysis:")
            for key, value in analysis.items():
                print(f"{key}: {value}")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
