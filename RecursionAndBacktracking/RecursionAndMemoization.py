# All recursive functions should have the following: 
# Base Case, Working towards a base case, and Recursive step.

class RecursionAndMemoization :
  def power(self, x , n) :
    value = self.positivePower(abs(x), abs(n))

  def positivePower(self, x ,n) :
    if n == 0 :
      return 1 

    if n == 1 :
      return x 

    halfValue = self.positivePower(x,n//2)

    if n%2 == 0 :
      return self.halfValue * self.halfValue 
    else :
      return self.halfValue * self.halfValue * x
