class Node:
    def __init__(self,value) -> None:
        self.value=value
        self.next=None
    def set_next(self,next):
        self.next=next
    def get_next(self):
        return self.next


class SingleLinked:

    def __init__(self):
        self.head=None
        self.size=0
    
    def add(self,value):
        if self.size==0:
            self.head=Node(value)
            self.size+=1
        else:
            next=self.head
            while(1):
                if next.get_next()==None:
                    next.set_next(Node(value))
                    self.size+=1
                    break
                else:
                    next=next.get_next()
        
    def add_to_index(self,value,index):
        next=self.head
        if index==0:
            if self.size==0:
                print("Error")
                return
            elif self.size!=0:
                new_value,new_next=self.head.value,self.head.get_next()
                self.head.value=value
                self.head.set_next(new_next)
                self.add_to_index(new_value,1)
            return
        elif index>self.size or index<0:
            print("Error")
            return
        else:
            for i in range(self.size):
                if i!=index-1:
                    next=next.get_next()
                else:
                    new=Node(value)
                    new.set_next(next.get_next())
                    next.set_next(new)
                    self.size+=1    
        self.print_linked()
    def get(self,index):
        next=self.head
        if index>self.size-1 or index<0:
            return "Error"
        else:
            for i in range(self.size):
                if i!=index:
                    next=next.get_next() 
                else:
                    return next.value           

    def set(self,value,index):
        next=self.head
        if index>self.size-1 or index<0:
            print("Error")
            return
        else:
            for i in range(self.size):
                if i!=index:
                    next=next.get_next() 
                else:
                    next.value=value
        self.print_linked()

    def clear(self):
        if self.size==0:
            return
        self.size=0
        self.head.set_next(None)
    
    def is_empty(self):
        return not bool(self.size)


    def remove(self,index):
        next=self.head
        if index==0:
            if self.size==0:
                print("Error")
                return
            elif self.size!=0:
                self.head=self.head.get_next()
                self.size-=1

        elif index>self.size-1 or index<0:
            print("Error")
            return
        else:
            for i in range(self.size):
                if i!=index-1:
                    next=next.get_next()
                else:
                    next.set_next(next.get_next().get_next())
                    self.size-=1
        self.print_linked()
    def sublist(self,first,last):
        if first <0 or first >self.size-1 or last<0 or last > self.size-1 or last<first:
            print("Error")
            return
        else:
            next=self.head
            my_sub_list=[]
            for i in range(self.size):
                if i!=first:
                    next=next.get_next()
                else:
                    my_sub_list.append(next.value)
                    for j in range(i,self.size):
                        next=next.get_next()
                        if j == last:
                            print(my_sub_list)
                            return
                        my_sub_list.append(next.value)

    def contains(self,value):
        next=self.head
        for i in range(self.size):
            if value==next.value:
                print("True")
                return
            else:
                next=next.get_next()
        print("False")

    def linked_size(self):
        print(self.size)

    def print_linked(self):
        my_list=[]
        if self.size==0:
            return []
        else:
            next=self.head
            value=self.head.value

            while(next.get_next()!=None):
                my_list.append(value)
                next=next.get_next()
                value=next.value
            my_list.append(next.value)
        return(my_list)


poly_list=[]

def print_poly(set_name):
    poly_text=""
    for my_linked in poly_list:
        if set_name==my_linked[0]:
            try:
                my_poly_list=my_linked[1].print_linked()
            except:
                my_poly_list=my_linked[1]
                
            for i in range(len(my_poly_list)):
                my_poly_list[i]=str(my_poly_list[i])
                if my_poly_list[i][0]!="-" and i!=0:
                    my_poly_list[i]="+"+my_poly_list[i]
            for i in range(len(my_poly_list)):
                
                power=len(my_poly_list)-i-1
                if my_poly_list[i]=="+1" or my_poly_list[i]=="1" :
                    if i==0 or (i==1 and my_poly_list[0]=="0"):
                        if len(my_poly_list)==1:
                            my_poly_list[i]="1"
                        else:
                            my_poly_list[i]=""
                    elif i!=len(my_poly_list)-1:
                        my_poly_list[i]="+"
                    else:
                        my_poly_list[i]="+1"
                #elif my_poly_list[i]=="-1"  and i != len(my_poly_list)-1:
                   # my_poly_list[i]="-"
                
                    
                    
                if my_poly_list[i]=="+0" or my_poly_list[i]=="0" :
                    pass
                elif power==0:
                    poly_text+=f"{my_poly_list[i]}"
                    break
                elif power==1:
                    poly_text+=f"{my_poly_list[i]}x"
                else:
                    poly_text+=f"{my_poly_list[i]}x^{power}"
    #if poly_text=="-" or poly_text=="":
        #return poly_text+"1"
    #else:
    if poly_text=="":
        print("Error")
        quit()
    else:
       return poly_text
