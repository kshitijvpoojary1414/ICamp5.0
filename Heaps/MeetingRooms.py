import collections
import heapq
class MeetingRoomsIII:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        freeRooms = [i for i in range(n)]
        heapq.heapify(freeRooms)
        busyRooms = []
        currentTime = 0
        meetings.sort()
        rooms = collections.defaultdict(int)
        time = 0

        for i in range(len(meetings)) :
            start,end = meetings[i]
            time = max(time,start)

            while busyRooms and busyRooms[0][0] <= start :
                _,roomNo = heapq.heappop(busyRooms)
                heapq.heappush(freeRooms,roomNo)
                rooms[roomNo] += 1

            if not freeRooms :
                busyRoomTime,busyRoomNo = heapq.heappop(busyRooms)
                rooms[busyRoomNo] += 1
                heapq.heappush(busyRooms,(busyRoomTime + (end-start), busyRoomNo))

            else :
                newRoom = heapq.heappop(freeRooms)
                heapq.heappush(busyRooms,(end, newRoom))

        while len(busyRooms) > 0 :
            rooms[heapq.heappop(busyRooms)[1]] += 1
        
        maximum = 0
        value = float('inf') 

        for key in rooms :
            if rooms[key] > maximum or (rooms[key] == maximum and key < value):
                maximum = rooms[key] 
                value = key
            
        return value  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
