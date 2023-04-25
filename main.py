class Solution:
    def isPalindrome(self, x: int):
        f = str(x)
        if f == f[::-1]:
            return ('Is a Palendrome')
        return ('Is not a Palendrome')

s1 = Solution()

print(s1.isPalindrome(121))
print(s1.isPalindrome(569))
print(s1.isPalindrome(565))
print(s1.isPalindrome(15551))