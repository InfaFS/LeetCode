class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""
        i = 0

        while(i < len(word1) and i < len(word2)):        
            result = result + word1[i]
            result = result + word2[i]
            i += 1
        
        if (i < len(word1)):
            result = result + word1[i:]
        elif i < len(word2):
            result = result + word2[i:]

        return result

        