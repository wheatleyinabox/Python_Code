def foo(x, y = 0, z = 0):
    return 100+x + 10*y + 1*z

#print(foo(y = 2, x = 1, z = 3))
#print(foo(7))

def bar(*args, named_parameter = "bar"):
    for a in args:
        print(named_parameter, "bar arg ==", a)

#bar([1, 2, 3])
#bar(["Jelly", "Fish"])
#print(bar(["Jelly", "Fish"]))
print(bar(["list", "of", "strings"]))
