# rotate aray A by K positions

def solution(A, K):
    
    ret = A
    
    cnt = len(A)
    if K > cnt:
        raise ValueError(f"K cannot be more then {len(A)}")
    if K == 0 or K == cnt or cnt == 0:
        return ret
    
    #arr_ = A[cnt-K:].copy()          #v1-3. copy lask K elements
    # del A[cnt-K:]                   #v1-3. delete them from array
    # A[0:0] = arr_                   # v1. array slicing, to insert arr_
    # for i in range(0, K):           # v2. loop, to insert arr_
    #     A.insert(i, arr_[i])
    # arr_.extend(A)                  # v3. extend
    # ret = arr_                      # v3.
    
    A[0:0] = A[cnt-K:]                # v4. slicing
    del A[len(A)-K:]                  # v4.
    
    return ret
        
def main():
    
    K = 3
    arr = [1,2,3,4]
    
    # testing 0, max...
    #solution(arr, 4)
    #print(f"after ratate:", arr)
    #exit(0)
    
    print('before', arr)
    res  = solution(arr, K)
    print(f"after (K = {K}):", res)
     
    # for i in range(1, len(arr) + 1):
    #     arr_cpy = arr.copy()
    #     res  = solution(arr, i)
    #     print(f"after ratate{i}:", res)
    #     arr = arr_cpy.copy()
    
    print("test: the same array was transformed arr[0] = 111")
    res[0] = 111
    print(f"res :", res)
    print(f"arr :", res)
    
       
if __name__ == "__main__":
    main()