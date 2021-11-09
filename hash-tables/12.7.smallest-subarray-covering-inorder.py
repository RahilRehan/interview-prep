# not solved, some test cases are not passing
# below approach => https://www.youtube.com/watch?v=W2DvQcDPD9A
# t.c is O(S.T) in worst case ex: aaaaaaaaaaaaaa, aaa
# did not understand epi solution
# there is also a dp based approach which is expected
# https://leetcode.com/discuss/interview-question/923693/google-phone-screen-find-shortest-substring-which-contains-all-the-alphabets-of-another-string/759913
# leetcode premium question available on lintcode

def find_smallest_sequentially_covering_subset(paragraph: List[str],
                                               keywords: List[str]
                                               ) -> Subarray:
    minSubset = Subarray(-1, -1)
    j = 0
    minLength = len(paragraph)+1

    for i in range(len(paragraph)):
        if paragraph[i] == keywords[j]:
            j += 1
            if j >= len(keywords):
                end = i+1
                j -= 1
                while j >= 0:
                    if keywords[j] == paragraph[i]:
                        j -= 1
                    i -= 1
                i += 1
                j += 1
                if end-i < minLength:
                    minLength = end - i
                    minSubset = Subarray(i, end-1)
    return minSubset