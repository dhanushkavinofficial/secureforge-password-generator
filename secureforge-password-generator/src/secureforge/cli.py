"""SecureForge command-line interface."""

import argparse
import sys

from .entropy import estimate_entropy, rate_strength
from .generator import MAX_LENGTH, MIN_LENGTH, generate_password

BANNER = (
    "=" * 50
    + "\n             SECUREFORGE\n      Secure Password Generator\n"
    + "=" * 50
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="secureforge",
        description="Cryptographically secure password generator.",
    )
    parser.add_argument("-l", "--length", type=int,
                        help=f"password length ({MIN_LENGTH}-{MAX_LENGTH})")
    parser.add_argument("-n", "--label",
                        help="label for the password (e.g. GitHub); not used in generation")
    parser.add_argument("-c", "--count", type=int, default=1,
                        help="how many passwords to generate (default 1)")
    parser.add_argument("-q", "--quiet", action="store_true",
                        help="print only the password(s)")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)

    try:
        if not args.quiet:
            print(BANNER)

        label = args.label
        if label is None and not args.quiet and args.length is None:
            label = input("Enter your name / password label: ").strip()
            if not label:
                print("Error: label cannot be empty.", file=sys.stderr)
                return 1

        length = args.length
        if length is None:
            raw = input(f"Password length ({MIN_LENGTH}-{MAX_LENGTH}) [32]: ").strip()
            length = int(raw) if raw else 32

        if not 1 <= args.count <= 100:
            print("Error: count must be between 1 and 100.", file=sys.stderr)
            return 1

        passwords = [generate_password(length) for _ in range(args.count)]
        bits = estimate_entropy(length)
    except (ValueError, TypeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    except (KeyboardInterrupt, EOFError):
        print("\nCancelled.", file=sys.stderr)
        return 130

    if args.quiet:
        print("\n".join(passwords))
        return 0

    print()
    if label:
        print(f"Password label   : {label}")
    print(f"Password length  : {length}")
    print(f"Estimated entropy: {bits:.2f} bits ({rate_strength(bits)})")
    print("=" * 50)
    print("\nGenerated password(s):")
    for pw in passwords:
        print(pw)
    print("\nTip: store it in a password manager; never reuse passwords.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
