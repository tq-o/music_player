import csv
from collections import defaultdict

rows =[]
columns = defaultdict(list) # each value in each column is appended to a list

with open ('top2018.csv','r') as csvfile:
    #csvreader  = csv.reader(csvfile, delimiter = ',')
    csvreader  = csv.DictReader(csvfile) 
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row)
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
   
    # get total number of rows 
    print("Total no. of rows: %d"%(csvreader.line_num)) 


# #  printing first 5 rows 
# print('\nFirst 5 rows are:\n') 

# for row in rows[:5]: 
#  # parsing each column of a row 
#     for col in row: 
#         print(col), 
#     print('\n') 

# #Columns:

# print(columns['name'])


# for name in columns['name']:
#     if name[0]=='D' or name[0]=='d': print(columns['name'].index(name))

lens = len(columns['name'])

# love -> energy

def loveHelper():
    songList=[]
    for i in range (0, lens):
        if (float(columns['energy'][i]) > 0.7):
          songList.append(i) 
    return songList

# joy -> valence
def joyHelper():
    songList=[]
    for i in range (0, lens):
        if (float(columns['valence'][i]) > 0.4):
          songList.append(i)  
    return songList

# Anger -> tempo or loudness
def angerHelper():
    songList=[]
    for i in range (0, lens):
        if (float(columns['tempo'][i]) > 90):
          songList.append(i)  
    
    for j in range (0, lens):
        check = columns['loudness'][j]
        if (float(check) > -6) and (j not in songList):
          songList.append(j)

    return songList

# Fear -> loudness
def fearHelper():
    songList=[]
    for i in range (0, lens):
        if (float(columns['loudness'][i]) > -5.4):
          songList.append(i)
    return songList

# Sadness -> acousticness
def sadHelper():
    songList=[]
    for i in range (0, lens):
        if (float(columns['acousticness'][i]) > 0.17) and (
            float(columns['tempo'][i])<90):
          songList.append(i)
    return songList

songListNum=[]
songTempNum=[]

#dance 

def dance_helper(start, end): 
    
    global songListNum
    for i in range (0, lens):
        check = columns['danceability'][i]
        if (float(check) >= float(start)) and (float(check) <= float(end)):
            songListNum.append(i)


#energy

# another solution only require one list - songListNum list): 
# 
# global songListNum
# for i in range (0, lens):
#   check = columns['energy'][i]
#   if (float(check) >= float(start)) and (float(check) <= float(end)):
#             songListNum.remove(i)

def energy(start, end):

    global songListNum
    global songTempNum
    for i in range (0, lens):
        check = columns['energy'][i]
        if (float(check) >= float(start)) and (float(check) <= float(end)):
            songTempNum.append(i)

    songListNum = intersection(songListNum, songTempNum)
    songTempNum = []


#acousticness
def acousticness(start, end):

    global songListNum
    global songTempNum
    for i in range (0, lens):
        check = columns['acousticness'][i]
        if (float(check) >= float(start)) and (float(check) <= float(end)):
            songTempNum.append(i)

    songListNum = intersection(songListNum, songTempNum)
    songTempNum = []

#tempo
def tempo(start, end):

    global songListNum
    global songTempNum
    for i in range (0, lens):
        check = columns['tempo'][i]
        if (float(check) >= float(start)) and (float(check) <= float(end)):
            songTempNum.append(i)

    songListNum = intersection(songListNum, songTempNum)
    songTempNum = []


def resultList(T1,T2,T3,T4,T5,T6,T7,T8):
    global songListNum
    dance_helper(T1,T2)
    energy(T3,T4)
    acousticness(T5, T6)
    tempo(T7, T8)
    return songListNum

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

def getName(ind):
    return (columns['name'][int(ind)] + " by " + columns['artists'][int(ind)])
# A = resultList(0,1,0,1,0,1,64,198)
# for a in A:
#     print(a)

csvfile.close()