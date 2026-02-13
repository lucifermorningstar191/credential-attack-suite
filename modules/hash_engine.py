import hashlib


class HashEngine:

    def generate_hash(self, password, algorithm="sha256"):
        password_bytes = password.encode()

        if algorithm.lower() == "md5":
            return hashlib.md5(password_bytes).hexdigest()

        elif algorithm.lower() == "sha1":
            return hashlib.sha1(password_bytes).hexdigest()

        elif algorithm.lower() == "sha256":
            return hashlib.sha256(password_bytes).hexdigest()

        else:
            raise ValueError("Unsupported algorithm")

    def identify_hash(self, hash_string):
        length = len(hash_string)

        if length == 32:
            return "MD5"
        elif length == 40:
            return "SHA1"
        elif length == 64:
            return "SHA256"
        else:
            return "Unknown"
