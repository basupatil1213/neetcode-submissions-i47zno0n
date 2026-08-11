class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += f'{len(s)}#{s}'
        return encoded_str

    def decode(self, s: str) -> List[str]:

        strs = []
        i = 0
        n = len(s)
        while i < n:
            # read length until '#'
            j = i
            while j < n and s[j] != '#':
                j += 1
            length = int(s[i:j])
            # move past '#'
            start = j + 1
            end = start + length
            strs.append(s[start:end])
            i = end
        return strs