import pandas as pd
import datetime
import calendar
from os.path import split, join
from collections import defaultdict
import logging


def report(file, object=None):
    logging.basicConfig(filename='grafic.loc', filemode='w', level=logging.INFO, format='%(asctime)s -- %(message)s')
    file_path = split(file)[0]
    try:
        xl = pd.ExcelFile(file)
        spisok = xl.parse(xl.sheet_names[0])
    except Exception:
        if object:
            object.showMessage('У файла не то расширение')
        logging.exception('У файла не то расширение')
        return False
    if list(spisok.keys()) == ['Фамилия', "Часы"]:
            if object:
                object.showMessage('Файл прочитан')
            logging.info('Файл прочитан')
            d = datetime.datetime.now()
            year = d.timetuple()[0]
            month = d.timetuple()[1]
            result = defaultdict(set)
            d2 = calendar.Calendar()
            d3 = [x for x in d2.itermonthdays2(year, month+1) if x[0]]
            for num, weekday in d3:
                amount = 22 if weekday in (5, 6) else 15
                while amount > 0:
                    index = spisok['Часы'].idxmin()
                    result[spisok.loc[index, 'Фамилия']].add(num)
                    spisok.loc[index, 'Часы'] += 8
                    amount -= 1
            if object:
                object.showMessage('График создан')
            report = pd.DataFrame(data={'Фамилия': spisok['Фамилия']},
                                  columns=['Фамилия', *[x for x in d2.itermonthdays(year, month+3) if x], 'Часы'])
            for num, item in enumerate(result):
                for day in result[item]:
                    report.loc[num, day] = 'Смена'
                report.loc[num, 'Часы'] = spisok.loc[num, 'Часы']
            report.to_excel(join(file_path, 'grafic.xlsx'))
            if object:
                object.showMessage('Файл создан')
            logging.info('File created')
            return True
    else:
        if object:
            object.showMessage('Указан файл не с той структурой')
        logging.error('Указан файл не с той структурой')
        return False

if __name__ == '__main__':
    report('/sysroot/home/user/PycharmProjects/grafic/pos_west.xlsx')

