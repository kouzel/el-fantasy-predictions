import random

calculationCoefficientBaseFields = {
    # 'min': 0.4,
    'pts':1,
    'reb':1,
    'ast':1,
    'stl':1,
    'blk':1,
    'fouls_received':1,
    'pf':-1,
    'tov':-1,
    'blka':-1,

}
advancedCalculationKeys = ['ftmiss','fgmiss']

def calculateAdvanced(key,player):
    match key:
        case 'ftmiss':
            return (float(player['ftm'])-float(player['fta']))
        case 'fgmiss':
            return  float(player['fgm']) - float(player['fga'])
        case _:
            return 0 

def getStatisticCalculation(player):
    val = 0
    keys = calculationCoefficientBaseFields.keys()
    for key in keys:
        val+=calculationCoefficientBaseFields[key] * float(player[key])
    for key in advancedCalculationKeys:
        val+=calculateAdvanced(key,player=player)

    return round(val,2)

def processData(data):
    reformed=[]
    for item in data:
        reformed.append({'id':item['id'],
                         'name':item['first_name']+' '+item['last_name'],
                         'credit':item['cr'],
                         'calculated':getStatisticCalculation(item),
                         'teamId':item['team_id'],
                         'team_name':item['team_name'],
                         'position':item['position']
                         })
    return reformed