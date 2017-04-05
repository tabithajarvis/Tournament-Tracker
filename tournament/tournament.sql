-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

\c tournament;

CREATE TABLE players(
  id SERIAL PRIMARY KEY,
  name TEXT
);

CREATE TABLE matches(
  winner INTEGER REFERENCES players(id),
  loser INTEGER REFERENCES players(id),
  PRIMARY KEY (winner, loser)
);

CREATE VIEW player_standings AS
  SELECT players.id AS id,
         players.name AS name,
         COUNT(a.winner) AS wins,
         COUNT(b.*) AS total
    FROM players
      LEFT OUTER JOIN matches
        AS a
        ON(players.id = a.winner)
      LEFT OUTER JOIN matches
        AS b
        ON(players.id = b.winner OR
           players.id = b.loser)
    GROUP BY id
    ORDER BY wins;
