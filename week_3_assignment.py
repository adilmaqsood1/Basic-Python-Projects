def function1():
    x = 10
    print("In function 1")
    
def function2(data):
    print("In function 2 about to call function 3")
    function3() 
    print("In function 2 - after calling function 3")
     
def function3():
    print("In function 3 about to call function 1")
    function1() 
    print("In function 3 - after calling function 1")

def function4():
    print("In function 4")  

function1()
function2(30)
