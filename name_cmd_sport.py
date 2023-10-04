# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime
import requests
import json

def get_name_cmd():
    # Название команды
    data = '{"lang":"ru","sysId":1,"competitions":"actual","sportKinds":"actual","teams":"actual"}'

    response_name = requests.post('https://line51w.bk6bba-resources.com/line/logos',
                                  data=data)
    result_name = response_name.json()
    # Получаем название команды и ID    POST запрос
    name_cmd_id = {}
    name_cmd = {}
    full_name_id = {}
    # Записываем ID команды
    for key_t_id, val_t_id in result_name['teams'].items():
        name_cmd_id[key_t_id] = val_t_id;

    for key_tl, val_tl in result_name['teamLogos'].items():
        for key_o, val_o in val_tl.items():
            if key_o == 'object':
                for key_name, val_name in val_o.items():
                    if key_name == 'name':
                        name_cmd[val_tl['id']] = val_name

    for key_id, val_id in name_cmd_id.items():
        for key_cmd_id, val_cmd_id in name_cmd.items():
            if val_id == key_cmd_id:
                full_name_id[key_id] = val_cmd_id

    with open('get_name_cmd.json', 'w', encoding='utf-8') as f:
        json.dump(full_name_id, f, ensure_ascii=False, indent=4)
def get_name_sport():
    # Название спорта
    name_sport_id = {}
    name_sport = {}
    full_name_sport = {}
    data = '{"lang":"ru","sysId":1,"competitions":"actual","sportKinds":"actual","teams":"actual"}'

    response_name = requests.post('https://line51w.bk6bba-resources.com/line/logos',
                                  data=data)
    result_name = response_name.json()
    for key_s_id, val_s_id in result_name['sportKinds'].items():
        name_sport_id[key_s_id] = val_s_id
    for key_s_n, val_s_n in result_name['sportKindLogos'].items():
        for key_o, val_o in val_s_n.items():
            if key_o == 'object':
                for key_name, val_name in val_o.items():
                    if key_name == 'name':
                        name_sport[val_s_n['id']] = val_name
    for key_id, val_id in name_sport_id.items():
        for key_cmd_id, val_cmd_id in name_sport.items():
            if val_id == key_cmd_id:
                full_name_sport[key_id] = val_cmd_id

    with open('get_name_sport.json', 'w', encoding='utf-8') as f:
        json.dump(full_name_sport, f, ensure_ascii=False, indent=4)
def get_name_liga():
    # Название лиги
    name_liga = {}
    params = {
        'lang': 'ru',
        'scopeMarket': '1600',
    }
    response = requests.get('https://line55w.bk6bba-resources.com/events/listBase', params=params)
    result = response.json()

    for key in result['sports']:
        if key.get('parentId') != None:
            name_liga[key['id']] = key['name']
    with open('get_name_liga.json', 'w', encoding='utf-8') as f:
        json.dump(name_liga, f, ensure_ascii=False, indent=4)





def factor(x):
    params = {'lang': 'ru',
              'version': '0',
              'sysId': '1', }
    response = requests.get('https://line10w.bk6bba-resources.com/line/sportBasicMarkets/',
                            params=params)
    result_factors = response.json()
    itog = ''

    for keyfactors in result_factors['sportBasicMarkets']:
        for keycaption in keyfactors['columns']:
            #print(keycaption['factors'])
            for keyall in keycaption['factors']:
                if str(x) == keyall:
                    itog = str(keycaption['caption'])
                    break
    #if itog == 'Б' or itog == 'М' : itog='Тотал '+itog
    return itog
