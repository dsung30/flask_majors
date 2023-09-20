import requests
import json

# 2023 PGA CHAMPIONSHIP
ESPN_API_URL = ('https://site.api.espn.com/apis/site/v2/sports/golf/pga/scoreboard')

def espn_api_scoreboard():
    response = requests.get(ESPN_API_URL).json()
    tournaments = response['leagues'][0]['calendar']
    return tournaments

def tournament_list(tournaments):
    tournament_ids = []
    tournament_namedates = []

    for t in tournaments:
        tournament_ids.append(t['id'])
        tournament_namedates.append(t['label'] + ' ' + t['startDate'])

    tournaments = dict(zip(tournament_namedates, tournament_ids))

    return tournaments

def get_tournament_list():
    return tournament_list(espn_api_scoreboard())

def main():
    print(tournament_list(espn_api_scoreboard()))

if __name__ == '__main__':
    main()