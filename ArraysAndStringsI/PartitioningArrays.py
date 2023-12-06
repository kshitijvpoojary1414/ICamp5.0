class PartitioningArrays :
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pivot = 1
        leftBoundary = 0
        rightBoundary = len(arr) - 1
        i = 0

        while i <= rightBoundary :
            if arr[i] > pivot :
                arr[i],arr[rightBoundary] = arr[rightBoundary],arr[i]   
                rightBoundary -= 1
            elif arr[i] < pivot :
                arr[i],arr[leftBoundary] = arr[leftBoundary],arr[i] 
                i += 1 
                leftBoundary += 1 
            else :
                i += 1 
