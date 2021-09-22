import numpy as np

a1,b1,c1 = 0,0,0

for _ in range(100000):
    a = ["r"]*3
    b = ["y"]*3
    c = ["g"]*3
    x = np.random.choice(a)
    a.remove(x)
    b.append(x)
    y = np.random.choice(b)
    b.remove(y)
    c.append(y)
    z = np.random.choice(c)
    c.remove(z)
    a.append(z)
    
    draw = [np.random.choice(a), np.random.choice(b), np.random.choice(c)]
    
    if draw.count("r")==2:
        a1+=1
    elif draw.count("y")==2:
        b1+=1
    elif draw.count("g")==2:
        c1+=1        
        
probs = np.array([a1, b1, c1])
print(probs/np.sum(probs))