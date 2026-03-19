def can_construct(ransomNote: str, magazine: str) -> bool:
    d1 = {}
    d2 = {}

    # Count characters in ransomNote
    for ch in ransomNote:
        d1[ch] = d1.get(ch, 0) + 1

    # Count characters in magazine
    for ch in magazine:
        d2[ch] = d2.get(ch, 0) + 1

    # Compare counts
    for ch in d1:
        if ch not in d2 or d1[ch] > d2[ch]:
            return False

    return True


# Example usage
ransomNote = "bg"
magazine = "efjbdfbdgfhhaijgfhbaeajhgfbbgbjagbddfgdiaigdadhcfcj"

print(can_construct(ransomNote, magazine))
