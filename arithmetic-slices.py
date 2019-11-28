    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        res = [0]
        f = 1
        for i in range(2,len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
			#Use a list to record currenrt number of slices,
			#we keep adding and appending when the differences are the same, but here we are already keeping track of values 
			#with the if statement and if the pattern break we reset the append to 1 and skip the addition.	
                res.append(res[-1]+f)
                f += 1
            else:
                f=1
        
        return res[-1]