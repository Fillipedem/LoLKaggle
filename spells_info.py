import json

spells = {}

# lendo informação sobre os campeões
with open("./data/summoner_spell_info.json") as f:
    spells_info = json.load(f)

for it in spells_info['data']:
    info = spells_info['data'][it]
    
    spells[info['id']] = {}
    spells[info['id']]['name'] = info['name']
    spells[info['id']]['id'] = info['id']

    
def get_spell(spell_id):
    
    return spells[spell_id]['name']

def get_spell_id(name):
    
    for spell_id in spells:
        if spells[spell_id]['name'] == name:
            return spell_id

def all_spells_names():
    """
    Return all spells
    """
    return ['Teleport', 'Cleanse', 'Ghost', 
            'Barrier', 'Exhaust', 'Ignite',
           'Smite', 'Heal', 'Flash']

    