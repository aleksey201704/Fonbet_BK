import requests
from datetime import datetime
import json


def factor(x):
    itog = ''
    try:
        with open('fonbet/factors.json', encoding='utf-8') as json_file:
            data = json.load(json_file)
            for key_f, key_v in data.items():
                # print(key_f,key_v)
                if str(x) == key_f:
                    match key_v:
                        case 'Фора 1': itog='Ф1'
                        case 'Фора 2': itog='Ф2'
                        case 'Б': itog='ТБ'
                        case 'М': itog='ТМ'
                        case 'Поб1': itog='1'
                        case 'Поб2': itog='2'
                        case 'Ничья': itog='X'
                        case _:itog = key_v
                #     break
    except IOError:
        params = {'lang': 'ru',
                  'version': '0',
                  'sysId': '1', }
        response = requests.get('https://line10w.bk6bba-resources.com/line/sportBasicMarkets/',
                                params=params)
        result_factors = response.json()

        f_full = {} # Переписываем в справочник чтобы несколько раз обращаться GET
        for keyfactors in result_factors['sportBasicMarkets']:
            for keycaption in keyfactors['columns']:
                #print(keycaption)
                for keyall in keycaption['factors']:
                    if keycaption['caption'] != 'Тотал':   # Исключаем Тотал
                        f_full[keyall] = keycaption['caption']

        with open('fonbet/factors.json','w',encoding='utf-8') as f:
            json.dump(f_full,f,ensure_ascii=False,indent=4)

        for key_f, key_v in f_full.items():
            if str(x) == key_f:
                match key_v:
                    case 'Фора 1':itog = 'Ф1'
                    case 'Фора 2': itog = 'Ф2'
                    case 'Б': itog = 'ТБ'
                    case 'М': itog = 'ТМ'
                    case 'Поб1': itog = '1'
                    case 'Поб2': itog = '2'
                    case 'Ничья': itog = 'X'
                    case _: itog = key_v
    return itog
def main():
    print(factor(921))

if __name__ == '__main__':
        main()