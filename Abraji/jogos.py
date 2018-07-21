import urllib.request
import json
resp = urllib.request.urlopen('http://worldcup.sfg.io/matches').read()
for jogo in json.loads(resp.decode('utf-8')):
    if jogo['status'] == 'completed':
        print (jogo['home_team']['country'], jogo['home_team']['goals'], 'x', jogo['away_team']['country'], jogo['away_team']['goals'])
