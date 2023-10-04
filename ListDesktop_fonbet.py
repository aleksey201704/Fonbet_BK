import requests
from datetime import datetime
import json

def main():
    params = {
        'place': 'line',
        'sysId': '1',
        'lang': 'ru',
        'salt': '4njyg18xz04lmxf0w3q',
        'supertop': '4',
        'scopeMarket': '1600',
    }

    response = requests.get('https://line04w.bk6bba-resources.com/line/desktop/topEvents3',
                            params=params)
# Список спорта и ближаеших матчей
    result = response.json()
    list_full = {}
    id=0
    for key_r in result['events']:
        print(key_r['id'],key_r['startTimeTimestamp'] ,key_r['skName'],key_r['competitionName'],
              key_r.get('team1'),key_r.get('team2'))
        id +=1
        list_full [id] = {  'id': key_r['id'],
                            'time':key_r['startTimeTimestamp'],
                            'sportName': key_r['skName'],
                            'Liga': key_r['competitionName'],
                            'team1': key_r.get('team1'),
                            'team2': key_r.get('team2')}
    print('Количество матчей',id)
    with open('fonbet/list_fonbet.json','w',encoding = 'utf-8') as  f:
        json.dump(list_full,f,ensure_ascii=False,indent=4)
'''
print(list_full)
    for key_list in list_full.values():
        new_list = dict(key_list)
        for key_l,val_l in new_list.items():
            print(key_l,val_l)
'''


if __name__ == '__main__':
        main()