'''
Charlotte (Ciao-Wen) Chen
'''

def makeData(record_num, status):
    ''' 
    retrieve data from txt, calculate lateral distance and height, return a list 
    contains patient's status, id, age, gender, lateral distance, and height 
    param record_num: int
    param status: str, { "PREOP", "POSTOP" }
    ''' 
    patient_row_Data=[]
    patient_row_Data+=[status] #post or pre operation 
    with open("RECORDING_%i-%s.txt" %(record_num, status), 'r') as file:
        lines=file.readlines()
        patient_data=[]
        for line in lines: #make consistent delimiter
            line=line.strip('\n')
            line=line.replace('; ', ',')
            line=line.replace(';', ',')
            line.replace('| ', ', ')
            line=line.replace('|', ',')
            line=line.replace(', ', ',')
            line_array=line.split(',')
            patient_data+=[line_array]
    patient_row_Data+=patient_data[0][0:2]; #id, age
    patient_row_Data+=[patient_data[0][2].lower()]; #gender
    x=[]
    y=[]
    y_fall=False
    for i in range(1,len(patient_data)):
        if y_fall==True:
            continue
        elif float(patient_data[i][2])==0:
            y_fall=True
            y+=[float(patient_data[i][2])]
        y+=[float(patient_data[i][2])]
        x+=[float(patient_data[i][1])]
    patient_row_Data+=[max(x)-min(x)] #lateral distance 
    patient_row_Data+=[max(y)-min(y)] #height
    return patient_row_Data

def printAvg(pre_data, post_data, direction):
    '''
    print the average performance(direction) among pre, post-operation status
    param pre_data, post_data: list of patient data
    param direction: str, { "lateral", "height" }
    '''
    idx=4 if direction=="lateral" else 5 #get index of direction
    sum=0
    for pre in pre_data:
        sum+=pre[idx]
    for post in post_data:
        sum+=post[idx]
    print("Average distance: %.3f" 
        %(sum/(len(pre_data)+len(post_data)))) 


def printShortest(pre_data, post_data, direction):
    '''
    print the shortest performance(direction) among pre, post-operation status
    param pre_data, post_data: list of patient data
    param direction: str, { "lateral", "height" }
    '''
    direction_dic = { "height":"lowest", "lateral":"shortest" }
    idx=4 if direction=="lateral" else 5
    min=9223372036854775807
    minIdx=0
    preHasMinData=True
    for preIdx in range(len(pre_data)):
        preVal=pre_data[preIdx][idx]
        if preVal<min:
            min=preVal
            minIdx=preIdx
    for postIdx in range(len(post_data)):
        postVal=post_data[postIdx][idx]
        if postVal<min:
            min=postVal
            minIdx=postIdx
            preHasMinData=False
    if(preHasMinData==True):
        print("Patient %s %s threw the %s with %.1f" 
            %(pre_data[minIdx][1], pre_data[minIdx][0], direction_dic[direction], pre_data[minIdx][idx]))
    else: 
        print("Patient %s %s threw the %s with %.1f" 
            %(post_data[minIdx][1], post_data[minIdx][0], direction_dic[direction], post_data[minIdx][idx]))

def printLongest(pre_data, post_data, direction):
    '''
    print the highest/longest performance(direction) among pre, post-operation status
    param pre_data, post_data: list of patient data
    param direction: str, { "lateral", "height" }
    '''
    direction_dic = { "height":"highest", "lateral":"longest" }
    idx=4 if direction=="lateral" else 5
    max=0 
    maxIdx=0
    preHasMaxData=True
    for preIdx in range(len(pre_data)):
        preVal=pre_data[preIdx][idx]
        if preVal>max:
            max=preVal
            maxIdx=preIdx
    for postIdx in range(len(post_data)):
        postVal=post_data[postIdx][idx]
        if postVal>max:
            max=postVal
            maxIdx=postIdx
            preHasMaxData=False
    if(preHasMaxData==True):
        print("Patient %s %s threw the %s with %.1f" 
            %(pre_data[maxIdx][1], pre_data[maxIdx][0], direction_dic[direction], pre_data[maxIdx][idx]))
    else: 
        print("Patient %s %s threw the %s with %.1f" 
            %(post_data[maxIdx][1], post_data[maxIdx][0], direction_dic[direction], post_data[maxIdx][idx]))


