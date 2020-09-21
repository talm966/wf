from collections import Counter
import sys
from re import findall
import os





def function(name):
    # 判断传入的命令行参数是否含有.txt,如果没有，要加上，再作为打开路径
    a = '.txt'
    if a in name:
        path = name
    else:
        path = name + a
    f = open(path, 'r', encoding='utf-8')  # 用open（）函数打开文件，并返回文件对象
    # 通过正则表达式和findall()函数生成文件内容的列表
    lists = findall(r'[a-z0-9^-]+', f.read().lower())

    words = Counter(lists)
    # 遍历字典，统计键值对数
    num = 0
    for key, value in words.items():
        num += 1
    # 判断功能1或者2选择输出words
    if sys.argv[1] == '-s':
        print('total' + ' ' + str(num))
    else:
        print('total' + ' ' + str(num) + ' words')
    # most_common(n)返回计数值最大的n个元素的元素列表
    #most_common进行排序，选择位数5或者6的输出
    if sys.argv[1] == '5':
        maxwords = words.most_common()
        count = 0
        for i in maxwords:
            if len(i[0]) == 5:
                count += 1
                print('%-8s%5d' % (i[0], i[1]))
                if count == 10:
                    break
    elif sys.argv[1] == '6':
        maxwords = words.most_common()
        count = 0
        for i in maxwords:
            if len(i[0]) == 6:
                count += 1
                print('%-8s%5d' % (i[0], i[1]))
                if count == 15:
                    break
    else:
        maxwords = words.most_common(10)
        for i in maxwords:
            print('%-8s%5d' % (i[0], i[1]))

# 重定向
def function_four():
        str=input()

        filename = "D://python//Scripts//dist//test.txt"
        with open(filename,"w") as f:
            f.write(str)
        file = 'test.txt'
        function(file)



# 传入文件夹
def listfunction(path):
    files = os.listdir(path)  # 将文件夹中的文件列表化
    for file in files:
        filename = os.path.splitext(file)[0]
        print(filename)
        function(file)
        print('---------')


# 定义主函数
def main(argv):
    # 功能1
    if sys.argv[1] == '-s':
        if len(sys.argv) == 3:
            function(sys.argv[2])
        else:
            # 重定向1
            function_four()

    # 功能3
    elif os.path.isdir(sys.argv[1]):
        listfunction(sys.argv[1])
    #附加功能1
    elif sys.argv[1] == '5':
        function(sys.argv[2])
    #附加功能2
    elif sys.argv[1] == '6':
        function(sys.argv[2])

    # 功能2
    else :
        function(sys.argv[1])



# 主函数
main(sys.argv[1:])


