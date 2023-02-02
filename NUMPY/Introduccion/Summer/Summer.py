import numpy as np
import matplotlib.pyplot as plt


a = np.array([2, 4, 9, 5])
b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])

print(a.dtype)
print(b.dtype)
print(np.__version__)
print(a)


c = b[1:4]
# Show 
containIndex = [0, 2, 1, 3]
c = b[ containIndex ]
print(c)

b[ containIndex ] = 1000
print(b)


print(a.size)
print(a.ndim)
print(a.shape) # Shape like size
# print(d.ndim)


# Statistical Function
print("\n\nStatistical Function")
a = np.array([1, -1, 1, -1])
mean = a.mean()
print(mean)
# Get the standard deviation of numpy array
print(a.std())
print(a.max())
print(a.min())


# Numpy Array Operations
print("\n\nNumpy Array Operations")
u = np.array([1, 0])
v = np.array([0, 1])
z = np.add(u,v)


def Plotvec1(u, z, v):    
    ax = plt.axes() # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
    plt.ylim(-20, 20)#set the ylim to bottom(-2), top(2)
    plt.ylabel("Y")
    plt.xlim(-20, 20)#set the xlim to left(-2), right(2)
    plt.xlabel("X")
    plt.show()

Plotvec1(u, z, v)

arr1 = np.array([10, 20])
arr2 = np.array([20, 21])
arr3 = np.subtract(arr1, arr2)
print(arr3)

Plotvec1(arr1, arr3, arr2)



# Adding Constant to a Numpy Array
print("\n\nAdding Constant to a Numpy Array")
u = np.array([1, 2, 3, -1]) 
print(u+8)



# Mathematical Functions
print("\n\nMathematical Functions")
print("pi",np.pi)
x = np.array([0, np.pi/2 , np.pi])
print(x)
y = np.sin(x)
print(y)
ls = np.linspace(0,2*np.pi,6)
print(ls)
x = np.linspace(0, 2*np.pi, num=100)
y = np.sin(x)
plt.plot(x, y)
plt.show()
