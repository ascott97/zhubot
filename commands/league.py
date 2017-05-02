import requests
import json
import auth

  
class league:

    def __init__(self):
        self.api_key = auth.get_auth()['leagueoflegends']['api_key']

    def get_summoner_id(self, summoner_name):
        url = 'https://euw.api.riotgames.com/api/lol/EUW/v1.4/summoner/by-name/'
        params = {'api_key': self.api_key }    
        response = requests.get((url + summoner_name), params=params)
        response = json.loads(response.text)
        summoner_id = response[summoner_name]['id']
        return summoner_id

    def get_current_game(self, summoner_id):
        url = 'https://euw.api.riotgames.com/observer-mode/rest/consumer/getSpectatorGameInfo/EUW1/'
        params = {'api_key': self.api_key }
        response = requests.get((url + str(summoner_id)), params=params)
        if response.status_code == 404:
            game = "Looks like that players not in a game!"
        else:
            response = json.loads(response.text)
            players = []
            for i in response['participants']:
                players.append(i['summonerName'])
            game = ('{:<30}        {:>30}\n'.format(players[0], players[5]) + 
                    '{:<30}        {:>30}\n'.format(players[1], players[6]) + 
                    '{:<30}   vs   {:>30}\n'.format(players[2], players[7]) + 
                    '{:<30}        {:>30}\n'.format(players[3], players[8]) + 
                    '{:<30}        {:>30}'.format(players[4], players[9])
                   )
        return game
    

    def handle_message(self, message):
        if message.content.split()[1] == 'live':
            summoner_name = message.content.split()[2]
            summoner_id = self.get_summoner_id(summoner_name)
            current_game = self.get_current_game(summoner_id)
            return current_game
        
        
