class Node:
    def __init__(Node,data):
        Node.data=data
        Node.next=None
        Node.prev=None


def insertstart(head,newNode):
    newNode.next=head
    head.prev=newNode
    newNode.prev=None
    head=newNode
    return head

def insertmiddle(head,newNode):
    temp=head
    while(temp.next!='c'):
        temp=temp.next
    buffer=temp.next
    temp.next=newNode
    newNode.prev=temp
    newNode.next=buffer
    buffer.prev=newNode
    return head


def insertend(head,newNode):
    temp=head
    while(temp.next!='c'):
        temp=temp.next
    temp.next = newNode
    newNode.prev = temp
    newNode.next = None
    return head


def printlist(head):
    temp=head
    while(temp):
        print(temp.data)
        temp=temp.next

head=Node('a')
second=Node('b')
third=Node('c')
fourth=Node('d')


head.next=second
second.next=third
third.next=fourth

second.prev=head
third.prev=second
fourth.prev=third

z=insertstart(head,Node('z'))
printlist(z)


        
        
    
    
    
