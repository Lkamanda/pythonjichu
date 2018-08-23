'''
输入一个三位数与程序随机比较大小
如果大于程序随机数,则分别输出这个三位数的个位\十位百位
如果等于程序随机数,则提示中奖,记100分
如果小于程序随机数,则将120 个字符输入到文本文件中(规则是每一条字符串的长度为12,单独占一行,前4个是字母,后8个是数字)

'''
import random
import math
n = 0
n  = int(n)
def a():
    global n
    # 记录次数
    # 程序随机数

    random_num = random.randrange(100,1000)
    num = input('请输入一个三位数数字:')

    # 输入函数返回的是字符串类型,不能与整形直接比较需要强制类型转换

    if num == '-1':
        return False

    elif num.isdigit() and 100<=int(num)<=999:
        num = int(num)
        random_num = int(random_num)

        if num > random_num:
            # 如果输入的数大于随机生成的数则分必然返回三位数的百,十,个
            # 求百位数字方法是地板除100
            bai = num //100
            # 求十位是 先取100余数 再地板除
            shi = num%100//10
            #　求个位　求10的模
            ge =num%10
            print('你输入的数比程序随机数大,程序随机数是',random_num)
            print('这个三位数的个位是{0}十位是{1}百位{2}'.format(ge,shi,bai))

        if num ==random_num:
            source =0
            source += 100
            print('你中奖来了,当前分数为:',source)

            pass
        if num < random_num:

            # 由于120个字符每行12个可知需要存入10行就可以
            for i in range(10):
                str_line = line()
                # 执行文件存入操作
                # a 追加
                path =r'/home/tlxy/PCM/rccode/spliderexe/htmlcf/'

                with open(path +'str_num.txt','a') as f:
                    f.write(str_line +'\n')
        return a()
    else:
        n += 1
        print(n)
        if n <= 3:
            print('您还有{0}次机会'.format(3-n))
            print('请按照规定输入数字')
            return a()
        else:
            return False

def line():
    # 定义一个空字符串用于拼接字符
    str_num = ''
    # 循环前四个随机字母(用asc码对应的值来随机再转换为字母)
    for i in range(4):
        # 使用小写字母的asx值
        num = random.randrange(97,123)
        #  数字转换成asc码 转换成对应的字母
        str_s = chr(num)

        str_num = str_num + str_s
    # 循环后后八个随机数字
    for i in range(8):
        num =random.randrange(0,10)
        # 数字和字符串拼接需要强制类型转换
        str_num = str_num +str(num)
    return str_num



# 程序入口
if __name__ == '__main__':
    a()
    # 在本身模块中 __name == __main__, 当第三方导入的时候 __name__ == 文件名
