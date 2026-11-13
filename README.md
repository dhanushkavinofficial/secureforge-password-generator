<div align="center">

# 🔐 SecureForge

### Cryptographically Secure Password Generator

[![CI](https://github.com/YOUR_USERNAME/secureforge-password-generator/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/secureforge-password-generator/actions)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)

![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)

</div>

---

## 📖 Overview

**SecureForge** is a Python command-line tool that generates strong, unpredictable passwords using Python's `secrets` module, which is backed by the operating system's cryptographically secure random number generator (CSPRNG).

It also estimates the entropy of each generated password and rates its strength. The project is built with a clean, modular architecture, automated tests, and CI.

## ✨ Features

- 🔒 Cryptographically secure generation (`secrets`, never `random`)
- 📏 Configurable length from 20 to 128 characters
- ✅ Guaranteed lowercase, uppercase, digit, and symbol in every password
- 🔀 Secure shuffle, so required characters never sit in predictable positions
- 📊 Entropy estimation with a strength rating
- 💻 Interactive mode and flag-based CLI
- 🔢 Bulk generation (up to 100 passwords)
- 🧪 Unit-tested, with GitHub Actions CI on Python 3.10 to 3.13
- 📦 Zero external dependencies (standard library only)

## 🚀 Installation

```bash
git clone https://github.com/YOUR_USERNAME/secureforge-password-generator.git
cd secureforge-password-generator
python -m pip install -e .
```

**Requirements:** Python 3.10 or higher

## 🛠️ Usage

### Interactive mode

```bash
python -m secureforge
```

### Command-line flags

```bash
# Generate a 32-character password with a label
python -m secureforge --length 32 --label GitHub

# Generate 5 passwords, output only the passwords
python -m secureforge --length 24 --count 5 --quiet

# After installation, the shorter command also works
secureforge -l 32
```

| Flag | Short | Description | Default |
|------|-------|-------------|---------|
| `--length` | `-l` | Password length (20-128) | prompted (32) |
| `--label` | `-n` | Display-only label, e.g. `GitHub` | none |
| `--count` | `-c` | Number of passwords (1-100) | 1 |
| `--quiet` | `-q` | Print only the password(s) | off |

### Example output

```text
==================================================
             SECUREFORGE
      Secure Password Generator
==================================================

Password label   : GitHub
Password length  : 32
Estimated entropy: 194.49 bits (Very strong)
==================================================

Generated password(s):
r{-Ss7?}&iqb+MW&D&]QPFNK2{YyVEQD
```

### Use as a Python library

```python
from secureforge import generate_password, estimate_entropy

password = generate_password(32)
bits = estimate_entropy(32)
print(password, f"{bits:.1f} bits")
```

## 🏗️ Project Structure

```text
secureforge-password-generator/
├── src/
│   └── secureforge/
│       ├── __init__.py      # Public API
│       ├── __main__.py      # python -m secureforge entry point
│       ├── generator.py     # Secure password generation
│       ├── entropy.py       # Entropy estimation and strength rating
│       └── cli.py           # Command-line interface
├── tests/
│   ├── test_generator.py
│   ├── test_entropy.py
│   └── test_cli.py
├── docs/
│   └── security.md          # Security design notes
├── .github/workflows/ci.yml # Continuous integration
├── pyproject.toml
├── requirements.txt
├── LICENSE
└── README.md
```

## 🔐 Security Design

- **Secure randomness:** all randomness comes from `secrets` (OS CSPRNG).
- **Label is not an input:** the name or label is display-only. It is never used to derive the password, so knowing it gives an attacker no advantage.
- **No deterministic derivation:** passwords are never generated from names, birthdays, emails, or other personal data.
- **Entropy estimate:** the estimate models the independent random character choices. It is a conservative approximation, ignores the extra randomness from the shuffle, and is not a formal proof of the exact output space.
- **Best practice:** use a unique password per account and store them in a password manager.

See [docs/security.md](docs/security.md) for details.

## 🧪 Running Tests

```bash
python -m unittest discover -s tests -v
```

## 🗺️ Roadmap

- [x] **v1.0**: secure generation, entropy estimate, CLI, tests, CI
- [ ] **v1.1**: configurable character policies (exclude ambiguous characters, symbol sets)
- [ ] **v1.2**: passphrase mode
- [ ] **v1.3**: clipboard integration with auto-clear
- [ ] **v1.4**: GUI interface
- [ ] **v2.0**: encrypted local password vault

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Make sure the tests pass
5. Push and open a Pull Request

## 📄 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for details.

## 👤 Author

**Dhanush Kavin G**
Software Engineer | Java • Python • Spring Boot

⭐ If you find this project useful, consider giving it a star!
