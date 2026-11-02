#Area Calculator Create a function called area() that accepts length and breadth as arguments and returns the area of a rectangle.

def area(length,breadth):
        area=length*breadth
        return area
len=int(input("ENTER THE LENGTH OF RECTANGLE : "))
bre=int(input("ENTER THE BREADTH OF RECTANGLE :"))
result=area(len,bre)
print("AREA OF RECTANGLE IS :",result)
