# homework-12
##太阳系中的共振
##背景
![](https://github.com/Wangzhengwhu/homework-12/blob/master/1.png)  
上图为太阳系中小行星的分布图，根据观察所得。在火星和木星之间，却有一个空缺，被命名为kirkwood gaps。其中kirkwood gaps 出现的位置是小行星的周期与木星的周期呈整数比的位置。kirkwoodgaps形成的原因可以用木星和小行星的共振来解释。当木星的轨道周期与小行星的轨道周期成整数比时，小行星最靠近木星的位置将是确定的，在这些位置上，小行星受到木星引力的摄动非常明显，这些摄动长期累积，导致小行星的轨道成为不断进动的椭圆，最终可能与其他行星相撞。  
小行星和木星的受力由以下方程给出  
![](https://github.com/Wangzhengwhu/homework-12/blob/master/%E5%85%AC%E5%BC%8F1.png)  
##正文
###1/2周期的gap附近小行星的运动
当小行星与木星的周期比为1/2时，(即在1/2 Kirkwood gap附近)，我们进行数值解，结果如下  
[程序](https://github.com/Wangzhengwhu/homework-12/blob/master/1.py)  
![](https://github.com/Wangzhengwhu/homework-12/blob/master/4.png)  
从图上可以看出，小行星运动收木星影响强烈，其轨迹类似进动的椭圆。第二张图看出当小行星运动周期偏离木星周期的一半时，小行星的运动受木星影响较小。  
###共振位置
[程序](https://github.com/Wangzhengwhu/homework-12/blob/master/3.py)  
![](https://github.com/Wangzhengwhu/homework-12/blob/master/2.png)  
上图给出的是小行星运动的振幅-半径共振曲线。当距离在3.33-3.34附近，共振最强烈。
###其他Kirkwood gaps附近小行星的运动
![](https://github.com/Wangzhengwhu/homework-12/blob/master/3.png)  上图展示了在6/7gap与3/4gap附近的小行星的运动情况。在3/4处小行星的偏离比较小，在6/7处偏离较大。在6/7处小行星的近日点离木星很近，受到的作用力强，偏离轨道就越大。
##总结
讨论了太阳系中小行星运动受木星引力影响的问题，在周期成整数比时共振最强，小行星的运动会受到木星很大的影响而偏离原来位置。
##致谢
感谢陈洋遥和刘星辰同学
