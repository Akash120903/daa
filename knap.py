#Given N items with their corresponding weights and values, and a package of capacity C, choose either the entire item or fractional part of the item among these N unique items to fill the package such that the package has maximum value. 

# a dynamic approach
# Returns the maximum value that can be stored by the bag
def knapSack(W, wt, val, n):
   K = [[0 for x in range(W + 1)] for x in range(n + 1)]

   for i in range(n + 1):
      for w in range(W + 1):
         if i == 0 or w == 0:
            K[i][w] = 0
         elif wt[i-1] <= w:
            K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
         else:
            K[i][w] = K[i-1][w]
   set=[0]*n
   max_val=K[n][W]
   print("Maximum score= ")
   print(K[n][W])
   for i in range(n,0,-1):
      if K[i][W]!=K[i-1][W]:
         set[i-1]=1
         W-=wt[i-1]
         max_val-=val[i-1]

   return set

val = [1,2,5,6]
wt = [2,3,4,5]
W = 8
n = len(val)
print(knapSack(W, wt, val, n))

