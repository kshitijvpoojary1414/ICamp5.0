class BinarySearchWithDuplicates :
  def firstOccurence(self, arr, target) :
    start, end = 0, len(arr) - 1

    while start < end :
      mid = start + (end - start)//2 

      if target < arr[mid] or (target == arr[mid] and (mid > 0 and arr[mid-1] != target)) :
        end = mid - 1 
      elif :
        start = mid + 1 
      else :
        return mid 

    return -1

  def insertTInSortedArray(self, arr, target) :

    start, end = 0, len(arr) - 1

    while start < end :
      mid = start + (end - start)//2 

      if target >= arr[mid] :
          if mid == len(arr) - 1 :
            return mid 
          start = mid + 1 
      elif :
        if mid == 0 or arr[mid-1] <= target : 
          return mid 
        end = mid - 1
      else :
        return mid 

    return -1