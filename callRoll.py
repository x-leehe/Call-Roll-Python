################################################################
##         Developer: Wenyuan Xue (Github:@X-LeeHe)           ##
##    Repo:https://github.com/x-leehe/Call-Roll-Python        ##
##                  License: MIT License                      ##
##            任何情况下使用本代码都需要经过本人同意。            ##
################################################################

import random
import pyttsx3
import time
import sys      # 引入模块

with open(input("请输入学生名单文件路径："),encoding='utf-8') as f:
    studentList=f.read()
engine=pyttsx3.init()
print("名单已就绪！")
studentList=studentList.split("\n")         # 对学生名单和语音引擎进行初始化

def callRoll():         # 基础点名功能，后续加入的功能基于此函数
    time.sleep(5)
    luckyDog=random.randint(0,len(studentList)-1)
    print("幸运儿是：%s"%studentList[luckyDog])
    engine.say(studentList[luckyDog])
    engine.runAndWait()
    time.sleep(5)

startInit=int(input("请选择点名模式！\n0.我怂了，退出！\n1.正常模式！\n2.击鼓传花！\n3.一站到底！\n请选择……（0/1/2/3）"))

while startInit==1:
    startTrigger='y'
    print("即将开始点名……")
    callRoll()
    startTrigger=input("是否继续点名？（Y/n）:")
    try:
        if startTrigger=='Y' or startTrigger=='y':
            continue
        else:
            break
    except:
        break

while startInit==2:
    startTrigger='y'
    drumTimes=int(input("请输入击鼓传花的次数："))
    print("即将开始击鼓传花……")
    for i in range(drumTimes):
        callRoll()
        startTrigger=input("是否继续击鼓传花？（Y/n）:")
        try:
            if startTrigger=='Y' or startTrigger=='y':
                continue
            else:
                break
        except:
            break
    break

while startInit==3:
    startTrigger='c'
    while startTrigger=='c':
        print('一站到底，即将开始……')
        callRoll()
        try:
            startTrigger=input("是否继续（y），或者换人（c）？（Y/c/n）:")
        except:
            startTrigger='n'
    while startTrigger=='Y' or startTrigger=='y':
        try:
            startTrigger=input("是否继续（y），或者换人（c）？（Y/c/n）:")
        except:
            startTrigger='n'
    if startTrigger=='n':
        break
    break
    
print("点名结束！")
time.sleep(5)
sys.exit()
