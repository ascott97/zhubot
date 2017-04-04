import requests
import json
import auth

  
        
def get_summoner_id(summoner_name):
    url = 'https://euw.api.riotgames.com/api/lol/EUW/v1.4/summoner/by-name/'
    params = {'api_key': auth.get_auth()['leagueoflegends']['api_key'] }    
    response = requests.get((url + summoner_name), params=params)
    response = json.loads(response.text)
    summoner_id = response[summoner_name]['id']
    return summoner_id

def get_current_game(summoner_id):
    url = 'https://euw.api.riotgames.com/observer-mode/rest/consumer/getSpectatorGameInfo/EUW1/'
    params = {'api_key': auth.get_auth()['leagueoflegends']['api_key'] }
    response = requests.get((url + str(summoner_id)), params=params)
    response = json.loads(response.text)
    return response
    

def handle_message(message):
    if message.content.split()[1] == 'live':
        summoner_name = message.content.split()[2]
        summoner_id = get_summoner_id(summoner_name)
        current_game = get_current_game(summoner_id)
        return current_game
        
        
