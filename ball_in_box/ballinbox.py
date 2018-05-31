import math
import random
from .validate import validate

__all__ = ['ball_in_box']

#判断随机点是否在圆外
def is_correct (x,y,circles):
    if circles is None:
        return True
    else:
        for circle in circles:
            if math.sqrt((x-circle[0])**2 + (y-circle[1])**2) > circle[2]:
                return True
            else:
                return False

#计算以随机点为圆心的最大半径
def max_r (x,y,circles):
    a = math.sqrt((x-0.5)**2 + (y-0.5)**2)
    b = math.sqrt((x-0.5)**2 + (y+0.5)**2)
    c = math.sqrt((x-0.5)**2 + (y-0.3)**2)
    if circles is not None:
        p = 1
        d_s = []

        for circle in circles:
	        d = math.sqrt((x-circle[0])**2 + (y-circle[1])**2) - circle[2]
        	d_s.append(d)
		
        for dx in d_s:
            p = min(dx,p)
	
        max_r = min(a,b,c,p)
    else:
        max_r = min(a,b,c) 
    return max_r

#获取五个圆
def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
    """
    m is the number circles.
    n is the list of coordinates of tiny blocks.
    
    This returns a list of tuple, composed of x,y of the circle and r of the circle.
    """

    # The following is an example implementation.
    #circles = []
    #for circle_index in range(m):

    #    x = random.random()*2 - 1
    #    y = random.random()*2 - 1
    #    r = random.random()*0.1

    #    circles.append((x, y, r))
    #    while not validate(circles, blockers):
    #        x = random.random()*2 - 1
    #        y = random.random()*2 - 1
    #        r = random.random()*0.1
    #        circles[circle_index] = (x, y, r)

    #    circle_index += 1
    
    #return circles
    circles = []
    for num in range(m):
        x = random.random()*2 - 1
        y = random.random()*2 - 1
        while not is_correct(x,y,circles):
            x = random.random()*2 - 1
            y = random.random()*2 - 1
        r = max_r(x,y,circles)
        circles[num] = (x,y,r)
    return circles	
