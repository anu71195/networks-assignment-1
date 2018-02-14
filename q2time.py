import matplotlib.pyplot as plt
x=[1,11.50,19];
y1=[108,104,100,106,98,107,107,107,102,102,104,104,102,98,103,111,108,110,109,112,111,111]
y2=[116,117,118,116,117,118,116,117,116,116,118,116,116,117,117,116,117,117,117,116,117,117]
y3=[97, 97, 99, 97, 98, 97, 97, 97, 97, 98, 97, 97, 97, 97, 97, 104, 104, 106, 105, 104, 104, 106]
observations=len(y1);
y=[];
y.append(sum(y1)/observations);
y.append(sum(y2)/observations);
y.append(sum(y3)/observations);
print(y)
axes=[0,24,90,120];
plt.plot(x,y);
plt.plot(x,y,'ro');
plt.axis(axes);
plt.xlabel('time of the day (24 hour format)');
plt.ylabel('round trip time (rtt) (in ms)');
plt.show();