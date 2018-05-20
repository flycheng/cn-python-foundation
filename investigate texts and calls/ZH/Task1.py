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
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""

texts_from, texts_to, texts_date = zip(*texts)

# set of text sender
set_texts_from = set(texts_from)
# set of text receiver
set_texts_to = set(texts_to)
# get the unique phone number set by union two sets
set_texts = set_texts_from.union(set_texts_to)

calls_from, calls_to, calls_date, calls_duration = zip(*calls)

# set of caller
set_calls_from = set(calls_from)
# set of call receiver
set_calls_to = set(calls_to)
# get the unique phone number set by union two sets
set_calls = set_calls_from.union(set_calls_to)

# get result set by union set_texts with set_calls
set_phone_number = set_texts.union(set_calls)

print("There are {} different telephone numbers in the records.".format(len(set_phone_number)))
