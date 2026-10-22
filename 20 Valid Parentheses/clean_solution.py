class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        pair = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        for c in s:
            if len(st) == 0 and c in pair:
                return False
            elif c not in pair:
                st.append(c)
            elif c in pair:
                expected = pair[c]
                actual = st.pop()
                if expected != actual:
                    return False
        
        return len(st) == 0
        
            