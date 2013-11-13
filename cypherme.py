# coding=UTF-8

import nltk
from textblob import TextBlob
from textblob.taggers import NLTKTagger
from nltk import pos_tag, ne_chunk
from textblob.classifiers import NaiveBayesClassifier
import json

from py2neo import neo4j

countries = ["Argentina","Australia","Austria","Barbados","Belgium","Benin","Bosnia and Herzegovina","Brazil","Bulgaria","Cameroon","Canada","Chile","Colombia","Congo","Costa Rica","Croatia","Czech Republic","Denmark","Ecuador","Egypt","England","Finland","France","Germany","Greece","Grenada","Honduras","Hungary","Iceland","Iran","Ireland","Israel","Italy","Ivory Coast","Jamaica","Japan","Latvia","Macedonia","Mali","Mexico","Morocco","Netherlands","New Zealand","Nigeria","Northern Ireland","Norway","Oman","Paraguay","Poland","Portugal","Romania","Russia","Scotland","Senegal","Serbia","Sierra Leone","Slovakia","South Africa","South Korea","Spain","Sweden","Switzerland","Togo","Trinidad and Tobago","Turkey","USA","Uruguay","Wales","Zambia","Zimbabwe"]
players  = ["Steve Harper","Fabricio Coloccini","Mapou Yanga-Mbiwa","Mathieu Debuchy","Steven Taylor","Yohan Cabaye","Hatem Ben Arfa","Jonás Gutiérrez","Ismael Cheik Tioté","Papiss Demba Cisse","Yoan Gouffran","Wojciech Szczesny","Bacary Sagna","Per Mertesacker","Laurent Koscielny","Kieran Gibbs","Tomas Rosicky","Mikel Arteta","Theo Walcott","Aaron Ramsey","Santi Cazorla","Lukas Podolski","Vurnon Anita","Sylvain Marveaux","Adam Campbell","Jack Wilshere","Alex Oxlade-Chamberlain","Olivier Giroud","Ali Al Habsi","Emmerson Boyce","Roger Espinoza","Roman Golobart","Paul Scharner","James McCarthy","Ben Watson","Shaun Maloney","Jordi Gómez","James McArthur","Arouna Koné","Brad Guzan","Ron Vlaar","Joseph Bennett","Nathan Baker","Matthew Lowton","Ashley Westwood","Fabian Delph","Yacouba Sylla","Darren Bent","Gabriel Agbonlahor","Andreas Weimann","Eduard Campabadal","Fraser Fyvie","Angelo Henriquez","Gary Gardner","Jordan Bowery","Simon Dawkins","Petr Cech","Branislav Ivanovic","Ashley Cole","David Luiz","Gary Cahill","Frank Lampard","Fernando Torres","Juan Mata","Oscar","Nathan Ake","Demba Ba","Tim Howard","Leighton Baines","Phil Jagielka","Sylvain Distin","Seamus Coleman","Darron Gibson","Steven Naismith","Steven Pienaar","Marouane Fellaini","Kevin Mirallas","Victor Anichebe","Paulo Ferreira","César Azpilicueta","Victor Moses","John Heitinga","Nikica Jelavic","Michel Vorm","Chico","Ashley Williams","Angel Rangel","Ben Davies","Leon Britton","Pablo","Nathan Dyer","Wayne Routledge","Jonathan De Guzman","Michu","Mark Schwarzer","John Arne Riise","Philippe Senderos","Brede Hangeland","Sascha Riether","Emmanuel Frimpong","Damien Duff","Alexander Kacaniklic","Eyong Enoh","Dimitar Berbatov","Bryan Ruiz","Neil Taylor","Kemy Agustien","Itey Shechter","Giorgos Karagounis","Urby Emanuelson","Hugo Rodallega","Ben Foster","Jonas Olsson","Liam Ridgewell","Gareth McAuley","Billy Jones","Claudio Yacob","James Morrison","Chris Brunt","Graham Dorrans","Youssuf Mulumbu","Shane Long","Anders Lindegaard","Phil Jones","Jonathan Evans","Antonio Valencia","Alexander Büttner","Anderson","Javier Hernández","Michael Carrick","Tom Cleverley","Shinji Kagawa","Robin Van Persie","Markus Rosenberg","Romelu Lukaku","Marc-Antoine Fortune","Rio Ferdinand","Ryan Giggs","Paul Scholes","Joe Hart","Micah Richards","Pablo Zabaleta","Joleon Lescott","Aleksandar Kolarov","James Milner","Samir Nasri","Jack Rodwell","Yaya Touré","Edin Dzeko","Carlos Tevez","John Ruddy","Russell Martin","Steven Whittaker","Javier Garrido","Ryan Bennett","Bradley Johnson","Robert Snodgrass","Jonathan Howson","Anthony Pilkington","Grant Holt","Wesley Hoolahan","David Silva","Sergio Agüero","Elliott Bennett","Alexander Tettey","Luciano Becchio","Pepe Reina","Glen Johnson","José Enrique","Jamie Carragher","Martin Skrtel","Philippe Coutinho","Jordan Henderson","Stewart Downing","Lucas","Jordan Ibe","Daniel Sturridge","Robert Green","Armand Traore","Clint Hill","Nedum Onuoha","Michael Harriman","Shaun Derry","Park Ji-Sung","Andros Townsend","Stéphane M'Bia","Loïc Remy","Bobby Zamora","Sebastián Coates","Fabio Borini","Suso","Esteban Granero","Jamie Mackie","David Hoilett","Hugo Lloris","Jan Vertonghen","Michael Dawson","Kyle Walker","Benoit Assou-Ekotto","Clint Dempsey","Tom Huddlestone","Aaron Lennon","Scott Parker","Gareth Bale","Emmanuel Adebayor","Simon Mignolet","Sebastian Larsson","Jack Colback","John O'Shea","Carlos Jimenez Cuellar","Alfred Ndiaye","David Vaughan","Adam Johnson","James McClean","Danny Graham","Connor Wickham","Gylfi Sigurdsson","Jermain Defoe","Mousa Dembele","Adam Mitchell","Mikael Mandron","Billy Knott","Eric Lichaj","Christian Benteke","John Terry","Ramires","Eden Hazard","Kieran Richardson","Aaron Hughes","Andre Wisdom","Jonjo Shelvey","Mladen Petric","Conor Coady","José Bosingwa","Jermaine Jenas","Robert Elliot","Michael Williamson","Fabio","Adel Taarabt","James Perch","Gabriel Obertan","David De Gea","Patrice Evra","Nemanja Vidic","Danny Welbeck","Gerhard Tremmel","Dwight Tiendalli","Asmir Begovic","Robert Huth","Marc Wilson","Ryan Shawcross","Ryan Shotton","Steven Nzonzi","Charlie Adam","Dean Whitehead","Jonathan Walters","Matthew Etherington","Peter Crouch","Steven Caulker","Andy Wilkinson","Geoff Cameron","Cameron Jerome","Sebastien Bassong","Steven Reid","Goran Popov","Peter Odemwingie","Leon Osman","Jussi Jaaskelainen","Winston Reid","Joey O'Brien","James Collins","Guy Demel","Kevin Nolan","Matthew Jarvis","Jack Collison","Mohamed Diame","Gary O'Neil","Andrew Carroll","Tony Hibbert","Bryan Oviedo","Mark Noble","Joe Cole","Carlton Cole","Joel Robles","Antolín Alcaraz","Callum McManaman","Thomas Vermaelen","Franco Di Santo","Tal Ben Haim","Nacho Monreal","Mark Bunn","Simeon Jackson","Kei Kamara","Brett Holman","Rafael","Wayne Rooney","Daniel Agger","Steven Gerrard","Vincent Kompany","Gaël Clichy","Matija Nastasic","Gareth Barry","Luke Moore","Ricardo Vaz Te","Danny Simpson","Matthew Taylor","Dan Gosling","Shola Ameobi","Danny Rose","Craig Gardner","Phillip Bardsley","Kenwyne Jones","Jean Beausejour","Ronnie Stam","Jerome Thomas","Isaiah Brown","Stanislav Manolev","Ross  Barkley","Massadio Haidara","Moussa Sissoko","Nani","Gervinho","Glenn Whelan","Stephane Sessegnon","Ki Sung-Yueng","Maynor Figueroa","Kyle Naughton","Lewis Holtby","Kolo Touré","Javi Garcia","Steve Sidwell","Kerim Frei","Charles N'Zogbia","Ciaran Clark","Karim El Ahmadi","Luis Suárez","Ryan Bertrand","John Mikel Obi","Yossi Benayoun","Abdou Kader Mangane","Scott Sinclair","Christopher Samba","Jay Bothroyd","Gary Caldwell","Michael Owen","Lukasz Fabianski","Michael Turner","David Fox","Júlio César","Samba Diakité","Tim Krul","Garry Monk","Boaz Myhill","Craig Dawson","Gabriel Tamas","Maicon","Abdul Razak","Francis Coquelin","Michael Kightly","Thomas Carroll","Davide Santon","Ashley Young","Matthew Kilgallon","Lee Camp","Roland Lamah","James Tomkins","Oussama Assaidi","Emanuel Pogatetz","Barry Bannan","Raheem Sterling","Titus Bramble","Chris Smalling","Gael Bigirimana","Ashkan Dejagah","Brad Friedel","George McCartney","Carl Jenkinson","Abou Diaby","Jan Mucha","Steven Fletcher","Shaun Wright-Phillips","Brad Jones","Jake Livermore","Joe Allen","William Gallas","Brek Shea","Chris Baird","Kyle Bartley","Lee Cattermole","Ignasi Miquel","Phil Neville","Marko Marin","David Jones","George Thorne","Marouane Chamakh","André Santos","Ryan Nelsen","Alejandro Damian Faurlin","Andrei Arshavin","Matthew Briggs","Mauro Boselli","Ahmed Elmohamady","Mario Balotelli","Apostolos Vellios","Sandro","Daniel Potts","Alou Diarra","James McFadden","Ivan Ramis","Enda Stevens","Chris Herd","Marc Albrighton","Sammy Ameobi","Nile Ranger","Zoltan Gera","David Stockdale","Harry Kane","Jordan Spence","Modibo Maíga","Ross Turnbull","Kieron Courtney Dyer","Fraizer Campbell","Thomas Hitzlsperger","Djibril Cissé","Steve Morison","James Tavernier","Shane Ferguson","Stephen Ireland","Darren Fletcher","Anton Ferdinand","Lucas Piazon","Shane Duffy","Stephen Kelly","Adrián López Rodríguez","Oriol Romeu","Louis Saha","Leon Barnett","Yago Falqué","Derrick Williams","Mahamadou Diarra","Nick Powell","Wilson Palacios","Ryo Miyaichi","Vito Mannone","Nuri Sahin","Magaye Gueye","Serge Gnabry","Gonzalo Jara","Maurice Edu","Andrew Surman","Alan Tate","Martin Kelly","David Meyler","Andrew Johnson","Alex Smith","Pajtim Kasami","Robert Hall","Jermaine Pennant","Shay Given","Nathan Delfouneso","Nigel De Jong","Raul Meireles","Ryan Taylor","Chris Martin","Rafael Van der Vaart","Marc Tierney","Mark Gower","Younes Kaboul","Alex McCarthy","Chris Gunter","Sean Morrison","Kaspars Gorkss","Jem Karacan","Jobi McAnuff","Garath McCleary","Hal Robson-Kanu","Danny Guthrie","Pavel Pogrebnyak","Adam Le Fondre","Nick Blackman","Adrian Mariappa","Daniel Carriço","Ian Harte","Noel Hunt","Stuart Taylor","Nicky Shorey","Alex Pearce","Mikele Leigertwood","Hope Akpan","Jimmy Kebe","Adam Federici","Karim Rekik","Jay Tabb","Shaun Cummings","Jason Roberts","Dominic Samuel","Rory Delap","Kelvin Davis","Nathaniel Clyne","Jos Hooiveld","Jose Fonte","Luke Shaw","Morgan Schneiderlin","Steven Davis","Jay Rodriguez","Jack  Cork","Adam Lallana","Rickie Lambert","James Ward-Prowse","Jason Puncheon","Emmanuel Mayuka","Artur Boruc","Guilherme Do Prado","Maya Yoshida","Daniel Fox","Gaston Ramirez","Frazer Richardson","Steve  De Ridder","Matthew Upson","Richard Chaplow","Paulo Gazzaniga","Ben Reeves","Billy Sharp"]
teams = ["Arsenal","Aston Villa","Birmingham City","Blackburn Rovers","Blackpool","Bolton Wanderers","Burnley","Charlton Athletic","Chelsea","Crystal Palace","Derby County","Everton","Fulham","Hull City","Ipswich Town","Leeds United","Leicester City","Liverpool","Manchester City","Manchester United","Middlesbrough","Newcastle United","Norwich City","Portsmouth","Queens Park Rangers","Reading","Sheffield United","Southampton","Stoke City","Sunderland","Swansea City","Tottenham Hotspur","Watford","West Bromwich Albion","West Ham United","Wigan Athletic","Wolverhampton Wanderers"]

