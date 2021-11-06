def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:

    letterFreq = collections.Counter(letter_text)
    
    for c in magazine_text:
        if c in letterFreq:
            letterFreq[c] -= 1
            if letterFreq[c] == 0:
                del letterFreq[c]
                if not letterFreq:
                    return True
    return not letterFreq