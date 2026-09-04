class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        isAdded = [0] * 27 # THis is the way to initiaalise the array

        macroResult = []

        for index, word in enumerate(strs):
            if isAdded[index] == 0:
                isAdded[index] = 1
                resultList = [word]
                for index2 in range(index + 1, len(strs)):
                    if isAdded[index2] == 0:
                        nextWord = strs[index2]
                        result = self.checkAnagram(word, nextWord)
                        if result == True:
                            resultList.append(nextWord)
                            isAdded[index2] = 1

                macroResult.append(resultList)

        return macroResult

    # Implementing the hastable method here as it only contains the 26 alphabet chars
    def checkAnagram(self, word, nextWord):

        if len(word) != len(nextWord):
            return False

        hashtable = [0] * 27 # THis is the way to initiaalise the array

        for char in word:
            hashtable[ord(char) - ord('a') + 1] += 1
        
        for char in nextWord:
            hashtable[ord(char) - ord('a') + 1] -= 1


        for i in range(1,27):
            if hashtable[i] != 0:
                return False
        
        return True




        

        