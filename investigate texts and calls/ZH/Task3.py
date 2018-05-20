"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
'''
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
'''
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。
"""

# do filtering: 
# 1. first col - start with '(080)'; 
# 2. second col - start with '(0xx...)' and ('7xxxx xxxxx' or '8xxxx xxxxx' or '9xxxx xxxxx')
calls_from_BL = filter(lambda x: x[0].startswith('(080)') \
    and (x[1].startswith('(0') or x[1].startswith('7') or x[1].startswith('8') or x[1].startswith('9')), \
    calls)
BL_call_from, BL_call_to, call_date, duration = zip(*calls_from_BL)

# delete duplicated item
BL_call_to = list(set(BL_call_to))

result = []
# filtering fixed telephone numbers start with '(0'
telephone_numbers = filter(lambda x: x.startswith('(0'), BL_call_to)
# get codes from telephone numbers
for n in telephone_numbers:
    try:
        code = n[1:n.index(')')]
        if code not in result:
            result.append(code)
    except ValueError:
        pass
    

# filtering cellphone numbers start with '7' or '8' or '9'
cellphone_numbers = filter(lambda x: x.startswith('7') or x.startswith('8') or x.startswith('9'), BL_call_to)
# get codes from cellphone numbers
for n in cellphone_numbers:
    try:
        code = n[:4]
        if code not in result:
            result.append(code)
    except ValueError:
        pass

print("The numbers called by people in Bangalore have codes:")
result.sort()
for item in result:
    print(item)

"""
第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""

# total calls from BL
list_call_from_BL = filter(lambda x: x[0].startswith('(080)'), calls)
BL_call_total = len(list(list_call_from_BL))

# total calls from BL to BL, do filtering: 
# 1. first col - start with '(080)'; 
# 2. second col - also start with '(080)'; 
list_call_from_BL_to_BL = filter(lambda x: x[0].startswith('(080)') and x[1].startswith('(080)'), calls)
BL_to_BL_total = len(list(list_call_from_BL_to_BL))

# percentage
p = BL_to_BL_total/BL_call_total
#print(round(p,2))
#print('%.2f' % p)
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format('%.2f' % p))

