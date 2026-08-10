class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        answer = 0
        count = {}
        max_freq=0
        max_len=0

        for right in range(len(s)):

    # 1. Expand the window
            count[s[right]] = count.get(s[right], 0) + 1
    # Add data[right] to the window
            max_freq = max(max_freq, count[s[right]])
            while (right - left + 1) - max_freq > k:
        # 2. Shrink the window
                count[s[left]] -= 1
        # Remove data[left]
                left += 1

    # 3. Update the answer
        answer = max(answer, right - left + 1)

        return answer