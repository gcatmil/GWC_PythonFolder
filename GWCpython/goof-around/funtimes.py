from turtle import *

color('#ccffff', '#ffccff')
begin_fill()
while True:
    forward(300)
    right(-230)
    left(270)
    forward(30)
    if abs(pos()) < 1:
        break
end_fill()
done()
