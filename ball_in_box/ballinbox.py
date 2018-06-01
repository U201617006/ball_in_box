import math
import random


__all__ = ['ball_in_box']

def ball_in_box(m, blockers):
    k=0
    max=0
    circles = []
    BalloonR=[0]*int(m)
    BalloonXPos=[0]*int(m)
    BalloonYPos=[0]*int(m)
    mBalloonR=[0]*int(m)
    mBalloonXPos=[0]*int(m)
    mBalloonYPos=[0]*int(m)
    while k<50000:  #循环50000次，每次随机在正方形内选取m个气球求得半径平方和，50000次中平方和最大的为结果。
        sum=0
        BalloonR=[0]*int(m)
        for j in range(0,int(m)):   #随机为气球的圆心选取一个位置
            r=0
            BalloonXPos[j]=random.random()*2-1
            BalloonYPos[j]=random.random()*2-1
            i=0
            while(i<j):     #判断当前的圆心位置是否在之前的气球内部，若是则重新随机位置
                if(math.sqrt((BalloonXPos[j]-BalloonXPos[i])**2+(BalloonYPos[j]-BalloonYPos[i])**2)-BalloonR[i]>0):
                    i=i+1
                else:
                    i=0
                    BalloonXPos[j]=random.random()*2-1
                    BalloonYPos[j]=random.random()*2-1
                    continue
    
            r=math.fabs(1-BalloonXPos[j])       #分别与正方形四边，障碍物以及之前的气球比较，求得当前气球半径
            if(math.fabs(1-BalloonYPos[j])<r):
                r=math.fabs(1-BalloonYPos[j])
            if(math.fabs(-1-BalloonXPos[j])<r):
                r=math.fabs(-1-BalloonXPos[j])
            if(math.fabs(-1-BalloonYPos[j])<r):
                r=math.fabs(-1-BalloonYPos[j])
            if(math.sqrt((BalloonXPos[j]-0.5)**2+(BalloonYPos[j]-0.5)**2)<r):
                r=math.sqrt((BalloonXPos[j]-0.5)**2+(BalloonYPos[j]-0.5)**2)
            if(math.sqrt((BalloonXPos[j]-0.5)**2+(BalloonYPos[j]+0.3)**2)<r):
                r=math.sqrt((BalloonXPos[j]-0.5)**2+(BalloonYPos[j]+0.3)**2)
            for i in range(0,j):
                if(math.sqrt((BalloonXPos[j]-BalloonXPos[i])**2+(BalloonYPos[j]-BalloonYPos[i])**2)-BalloonR[i]<r):
                    r=math.sqrt((BalloonXPos[j]-BalloonXPos[i])**2+(BalloonYPos[j]-BalloonYPos[i])**2)-BalloonR[i]
            BalloonR[j]=r
            sum=sum+BalloonR[j]**2      #求当前循环的平方和
        if(sum>max):        #求平方和最大值
            for x in range(m):
                mBalloonXPos[x]=BalloonXPos[x]
                mBalloonYPos[x]=BalloonYPos[x]
                mBalloonR[x]=BalloonR[x]  
            max=sum
        k=k+1
    for circle_index in range(m):

        x = mBalloonXPos[circle_index]
        y = mBalloonYPos[circle_index]
        r = mBalloonR[circle_index]
        circles.append((x, y, r))
        
    
    return circles
