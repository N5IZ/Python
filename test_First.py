from First import square
def test_square():
    x = int(input("Please Enter The Number You Want To Test"))
    if square(x) != x*x:
        print("Its not working")
    else: 
        print("Its Okay")

test_square()