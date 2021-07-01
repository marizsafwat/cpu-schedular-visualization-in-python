import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

#### joing function ####
def joining(burst_arr,arrival_arr):
    p=[]
    i=1

    for j in range(0,len(burst_arr)):
        p.append((i,arrival_arr[j],burst_arr[j]))
        i+=1
    #print(p)
    return p

#### non-preemptive SJF  ####
def sjf_idl(process):
    # process = [('p1', 2, 10), ('p2', 2, 2), ('p3', 15, 3)]
    p = sorted(process, key=lambda k: [k[1], k[2], k[0]])
    queue = []
    i = 1
    flag = 0
    burst = p[0][2] + p[0][1]
    burst_arr = []
    idl = []
    idl.append((0,p[0][1]))
    burst_arr.append((p[0][0], burst))

    while len(burst_arr) < len(p):

        while i < len(p):

            if p[i][1] <= burst and flag == 0:
                queue.append((p[i][0], p[i][1], p[i][2]))
                i += 1
            # elif p[i][1] > burst:
            #     flag = 1
            #     queue.append((p[i][0], p[i][1], p[i][2]))
            #     burst +=(p[i][1]-burst)
            else:
                break
        if queue == []:
            burst += 1
            idl.append((0, burst))


        else:
            queue = sorted(queue, key=lambda k: [k[2], k[1], k[0]])
            burst += queue[0][2]
            burst_arr.append((queue[0][0], burst))
            queue.pop(0)
    joined=[]
    # for item in burst_arr:
    #     idl.append(item)
    # idl = sorted(idl, key=lambda k: [k[1], k[0]])
    joined=burst_arr+idl
    joined=sorted(joined, key=lambda k: [k[1], k[0]])
    print(joined)
    return joined


def non_preemp_sjf(process):
    #process = [('p1', 0, 10), ('p2', 12, 2), ('p3', 13, 3),('p4',14,6),('p5',15,3)]
    p = sorted(process, key=lambda k: [k[1], k[2], k[0]])
    queue=[]
    i=1
    flag=0
    burst=p[0][2]+p[0][1]
    burst_arr=[]
    burst_arr.append((p[0][0], burst))

    while len(burst_arr)<len(p):
        while i<len(p):

            if p[i][1]<=burst and flag==0:
                queue.append((p[i][0],p[i][1],p[i][2]))
                i+=1
            # elif p[i][1] > burst:
            #     flag = 1
            #     queue.append((p[i][0], p[i][1], p[i][2]))
            #     burst +=(p[i][1]-burst)
            else:
                break
        if queue==[]:
            burst+=1
        else:
            queue=sorted(queue,key=lambda k:[k[2],k[1],k[0]])
            burst+=queue[0][2]
            burst_arr.append((queue[0][0],burst))
            queue.pop(0)

    #print(burst_arr)
    return burst_arr

#### non-preemptive SJF waiting time ####
def waiting_time_nonsjf(process,burst_arr):
    #process = [('p1', 0, 10), ('p2', 12, 2), ('p3', 13, 3),('p4',14,6),('p5',15,3)]
    p = sorted(process, key=lambda k: [k[0], k[1], k[2]])
    burst_arr=sorted(burst_arr, key=lambda k:[k[0], k[1]])
    waiting=0
    i=0
    while i<len(burst_arr):
        turnaround=burst_arr[i][1]-p[i][1]
        waiting+=turnaround-p[i][2]
        i+=1

    #print("wait",waiting/len(p))
    w2 = waiting/len(p)

    ########################graph#####################################

    return str(w2)


def draw():  ##burst array
    final_arr=sjf_idl(joining(burst,arrival))
    # drawing
    y = ["process"]
    # CPU_TIME = []  # xaxis
    # for x in range(0, len(final_arr)):
    #     CPU_TIME.append(final_arr[x][1])  ####class
    left_var = 0
    # for x in range(0, len(final_arr)):
    #
    #     if (final_arr[x].number == 0):  ##ideal
    #         plt.barh(y, CPU_TIME[x], 0.1, left=left_var, color='white')
    #         left_var += CPU_TIME[x]
    #     else:
    #         plt.barh(y, CPU_TIME[x], 0.1, left=left_var, label='P' + str(final_arr[x].number))
    #         left_var += CPU_TIME[x]
    for x in range(0, len(final_arr)):
        if final_arr[x][0] == 0 and x<len(final_arr)-1:
            plt.barh(y, final_arr[x][1], 0.1, left=left_var, color='white')
            left_var = final_arr[x][1]
        else:
            plt.barh(y, final_arr[x][1], 0.1, left=left_var, label='P' + str(final_arr[x][0]))
            left_var = final_arr[x][1]

    plt.legend()
    plt.title('GANT CHART')
    axes = plt.subplot(1, 1, 1)
    axes.axis([0, left_var, 0, 0.5])
    axes.xaxis.set_major_locator(MultipleLocator(1))
    plt.show()




arrival=[0,1,2]
burst=[2,5,1]
y=joining(burst,arrival)
x=non_preemp_sjf(y)
waiting_time_nonsjf(y,x)
draw()