import string


class StrengthAnalyzer:

    def analyze_strength(self, password):
        analysis = {}

        length = len(password)
        analysis["Length"] = length

        if length < 6:
            analysis["Strength"] = "Very Weak"
        elif length < 8:
            analysis["Strength"] = "Weak"
        elif length < 12:
            analysis["Strength"] = "Moderate"
        else:
            analysis["Strength"] = "Strong"

        analysis["Has Uppercase"] = any(c.isupper() for c in password)
        analysis["Has Lowercase"] = any(c.islower() for c in password)
        analysis["Has Digit"] = any(c.isdigit() for c in password)
        analysis["Has Special Character"] = any(c in string.punctuation for c in password)

        return analysis
