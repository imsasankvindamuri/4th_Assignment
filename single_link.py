class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class lnkdlst:
    def __init__(self):
        self.head=None
    
    def addfront(self,val):
        new=node(val)
        new.next=self.head
        self.head=new
        print("Done!")

    def addmid(self,val,prev):
        if prev is None:
            print("Error: Previous Node Cannot be None")
        else:
            new=node(val)
            new.next=prev.next
            prev.next=new
            print("Done!")
    
    def addend(self,val):
        new=node(val)
        if self.head is None:
            self.head=new
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new
        print("Done!")

    def delfront(self):
        if self.head is None:
            print("Error: Can't delete from empty list")
        else:
            temp=self.head
            self.head=temp.next
            temp=None
            print("Deleted")

    def delmid(self,prev):
        if self.head is None:
            print("Error: Can't delete from empty list")
        elif prev is None or prev.next is None:
            print("Invalid Node")
        temp=prev.next
        prev.next=temp.next
        temp=None
        print("Deleted")
    
    def delend(self):
        if self.head is None:
            print("Error: Can't delete from empty list")
        if self.head.next is None:
            self.head=None
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None
        print("Deleted")
    
    
    def disp(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=' ')
            temp=temp.next

    def search(self,val):
        temp=self.head
        indx=1
        dup=0
        while temp is not None:
            if temp.data==val:
                print(f"Found in position {indx}")
                dup+=1
            temp=temp.next
            indx+=1
        if dup==0:
            print("Not in list")

if __name__ == "__main__":
    linked_list = lnkdlst()
    
    while True:
        print('''\nLinked List Operations:
        1 = Insert at start
        2 = Insert in the middle
        3 = Insert at end
        4 = Delete from start
        5 = Delete from middle
        6 = Delete from end
        7 = Display list
        8 = Search for an element
        9 = Exit''')
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            value = int(input("Enter value to insert: "))
            linked_list.addfront(value)
        elif choice == 2:
            value = int(input("Enter value to insert: "))
            linked_list.addmid(value, linked_list.head)
        elif choice == 3:
            value = int(input("Enter value to insert: "))
            linked_list.addend(value)
        elif choice == 4:
            linked_list.delfront()
        elif choice == 5:
            if linked_list.head is not None and linked_list.head.next is not None:
                linked_list.delmid(linked_list.head)
            else:
                print("Insufficient nodes for mid deletion.")
        elif choice == 6:
            linked_list.delend()
        elif choice == 7:
            linked_list.disp()
        elif choice == 8:
            value = int(input("Enter value to search: "))
            linked_list.search(value)
        elif choice == 9:
            break
        else:
            print("Invalid choice.")