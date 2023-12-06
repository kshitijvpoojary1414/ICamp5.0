class Hashing :
  def rollingHash(str) :
    x = 31 
    hash = 1
    for i in range(len(str)) :
      hash = (hash*x) + str[i]

  def rabinKarp(self, s, substr) :
    #To do 