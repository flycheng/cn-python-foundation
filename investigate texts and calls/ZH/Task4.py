"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

caller, receiver, call_time, call_dura = zip(*calls)
text_sender, text_receiver, text_time = zip(*texts)

# set of caller
set_caller = set(caller)
# set of call receiver
set_receiver = set(receiver)
# set of text sender
set_text_sender = set(text_sender)
# set of text receiver
set_text_receiver = set(text_receiver)

# telemarketer is always a caller and not a receiver
set_telemarketer = set_caller - set_receiver

# telemarketer is not a text sender
set_telemarketer = set_telemarketer -  set_text_sender

# telemarketer is not a text receiver
set_telemarketer = set_telemarketer - set_text_receiver

# convert to a list and sort
list_telemarketer = list(set_telemarketer)
list_telemarketer.sort()

print("These numbers could be telemarketers: ")
for telemarketer in list_telemarketer:
    print(telemarketer)