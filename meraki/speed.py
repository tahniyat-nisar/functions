def vechile(speed):
    if speed<70:
        print("OK")
    elif speed>70:
        diff=speed-70
        if diff%5==0:
            i=diff
            point=0
            while i>0:
                i=i-5
                point+=1
            print("point:",point)
            if point>=12:
                print("License suspended")

speed=int(input("enter speed of your vechile:"))
vechile(speed)