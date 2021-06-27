def bubbleSort(arr,arr2):
    n = len(arr)     
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
               arr[j], arr[j+1] = arr[j+1], arr[j]
               arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
               
def prioritySort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j].priority > arr[j+1].priority :
               arr[j], arr[j+1] = arr[j+1], arr[j]
               
class process :
    def __init__(self,number, arrival_time, brust_time  ):
     self.number=number
     self.arrival_time = arrival_time
     self.brust_time = brust_time
     self.remaining_time = brust_time 
     self.departure_time = 0 
     self.priority = 0 
#///////////////////////////////////////////main function//////////////////////////////////////////

def main_priority_NON(n,arrival_time,brust_time,priority) :
    p = []
    for x in range (0,n):
        p.append(process(x+1,arrival_time[x],brust_time[x])) 
        p[x].priority=priority[x]

    bubbleSort(arrival_time,p)
    next_time = 0 
    array = [] 
    final_arr = []
    counter = 0 
    sum_of_prev=0    

    while (counter < n ) :
        for i in range(n) :
            if p[i].arrival_time <= next_time and p[i].remaining_time != 0:
                array.append(p[i])
            elif (p[i].arrival_time>next_time) and (p[i].arrival_time>sum_of_prev) and ((p[i-1].remaining_time==0) or (i==0)) :
                idle_process=process(0,p[i].arrival_time,(p[i].arrival_time - next_time))
                idle_process.priority=1000
                array.append(idle_process)

        prioritySort(array) 
        final_arr.append(array[0])
        next_time += array[0].brust_time 
        sum_of_prev+=array[0].brust_time    

        for i in range(n) :
            if p[i].number==array[0].number :
                p[i].remaining_time = 0 
                
        #dont increment counter if process was idle_process
        # prev_counter=counter
        if (array[0].number != 0):
            p[(array[0].number)-1].departure_time = next_time 
            counter+=1
            

        array.clear() 
    waiting_time = 0 
    for x in range (n):
        waiting_time += ( p[x].departure_time - p[x].arrival_time - p[x].brust_time )
            
    average_waiting_time = waiting_time/n

    for x in range (0,len(final_arr)):
        print(final_arr[x].number , end=" ")
        print(final_arr[x].priority, end=" "  )
        print(final_arr[x].brust_time ) 
    print(average_waiting_time) 
    
#////calling main function///////////////////////
no_of_processes=5
arrival_arr = [0,0,0,0,0]
brust_arr = [10,1,2,1,5]
priority_arr = [3,1,4,5,2]    
main_priority_NON(no_of_processes,arrival_arr,brust_arr,priority_arr)


