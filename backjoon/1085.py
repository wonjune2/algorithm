x,y,w,h = map(int,input().split())

width = x
if width > w - x:
    width = w - x
height = y
if height > h - y:
    height = h - y

if width < height:
    print(width)
else:
    print(height)