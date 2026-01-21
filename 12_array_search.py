import numpy as np
# search an array for a certain value and return the index that has that value,,using  where()

d=np.array([1,2,3,2,2,4,5])
index=np.where(d==2)  #yani "d" m 2 jhan jhan bhi h us ka index bta do
print(index)

# now we will find the indexes where the values are even
for i in d:
    if (i%2==0):
        index=np.where(d==i)  #2nd iteration m dekha k value "2" pr remainder "0" h, or phir
        # hr us index ko dekhyn gy jha jha "2" present ho ga, is liye output m repeatation 
        # a rhi ,,,, asal m is time "i" m "2" mojood h or hm keh rhyn hn k "d" m jhan jhan
        # bhi "2" mojod h un ka indexes bta do , isliye bhi repeatation a rhi
        print(index)  #1 3 4 5 

print()
print()
print()
print()
#   !!!!!!!!!!!!!!!1  searchsorted()  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# searchsort performs a binary search in an array and returns an index where the specified
# value would be inserted to maintain the search order

# you get correct answer, you must have sorted array
x=np.array([1,2,4,5])
index_where_element_should_insert=np.searchsorted(x,3) #yani "3" ko mujy kis index pr
# insert krvana chahye k order maintain rhy(yani k array sorted hi rhy)
print(index_where_element_should_insert)


x=np.array([1,2,4,5])
index_where_element_should_insert=np.searchsorted(x,100) #yani "100" ko mujy kis index pr
# insert krvana chahye k order maintain rhy(yani k array sorted hi rhy)
print(index_where_element_should_insert)


x=np.array([1,2,4,5])
index_where_element_should_insert=np.searchsorted(x,2) #yani "2" ko mujy kis index pr
# insert krvana chahye k order maintain rhy(yani k array sorted hi rhy)
print(index_where_element_should_insert)


# ---------------------- side
# searchsorted bydefault left to right move krta h but hm is ko right s left bhi move krva
# skty

x=np.array([1,2,4,5])
index_where_element_should_insert=np.searchsorted(x,2,side="right") #yani "2" ko mujy kis index pr
# insert krvana chahye k order maintain rhy(yani k array sorted hi rhy) agar m right side 
# s dekhu to!
print(index_where_element_should_insert)


# -----------------------------  passing multiple values
c=np.array([2,3,9,12])
indexes=np.searchsorted(c,[1,5,100]) #yani (1,5,100) ko kin kin indexese pr place krna chhaye
print(indexes)








