# 代码总计
## [main.cpp](latest/main.cpp)
主要运算代码
#23 [TODO](latest/main.cpp#23)：文件读写错误，最后一个数据未导入。
```CPP
freopen("FAccelerometer.csv","r",stdin);
getline(cin,temp);
while(cin>>ta[len1++]>>ax[len1]>>ay[len1]>>temp){}
len1-=2;
//Todo: Check out why the last number wasn't read.
//      Now just modify len1 to let it looks right.
fclose(stdin);
```
## [img_ani.py](latest/img_ani.py)
绘制动态图像。
## [img_sav.py](latest/img_sav.py)
保存图像。
## [inter.py](latest/inter.py)
原始数据分析
## [transfer.py](latest/transfer.py)
数据格式转换

# 2022/01/01--1
[链接](20220101_1)

![X-Y](20220101_1/X-Y.png)
# 2022/01/14--1
[链接](20220114_1)

目前观察数据发现，加速度（线速度）传感器在x、y上均有极大的累计值。

||Acceleration x (m/s^2)|Acceleration y (m/s^2)
|--|--|--|
|求和|-667.79|290.8859|
|平均|-0.10974|0.047804|

猜测：g在x、y方向上有分加速度
# 2022/01/16
静止状态下的加速度
# [2022/01/18](20220118/readme.md)
测试直线运动的效果
# [2022/01/19--1](20220119_1/README.md)
大量修改代码
# [2022/01/19--2](20220119_2/README.md)
直线测试
