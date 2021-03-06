import requests
import json
import auth


class league:

    def __init__(self):
        self.api_key = auth.get_auth()['leagueoflegends']['api_key']

    def get_summoner_id(self, summoner_name):
        url = 'https://euw1.api.riotgames.com/lol/summoner/v3/summoners/by-name/'
        params = {'api_key': self.api_key }
        response = requests.get((url + summoner_name), params=params)
        response = json.loads(response.text)
        summoner_id = response['id']
        return account_id

    def get_current_game(self, summoner_id):
        url = 'https://euw1.api.riotgames.com/lol/spectator/v3/active-games/by-summoner'
        params = {'api_key': self.api_key }
        response = requests.get((url + str(summoner_id)), params=params)
        if response.status_code == 404:
            return "Looks like that players not in a game!"
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

    def get_profile(self, summoner_id):
      url = 'https://euw.api.riotgames.com/placeholder'
      params = {'api_key': self.api_key}
      response = requests.get((url + str(summoner_id)), params=params)
      if response.status_code == 404:
          return "Looks like that player doesn't exist."
      else:
        response = json.loads(response.text)
        # do stuff
        # set url

    def handle_message(self, message):
        if message.content.split()[1] == 'live':
            summoner_name = message.content.split()[2]
            summoner_id = self.get_summoner_id(summoner_name)
            current_game = self.get_current_game(summoner_id)
            return current_game
        elif message.content.split()[1] == 'profile':
            summoner_name = message.content.split[2]
            summoner_id = self.get_summoner_id(summoner_name)
            profile = self.get_profile(summoner_id)
            return profile
        else:
            return "Unkown command, must be one of `live` or `profile`"
