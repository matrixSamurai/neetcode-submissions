class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        if len(s) <=10:
            return []

        count_map = {}
        result_set = []
        
        for i in range(len(s) - 10 + 1):

            dna_str = s[i : i+10]

            if dna_str in count_map and count_map[dna_str] == 1:
                count_map[dna_str] += 1
                result_set.append(dna_str)
            elif dna_str not in count_map:
                count_map[dna_str] = 1
            else:
                count_map[dna_str] += 1
           
        
        return result_set


