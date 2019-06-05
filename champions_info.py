import json

champions_info = {}

# lendo informação sobre os campeões
with open("./data/champion_info.json") as f:
    champ_info = json.load(f)

with open("./data/champion_info_2.json") as f:
    champ_info_2 = json.load(f)

# pegando informação dos nomes/ids
for it in champ_info['data']:
    champion = champ_info['data'][it]
    
    champions_info[champion['id']] = {}
    champions_info[champion['id']]['id'] = champion['id']
    champions_info[champion['id']]['name'] = champion['name']
    
# adicionando informação do tipo de classe do campeão    
for it in champ_info_2['data']:
    champion = champ_info_2['data'][it]
    
    if champion['id'] in champions_info:
        champions_info[champion['id']]['tags'] = champion['tags']
    
# Method
def champion_first_tag(champion_id):
    """
    Retorna a classe principal do campeão
    """
    tags = champions_info[champion_id]['tags']
    
    return tags[0]
    
def champion_name(champion_id):
    """
    Retorna o nome do campeão
    """
    return champions_info[champion_id]['name']

def get_champion_id(champion_name):
    """
    Retorna o nome do campeão
    """
    for champion_id in champions_info:
        if champions_info[champion_id]['name'] == champion_name:
            return champion_id

def all_champions_tags():
    """
    Retorna uma lista contendo todas as tags possiveis
    """
    ans = []
    
    for id in champions_info:
        for tag in champions_info[id]['tags']:
            if tag not in ans:
                ans.append(tag)
    
    return ans
    
def is_s_tier(champion_id):
    """
    Retorna true se o campeão é S-Tier no Patch
    """
    pass

def is_mechanical_intensive(champion_id):
    """
    Retorna true se o campeão é dificil de jogar
    """
    pass
    