class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        if len(s) <=10:
            return []

        count_map = defaultdict(int)
        result = []

        for i in range(len(s) - 10 + 1):
            dna_str = s[i:i+10]
            
            count_map[dna_str] += 1
            if count_map[dna_str] == 2:
                result.append(dna_str)
           
    
        return result


