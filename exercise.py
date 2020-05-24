with open('/Users/rameswarimishra/Desktop/ML/brent (1).txt','r')as f:
    brent =f.read().splitlines()
with open('/Users/rameswarimishra/Desktop/ML/camden.txt','r')as f:
    camden =f.read().splitlines()
with open('/Users/rameswarimishra/Desktop/ML/southwark.txt','r')as f:
    southwark =f.read().splitlines()
with open('/Users/rameswarimishra/Desktop/ML/redbridge.txt','r')as f:
    redbridge =f.read().splitlines()
print(type(brent))