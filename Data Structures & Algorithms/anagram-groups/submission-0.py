class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list)

        for i in range(len(strs)):
            char_count = [0] * 26
            for ch in strs[i]:
                char_count[ord(ch) - ord('a')] += 1
            
            anagram_group[tuple(char_count)].append(strs[i])
        
        return list(anagram_group.values())
        