my=["A","B","C"]
while(1):
    try:
        operation=input().strip()
    except:
        break
    if operation=="set":
        name=input().strip()
        coof=input().strip()
        coof=coof[1:len(coof)-1].split(",")
        if name in my:
            if name=="A":
                #my.append("A")
                single_a=SingleLinked()
                for i in range(len(coof)):
                    try:
                        single_a.add(int(coof[i]))
                    except (ValueError):
                        del coof[i]
                if single_a.size==0:
                    print("Error")
                    quit()
                poly_list.append(("A",single_a))
            elif name=="B":
                #my.append("B")
                single_b=SingleLinked()
                for i in range(len(coof)):
                    try:
                        single_b.add(int(coof[i]))
                    except (ValueError):
                        del coof[i]
                if single_b.size==0:
                    print("Error")
                    quit()
                poly_list.append(("B",single_b))
            elif name=="C":
                #my.append("C")
                single_c=SingleLinked()
                for i in range(len(coof)):
                    try:
                        single_c.add(int(coof[i]))
                    except (ValueError):
                        del coof[i]
                if single_c.size==0:
                    print("Error")
                    quit()
                poly_list.append(("C",single_c))
        else:
            print("Error")
            quit()
    elif operation=="print":
        set_name=input().strip()
        if set_name in my:
            print(print_poly(set_name))
        else:
            print("Error")
            quit()
        
    elif operation=="add":
        name1=input().strip()
        name2=input().strip()
        if name1 in my and name2 in my:
            first_list=[]
            second_list=[]
            final=[]
            for i in range(len(poly_list)):
                if poly_list[i][0]==name1:
                    first_list=poly_list[i][1].print_linked()
                elif poly_list[i][0]==name2:
                    second_list=poly_list[i][1].print_linked()
            if len(first_list) == 0 or len(second_list)==0:
                print("Error")
                break

            pad=abs(len(first_list)-len(second_list))
            if len(first_list)>len(second_list):
                for i in range(pad):
                    second_list.insert(0,0)
            elif len(first_list)<len(second_list):
                for i in range(pad):
                    first_list.insert(0,0)
            #for i in range(len(first_list)):
            #    final.append(first_list[i]+second_list[i])  
            final = [sum(value) for value in zip(first_list, second_list)] 
            final=[i  for i in final if i!=0 ]
            poly_list.append(("final",final))
            print(print_poly("final"))
            del poly_list[-1]
        else:
            print("Error")
    elif operation=="sub":
        name1=input().strip()
        name2=input().strip()
        if name1 in my and name2 in my:
            first_list=[]
            second_list=[]
            final=[]
            for i in range(len(poly_list)):
                if poly_list[i][0]==name1:
                    first_list=poly_list[i][1].print_linked()
                elif poly_list[i][0]==name2:
                    second_list=poly_list[i][1].print_linked()
            if len(first_list) == 0 or len(second_list)==0:
                print("Error")
                break
            pad=abs(len(first_list)-len(second_list))
            if len(first_list)>len(second_list):
                for i in range(pad):
                    second_list.insert(0,0)
            elif len(first_list)<len(second_list):
                for i in range(pad):
                    first_list.insert(0,0)
            
            second_list=[-i for i in second_list]
            #for i in range(len(first_list)):
            #    final.append(first_list[i]+second_list[i])  
            final = [sum(value) for value in zip(first_list, second_list)]
            final=[i  for i in final if i!=0 ]
            poly_list.append(("final",final))
            ans=print_poly("final")
            if ans=="":
                print("0")
            else:
                print(ans)
            del poly_list[-1]  
        else:
            print("Error")
    elif operation=="mult":
        name1=input().strip()
        name2=input().strip()
        if name1 in my and name2 in my:
            first_list=[]
            second_list=[]
            final=[]
            for i in range(len(poly_list)):
                if poly_list[i][0]==name1:
                    first_list=poly_list[i][1].print_linked()
                elif poly_list[i][0]==name2:
                    second_list=poly_list[i][1].print_linked()
            if len(first_list) == 0 or len(second_list)==0:
                print("Error")
                break
            m=len(first_list)
            n=len(second_list)     
            prod = [0] * (m + n - 1)
            for i in range(m):
                for j in range(n):
                    prod[i + j] += first_list[i] * second_list[j]

            poly_list.append(("prod",prod))
            ans=print_poly("prod")
            if ans=="":
                print(0)
            else:
                print(ans)
            del poly_list[-1]
        else:
            print("Error")

    
    elif operation=="clear":
        name=input().strip()
        if name in my:
            for i in range(len(poly_list)):
                if poly_list[i][0]==name:
                    if poly_list[i][1].size==0:
                        print("Error")
                        break
                    poly_list[i][1].clear()
                    print(poly_list[i][1].print_linked())
                    break
        else:
            print("Error")

    elif operation=="eval":
        name=input().strip()
        try:
            value=float(input().strip())
        except ValueError:
            print("Error")
        if name in my:
            mylist=[]
            ans=0
            for i in range(len(poly_list)):
                if poly_list[i][0]==name:
                    mynode=poly_list[i][1]
                    mylist=mynode.print_linked()
                    break
                
            if mynode.size==0:
                print("Error")
            elif mynode.size==1:
                print(mylist[0])
            else:
                for i in range(len(mylist)):
                    power=len(mylist)-i-1
                    ans+=mylist[i]*(value**power)
                print(int(ans))
        else:
            print("Error")
    else:
        print("Error")
        quit()

        