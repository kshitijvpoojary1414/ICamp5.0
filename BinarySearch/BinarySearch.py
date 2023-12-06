class BinarySearch :
  def search(self, arr, target) :
    start, end = 0, len(arr) - 1

    while start <= end :
      mid = start + (end - start) // 2

      if target > mid :
        start = mid + 1
      elif target < mid :
        end = mid - 1
      else :
        return mid 

    return -1