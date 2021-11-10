def find_all_substrings(s: str, words: List[str]) -> List[int]:

    wordSize = len(words[0])
    wordCounter = Counter(words)

    def matches(start):
        matchCounter = Counter()
        for i in range(start, start + len(words)*wordSize, wordSize):
            curWord = s[i:i+wordSize]
            if curWord not in wordCounter:
                return False
            matchCounter[curWord] +=1
            if matchCounter[curWord] > wordCounter[curWord]:
                return False
        return True

    return [i for i in range(len(s) - len(words)*wordSize+1) if matches(i)]