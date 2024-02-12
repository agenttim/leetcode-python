from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]

                if not prefix:
                    return ""

        return prefix










strs = ["flower", "flow", "flight"]
#
# print(strs[1].find(strs[0]))
# print(strs[0][:-1])

print(Solution().longestCommonPrefix(strs))