import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
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


def bubbleSort(arr,arr2):
    n = len(arr)
      
    for i in range(n-1):
    
        for j in range(0, n-i-1):
          
            if arr[j] > arr[j+1] :
               arr[j], arr[j+1] = arr[j+1], arr[j]
               arr2[j], arr2[j+1] = arr2[j+1], arr2[j]


class process :
    def __init__(self,number, arrival_time, brust_time  ):
     self.number=number
     self.arrival_time = arrival_time
     self.brust_time = brust_time
     self.remaining_time = brust_time 
     self.departure_time = 0 
     self.priority = 0 

     
#round_robin
class process_queue :
     def __init__(self,number, Time_in_cpu  ):    
         self.number = number
         self.Time_in_cpu = Time_in_cpu 
         self.color = "black" #intial
         self.ideal = 0 

def main_roundRobin(N,quantm_time,arrival_time,brust_time):
        p = [] # array of process 
        for x in range (0,N):
            p.append(process(x+1,arrival_time[x],brust_time[x])) 

        bubbleSort(arrival_time,p)
        READY_QUEUE = []
        new_arr = [] #final array 
        count = 0    # TO COUNT PROCESS WHICH FINISH 
        Timer = 0   #if first arrival not equal zero [EDIT : Timer=x[0].arrivaltime] 
        flag_queue = 0 
        flag_ideal =  0 
        nothing = 0  
        flag_back_READY = 0
        TRIAL = 0 
        flag = 0
        flag_remideal = 0
        for x in range (N):
            if p[x].arrival_time > Timer and x ==0 :
                idle_process=process(0,p[x].arrival_time,1000)
                READY_QUEUE.append(idle_process)
            elif p[x].arrival_time <= Timer :
                READY_QUEUE.append(p[x]) 

                
        while count < N :
            if READY_QUEUE[0].number == 0 :
                
                new_arr.append(process_queue(0, READY_QUEUE[0].arrival_time-Timer))
                Timer = READY_QUEUE[0].arrival_time 
                
            elif READY_QUEUE[0].remaining_time == 0 :
                nothing+=1
            
            elif READY_QUEUE[0].remaining_time <= quantm_time :
                
                new_arr.append(process_queue(READY_QUEUE[0].number, READY_QUEUE[0].remaining_time) )
                Timer += READY_QUEUE[0].remaining_time 
                READY_QUEUE[0].remaining_time = 0 
                for i in range (N) :
                    if READY_QUEUE[0].number == p[i].number :
                        p[i].departure_time = Timer
                        break
                
                
                count += 1
                
            elif READY_QUEUE[0].remaining_time > quantm_time :
                new_arr.append(process_queue(READY_QUEUE[0].number, quantm_time) )
                Timer += quantm_time 
                READY_QUEUE[0].remaining_time =  READY_QUEUE[0].remaining_time - quantm_time
                flag_back_READY = 1
            
            for i in range (N):
                if p[i].number == READY_QUEUE[0].number:
                    TRIAL = i 
                    flag = 1
                    break
            if TRIAL < N-1 and flag == 1 :
                for i in range (len(READY_QUEUE)):
                    if READY_QUEUE[i].remaining_time != 0 :
                        flag_remideal = 1
                        break
                    

                if p[TRIAL+1].arrival_time > Timer and flag_remideal == 0 :
                    idle_process=process(0,p[TRIAL+1].arrival_time,1000)
                    READY_QUEUE.append(idle_process)
                    
            for x in range (N):
               if p[x].number == READY_QUEUE[0].number:
                  continue 
                
               elif p[x].arrival_time <= Timer :
                 for i in range (len(READY_QUEUE)):
                    if p[x].number == READY_QUEUE[i].number :
                        flag_queue = 1 
                        break
                 if flag_queue == 0 :
                        READY_QUEUE.append(p[x])
                 flag_queue = 0    
            flag_ideal = 0 
            flag = 0   
            flag_remideal = 0    
            t = READY_QUEUE[0]
            READY_QUEUE.pop(0)
            
            if flag_back_READY == 1 :
                if t.number != 0 :
                    READY_QUEUE.append(t)  
            flag_back_READY = 0
            
        waiting_time = 0 

        for x in range (0,N): 
            waiting_time += p[x].departure_time - p[x].arrival_time - p[x].brust_time 
        average_waiting_time = waiting_time/N  # TO GUI

        print (average_waiting_time)   
        #drawing 
        y = ["process"] 
        CPU_TIME = [] #XAXIS
        COLORS = []

        color = ["black","red","blue","DarkMagenta","yellow","Brown","Chocolate","Cyan", "Chartreuse","DarkGoldenRod","DarkCyan","Crimson","DarkSlateGray",
                 "DarkOrange","DarkRed","IndianRed ","LawnGreen","LightBlue","LightCoral","MediumPurple","MediumAquaMarine","MediumVioletRed","Teal","SteelBlue",
                 "SaddleBrown"]
        for x in range (0,len(new_arr)):
            CPU_TIME.append(new_arr[x].Time_in_cpu)
            COLORS.append(new_arr[x].number)
            
                
        class final_color1 :
            def __init__(self,number, color  ):    
                self.number = number
                self.color = color 
                
        C=[]       
        COLORS.sort()
        print (COLORS)
        final_color = next_arrival1 (COLORS)
        print (final_color)
        for x in range (0,len(final_color)):
            C.append(final_color1(final_color[x],color[x])) 
        for x in range (len(new_arr)) :
            if new_arr[x].number == 0 :
                new_arr[x].color = 'white' 
            else :  
                for i in range (len(final_color)) :     
                    
                    if new_arr[x].number == C[i].number :
                        new_arr[x].color = C[i].color
                        break       
                    
        label_repeated = []
        left_var = 0 # to complete drawing in same horizontal bar 
        flag_repeated = 0 
        for x in range (0,len(new_arr)):
            label_repeated.append(new_arr[x].number)
            if new_arr[x].number == 0 :
                plt.barh(y,CPU_TIME[x], 0.1 ,left= left_var ,color = new_arr[x].color )
                left_var += CPU_TIME [x]
            elif x > 0 :
                for i in range (len(label_repeated)-1) :
                    if new_arr[x].number == label_repeated[i] :
                        flag_repeated = 1
                        break 
                if flag_repeated == 1 :
                    plt.barh(y,CPU_TIME[x], 0.1 ,left= left_var ,color = new_arr[x].color )
                    left_var += CPU_TIME [x]     
                else :
                    plt.barh(y,CPU_TIME[x], 0.1 ,left= left_var ,label ='P'+str(new_arr[x].number ) ,color = new_arr[x].color )
                    left_var += CPU_TIME [x]  
            else :
                plt.barh(y,CPU_TIME[x], 0.1 ,left= left_var ,label ='P'+str(new_arr[x].number ) ,color = new_arr[x].color )
                left_var += CPU_TIME [x]  
            flag_repeated = 0
            
            
        plt.legend() # to show labels
        plt.title('GANT CHART')

        axes = plt.subplot(1,1,1)
        axes.axis([0,left_var,0,0.5])
        axes.xaxis.set_major_locator (MultipleLocator(1))
        plt.show()  


        for x in range (0,len(new_arr)):
            print (new_arr[x].number , end=" ") 
            print (new_arr[x].Time_in_cpu)

        w1=average_waiting_time
        return str(w1)

 #////calling  function///////////
 
'''arrival_arr = [5,4,3,1,2,6] #FROM GUI
brust_arr= [5,6,7,9,2,3]  #FROM GUI
no_of_processes = 6 # number of process [FROM GUI]
quantm = 3  #FROM GUI
main_roundRobin(no_of_processes,quantm,arrival_arr,brust_arr)  '''
