class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for detail in details:
            res += 1 if int(detail[-4:-2]) > 60 else 0
        
        return res
        