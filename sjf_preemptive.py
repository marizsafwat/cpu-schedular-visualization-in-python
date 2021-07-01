#### joing function ####
def joining(burst_arr,arrival_arr):
    p=[]
    i=1

    for j in range(0,len(burst_arr)):
        p.append((i,arrival_arr[j],burst_arr[j]))
        i+=1
    #print(p)
    return p



#### preemptive SJF ####
def preemptive_sjf(process):  # preemptive
    #process = [('p1', 2, 15), ('p2', 2, 2), ('p3', 15, 3)]
    p = sorted(process, key=lambda k: [k[1], k[2], k[0]])
    # print(p)
    i = 0
    burst_arr = []
    b = p[0][2]
    y = []
    counter = 0
    flag = 0
    flag2=0
    # premetive
    # for i in range(0,len(p)-1):
    #     if  is_integer_num(p[i][1]):
    #         a=1
    #
    #     else:
    #         a=0.1
    j = 0
    while i < len(p):
        j = i
        if counter == p[i][1]:
            y.append((p[i][0], p[i][2]))
            if i < len(p) - 1:  # 3shan lw etnen gom nfs el wat
                while p[j][1] == p[j + 1][1]:
                    y.append((p[i + 1][0], p[i + 1][2]))

                    if j < len(p) - 2:
                        j += 1
                        i = j
                    else:
                        flag = 1
                        break

            if y[0][0] == p[i][0]:  # heya heya  lw el burst el gdeda as3'r mn el adema el kant sh3'ala
                burst_arr.append((y[0][0], counter))
                o = y[0][0]
            else:  # wa7da gdeda
                burst_arr.append((y[0][0], counter))
                o = y[0][0]

                # 3shan ngeb el index f nshof fadl ad eh
            # for item in range(0,len(p)):
            #     if o in p[item][0]:
            #         index=item
            #         break

            if b != 0 and i != 0:  # and p[i][2]<=y[0][1]:
                h = y[0][0]
                y.pop(0)
                y.append((h, b))  # 3shan y7ot el kan sh3'al 3leha b2elha ad eh
                # if i==0:
                #     y.append((p[i-1][0],b))

            if b == 0 and flag2 !=1:
                y.pop(0)
            flag2=0

            y = sorted(y, key=lambda k: [k[1], k[0]])

            b = y[0][1]
            b -= 1
            # flag 3shan yzawd
            # if  i+1==len(p) and p[index][2]>counter:  #comparing real burst with remaining time
            #     flag=1
            # if b==0 and i+1==len(p):
            #     burst_arr.append((y[0][0], counter+1))
            if i == len(p) - 2 and flag == 1:
                i = len(p)
                break;
            i += 1


        else:

            if b == 0:
                if y!=[]:
                    burst_arr.append((y[0][0], counter))
                    y.pop(0)
                if y == []:
                    counter += 1
                    b=0
                    flag2=1
                else:
                    b = y[0][1]
            # if y==[]:
            #     counter+=1
            b -= 1
            if y == []:
                b = 0
        if y!=[]:
            counter += 1
    # zwdnah 3shan msh by7ot a5r wa7d fl queue
    #     if flag==1:
    #         if b==0:
    #             burst_arr.append((o, counter))
    # else:
    #     y.append((o,b+1))

    # print(y)
    # print(burst_arr)
    if flag == 1 and b == 0:
        sum2 = burst_arr[len(burst_arr) - 2][1]
    else:
        sum2 = burst_arr[len(burst_arr) - 1][1]
    # y = sorted(y, key=lambda k: [k[1], k[0]]) # ---->
    for item in range(0, len(y)):
        sum2 += y[item][1]
        burst_arr.append((y[item][0], sum2))
    print(burst_arr)
    return burst_arr

#### preemptive SJF waiting time ####
def waiting_time_psjf(process,burst_arr):
    departure_time = []
    p = []
    #process = [('p1', 0, 3), ('p2', 5, 4), ('p3', 6, 1)]
    #process = [('p1', 2, 15), ('p2', 2, 2), ('p3', 15, 3)]
    k = sorted(process, key=lambda k: [k[0], k[1], k[2]])
    i = len(burst_arr) - 1
    while i >= 0:
        if burst_arr[i][0] not in p:
            p.append(burst_arr[i][0])
            departure_time.append((burst_arr[i][0], burst_arr[i][1]))
        i -= 1
    i = 0
    d = sorted(departure_time, key=lambda k: [k[0], k[1]])

    waiting = 0
    while i < len(p):
        turnaround = d[i][1] - k[i][1]
        waiting += turnaround - k[i][2]
        i += 1
    # print('dep',departure_time)
    # print("wait",waiting/len(p))
    w1= waiting/len(p)

    ########################graph###########################


    return str(w1)