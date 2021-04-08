# LRU Algorithm

def find(value, queue):  # queue에서 value를 찾아본다. 대상이 있다면 index를 없다면 -1를 리턴한다.
    if value in queue:
        return queue.index(value)
    else:
        return -1


def append(value):  # Cache_memory에 value를 추가한다. CACHE_SIZE까지만 된다.
    global Cache_memory
    if (len(Cache_memory) <= (CACHE_SIZE - 1)):
        Cache_memory.append(value)
    elif (len(Cache_memory) == (CACHE_SIZE)):  # queue size가 chach_size와 같다면(꽉 찼다면)
        del Cache_memory[0]
        Cache_memory.append(value)


CACHE_SIZE = 10000
  # cache size를 미리 정해준다.

Hit_count =0
Miss_count =0
Cache_request = 0  # id 값을 불러와 임시적으로 저장할 변수

Cache_memory = []  # global list

# for i in range(CACHE_SIZE):
#     Hit_count[i]=0
#     #Hit_count리스트를 초기화해준다.

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

print("Hit Count:"+str(Hit_count)+"Miss Count:"+str(Miss_count))