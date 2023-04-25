
# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from datetime import datetime

database = "players_schema"


class Player:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.attemps = data['attemps']
        self.ranks = data['ranks']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database
    #! Create

    @classmethod
    def add_new_player(cls, data):
        # this query is for adding new winner info to mySQL database
        query = "INSERT INTO players (name, attemps) VALUES ( %(name)s, %(attemps)s);"
        return connectToMySQL(database).query_db(query, data)

    # Now we use class methods to query our database
    #! READ ALL
    @classmethod
    def get_all_player(cls):
        query = "SELECT *, DENSE_RANK() OVER (ORDER BY attemps ASC) AS ranks FROM players LIMIT 30;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(database).query_db(query)
        pprint(results)
        players = []
        for player in results:
            formatted_date = player['updated_at'].strftime('%m/%d/%Y')
            player['updated_at'] = formatted_date
            players.append(Player(player))
        return players
