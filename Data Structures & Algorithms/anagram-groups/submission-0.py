class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for word in strs:
            key = tuple(sorted(word))

            if key not in hashMap:
                hashMap[key] = []

            hashMap[key].append(word)

        return list(hashMap.values())