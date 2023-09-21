def countSubstrings(s: str) -> int:

        res = []
        track = []
        def backtrack(start):

            if start >= len(s):
                res.append(track.copy())
                return
            

            for i in range(start, len(s)):
                if s[start:i+1][::1] == s[start:i+1][::-1]:
                    track.append(s[start:i+1])
                    backtrack(i+1)
                    track.pop()
        
        backtrack(0)
        return res

input = "babad"

res = countSubstrings(input)
print()

