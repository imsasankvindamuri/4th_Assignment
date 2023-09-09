class node:
    def __init__(self,data):
        self.data=data
        self.nxt=None
        self.prv=None

class crcllnk:
    def __init__(self):
        self.head=None
    
    def addfront(self,data):
        new=node(data)
        if self.head is None:
            new.prv=new
            new.nxt=new
            self.head=new
        else:
            new.nxt=self.head
            new.prv=self.head.prv
            self.head.prv.nxt=new
            self.head.prv=new
            self.head=new

    def addend(self,data):
        new=node(data)
        if self.head is None:
            new.prv=new
            new.nxt=new
            self.head=new
        else:
            new.prv=self.head.prv
            new.nxt=self.head
            self.head.prv.nxt=new
            self.head.prv=new

    def disp(self):
        temp=self.head
        while True:
            print(temp.data,end=' ')
            if temp.nxt == self.head:
                break
            temp=temp.nxt

    def search(self,val):
        temp=self.head
        indx=1
        dup=0
        while True:
            if temp.data==val:
                print(f"Found in position {indx}")
                dup+=1
            if temp.nxt is self.head:
                break    
            temp=temp.nxt
            indx+=1
        if dup==0:
            print("Not in list")

    def delete(self,val):
        temp=self.head
        dup=0
        while True:
            if temp.data==val:
                temp.nxt.prv=temp.prv
                temp.prv.nxt=temp.nxt
                self.head=temp.nxt
                break
            elif temp.nxt==self.head:
                break
            temp=temp.nxt

if __name__ == "__main__":
    linked_list = crcllnk()
    
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
            val = int(input("Enter value to insert: "))
            linked_list.addfront(val)
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