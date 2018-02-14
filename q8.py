import matplotlib.pyplot as plt
x=[0,1.5,9.75,13.8,18.5]
y=[9,5,5,6,7]
print(y)
axes=[-1,25,0,12];
plt.plot(x,y );
plt.plot(x,y ,'ro');
plt.axis(axes);
plt.xlabel('Time of the day (24 hour format');
plt.ylabel('Number of users online');
plt.title('');
plt.show();