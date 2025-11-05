import math
import string
import re

SPECIALS = string.punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

def entropy_bits(password):
    """Estimate entropy bits using the set of character classes used."""
    pool = 0
    if re.search(r'[a-z]', password): pool += 26
    if re.search(r'[A-Z]', password): pool += 26
    if re.search(r'\d', password): pool += 10
    if re.search(r'[{}]'.format(re.escape(SPECIALS)), password): pool += len(SPECIALS)

    if pool == 0:
        return 0.0
    return len(password) * math.log2(pool)

def repeated_sequence_penalty(password):
    """Return True if there are obvious repeated sequences or repeated single char."""
    # repeated single char (aaaa), or short repeated sequences like 'abcabc' or '121212'
    if re.search(r'(.)\1\1', password):  # same char 3 times consecutively
        return True
    # detect short repeated block (length 2-4) repeated at least twice
    for block_len in range(2, 5):
        for i in range(len(password) - block_len * 2 + 1):
            block = password[i:i+block_len]
            if block and password.count(block) >= 2 and re.search(re.escape(block) + r'.*' + re.escape(block), password):
                return True
    return False

def assess_password(pw):
    length = len(pw)
    has_upper = bool(re.search(r'[A-Z]', pw))
    has_lower = bool(re.search(r'[a-z]', pw))
    has_digit = bool(re.search(r'\d', pw))
    has_special = bool(re.search(r'[{}]'.format(re.escape(SPECIALS)), pw))

    # scoring rules (simple, transparent)
    score = 0
    # length points
    if length >= 15:
        score += 3
    elif length >= 11:
        score += 2
    elif length >= 8:
        score += 1
    # char class points
    score += int(has_lower) + int(has_upper) + int(has_digit) + int(has_special)

    # penalty for repeated patterns
    penalty = 0
    if repeated_sequence_penalty(pw):
        penalty = 1
        score -= penalty

    # clamp score
    if score < 0: score = 0

    # entropy estimate
    ent = entropy_bits(pw)

    # map score -> label (0..7 possible score range)
    if score <= 1:
        label = "Very Weak"
    elif score == 2:
        label = "Weak"
    elif score <= 4:
        label = "Moderate"
    elif score <= 5:
        label = "Strong"
    else:
        label = "Very Strong"

    suggestions = []
    if length < 12:
        suggestions.append("Increase length to at least 12–16 characters.")
    if not has_upper:
        suggestions.append("Add uppercase letters (A-Z).")
    if not has_lower:
        suggestions.append("Add lowercase letters (a-z).")
    if not has_digit:
        suggestions.append("Add numbers (0-9).")
    if not has_special:
        suggestions.append("Add special characters (e.g., !@#$%).")
    if repeated_sequence_penalty(pw):
        suggestions.append("Avoid repeated characters or repeated patterns (e.g., 'aaa' or 'abcabc').")
    if ent < 50:
        suggestions.append("Consider using a mix of character classes to raise entropy.")

    return {
        "password": pw,
        "length": length,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_special": has_special,
        "score": score,
        "entropy_bits": round(ent, 2),
        "strength": label,
        "penalty": penalty,
        "suggestions": suggestions
    }

def pretty_print(result):
    print("\n--- Password Strength Report ---")
    print(f"Password (displaying safely): {'*' * min(6, len(result['password']))}{'' if len(result['password'])<=6 else '...'}")
    print(f"Length: {result['length']}")
    print(f"Uppercase: {result['has_upper']}, Lowercase: {result['has_lower']}, Digits: {result['has_digit']}, Special: {result['has_special']}")
    print(f"Estimated Entropy: {result['entropy_bits']} bits")
    print(f"Score: {result['score']}  -> {result['strength']}")
    if result['penalty'] > 0:
        print("Penalty applied for repeated patterns.")
    if result['suggestions']:
        print("\nSuggestions to improve:")
        for s in result['suggestions']:
            print(f" - {s}")
    else:
        print("\nGood password! No suggestions.")
    print("-------------------------------\n")

def main():
    print("Password Strength Assessment Tool")
    pw = input("Enter password to evaluate: ").strip()
    res = assess_password(pw)
    pretty_print(res)

if __name__ == "__main__":
    main()
    