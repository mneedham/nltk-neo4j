import nltk
from textblob import TextBlob
from textblob.taggers import NLTKTagger
from nltk import pos_tag, ne_chunk

from py2neo import neo4j

def break_down(query):
	nltk_tagger = NLTKTagger()
	blob = TextBlob(query, pos_tagger=nltk_tagger)
	return blob.pos_tags

def pos_tagify(query):
	tokens = nltk.tokenize.word_tokenize(query)
	return nltk.pos_tag(tokens)	

def extract_players(query):
	grammar = r"""
		NP: {<NNP>+}
		"""
	
	tree = nltk.RegexpParser(grammar, loop=2).parse(pos_tagify(query))

	player = []
	for subtree in tree.subtrees():
		if(subtree.node == "NP"):
			player.append(subtree)	

	return [" ".join([word for (word, tag) in p.leaves()]) for p in player]

def cypher_me(query):
	players = extract_players(query)
	
	cypher_query = []
	cypher_query.append("MATCH (p:Player)-[:played]-(stats)")

	or_clause = " OR ".join(["p.name = '%s'" % player for player in players])
	where_clause = "WHERE " +  or_clause
	cypher_query.append(where_clause)

	cypher_query.append("RETURN p.name, SUM(stats.goals) AS goalsScored")
	return "\n".join(cypher_query)

def query(cypher_query):
	graph_db = neo4j.GraphDatabaseService()
	query = neo4j.CypherQuery(graph_db, cypher_query)
	return query.execute().data

# cypher_me("goals scored by Gareth Bale")

print query(cypher_me("goals scored by Gareth Bale"))
print query(cypher_me("goals scored by Gareth Bale or Robin Van Persie"))

# Determine whether the pronouns that exist in the data set are players, teams or whatever
# Determine a type of query e.g. goals scored query
