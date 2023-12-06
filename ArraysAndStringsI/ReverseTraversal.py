def replaceEvenWithTwoQuantity(arr):
  end = len(arr) - 1

  for i in range(len(arr)) :
    if arr[i] % 2 == 0 :
      arr[i], arr[end] = arr[end], arr[i]
      end = end - 1
    arr[i], arr[end] = arr[end], arr[i]
    end = end - 1
    
def reverseSentence(arr) :
  output = ""
  word = ""
  for i in range(len(arr) - 1, -1, -1) :
    char = arr[i]
    if char == " " :
      if len(output) > 0 :
        output += " "
      output += word
      word = ""

    word = char + word 
    
    print(word)
  output += word
  return output 

print(reverseSentence("I am king"))