import time

task_time = int(input('请输入倒计时时间（分钟）：'))
start_time = time.strftime('%H:%M:%S',time.localtime())     #获取格式化当前时区时间
print('开始时间：' + start_time)

for i in range(0, task_time*60, 5):                         #分钟化为秒,加步长5
    print('剩余时间：%i秒' %(task_time*60 - i))               #每5秒打印一次
    time.sleep(5)

final_time = time.strftime('%H:%M:%S',time.localtime())     #获取结束时间
print('结束时间：' + final_time)
