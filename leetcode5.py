# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# # Explanation: 
# # 1st customer has wealth = 1+2+3 = 6
# # 2nd customer has wealth = 3+2+1 = 6
# # Max wealth = 6


# -->approach followed:

# to solve the richest customer wealth problem 
# initially I thought of using the split etc but later on 
# the apporach is 
# to run in for loop then sum(i) then to store that it....

def accounts(l1):
    maxwealth=0
    for i in l1:
        wealth=sum(i)
        if wealth >maxwealth:
            maxwealth=wealth
    return maxwealth

l1=[[1,2,8],[3,2,1]]
print(accounts(l1))

# Analyses of Time Complexity:

# O(m*n)
# because m no of customers (i)
#         n  no of accounts  (l1)

# the space complexity

# O(1)
