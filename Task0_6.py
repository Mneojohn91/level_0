# code to find the highest number

def maximum(*number):
    # 3 numbers



    # Finding the highest and showing/printing result
    if number[0] > number[1] and number[0] > number[2]:
        highest = number[0]
        print("highest number: ", number[0])
    elif number[1] > number[0] and number[1] > number[2]:
        highest = number[1]
        print("highest number: ", number[1])
    else:
        highest = number[2]
        print("highest number: ", number[2])


number =(25, 60,100)


maximum(*number)
