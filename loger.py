# честно скопипастил работает или нет не знаю

def add_in_log(strlog):
    with open('Log.csv', 'a', encoding='UTF-8') as log:
        stringLog = strlog + '\n'
        log.write(stringLog)
