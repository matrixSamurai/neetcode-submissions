class Solution:
    def groupAnagramsInefficient(self, strs: List[str]) -> List[List[str]]:

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
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # This default dictionary solves the problem of the non-existent 
        # disctionary key. If the key is not present the default function 
        # create an empty list
        resultHashtable = defaultdict(list)

        for s in strs:
            hashtableIndividual = [0] * 27
            for c in s:
                hashtableIndividual[ord(c) - ord('a') + 1] += 1
            # This below is the smartest move here, as we use the 
            # hashtableIndividual as the unique key here
            # Also, we need to use the tuple here becuase the tuple in immutable
            # and hence can be sued as the key to the disctionary
            resultHashtable[tuple(hashtableIndividual)].append(s)
        
        # Now returning the values of the Hashtable values as the list

        return list(resultHashtable.values())

        
        







        

        