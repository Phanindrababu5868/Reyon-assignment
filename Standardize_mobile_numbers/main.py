# link;-

def wrapper(f):
    def fun(l):
        return f([('+91 '+ number[-10:-5] + ' ' + number[-5:]) for number in l])
    return fun

