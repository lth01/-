#LRU Algorithm #2
#이전 알고리즘은 시간 복잡도가 높아 캐시가 많을경우 최대 1시간까지도 실행시간이 걸렸었다.

class Cache_memory:

    def __init__(self,_val,_prev=None,_next=None):

        self.val=_val
        self.prev=_prev
        self.next=_next

    def Cache_update(self): #좌우 노드들의 연결을 서로 시키고 나는 맨앞으로 이동 head,tail의 앞뒤에 있는 노드는 아니라고 가정
        tmp=self.prev
        (self.next).prev=tmp #다음 노드의 이전 값을 tmp로 설정
        (self.prev).next=self.next
        self.next=Cache_head.next
        self.prev=Cache_head
        Cache_head.next=self





def _init_Cache(head,tail):
    head.next=tail
    tail.prev=head

def find(key,map): #map의 node값이 None이 아니면 key값을 리턴한다. 만약 None이라면 -1을 리턴한다.(리스트안에 없다)
    if(map[key][0]!=None):
        return key
    else:
        return -1


CACHE_SIZE = 10000
  # cache size를 미리 정해준다.

Hit_count =0
Miss_count =0
Cache_request = 0  # id 값을 불러와 임시적으로 저장할 변수

map=dict() #dict은 key:[node,count]로 관리될 것이다.

Cache_head=Cache_memory(-1)
Cache_tail=Cache_memory(-1)

_init_Cache(Cache_head,Cache_tail)



F = open("./request.tr", 'r')  # f라는 객체에 파일 request.tr을 일여놓는다.

while(True):
    Cache_request=F.readline()
    if not Cache_request:
        break #""를 읽어오면 EOF이므로 종료한다.
    else:
        Cache_request=int(Cache_request)#읽어온 str문자열을 정수로 바꾼다.
    index=find(Cache_request, Cache_memory)
    if(index>=0):#이미 캐시메모리 안에 해당 값이 있다면 그 값의 index=0으로한다 삭제 x
        tmp=Cache_memory[index]
        del Cache_memory[index]
        append(tmp)
        Hit_count+=1
    else:#캐시메모리에 index가 존재하지 않는다면 Cache_memory의 첫번째 인덱스를 삭제하고, 맨 마지막에 값을 추가해준다.
        append(Cache_request)
        Miss_count+=1
