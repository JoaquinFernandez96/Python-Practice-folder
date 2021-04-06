import matplotlib.pyplot as plt
import numpy as np
e=1504170715041707
mod=4503599627370517
tot=e
min=e
max=e

temp=[]
v_temp=[]
min_temp=[]
max_temp=[]

while True:
    if min==1:
        break
    v=min+max
    v_temp.append(v)
    min_temp.append(min)
    max_temp.append(max)
    temp+=1
    v%=mod
    if v>max:
        max=v
    if v<min:
        min=v
        tot+=min    
print("TOTAL:",tot)
