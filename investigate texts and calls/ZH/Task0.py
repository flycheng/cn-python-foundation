"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
import time

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# sort by text time, reverse is False(default)
texts.sort(key = lambda x: time.strptime(x[2], '%d-%m-%Y %H:%M:%S'), reverse = False)
# get the first record
result_first_text = "First record of texts, {} texts {} at time {}".format(texts[0][0], texts[0][1], texts[0][2])
print( result_first_text )

# sort by call time, reverse is True
calls.sort(key = lambda x: time.strptime(x[2], '%d-%m-%Y %H:%M:%S'), reverse = True)
# get the first record
result_last_call = "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(calls[0][0], calls[0][1], calls[0][2], calls[0][3])
print( result_last_call )

