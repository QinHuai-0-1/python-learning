#不使用len()代码求字符串长度（函数解析）
# def my_len(s):#def 定义函数，s为参数
#     count = 0
#     for i in s:
#         count += 1
#     print(count)
# msg = input("请输入字符串：")
# print(f"字符串的长度为：{my_len(msg)}")

#列表的定义
#初始列表
# name_list = ['秦淮','狄玖','秦淮','盛歌','陆离','沈夜']

#1.index()方法返回列表中第一个匹配项的索引位置
# print(name_list.index('盛歌'))

#2.通过索引修改列表中的元素
# name_list[2] = '欢宴'
# print(name_list[2])

#3.insert()方法在指定位置插入元素
# print(name_list.insert(2,'盛歌'))

#4.append()方法在列表末尾添加元素
# print(name_list.append('白夜'))

#5.remove()方法删除列表中的指定元素
# print(name_list.remove('白夜'))

#6.pop()方法删除列表中的指定位置的元素，并返回该元素的值
# print(name_list.pop(2))

#7.clear()方法清空列表中的所有元素
# print(name_list.clear())

#8.len()函数返回列表中元素的个数
# print(len(name_list))

#9.sort()方法对列表中的元素进行排序
# print(name_list.sort())

#10.reverse()方法将列表中的元素反转
# print(name_list.reverse())

#11.count()方法返回列表中指定元素的出现次数
# print(name_list.count('秦淮'))

#12.copy()方法返回列表的浅复制
# print(name_list.copy())

#13.extend()方法将一个可迭代对象中的元素添加到列表末尾
# name_list.extend(['白夜','盛歌'])

#14.切片操作可以获取列表中的一部分元素，语法为list[start:end:step]，其中start表示起始索引位置，end表示结束索引位置（不包含），step表示步长（默认为1）。
# print(name_list[1:4])

#15.列表的嵌套：列表中可以包含其他列表，形成嵌套结构。可以通过多层索引来访问嵌套列表中的元素。
# nested_list = [1, 2, [3, 4], 5]
# print(nested_list[2][0])

#列表案例实操
#学生成绩管理系统
#1. 添加成绩
#2. 查看成绩
#3. 退出

scores = [96, 88, 92]  # 初始成绩列表
while True:
        print("欢迎使用学生成绩管理系统！")
        print("1. 添加成绩")
        print("2. 查看成绩")
        print("3. 退出")
        choice = input("请输入您的选择(1/2/3):")
        if choice == '1':
            score = float(input("请输入学生成绩:"))
            scores.append(score)
            print("成绩添加成功！")
        elif choice == '2':
            if scores:
                print("学生成绩如下：")
                for i, score in enumerate(scores, start=1):
                    print(f"{i}. {score}")
            else:
                print("没有成绩记录！")
        elif choice == '3':
            print("感谢使用学生成绩管理系统，再见！")
            break
        else:
            print("输入错误，请重新输入！")