import time 
print ("Prohram execution has been started ==========> ")
def de(f):
    def f():
        t1=time.time()
        f()
        time.sleep(10)
        t2=time.time()
        t=t2-t1
    return f
@de
def nub():
    l=[1,2,"a",5,6,"hi",0,"hello",7]
    for numb in l:
        if type(numb)==int:
            print(numb,end=" ")
nub()
print ("Program execution has been stopped =========>")

    
    
       
