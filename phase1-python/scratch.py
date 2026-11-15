name: str = "ada"
age: int = 36
price = 19.99
print(f"{name} is {age} , price {price:.2f}")

for i in range(1,6):
    if i % 2 ==0 :
        print(i, "even")
    else : 
        print (i,"odd")

n=3
while n > 0:
    print("countdow" , n)
    n-=1

def greet(name: str , greeting: str = "hello") -> str :
    return f"{greeting}, {name}!"

def total(*nums: float):
    return sum(nums)

def show(**opts):
    for k, v in opts.items():
        print(k, v)

print(greet("ada"))
print(greet("ada",greeting="salut"))
print(total())
show(a=1,b=2)

