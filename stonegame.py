class Solution(object):
def stoneGame(self, piles):
"""
:type piles: List[int]
:rtype: bool
"""
if len(piles)==2:
	return True
#define the check interval when going through the pile
to_add = 3
#first compute the situation where only two stones are left to pick
smaller = [max(piles[i],piles[i+1]) for i in range(len(piles)-1)]
#further compute situation where only 4,6,8.... stones are left to pick
#the 'recursive' part is that we keep track of values as they are calculated inside the while when they are clculated 
while to_add < len(piles):
	s1 = []
		for i in range(len(piles)-to_add):
#the opponent plays optimally, so when caculating n+2 stones when we have the
#solution for n stones, we take the first stone and add its value to the minimum of
#the next 2 opitmal solution to get candidate one
#then add the value of the stone 'to_add' step further to the minimum of the value
#of its previous two optimal solution to get candidate two
#the solution for the current size is the max of the two candidates
#for example we have [3,4,5,6], the solution for size2 is [4,5,6]
#we take the max(3+min(5,6),6+min(4,5)) to get the size4 solution
#there are even number of stones,which means the index of the two stones on the ends are 1 odd and 1 even
#Since we get to pick first, if we pick the last one(which has a index of odd number) 
#we leave the oponent with two stones with even number to choose from
#So no matter which one he picks, we get to choose a stone with odd index again
#Same for the case if we choose the first one(we then get to pick all the stones with even index)
		cand1 = piles[i]+min(smaller[i+1],smaller[i+2])
		cand2 = piles[i+to_add]+min(smaller[i],smaller[i+1])
		ans = max(cand1,cand2)
		s1.append(ans)
	to_add+=2
	smaller = s1
#return true if our optimal solution is bigger than the value left
return smaller[0]>=sum(piles)-smaller[0]