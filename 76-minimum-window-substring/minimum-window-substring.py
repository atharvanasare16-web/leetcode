from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        target = Counter(t)
        window = {}

        have = 0
        need = len(target)

        left = 0
        res = [-1, -1]
        resLen = float("inf")

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in target and window[c] == target[c]:
                have += 1

            while have == need:
                # Update result
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                # Shrink window
                window[s[left]] -= 1

                if s[left] in target and window[s[left]] < target[s[left]]:
                    have -= 1

                left += 1

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""