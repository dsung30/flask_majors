from flask import Flask, render_template, request
import espn_scoreboard_api

app = Flask(__name__)



headers = ['fruit', 'price', 'country']

@app.route('/', methods=['GET', 'POST'])
def home():
    headers = ['Player', 'Draft Status', 'Action']

    tableData = [
        {'Player':'Scottie Scheffler', 'Draft Status': 'Available', 'Action':'Draft'},
        {'Player':'Scottie Scheffler', 'Draft Status': 'Available', 'Action':'Draft'},
        {'Player':'Scottie Scheffler', 'Draft Status': 'Available', 'Action':'Draft'}
    ]

    return render_template(
        'index.html',
        headers=headers,
        tableData=tableData
    )

    return render_template('index.html')

@app.route('/data/')
def player_table():

    return render_template(
        'player_table.html',
        headers=headers,
        tableData=tableData
    )

#@app.route('/tournaments/')
#def tournament_selection():
#    tournaments = espn_scoreboard_api.get_tournament_list()
#    return render_template(
#        'tournament_select.html',
#        tournament = tournaments.keys()
#    )


if __name__ == '__main__':
    app.run(debug=True)
