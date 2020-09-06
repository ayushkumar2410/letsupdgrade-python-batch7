plane_altitude=float(input("enter plane altitude "))

if plane_altitude<= 1000:
    print("land the plane")
elif plane_altitude>1000 and plane_altitude<5000:
    print('come down to 1000 ft')
else:
    print('go around and try again later')