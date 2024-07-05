#TO FIND AREA OF CIRCLE USING MODULE


import math                        #where math is the module

def calculate_circle_area(radius): #calculate_circle_area is a function and radius is argument
    area = math.pi * radius**2     #radius**2 given the square of radius
    return area

def main():
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_circle_area(radius)
    print(f"The area of the circle with radius {radius} is: {area} square units.")

if __name__ == "__main__":          #execution began from here
    main()

