# t.c => sorting n string => n*mlogm where m is longest string length
def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    anagram_store = collections.defaultdict(list)

    for s in dictionary:
        anagram_store["".join(sorted(s))].append(s)

    return [group for group in anagram_store.values() if len(group)>=2]