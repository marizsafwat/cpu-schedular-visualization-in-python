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

def next_arrival1 (arr):
  next_arrival = []
  i = 0
  j = 0
  while (i < len(arr) and j < len(arr) ):
    if arr[i] == arr[j] :
          j+=1
    elif (arr[i] != arr[j] ):
          next_arrival.append(arr[i])
          i = j     
    if j == len (arr) and i < len(arr) :
          next_arrival.append(arr[i])
  return next_arrival               

class process :
    def __init__(self,number, arrival_time, brust_time  ):
     self.number=number
     self.arrival_time = arrival_time
     self.brust_time = brust_time
     self.remaining_time = brust_time 
     self.departure_time = 0 
     self.priority = 0 

class process_queue :
     def __init__(self,number, Time_in_cpu  ):    
         self.number = number
         self.Time_in_cpu = Time_in_cpu 
         self.color = "black" #intial
         self.ideal = 0  

#///////////////////////////////////////////main function//////////////////////////////////////////

def main_priority_preemptive(n,arrival_time,brust_time,priority) :
    p = [] # array of process 
    for x in range (0,n):
      p.append(process(x+1,arrival_time[x],brust_time[x])) 
      p[x].priority=priority[x]

    bubbleSort(arrival_time,p)
    next_time = 0 
    array = [] 
    final_arr = []
    counter = 0 
    y = 1 
    #next_arrival = [0,1,7,8]
    next_arrival = next_arrival1(arrival_time)
    #sum for idle process
    sum_of_prev=0

    while (counter < n ) :
      for i in range(n):
        if p[i].arrival_time <= next_time and p[i].remaining_time != 0:
            array.append(p[i])
        #///////// added code for idle process ////////////////////////////////////////////
        elif (p[i].arrival_time>next_time) and (p[i].arrival_time>sum_of_prev) and ((p[i-1].remaining_time==0) or (i==0)) :
                idle_process=process(0,p[i].arrival_time,(p[i].arrival_time - next_time))
                idle_process.priority=1000
                array.append(idle_process)
        #//////////////////////////////////////////////////////////////////////////////////
      prioritySort(array) 

      if y < len (next_arrival) :
          if (next_arrival[y] > next_time ) :
              if (next_time+array[0].remaining_time)<next_arrival[y] :
                cpu = array[0].remaining_time
                next_time += cpu 
                y-=1
              else :
                  cpu= next_arrival[y] - next_time
                  next_time += cpu
          else :    
            cpu = next_arrival[y] - next_time
            next_time += cpu
          y+=1
      else :
          cpu = array[0].remaining_time
          next_time += cpu

      for i in range(n):
          if p[i].number==array[0].number :
              p[i].remaining_time = p[i].remaining_time - cpu  
              if p[i].remaining_time == 0 :
                  p[i].departure_time=next_time
                  counter+=1 

      final_arr.append(process_queue(array[0].number,cpu))
      sum_of_prev+=cpu
      array.clear()

    waiting_time = 0 
    for x in range (0,n): 
      waiting_time += p[x].departure_time - p[x].arrival_time - p[x].brust_time 
    average_waiting_time = waiting_time/n  # TO GUI
    for x in range (0,len(final_arr)):
      print(final_arr[x].number , end=" ")
      print(final_arr[x].Time_in_cpu  )
    print(average_waiting_time) 

#////calling main function///////////////////////
no_of_processes=5
arrival_arr = [0,0,6,11,12]
brust_arr = [4,3,7,4,2]
priority_arr = [1,2,1,3,2]    
main_priority_preemptive(no_of_processes,arrival_arr,brust_arr,priority_arr)    