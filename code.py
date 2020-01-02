
import csv
from math import sin, cos, sqrt, atan2, radians
with open(r"comp1.csv")as f:
    i=0
    count=0
    data = csv.reader(f)
    for row1 in data:
        first = second = 9999999
        lat1=radians(float(row1[2]))
        lon1=radians(float(row1[3]))
        with open(r"weather11.csv")as f1:
            data1=csv.reader(f1)
            for n in data1: 
                                                     
                    lat2 = radians(float(n[2]))
                    lon2 = radians(float(n[3]))       
                    R = 6373.0

                   

                    dlon = lon2 - lon1
                    dlat = lat2 - lat1

                    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
                    c = 2 * atan2(sqrt(a), sqrt(1 - a))

                    distance = R * c
                    
                    count=count+1 
                    if distance < first: 
                        second = first 
                        first = distance
                        p1=row1[1]
                        p2=row1[2]
                        p3=row1[3]
                        p4=n[1]
                        p5=n[2]
                        p6=n[3]
                       
  
         
                    elif (distance < second and distance != first): 
                        second = distance
                        p11=row1[1]
                        p12=row1[2]
                        p13=row1[3]
                        p14=n[1]
                        p15=n[2]
                        p16=n[3]
        print(p1,p2,p3,p4,p5,p6,first)
        print(p11,p12,p13,p14,p15,p16,second)
        print(first)        
        print(second)
        print("_____________")
        
        i=i+1
         
        with open(r"manuop1.csv","a",newline='' ) as f3:
                       wtr = csv.writer(f3)
                       wtr.writerows([[p1,p2,p3,p4,p5,p6,first],[p11,p12,p13,p14,p15,p16,second]])
print(i) 
print(count)