def main():
# sportId Какие матчи в лиге
# в customFactors ключ 'e'       номер матча
# 921 - Победа 1 в основное время
# 922 - Ничья  в основное время
# 923 - Победа 2  в основное время
# 924 - Победа 1 или ничья   в основное время
# 925 - Ничья  или Победа 2  в основное время
# 925 - Победа 1 или Победа 2  в основное время
# 930 -
#   get_name_cmd()
#   get_name_sport()
#   get_name_liga()



        # packetVersion
        # fromVersion
        # catalogTablesVersion
        # catalogSpecialTablesVersion
        # catalogEventViewVersion
        # sportBasicMarketsVersion
        # sportBasicFactorsVersion
        # independentFactorsVersion
        # factorsVersion
        # comboFactorsVersion
        # sportKindsVersion
        # topCompetitionsVersion
        # topParameters
        # sports            Все лиги
        # events            Все события
        # eventBlocks
        # eventMiscs
        # liveEventInfos
        # customFactors    Все ставки

        # team_name_lst = dict(team_name['object'])
        # #print('ID',team_name['id'],'Name_Team = ',team_name_lst['name'],
        # #      'Sport Id = ',team_name_lst['sport'])
   #
   #  sport_name_full={} # Создаем библиотеку временную
   #  sport_name_All={} # Создаем библиотеку для END Названия лиг
   #
   #  for sport_name in result_name['sportKindLogos'].values():
   #      sport_name_lst = dict(sport_name['object'])
   #      # Проверка на ключей name  caption
   #      if 'name' not in sport_name_lst:
   #          sport_name_full[sport_name['id']]=sport_name_lst['caption']
   #      else:
   #          sport_name_full[sport_name['id']]=sport_name_lst['name']
   #
   # # Обьеденение двух библиотек
   #  for key_sportName , values_sportName in result_name['sportKinds'].items():
   #      for key_sportFull, values_sportFull in sport_name_full.items():
   #          if values_sportName == key_sportFull:
   #                sport_name_All[key_sportName]=values_sportFull
   #  #=================================
   #
   #  line_full =[]
   #
   #  for line_name in result_line['events']:
   #      s = line_name['startTimeTimestamp']+18000 # Пермское время
   #      dt=datetime.utcfromtimestamp(s)
   #      print (dt)
   #      print(line_name['id'],
   #            line_name['skName'], line_name['competitionName'], line_name['team1'],
   #            line_name['team2'])
   #
   #
   #
   #      new_market_id = list(line_name['markets']) # Market матча
   #
   #      print('marketId',new_market_id[0]['marketId'],new_market_id[0]['caption'])
   #      print('marketId',new_market_id[1]['marketId'],new_market_id[1]['caption'])
   #      print('marketId',new_market_id[2]['marketId'],new_market_id[2]['caption'])
   #      print('marketId',new_market_id[3]['marketId'],new_market_id[3]['caption'])
   #      print('marketId',new_market_id[4]['marketId'],new_market_id[4]['caption'])
   #
   #      '''
   #      for key_cell_0 in new_market_id:
   #          for key_cell_rows_0 in key_cell_0['rows']:
   #              new_list_cell_0=list(key_cell_rows_0['cells'])
   #              for key_cell_rows_1 in new_list_cell_0:
   #                  print(key_cell_rows_1)
   #              break
   #          break
   #      print(new_market_id[0]['rows'][0]['cells'])
   #      '''
   #
   #      for key_cell_1 in new_market_id:
   #          print(key_cell_1) # Отображение маркета
   #          print('--------------------')
   #          for key_cell_1_rows in key_cell_1['rows']:
   #              new_list_cell_0 = list(key_cell_1_rows['cells'])
   #              f_t = 0
   #              for keycellall in new_list_cell_0:
   #
   #                  for keyC, valC in keycellall.items():
   #                      if keyC == 'factorId':
   #                          print(factor(valC))
   #                          z=factor(valC)
   #                          #line_full.append()
   #                      if keyC == 'value': print(valC)
   #                      if keyC == 'paramText':
   #                          if f_t == 0:
   #                              if 'Форы' == key_cell_1['caption']: print('ФОРА',valC)
   #                              if 'Тоталы' == key_cell_1['caption']: print('ТОТАЛ',valC)
   #                              f_t=1;
   #
   #      print('================',line_full) # Заканчивается линия матча
   #      #print(new_market_id[0]['rows'][1]['cells'])
   #      break




    '''
    for points in result_factors['independentFactors']:
        new_p=list(points.values())
        #if new_p[0] == 730: print('+')
        new_p_n = list(new_p[2].values())
        print(new_p[2].values())
        print(new_p_n[1][0])
        break
    for game in result['sports']:
        print(game)

    '''
    #champ=12018 # Футбол. Англия. Чемпион-Лига

'''
    for game in result['events']:
        # Прочитать Parents ID Как?
        new_dict = list(game.values()) # Конвератируем в LISt для того чтобы получить значения
        if game['id'] == 42261923 : print(game)
        if 42261923 == new_dict[1]:
            print(game['name'])
            print(game['kind'],'factors')
'''
if __name__ == '__main__':
    main()

