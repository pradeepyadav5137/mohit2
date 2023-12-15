f=open("city.txt","w+")
l=['Delhi','Mumbai','Kolkata','Lucknow',
'Haryana','Dehradun','Patna','Kota','Jaipur',
'Pune']

for i in l:
    f.write(i+"\n")
f.close()