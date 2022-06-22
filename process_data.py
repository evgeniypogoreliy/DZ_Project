from process_file import writer_planned
from process_file import writer_compl
from loger import add_in_log
from process_file import del_record


def build_planned(string):
    record = string
    final_record = tuple( i for i in record.split(' '))
    add_in_log(record)
    writer_planned(final_record)


def build_compl(string):
    writer_compl(string)


def build_del(string):
    del_record(string)





