class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""

        left = 0
        req = {}
        window = {}
        have = 0

        for ch in t:
            req[ch] = req.get(ch, 0) + 1

        need = len(req)

        res = [-1, -1]
        res_len = float("inf")

        for right in range(len(s)):

            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in req:
                if window[c] == req[c]:
                    have += 1

            while have == need:

                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                window[s[left]] -= 1

                if s[left] in req:
                    if window[s[left]] < req[s[left]]:
                        have -= 1

                left += 1

        if res_len == float("inf"):
            return ""

        l = res[0]
        r = res[1]

        return s[l:r + 1]
            
