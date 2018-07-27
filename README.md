# Use_74HC595 By Raspberry PI
<br><br>
# 74HC595控制4位数码管
### 本篇的核心在于74HC595的使用，首先介绍74HC595：
74HC595是一个8位串行输入、并行输出的位移缓存器。简单来说，它的输入端口只有一个（串行输入），而输出端口却有8个（并行输出），所以它的本质是串行数据和并行数据的转换。使用74HC595最主要的目的在于节约GPIO口，那么，接下来我们来看看，它是如何通过串入并出来节约GPIO的。<br>
<img src="https://github.com/HarsonYoung/Use_74HC595/blob/master/%E6%9C%AC%E8%B4%A8.png" width="500" height="300"><br>
要了解74HC595的使用，首先要了解它的引脚定义<br>
<img src="https://github.com/HarsonYoung/Use_74HC595/blob/master/%E5%BC%95%E8%84%9A.png"  width="300" height="250">
<img src="https://github.com/HarsonYoung/Use_74HC595/blob/master/595.jpg"><br>

简单解释一下<br>

DS：   接收串行信号
SH_CP：当给该针脚给一个高电平时，将接收到的串行信号向右移动一位<br>
ST_CP：当给该针脚给一个高电平时，将所有接收到的8个信号依次从Q0\~Q7输出<br>
MR：  当该针脚处于低电平状态时，会将芯片内数据清空，即Q0\~Q7不再有输出，我们在实际接线时，直接电源正极，使芯片正常工作<br>
OE: 当该针脚处于低电平状态时，ST_CP的操作才有效，因此，为使芯片正常工作，OE直接GND<br>
Q7’：PASS<br>
### 工作原理：
芯片工作时，分三个步骤<br>

第一步：向DS口输入数据，数据用高低电平表示，以二进制的形式输入<br>

第二步：给予SH_CP一个高电平，数据右移一位<br>

第三步：拉低SH_CP成低电平，重复第一、二、三步，直到输出8位数据<br>

第四步：给予ST_CP一个高电平，Q0~Q7口输出数据<br>

这样，我们就可以仅仅通过三个GPIO的操作来达到使用8个GPIO口的目的了。<br>
### 代码实现：

[595.py](https://github.com/HarsonYoung/Use_74HC595/blob/master/595.py)
