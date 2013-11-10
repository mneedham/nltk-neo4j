// goals scored by Gareth Bale
MATCH (p:Player)-[:played]->(stats)
WHERE p.name = "Gareth Bale"
RETURN SUM(stats.goals) AS goals

// games Gareth Bale scored in
MATCH (p:Player)-[:played]->(stats)-[:in]-(game)
WHERE stats.goals > 0 AND p.name = "Gareth Bale"
RETURN game, stats.goals

// score draws
MATCH (g:Game)
WHERE g.home_goals = g.away_goals AND g.home_goals > 0
RETURN g

// no score draws
MATCH (g:Game)
WHERE g.home_goals = g.away_goals AND g.home_goals = 0
RETURN g

// teams with the most no score draws
MATCH (g:Game)
WHERE g.home_goals = g.away_goals AND g.home_goals = 0
WITH g
MATCH g<-[:home_team|:away_team]-(team)
RETURN team.name, COUNT(g) AS noScoreDraws, COLLECT(g.name) AS games
ORDER BY noScoreDraws DESC


// NER = Named Entity Recogniser
// gensim - topic modelling

// name similarity e.g. Gareth bale => Gareth Bale