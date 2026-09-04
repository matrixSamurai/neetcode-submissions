class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Base case here - If len of S1 > S2, return false, can never be true
        if len(s1) > len(s2):
            return False



        frequencys1 = [0] * 27
        frequencys2 = [0] * 27
        currentMatches = 0


        left = 0
        right = len(s1)

        for i in range(left, right):
            frequencys1[ord(s1[i])-ord('a') + 1] += 1
            frequencys2[ord(s2[i])-ord('a') + 1] += 1

        for i in range(0,27):  
            if frequencys1[i] == frequencys2[i]:
                currentMatches += 1
        
        print(frequencys1)
        print(frequencys2)
        print(currentMatches)


        
        if currentMatches == 27:
            print("I am heree")
            return True


        while right < len(s2):

            print("Printing the while loops")

            leftIndex = ord(s2[left])-ord('a') + 1
            rightIndex = ord(s2[right])-ord('a') + 1


            if frequencys2[leftIndex] == frequencys1[leftIndex]:
                frequencys2[leftIndex] -= 1
                currentMatches -= 1
            elif frequencys2[leftIndex] - 1 == frequencys1[leftIndex]:
                frequencys2[leftIndex] -= 1
                currentMatches += 1
            else:
                frequencys2[leftIndex] -= 1

            
            if frequencys2[rightIndex] == frequencys1[rightIndex]:
                frequencys2[rightIndex] += 1
                currentMatches -= 1
            elif frequencys2[rightIndex] + 1 == frequencys1[rightIndex]:
                frequencys2[rightIndex] += 1
                currentMatches += 1
            else:
                frequencys2[rightIndex] += 1


            print(frequencys1)
            print(frequencys2)
            print(currentMatches)


            if currentMatches == 27:
                return True

            left += 1
            right += 1

        
        return False

            

        