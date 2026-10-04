class Solution:
    def checkValidString(self, s: str) -> bool:
        sopb = []
        sast = [] 
        for i in range(len(s)):
            if s[i] == '(':
                sopb.append(i)
            elif s[i] == '*':
                sast.append(i)
            else:
                if sopb:
                    sopb.pop()
                elif sast:
                    sast.pop()
                else:
                    return False
        while sopb and sast:
            if sopb[-1] > sast[-1]:
                return False
            else:
                sopb.pop()
                sast.pop()
        if not sopb:
            return True
        return False
