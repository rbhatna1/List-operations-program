def space(): #To make it look good and have proper demarcations
    print()
    print("**********************************************************")
    print()

def cubetuple(list1):
    newlist=[]
    for a in list1:
        tuple=()
        b=a**3
        tuple=(a,b)
        newlist.append(tuple)
    print("The cube of the elements in the list are:",newlist)

def bubblesort(List):
    n=len(List)
    for i in range(n):
        for j in range(n-i-1):
            if List[j+1][1]<List[j][1]:
                List[j+1],List[j]=List[j+1],List[j] #Cannot use indexing as tuple are immutable
    print("The sorted list on the basis of last element is:",List)
    
choice=0
    
while choice!=3:
    print("Choose from one of the folowing options")
    print("1)If you want to find the cube of the list")
    print("2)If you want to sort the list on the basis of the last number")
    choice=int(input("Enter the choice"))
    
    if choice==1:
        space()
        list=eval(input("Enter the list"))
        cubetuple(list)
        space()
        
    if choice==2:
        space()
        list=eval(input("Enter the list"))
        bubblesort(list)
        space()
    