with open('nationalities.json') as nationalities_file:    
    nationalities = dict((n['nationality'], n['country'].strip()) for n in json.load(nationalities_file))

def pronoun_extractor(pronoun):	
	feats = {}
	feats["contains team"] = pronoun in teams
	feats["contains player"] = pronoun in players
	feats["contains country"] = pronoun in countries
	feats["contains nationality"] = pronoun in nationalities.keys()
	return feats

def pos_tagify(sentence):
	tokens = nltk.tokenize.word_tokenize(sentence)
	return nltk.pos_tag(tokens)	

def extract_proper_nouns(sentence):
	grammar = r"""
		NP: {(<NNP>|<NNPS>)+}
		"""
	
	tree = nltk.RegexpParser(grammar, loop=2).parse(pos_tagify(sentence))

	proper_noun = []
	for subtree in tree.subtrees():
		if(subtree.node == "NP"):
			proper_noun.append(subtree)	

	return [" ".join([word for (word, tag) in p.leaves()]) for p in proper_noun]

def as_cypher(sentence, classifier):
	proper_nouns = extract_proper_nouns(sentence)
	
	classified_proper_nouns = [(proper_noun, classifier.classify(proper_noun)) for proper_noun in proper_nouns]
	print(classified_proper_nouns)

	if all(category == "player" for (pnoun, category) in classified_proper_nouns):
		cypher_query = []
		cypher_query.append("MATCH (p:Player)-[:played]-(stats)")

		or_clause = " OR ".join(["p.name = '%s'" % player for player in proper_nouns])
		where_clause = "WHERE " +  or_clause
		cypher_query.append(where_clause)

		cypher_query.append("RETURN p.name, SUM(stats.goals) AS goalsScored")
	else:		
		proper_nouns = [nationalities[pnoun] if category == "nationality" else pnoun for (pnoun, category) in classified_proper_nouns]

		cypher_query = []
		cypher_query.append("MATCH (c:Country)<-[:comes_from]-(p)-[:played]-(stats)")

		or_clause = " OR ".join(["c.name = '%s'" % country for country in proper_nouns])
		where_clause = "WHERE " +  or_clause
		cypher_query.append(where_clause)

		cypher_query.append("RETURN p.name, SUM(stats.goals) AS goalsScored")

	return "\n".join(cypher_query)

def query(cypher_query):
	graph_db = neo4j.GraphDatabaseService()
	query = neo4j.CypherQuery(graph_db, cypher_query)
	print(cypher_query)
	return query.execute().data

data = [(team, "team") for team in teams] + [(player, "player") for player in players] + [(country, "country") for country in countries] + [(n, "nationality") for n in nationalities.keys()]

cl2 = NaiveBayesClassifier(data, feature_extractor=pronoun_extractor)

# print query(as_cypher("goals scored by Gareth Bale", cl2))
# print query(as_cypher("goals scored by Gareth Bale or Robin Van Persie", cl2))
# print query(as_cypher("goals scored by England players", cl2))
# print query(as_cypher("goals scored by Dutch players", cl2))

# Determine whether the pronouns that exist in the data set are players, teams or whatever
# Determine a type of query e.g. goals scored query
# English should be converted to England, Spanish to Spain
