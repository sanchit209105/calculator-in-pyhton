while True:
    print("Welcome to Calculator \n1.Calculate Finfer \n2.Area Finder \n3.Volume of finder \n4.Exit")
    opt=int(input("Choose any option:"))
    if opt==1:
        while True:
            print("1.Add \n2.Subtract \n3.Multiple \n4.Divide")
            opt2=int(input("Choose any option:"))
            if opt2==1:
                a=int(input("Enter the 1st value:"))
                b=int(input("Enter the 2st value:"))
                print(a+b)
            if opt2==2:
                a=int(input("Enter the 1st value:"))
                b=int(input("Enter the 2st value:"))
                print(a-b)
            if opt2==3:
                a=int(input("Enter the 1st value:"))
                b=int(input("Enter the 2st value:"))
                print(a*b)
            if opt2==4:
                a=int(input("Enter the 1st value:"))
                b=int(input("Enter the 2st value:"))
                print(a/b)
            else:
                print("Invalid option")
            a=input("Do you want to go in main  menu (Y/N)")
            if a=="Y":
                break
            elif a=="N":
                continue
            else:
                print("Invalid option")
            
            
                
    elif opt==2:
        while True:
            print("1.Area of Square \n2.Area of Triangle \n3.Area of Rectangle \n4.Area of circle")
            opt2=int(input("Choose any option:"))
            if opt2==1:
                a=int(input("Side of Square:"))
                print("Area of swuare is:",a**2)
            if opt2==2:
                b=int(input("Base of Triangle:"))
                h=int(input("Height of Triangle:"))
                a=b*h
                print("Area of Triangle is:",a*0.5)
            if opt2==3:
                l=int(input("Length of Rectangle:"))
                h=int(input("Height of Rectangle:"))
                a=l*h
                print("Area of Rectangle is:",a)
            if opt2==4:
                r=int(input("Radius of Circle:"))
                p=22/7
                a=(r**2)*p
                print("Area of Circle is:",a)
            else:
                print("Invalid option")
            a=input("Do you want to go in main  menu (Y/N)")
            if a=="Y":
                break
            elif a=="N":
                continue
            else:
                print("Invalid option")
    elif opt==3:
        while True:
            print("1.Volume of Square \n.2. Volume of circle ")
            opt3=int(input("Choose any option:"))
            if opt3==1:
                a=int(input("Side of Square:"))
                print("Volume of square is:",(a*a))
            if opt3==2:
                r=int(input("Radius of Circle:"))
                p=(22/7)*(4/3)
                print("volume of circle:",(r**3)*p)
            else:
                print("Invalid option")
            a=input("Do you want to go in main  menu (Y/N)")
            if a=="Y":
                break
            elif a=="N":
                continue
            else:
                print("Invalid option")
                
    elif opt==4:
            print("Bye Bye")
            break
    else:
        print("Invalid option")

