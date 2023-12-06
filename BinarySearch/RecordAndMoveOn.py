class RecordAndMoveOn :
  def closestToTarget(self, arr, target) :
    start,end = 0 ,len(arr) - 1
    closest = None

    while start <= end :
      mid = start + (end - start)//2 
      closest = self.recordClosest(closest, arr, mid, target)

      if arr[mid] < target : 
        start = mid + 1
      elif arr[mid] > target :
        end = mid - 1 
      else :
        return mid 

    
    return closest 
    
  def recordClosest(self, closest, arr, current, target) :
    if closest is None or abs(target - arr[current]) < abs(arr[closest]-target) :
      closest = current

    return closest