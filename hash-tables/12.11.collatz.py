# Open ended question, can solve in any way
# some optimizations
# if even, will definitely reach to one, as we just half it
# add any number to seen set, if after some operations we reach to same number we can return false as a cycle occurs
# for all verified numbers, add it to alreadyProvenSet

def test_collatz_conjecture(n: int) -> bool:
    alreadyProven = set()

    def isToOneRec(n: int, seen: set) -> bool:        
        if n == 1:
            return True

        if n in seen:
            return False
        seen.add(n)

        if n in alreadyProven:
            return True
    
        if n % 2:
            return isToOneRec(3 * n + 1, seen)
        else:
            return isToOneRec(n // 2, seen)
    
    def isToOne(n: int) -> bool:
        seen = set()
        if isToOneRec(n, seen):
            alreadyProven.add(n)
            return True
        else:
            return False

    for i in range(3, n+1):
        if not isToOne(i):
            return False
    
    return True