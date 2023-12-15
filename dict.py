"""


Dictionaries are unordered set of key value pairs, they themselves are mutable, 
where the KEY is UNIQUE IMMUTABLE data type 
            whereas value can
be both mutable and immutable


"""

d={"Alice":1,"Aman":2,9:10}
print(d[9])

d[9]=9
d["new"]="new"

d.clear()
print(d)

del d
# print(d)             gives an error

d={1:1,2:2,3:3}
dd=d.copy()

d[2]=4
dd[3]=7
print(d,dd)

        #           suppose we have been given a sequence and want to 
        #               create a dictionary at instance

seq=("abc","bdc","bds","hello")
new=dict.fromkeys(seq,None)
print(new)


#               {'abc': None, 'bdc': None, 'bds': None, 'hello': None}


d={1:1,2:2,3:2}
x=d.get(7,-1)
print(x)

d={"Alice":1,"Aman":2,9:10}
print(d.items())
            #       [('Alice', 1), ('Aman', 2), (9, 10)]

print(d.keys())
            #       ['Alice', 'Aman', 9]

print(d.values())
            #       [1, 2, 10]

d={'Name':"akshat","rn":1}
d.setdefault("rnn",0)
print(d)                    #       {'Name': 'akshat', 'rn': 1, 'rnn': 0}

d={1:1,2:2,3:3}
d1={1:22,2:2,3:12}

d.update(d1)
print(d)