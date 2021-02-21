def area_of_circle():
    r=float(input('Enter radius:'))
    area=3.14*(r**2)
    print('Area of circle is ',area)

def circumference_of_circle():
    r=float(input('Enter radius:'))
    circ=2*3.14*r
    print('Circumference of the circle is ',circ)

def area_of_rect():
    l=float(input('Enter length:'))
    b=float(input('Enter breadth:'))
    area=l*b
    print('Area of rectangle is ',area)

def perimeter_of_rect():
    l=float(input('Enter length:'))
    b=float(input('Enter breadth:'))
    perimeter=2*(l+b)
    print('Perimeter of rectangle is ',perimeter)

intro='''
Please enter the option you want
1. To find the area of a circle
2. To find the circumference of a circle
3. To find the area of a rectangle
4. To find the perimeter of a rectangle
'''
ans=1
while ans==1:
    print(intro)
    inp=int(input())
    if inp==1:
        area_of_circle()
    elif inp==2:
        circumference_of_circle()
    elif inp==3:
        area_of_rect()
    elif inp==4:
        perimeter_of_rect()
    else:
        print('Invalid entry')
    print()
    ans=int(input('If u wanna continue, press 1, else press any other key:'))    
