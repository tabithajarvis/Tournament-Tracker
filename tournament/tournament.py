"""
Tournament database handler.

This module performs the interface between a tournament application and the
tournament database.
"""

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    cursor = DB.cursor()
    query = "DELETE FROM matches"
    cursor.execute(query)
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    cursor = DB.cursor()
    query = "DELETE FROM players"
    cursor.execute(query)
    DB.commit()
    DB.close()


def countPlayers():
    """Return the number of players currently registered."""
    DB = connect()
    cursor = DB.cursor()
    query = "SELECT id FROM players"
    cursor.execute(query)
    result = cursor.rowcount
    DB.close()
    return result


def registerPlayer(name):
    """Add a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    cursor = DB.cursor()
    query = "INSERT INTO players (name) VALUES (%s);"
    data = (name,)
    cursor.execute(query, data)
    DB.commit()
    DB.close()


def playerStandings():
    """Return a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    cursor = DB.cursor()
    query = \
        "SELECT players.id, players.name, COUNT(a.winner), COUNT(b.*) \
        FROM players LEFT OUTER JOIN matches AS a \
        ON(players.id = a.winner) \
        LEFT OUTER JOIN matches AS b\
        ON(players.id = b.winner OR \
           players.id = b.loser) \
        GROUP BY players.id \
        ORDER BY COUNT(a.winner)"
    cursor.execute(query)
    result = cursor.fetchall()
    DB.close()
    return result


def reportMatch(winner, loser):
    """Record the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    cursor = DB.cursor()
    query = "INSERT INTO matches (winner, loser) VALUES (%s, %s)"
    data = (winner, loser)
    cursor.execute(query, data)
    DB.commit()
    DB.close()


def swissPairings():
    """Return a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    pairings = []
    for i in xrange(0, len(standings), 2):
        pairings.append((
            standings[i][0],    # id1
            standings[i][1],    # name1
            standings[i+1][0],  # id2
            standings[i+1][1]   # name2
            ))

    return pairings