def printHighest(pre_data, post_data, gender, direction):
    '''
    print the highest/longest performance(direction) among pre, post-operation status refer to gender
    param pre_data, post_data: list of patient data
    param gender: str, { "female", "male" }
    param direction: str, { "lateral", "height" }
    '''
    direction_dic = { "height":"highest", "lateral":"longest" }
    gender_dic ={ "female":"Female", "male":"Male" }
    idx=4 if direction=="lateral" else 5
    max=0
    maxIdx=0
    preHasMaxData=True
    for preIdx in range(len(pre_data)):
        preVal=pre_data[preIdx][idx]
        if preVal>max and pre_data[preIdx][3]==gender:
            max=preVal
            maxIdx=preIdx
    for postIdx in range(len(post_data)):
        postVal=post_data[postIdx][idx]
        if postVal>max and post_data[postIdx][3]==gender:
            max=postVal
            maxIdx=postIdx
            preHasMaxData=False
    if(preHasMaxData==True):
        print("%s patient %s threw the ball the %s"
        %(gender_dic[gender], pre_data[maxIdx][1], direction_dic[direction])) 
    else: 
        print("%s patient %s threw the ball the %s" 
        %(gender_dic[gender], post_data[maxIdx][1], direction_dic[direction]) )

def printSortBy(dataList, sortedOn, reverse):
    '''
    print the data sorted on indicated features by ascending or descending
    param dataList: list of patient data
    param sorted_item: list of features
    param reverse: boolean, { False: "ascending ", True: "descending" }
    '''
    features_dict={ "PREOP":0, "id":1, "age":2, "female":3, "lateral":4, "height":5 }
    sortedDataList = sorted(sorted(dataList, 
                    key = lambda x : x[features_dict[sortedOn[1]]], reverse = reverse), 
                    key = lambda x : x[features_dict[sortedOn[0]]], reverse = reverse)  
    print("Post op by %s and throw:" %(sortedOn[0]))
    for i in range(len(sortedDataList)):
        print("%s %s %.1f" 
            %(sortedDataList[i][features_dict["id"]], 
            sortedDataList[i][features_dict[sortedOn[0]]], 
            sortedDataList[i][features_dict[sortedOn[1]]]))

def printLargestDifferent(pre_data, post_data, direction):
    '''
    print the data which has the largest difference of performance(direction)
    param pre_data, post_data: list of patient data
    param direction: str, { "lateral", "height" }
    '''
    idx=4 if direction=="lateral" else 5
    max=0
    maxidx=-1
    for i in range(len(pre_data)):
        diff = abs(pre_data[i][idx]-post_data[i][idx])
        if diff>max:
            max=diff
            maxidx=i
    print("Patient %s had the largest difference of %.1f" 
        %(pre_data[maxidx][1], max))

post_data=[]
pre_data=[]
file_dict={ 1:"POST", 2:"PRE", 3:"POST", 4:"PRE", 5:'PRE', 6:"POST", 7:"PRE", 8:"POST" }
direction={ 1:"lateral", 2:"height" }
gender={ 0:"female", 1:"male" }

for record_num in file_dict.keys():
    if file_dict[record_num]=="PRE":
        pre_data+=[makeData(record_num, file_dict[record_num]+"OP")]
    else:
        post_data+=[makeData(record_num, file_dict[record_num]+"OP")]
        
printAvg(pre_data,post_data,direction[1])
printShortest(pre_data, post_data,direction[1])
printLongest(pre_data, post_data,direction[1])
printHighest(pre_data, post_data, gender[1], direction[2])
printHighest(pre_data, post_data, gender[0], direction[2])
print()
printSortBy(post_data, ["age", direction[1]], reverse=False) #age, lateral
print()
printLargestDifferent(pre_data, post_data, direction[1])
