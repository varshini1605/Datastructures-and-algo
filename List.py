#Lists need not be homogeneous always which makes it the most powerful tool in Python
#Python len() is used to get the length of the list.
X= ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
Y = [0,   1,   1,    0,   1,   2,   2,   0,   1]
l={}
final_list={}
l={X[i]:Y[i] for i in range(len(Y))}
#d={k:v for k, v in sorted(l)}
print(l)
