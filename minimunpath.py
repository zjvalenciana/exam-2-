def minFallingPathSum(self, A: List[List[int]]) -> int:
    for i in range(1,len(A)):
        for j in range(len(A[0])):
			# new value for number at A[1][1] will be  min(5 + 1, 5 + 2, 5 + 3)
			# therefore it will be 5 + 1 = 6, and 6 will then replace the value at A[1][1]

			#new value for number at A[1][0] will be  min(4 + 1, 4 + 2) = 5
			#it will only have two values to compare since there is no upper left value

			#new value for number at A[1][2] will be  min(6 + 2, 6 + 3) = 8
			#it will only have two values to compare since there is no upper right value
		
            #edge cases are first column and last column which only have two paths from above
            if j == 0:
                A[i][j]  = min((A[i][j] + A[i - 1][j]), (A[i][j] + A[i - 1][j + 1]) )
				
            elif (j == len(A[0]) - 1):
                A[i][j]  = min((A[i][j] + A[i - 1][j]), (A[i][j] + A[i - 1][j - 1]) )
			#this keeps track of the minimum path 'recursively' with the conditional statements by calculating tha values 	
            #every other column will have three paths coming from above
            else:
                A[i][j] = min(A[i][j] + A[i - 1][j],A[i][j] + A[i - 1][j + 1], A[i][j] + A[i - 1][j - 1])
        
	# Now that minimum falling sums for each value at the bottom row have been computed
	# We can just take the min of the bottow row to get the smallest overall path sum 
    return min(A[len(A) - 1])