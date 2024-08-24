#Solucion buena
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])

#Mi solucion
class Solution(object):
    def gcdOfStrings(self, str1, str2):

        i = 0
        max_len = max(len(str1),len(str2))
        min_len = min(len(str1),len(str2))
        divisor = 0
        print(max_len)
        for i in range (min_len):
            if (((max_len % (i+1)) == 0)) and (((min_len % (i+1)) == 0)):
                divisor = i+1

        equals_str_1 = ""
        equals_str_2 = ""
        equals_bool = False
        
        for _ in range(len(str1) / divisor):
            equals_str_1 += str1[:divisor]
        for _ in range(len(str2) / divisor):
            equals_str_2 += str1[:divisor]
            if(str1 == equals_str_1) and (str2 == equals_str_2):
                equals_bool = True

        if (divisor == 0) or (equals_bool == False):
            return ""
        return str1[:divisor]
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        