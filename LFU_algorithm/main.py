class Node:
    def __init__(self,data,left=None,right=None):
        self.next= next
        self.data= data
        self.map={}#key:val,순서
        self.prev=prev
class List:#node들을 관리해준다.
    def find(self,head,map,val):
        if(map.get(val)==None):
            return -1
        else:
            return map.get(val)

    def update(self,head,map,val,count_map):#val을 찾아 첫번째 노드로 가져온다.
        node=self.find(head,map,val)
        if(node==-1): #노드가 없었다면
            return -1
        else:
            if(node.next):
                tmp_node=node.next
                tmp_node.prev=node.prev
                node.prev.next=tmp_node
                #노드의 연결을 끊었으므로 head.next node로 설정한다.
                tmp_node=head.next
                head.next=node
                node.prev=head
                node.next=tmp_node
                tmp_node.prev=node
                if(count_map.get(val)==None):
                    count_map[val]=1
                else:
                    count_map[val]+=1

    def delete(self,head,tail,map):#해당 함수는 tail만 사용할 수 있다.
        if(tail.next==None):
            tmp_node=tail.prev
            tail.prev=tmp_node.prev
            tmp_node.prev.next=tail
            del map[tmp_node.data]
            head.data-=1
        else:
            print("is not tail node")

    def append(self,head,map,val):
        if(map.get(val)==None):#해당 map에 노드가 없다면
            node=Node(val)
            map[val]=node
        else:
            node=map.get(val)
        if(head.next!=None):
            tmp_node=head.next
            head.next=node
            node.prev=head
            node.next=tmp_node
            tmp_node.prev=node
            head.data+=1

def _init(head,tail):
    head.next=tail
    head.prev=None
    tail.prev=head
    tail.next=None

class FREQ:
    def __init__(self):
        self.head=Node(-1)
        self.tail=Node(-1)
        _init(self.head,self.tail)


    def new_freq(self,freq):#freq보다 작은 값의 노드들은 있다고 가정한다.
        new_node=Node(freq)
        tmp_node=self.tail.prev#가장 FREQ객체에서 freq가 큰 노드
        if (tmp_node.data == freq):
            return -1
        else:
            new_node.next=self.tail
            new_node.prev=tmp_node
            tmp_node.next=new_node
            self.tail.prev=new_node


    def append(self,head,freq):



CACHE_SIZE=100

print("Result of using LRU")
print("Hit :",)
print("Miss :",)
print("Most popular data ID :",)
print("The number of hits for the most popular ID :",)
