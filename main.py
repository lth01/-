class Node:
    def __init__(self,data,prev=None,next=None):
        self.prev= prev
        self.data= data
        self.next= next
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

CACHE_SIZE=3
Cache_head=Node(0)
Cache_tail=Node(-1)

_init(Cache_head,Cache_tail)

list=List()
map=dict() # key:node
count_map=dict() #key:hit_count
total_count=0
total_hit_count=0
popular_values=-1
index=0
F = open("./request1.tr", 'r')


while(True):
    Cache_request = F.readline()
    if not Cache_request:
        break  # ""를 읽어오면 EOF이므로 종료한다.
    else:
        Cache_request = int(Cache_request)  # 읽어온 str문자열을 정수로 바꾼다.
    total_count+=1
    types=list.update(Cache_head,map,Cache_request,count_map)
    if(type(types)==int): #읽어온 값이 없었다면
        list.append(Cache_head,map,Cache_request)
    if(Cache_head.data>CACHE_SIZE):
        list.delete(Cache_head,Cache_tail,map)

for val in count_map.keys():
    tmp=count_map.get(val)
    if(popular_values<tmp):
        popular_values=tmp
        index=val#해당 맵의 키값저장
    total_hit_count+=tmp

print("Result of using LRU")
print("Hit :",total_hit_count)
print("Miss :",total_count-total_hit_count)
print("Most popular data ID :",index)
print("The number of hits for the most popular ID :",count_map.get(index))
