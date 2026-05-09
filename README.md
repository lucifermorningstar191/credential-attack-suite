# 🔐 Credential Attack Suite

> **Educational Python tool for understanding password security, hashing mechanisms, and credential-based attack simulation.**

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-557C94?style=flat-square&logo=linux)
![Purpose](https://img.shields.io/badge/Purpose-Educational-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 📌 Overview

The **Credential Attack Suite** is a modular Python-based toolkit built to simulate and understand how credential-based attacks work in controlled, educational environments. It demonstrates the mechanics behind dictionary attacks, hash cracking, wordlist generation, and password strength evaluation — skills core to any cybersecurity practitioner's toolkit.

> ⚠️ **This tool is built strictly for educational purposes and authorized security testing only. Never use against systems you don't own or have explicit written permission to test.**

---

## 🎯 What This Project Demonstrates

| Concept | Description |
|---|---|
| **Hashing Mechanisms** | MD5, SHA1, SHA256 hash generation and analysis |
| **Dictionary Attack Logic** | Simulated wordlist-based credential testing |
| **Wordlist Generation** | Dynamic generation of candidate password lists |
| **Password Strength Analysis** | Evaluating passwords against complexity rules |

---

## 🗂️ Project Structure

```
credential-attack-suite/
│
├── modules/
│   ├── hasher.py          # Hash generation (MD5, SHA1, SHA256)
│   ├── dictionary.py      # Dictionary attack simulation logic
│   ├── wordlist_gen.py    # Wordlist generation module
│   └── strength.py        # Password strength analyser
│
├── images/                # Screenshots and output evidence
├── main.py                # Entry point — interactive menu
└── README.md
```

---

## ⚙️ Requirements

- Python 3.x
- Kali Linux (or any Linux distro)
- No external dependencies — uses Python standard library

---

## 🚀 Usage

Clone the repository and run:

```bash
git clone https://github.com/lucifermorningstar191/credential-attack-suite.git
cd credential-attack-suite
python3 main.py
```

You'll be presented with an interactive menu:

```
╔══════════════════════════════╗
║   Credential Attack Suite    ║
╚══════════════════════════════╝
  [1] Hash Generator
  [2] Dictionary Attack Simulation
  [3] Wordlist Generator
  [4] Password Strength Analyser
  [0] Exit
```

---

## 🔍 Module Breakdown

### 1. Hash Generator
Generates MD5, SHA1, and SHA256 hashes for any input string — useful for understanding how password storage works and why plain MD5/SHA1 are weak.

```
Input:  password123
MD5:    482c811da5d5b4bc6d497ffa98491e38
SHA1:   cbfdac6008f9cab4083784cbd1874f76618d2a97
SHA256: ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
```

### 2. Dictionary Attack Simulation
Simulates how an attacker iterates through a wordlist to match a target hash. Demonstrates why weak or common passwords are trivially cracked.

### 3. Wordlist Generator
Generates candidate wordlists based on patterns, character sets, and length constraints — illustrating how attackers build targeted password lists.

### 4. Password Strength Analyser
Evaluates passwords against common complexity rules (length, character diversity, common patterns) and returns a strength score with feedback.

---

## 🛡️ Defensive Takeaways

Building this tool reinforced key defensive insights:

- **Never store passwords as plain MD5/SHA1** — use bcrypt, Argon2, or scrypt
- **Common passwords are cracked in seconds** — enforce complexity requirements
- **Rate limiting & account lockout** are critical controls against brute-force
- **MFA eliminates the risk** of credential stuffing attacks entirely

---

## 📸 Screenshots

Output screenshots and demo runs are available in the `images/` directory.

---

## 🧠 Skills Demonstrated

- Python modular scripting
- Hashing and cryptographic concepts
- Offensive simulation for defensive understanding
- Security tool development
- Git/GitHub workflow and documentation

---

## 👤 Author

**Varun Dev Rawal**
Cybersecurity Practitioner | Ethical Hacker | BCA @ Amity University

- 🔗 [GitHub](https://github.com/lucifermorningstar191)
- 🔗 [LinkedIn](https://linkedin.com/in/varun-dev-rawal-210985361)
- 📧 veerrawal36@gmail.com

---

## ⚖️ Disclaimer

This project is created **for educational and research purposes only**.
The author does not condone or support unauthorized access to any system.
Always obtain written permission before testing any system you do not own.
