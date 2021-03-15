def maxRepeating(sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        first_l = word[0]
        len_seq = len(sequence)
        len_word = len(word)
        k=0
        highest = 0
        i=0
        while i < len_seq:
            if (sequence[i] == first_l):
                # edge case: out of range
                if i+len_word > len_seq:
                    break
                # word match
                if (sequence[i:i+len_word] == word):
                    k+=1
                    i+=len_word
                # no word match
                else:
                    i+=1
                    k=0
            else:
                i+=1
                k=0
            
            if k > highest:
                highest = k
            
        return highest

sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
word = "aaaba"

print(maxRepeating(sequence, word))