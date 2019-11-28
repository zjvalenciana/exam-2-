class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        dp = [[False for i in range(size)] for j in range(size)]
		# we define the solution recursively with 
		# use of a matrix to store the results, row stands for the start index of a 
		# substring, column stands for the end index of a substring. 
		# dp[i][j] = True means the substring starts from i, ends in j is a 
		# Palindromic Substrings. As start index <= end index, we only 
		# consider the up-right part of the matrix.
		
        for i in range(size):
            dp[i][i] = True
			# fisrt of all, all substring constains only one letter is a 
			# Palindromic Substrings
        for i in range(size-1):
            dp[i][i+1] = (s[i] == s[i+1])
			# then, any substring which contains two letters is a 
			# Palindromic Substrings if and only if the two letters are the same
        for i in range(size-2):
            for j in range(size-2-i):
                dp[j][j+i+2] = dp[j+1][j+i+1] and (s[j] == s[j+i+2])
			# for a substring containing more two letters, it is 
			# a Palindromic Substrings if and only if 
			# its fisrt letter = its last letter 
			# AND 
			# after removing these two letters, the subsubstring is 
			# a Palindromic Substrings
        return sum([line.count(True) for line in dp])