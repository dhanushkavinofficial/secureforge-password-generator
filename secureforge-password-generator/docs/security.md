# Security Notes

## Randomness
All randomness comes from Python's `secrets` module (OS CSPRNG).
The standard `random` module must never be used for passwords.

## The label is not an input
The name/label is display-only. It is never mixed into generation, so
knowing it gives an attacker no advantage.

## Entropy estimate
`estimate_entropy` sums log2 of each mandatory category plus
`(length - 4) * log2(pool size)` for the free characters. It is a
conservative model of the independent choices; it ignores the shuffle
and is not a formal proof of the exact output space.

## Guidance
- Never derive passwords from names, birthdays or emails.
- Use a unique password per account and store them in a password manager.
- Terminal scrollback/history may retain output; use `--quiet` with
  care and clear your terminal when needed.
