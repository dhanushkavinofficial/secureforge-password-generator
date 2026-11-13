# SecureForge 🔐
### Cryptographically Secure Password Generator

![CI](https://github.com/YOUR_USERNAME/secureforge-password-generator/actions/workflows/ci.yml/badge.svg)

SecureForge generates strong, unpredictable passwords using Python's
`secrets` module, with entropy estimation and a clean CLI.

## Features
- Cryptographically secure generation (`secrets`)
- Length 20–128, guaranteed lowercase/uppercase/digit/symbol
- Entropy estimate + strength rating
- Interactive mode and flag-based CLI (`--length`, `--count`, `--quiet`)
- Unit tests, CI, zero external dependencies

## Requirements
Python 3.10+

## Installation
```bash
git clone https://github.com/YOUR_USERNAME/secureforge-password-generator.git
cd secureforge-password-generator
python -m pip install -e .
```

## Usage
```bash
# Interactive
python -m secureforge

# One-liners
python -m secureforge -l 32 -n GitHub
python -m secureforge -l 24 -c 5 -q

# After install, also available as:
secureforge -l 32
```

## Example
```text
==================================================
             SECUREFORGE
      Secure Password Generator
==================================================

Password label   : GitHub
Password length  : 32
Estimated entropy: 205.xx bits (Very strong)
```

## Tests
```bash
python -m unittest discover -s tests
```
(If not installed: `PYTHONPATH=src python -m unittest discover -s tests`)

## Project structure
```
src/secureforge/   generator.py, entropy.py, cli.py
tests/             unit tests
docs/security.md   security notes
```

## Security
See [docs/security.md](docs/security.md). The label is display-only and is
never used to derive the password.

## Roadmap
v1.1 configurable policies · v1.3 clipboard · v1.4 GUI · v2.0 encrypted vault

## License
MIT
