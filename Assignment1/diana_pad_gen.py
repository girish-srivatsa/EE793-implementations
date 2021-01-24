import copy
string_set = ['0', '1', '2', '3', '4', '1', '0', '3', '2', None, '2', '3', '0', '1', None, '3', '2', '1', '0', None, '4', None, None, None, '0']
pair_set=['00', '01', '02', '03', '04', '10', '11', '12', '13', '14', '20', '21', '22', '23', '24', '30', '31', '32', '33', '34', '40', '41', '42', '43', '44']
init_set=[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
total_set=[init_set]

def printAllKLength(char_set, k):
    n = len(char_set)
    printAllKLengthRec(char_set, "", n, k)

def fill(x,y,ch,set_data):
  ch_int=int(ch)
  x_int=int(pair_set[5*x+y][0])
  y_int=int(pair_set[5*x+y][1])
  if set_data[5*x+y] or set_data[5*y+x] or set_data[5*x_int+ch_int] or set_data[5*ch_int+x_int] or set_data[5*y_int+ch_int] or set_data[5*ch_int+y_int] is not None:
    return False
  else:
    set_data[5*x_int+ch_int]=pair_set[5*x+y][1]
    set_data[5*ch_int+x_int]=pair_set[5*x+y][1]
    set_data[5*y_int+ch_int]=pair_set[5*x+y][0]
    set_data[5*ch_int+y_int]=pair_set[5*x+y][0]
    set_data[5*y+x]=ch
    set_data[5*x+y]=ch
    return True
def revert_fill(x,y,ch,set_data):
  ch_int=int(ch)
  x_int=int(pair_set[5*x+y][0])
  y_int=int(pair_set[5*x+y][1])
  set_data[5*x_int+ch_int]=None
  set_data[5*ch_int+x_int]=None
  set_data[5*y_int+ch_int]=None
  set_data[5*ch_int+y_int]=None
  set_data[5*y+x]=None
  set_data[5*x+y]=None

def find_empty(set_data):
  for i in range(25):
    if set_data[i] is None:
      x=i//5
      y=i-5*x
      return (x,y)
  return None

def mapping(ch):
  if ch == "0":
    return "A"
  if ch == "1":
    return "B"
  if ch == "2":
    return "C"
  if ch == "3":
    return "D"
  if ch == "4":
    return "E"
  if ch is None:
    return "-"

def print_table(set_data):
  print(" ")
  for i in range(8):
    print("-",end="-")
  print("-")
  for i in ["|","  |","A","B","C","D","E"]:
    print(i,end=" ")
  print("|")
  for i in range(8):
    print("-",end="-")
  print("-")
  for i in range(5):
    print("|",end=" ")
    print(mapping(str(i)),"|",end=" ")
    for j in range(5):
      print(mapping(set_data[5*i+j]),end=" ")
    print("|")
    for j in range(8):
      print("-",end="-")
    print("-")

def solver():
  total_set=[[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]
  flagGlob=True
  while flagGlob:
    t_set=copy.deepcopy(total_set)
    for i in total_set:
      iter=copy.deepcopy(i)
      ans=find_empty(iter)
      if ans is None:
        flagGlob=False
        pass
      else:
        x,y=ans[0],ans[1]
        test=copy.deepcopy(iter)
        flag=True
        for j in ["0","1","2","3","4"]:
          dat=fill(x,y,j,iter)
          if dat:
            flag=False
            t_set.append(iter)
            iter=copy.deepcopy(test)
        t_set.remove(test)
    total_set=copy.deepcopy(t_set)      
  for i in total_set:
    print_table(i)
  print(len(total_set))




# The main recursive method
# to print all possible
# strings of length k
def printAllKLengthRec(char_set, prefix, n, k):
    global string_set
    # Base case: k is 0,
    # print prefix
    if k == 0:
        string_set.append(prefix)
        return

    # One by one add all characters
    # from set and recursively
    # call for k equals to k-1
    for i in range(n):
        # Next character of input added
        newPrefix = prefix + char_set[i]

        # k is decreased, because
        # we have added a new character
        printAllKLengthRec(char_set, newPrefix, n, k - 1)
for i in range(0,25):
  string_set.append(None)

#printAllKLength(["0","1","2","3","4"],2)
solver()
#iter=init_set
#dat=fill(0,0,"0",iter)
#print(iter)
#iter=string_set
#print(iter)
