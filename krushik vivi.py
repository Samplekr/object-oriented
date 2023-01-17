#function methode
def tv_fun(model,operation):
    print("model is:",model)
    print("operation is:",operation)

def fridge_fun(model,operation):
    print("model is:",model)
    print("operation is:",operation)
tv_fun("public","video")
fridge_fun("onepluse","cooling")
tv_fun("video","make anchor")
fridge_fun("siddu","audio viral")

#object orianted

class tvfun:
    def tv_fun(self,model,operation):# (self is not key word in python)
        print("model:",model)
        print("operation:",operation)
class fridgefun:
    def fridge_fun(self,model,operation):
        print("model:",model)
        print("operation:",operation)
f1=tvfun()
f2=fridgefun()
f1.tv_fun("news 1st","video")
f2.fridge_fun("dkc","cool")
