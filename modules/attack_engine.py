import time
import hashlib


class AttackEngine:

    def dictionary_attack(self, target_hash, wordlist_path, algorithm="sha256"):
        start_time = time.time()
        attempts = 0

        try:
            with open(wordlist_path, "r") as file:
                for line in file:
                    word = line.strip()
                    attempts += 1

                    hashed_word = self._hash(word, algorithm)

                    if hashed_word == target_hash:
                        end_time = time.time()
                        return {
                            "status": "SUCCESS",
                            "password": word,
                            "attempts": attempts,
                            "time": round(end_time - start_time, 4)
                        }

        except FileNotFoundError:
            return {"status": "WORDLIST NOT FOUND"}

        end_time = time.time()

        return {
            "status": "FAILED",
            "attempts": attempts,
            "time": round(end_time - start_time, 4)
        }

    def _hash(self, password, algorithm):
        password_bytes = password.encode()

        if algorithm.lower() == "md5":
            return hashlib.md5(password_bytes).hexdigest()

        elif algorithm.lower() == "sha1":
            return hashlib.sha1(password_bytes).hexdigest()

        elif algorithm.lower() == "sha256":
            return hashlib.sha256(password_bytes).hexdigest()

        else:
            raise ValueError("Unsupported algorithm")
