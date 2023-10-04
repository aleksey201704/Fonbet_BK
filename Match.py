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
def get_liga(id_liga):
    itog=''
    with open('get_name_liga.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    for key_n,val_n in data.items():
        if key_n == id_liga: itog = val_n
    return itog
def get_full_bids():
    line_id = {}
    line_bids = {}
    line_full = {}
    params = {
        'lang': 'ru',
        'scopeMarket': '1600',
    }
    response = requests.get('https://line55w.bk6bba-resources.com/events/listBase', params=params)
    result = response.json()
    print(response.status_code)
    # Вытаскиваем события Line
    for key in result['events']:
        # if key['level'] == 3: print(key)
        # print(key)
        if key['place'] == 'line':
            if key.get('team1') != None:
                if key.get('team2') != None:
                    line_id[key['id']] = ({'sid': key.get('kind'),
                                           'lid': get_liga(str(key['sportId'])),
                                           'time': key['startTime'],
                                           'team1': key.get('team1'),
                                           'team2': key.get('team2')})

    # Вытаскиваем котировки по событиями
    for keyFactors in result['customFactors']:
        for key_l_id, val_l_id in line_id.items():
            if keyFactors['e'] == key_l_id:
                for key_f in keyFactors['factors']:
                    if factor(key_f['f']) != '':
                        if key_f.get('pt') != None:
                            line_bids[factor(key_f['f']) + '(' + key_f['pt'] + ')'] = key_f['v']
                        else:
                            line_bids[factor(key_f['f'])] = key_f['v']
                line_full[key_l_id] = ({
                    'time': val_l_id['time'],
                    'sportName': val_l_id['sid'],
                    'Liga': val_l_id['lid'],
                    'team1': val_l_id['team1'],
                    'team2': val_l_id['team2'],
                    'bids': line_bids})
                line_bids = {}
        print('=', end='')

    # Записываем данные в файл для сравнения других БК
    with open('full_fonbet.json', 'w', encoding='utf-8') as f:
        json.dump(line_full, f, ensure_ascii=False, indent=4)
def main():
    #get_full_bids()
    with open('full_fonbet.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
# Вытаскиваем Баскетбол
    full_bids_basket={}
    for key_id,val_id in data.items():
        # print (val_id['Liga'])
        t=val_id['Liga'].split('.')
        for m in range(len(t)):
            if t[m] == 'Баскетбол':
                full_bids_basket[key_id]=val_id

    with open('../Compare/full_basketball_fonbet.json', 'w', encoding='utf-8') as f:
        json.dump(full_bids_basket, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
