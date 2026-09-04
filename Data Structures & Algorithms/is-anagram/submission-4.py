class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        ## Soltuion 1 ; Brute force approach, Time - O(n^2), Space - O(n)
        
        # Edge case
        # if len(s) != len(t):
        #     return False

        # foundFlag = False

        # for char1 in s:
        #     foundFlag = False
        #     for char2 in t:
        #         if char1 == char2:
        #             foundFlag = True
        #             break
            
        #     if foundFlag == False:
        #         break
        
        # return foundFlag


        ## Solution 2

        # Create the Hashmap which is the frequency map of the elements
        # Time - O(n), space - O(n)

        ## Soltuion 3

        ## Create the arrayo of the frequency map
        ## First build the array from 1st string and then keep on deleting 
        # the elements using the 2nd string elements

        # frequencyArr = [0] * 26

        # ## Creating the frequency arr
        # for char in s:
        #     charIndex =  ord(char) - 97 ## As 'a' have the ascii value of 97
        #     frequencyArr[charIndex] += 1

        # for char in t:
        #     charIndex = ord(char) - 97
        #     if frequencyArr[charIndex] > 0:
        #         frequencyArr[charIndex] -= 1
        #     else:
        #         return False # This is the case where char not present in s, but in t
        
        # ## Now our final frequncyArr should be empty, iterating to check
        # for num in frequencyArr:
        #     if num != 0:
        #         return False
        
        # return True


        ## Soltuion 4 - Sort both the array, and then compare
        ## Time - O(nlogn + mlogm), space - O(n+m)
        return sorted(s) == sorted(t)







            
        