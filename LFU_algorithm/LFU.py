import operator



class Node:
    def __init__(self,data,freq_node,prev=None,next=None):
        self.data=data
        self.freq_node=freq_node #type is Freq_Node
        self.prev=prev
        self.next=next

class Freq_Node:
    def __init__(self,freq,prev=None,next=None):
        self.freq=freq
        self.prev=prev
        self.next=next
        self.head=Node(-1,self)
        self.tail=Node(-1,self)
        self._init(self.head,self.tail)

    def _init(self,head,tail):
        head.prev=self
        head.next=tail
        tail.prev=head
    def append_first(self,key,node):
        if(node==None):
            new_node=Node(key,self)
        else:
            new_node=node
        tmp_node=self.head.next
        new_node.prev=self.head
        new_node.next=self.head.next
        self.head.next=new_node
        tmp_node.prev=new_node
        new_node.freq_node=self
        return new_node

class LFU_CACHE(object):
    def __init__(self):
        self.head_freq=Freq_Node(-1)
        self.map={}
        self.capacity=100 #CACHE_SIZE

    def appned_freq(self,prev_freq_node,freq):
        new_freq_node=Freq_Node(freq+1)
        prev_freq_node.next=new_freq_node
        new_freq_node.prev=prev_freq_node
        return new_freq_node



    def find(self,key):
        if(self.map.get(key)):
            return key
        else:
            return False

    def update(self,key):
        cur_node=self.map[key]
        cur_freq_node=cur_node.freq_node
        if(cur_freq_node.next==None):
            self.appned_freq(cur_freq_node,cur_freq_node.freq)
        next_freq_node=cur_freq_node.next
        prev_node=cur_node.prev
        prev_node.next=cur_node.next
        cur_node.next.prev=prev_node
        next_freq_node.append_first(key,cur_node)


    def delete(self):
        search_freq_node=self.head_freq.next
        while(search_freq_node!=None):
            if(search_freq_node.tail.prev!=search_freq_node.head):
                that_node=search_freq_node.tail.prev #삭제될 노드
                that_node.prev.next=search_freq_node.tail
                search_freq_node.tail.prev=that_node.prev
                del self.map[that_node.data]
                self.capacity+=1
                break
            else:
                search_freq_node=search_freq_node.next

    def set(self,key):
        global hit_count
        global hit_map
        set_node=self.find(key)
        if(set_node==False):#노드가 없을경우
            if(self.head_freq.next==None):
                zero_freq_node=self.appned_freq(self.head_freq,self.head_freq.freq)
            else:
                zero_freq_node=self.head_freq.next
            set_node = zero_freq_node.append_first(key,None)
            self.map[key] = set_node
            self.capacity-=1
        else:
            hit_count+=1
            if(hit_map.get(key)==None):
                hit_map[key]=1
            else:
                hit_map[key]+=1
            self.update(key)
def print_func(freq_node):
    print(freq_node.freq,'\n')
    tmp=freq_node.head
    while(True):
        print(tmp.data)
        if(tmp.next==None):
            break
        tmp=tmp.next
    print("\n")


lfu=LFU_CACHE()
total_count=0
hit_count=0
hit_map={}#key:hit_count
F = open("./request.tr", 'r')

while(True):
    Cache_request=F.readline()
    if not Cache_request:
        break #""를 읽어오면 EOF이므로 종료한다.
    else:
        Cache_request=int(Cache_request)#읽어온 str문자열을 정수로 바꾼다.
    total_count+=1
    lfu.set(Cache_request)
    if(lfu.capacity<0):
        lfu.delete()
print("Result of using LFU\n")
print("Hit :", hit_count)
print("Miss :", total_count-hit_count)
popular_id=max(hit_map.items(), key=operator.itemgetter(1))[0]
print("Most popular data ID : ",popular_id)
print("The number of hits for the most popular ID :" ,hit_map[popular_id])
