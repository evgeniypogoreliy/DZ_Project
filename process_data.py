from process_file import writer_planned
from loger import add_in_log
from process_file import writer_completed

def build_planned(string):
    record = string
    final_record = tuple( i for i in record.split(' '))
    add_in_log(record)
    writer_planned(final_record)

def build_compl(string):
    record = string + " Выполненно"
    final_record = tuple( i for i in record.split(' '))
    add_in_log(record)
    writer_completed(final_record)

def red_data(string):
    red = string




