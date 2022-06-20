from process_file import writer_planned
from find_data import find
from process_file import writer_completed

def build_planned(string):
    record = string
    final_record = tuple( i for i in record.split(' '))
    writer_planned(final_record)

def build_compl(string):
    record = string + " Выполненно"
    final_record = tuple( i for i in record.split(' '))
    writer_completed(final_record)

def del_record(string):
    find(string)

