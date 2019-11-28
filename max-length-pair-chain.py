class Solution(object): #Time Limit Exceeded
    def findLongestChain(self, pairs):
        pairs.sort()
        dp = [1] * len(pairs)

        for j in xrange(len(pairs)):
			#by Sorting the pairs by first coordinate
			#so When i < j and pairs[i][1] < pairs[j][0] we extend the chain
			#because we iterate but use the conditional to compare 
			#its like recursively kepping track of values 
			#and so we have the candidate answer dp[j] = max(dp[j], dp[i] + 1).
            for i in xrange(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)
