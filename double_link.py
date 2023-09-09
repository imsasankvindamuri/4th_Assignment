class node:
    def __init__(self,data):
        self.data=data
        self.nxt=None
        self.prv=None

class dblelnk:
    def __init__(self):
        self.head=None
    
    def addfront(self,data):
        val=node(data)
        val.nxt=self.head
        if self.head is not None:
            self.head.prv=val
        self.head=val
        print("Done!")

    def addend(self,data):
        val=node(data)
        temp=self.head
        while temp.nxt is not None:
            temp=temp.nxt
        val.prv=temp
        val.prv.nxt=val
        temp=None
        print("Done!")

    def disp(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=' ')
            temp=temp.nxt

    def search(self,val):
        temp=self.head
        indx=1
        dup=0
        while temp is not None:
            if temp.data==val:
                print(f"Found in position {indx}")
                dup+=1
            temp=temp.nxt
            indx+=1
        if dup==0:
            print("Not in list")
    
    def delete(self,val):
        temp=self.head
        dup=0
        while temp is not None:
            if temp.data==val:
                if temp.prv is None:
                    temp.nxt.prv=temp.prv
                    self.head=temp.nxt
                    temp=None
                    print("Done!")
                    dup+=1
                    break 
                temp.prv.nxt=temp.nxt
                temp.nxt.prv=temp.prv
                temp=None
                print("Done!")
                dup+=1
                break
            temp=temp.nxt
        if dup==0:
            print("Not in list")



if __name__ == "__main__":
    linked_list = dblelnk()
    
    while True:
        print('''\nLinked List Operations:
        1 = Insert at start
        2 = Insert at end
        3 = Delete from start
        4 = Delete from middle
        5 = Display list
        6 = Search for an element
        7 = Exit''')
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            value = int(input("Enter value to insert: "))
            linked_list.addfront(value)
        # elif choice == 2:
        #     value = int(input("Enter value to insert: "))
        #     linked_list.addmid(value, linked_list.head)
        elif choice == 2:
            value = int(input("Enter value to insert: "))
            linked_list.addend(value)
        elif choice == 3:
            linked_list.delete(linked_list.head.data)
        elif choice == 4:
            if linked_list.head is not None and linked_list.head.nxt is not None:
                linked_list.delete(linked_list.head.nxt.data)
            else:
                print("Insufficient nodes for mid deletion.")
        elif choice == 5:
            linked_list.disp()
        elif choice == 6:
            value = int(input("Enter value to search: "))
            linked_list.search(value)
        elif choice == 7:
            break
        else:
            print("Invalid choice.")