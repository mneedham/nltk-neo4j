from textblob import TextBlob
from textblob.taggers import NLTKTagger
import nltk
from textblob.classifiers import NaiveBayesClassifier
import random

def break_down(query):
	blob = TextBlob(query, pos_tagger=nltk_tagger)
	return blob.pos_tags

def word_extractor(document):
	tokens = document.split()
	feats = {}
	for t in tokens:
		feats["contains team"] = t in teams
		feats["contains player"] = t in players
	
	return feats

players  = ["Steve Harper","Fabricio Coloccini","Mapou Yanga-Mbiwa","Mathieu Debuchy","Steven Taylor","Yohan Cabaye","Hatem Ben Arfa","Jonás Gutiérrez","Ismael Cheik Tioté","Papiss Demba Cisse","Yoan Gouffran","Wojciech Szczesny","Bacary Sagna","Per Mertesacker","Laurent Koscielny","Kieran Gibbs","Tomas Rosicky","Mikel Arteta","Theo Walcott","Aaron Ramsey","Santi Cazorla","Lukas Podolski","Vurnon Anita","Sylvain Marveaux","Adam Campbell","Jack Wilshere","Alex Oxlade-Chamberlain","Olivier Giroud","Ali Al Habsi","Emmerson Boyce","Roger Espinoza","Roman Golobart","Paul Scharner","James McCarthy","Ben Watson","Shaun Maloney","Jordi Gómez","James McArthur","Arouna Koné","Brad Guzan","Ron Vlaar","Joseph Bennett","Nathan Baker","Matthew Lowton","Ashley Westwood","Fabian Delph","Yacouba Sylla","Darren Bent","Gabriel Agbonlahor","Andreas Weimann","Eduard Campabadal","Fraser Fyvie","Angelo Henriquez","Gary Gardner","Jordan Bowery","Simon Dawkins","Petr Cech","Branislav Ivanovic","Ashley Cole","David Luiz","Gary Cahill","Frank Lampard","Fernando Torres","Juan Mata","Oscar","Nathan Ake","Demba Ba","Tim Howard","Leighton Baines","Phil Jagielka","Sylvain Distin","Seamus Coleman","Darron Gibson","Steven Naismith","Steven Pienaar","Marouane Fellaini","Kevin Mirallas","Victor Anichebe","Paulo Ferreira","César Azpilicueta","Victor Moses","John Heitinga","Nikica Jelavic","Michel Vorm","Chico","Ashley Williams","Angel Rangel","Ben Davies","Leon Britton","Pablo","Nathan Dyer","Wayne Routledge","Jonathan De Guzman","Michu","Mark Schwarzer","John Arne Riise","Philippe Senderos","Brede Hangeland","Sascha Riether","Emmanuel Frimpong","Damien Duff","Alexander Kacaniklic","Eyong Enoh","Dimitar Berbatov","Bryan Ruiz","Neil Taylor","Kemy Agustien","Itey Shechter","Giorgos Karagounis","Urby Emanuelson","Hugo Rodallega","Ben Foster","Jonas Olsson","Liam Ridgewell","Gareth McAuley","Billy Jones","Claudio Yacob","James Morrison","Chris Brunt","Graham Dorrans","Youssuf Mulumbu","Shane Long","Anders Lindegaard","Phil Jones","Jonathan Evans","Antonio Valencia","Alexander Büttner","Anderson","Javier Hernández","Michael Carrick","Tom Cleverley","Shinji Kagawa","Robin Van Persie","Markus Rosenberg","Romelu Lukaku","Marc-Antoine Fortune","Rio Ferdinand","Ryan Giggs","Paul Scholes","Joe Hart","Micah Richards","Pablo Zabaleta","Joleon Lescott","Aleksandar Kolarov","James Milner","Samir Nasri","Jack Rodwell","Yaya Touré","Edin Dzeko","Carlos Tevez","John Ruddy","Russell Martin","Steven Whittaker","Javier Garrido","Ryan Bennett","Bradley Johnson","Robert Snodgrass","Jonathan Howson","Anthony Pilkington","Grant Holt","Wesley Hoolahan","David Silva","Sergio Agüero","Elliott Bennett","Alexander Tettey","Luciano Becchio","Pepe Reina","Glen Johnson","José Enrique","Jamie Carragher","Martin Skrtel","Philippe Coutinho","Jordan Henderson","Stewart Downing","Lucas","Jordan Ibe","Daniel Sturridge","Robert Green","Armand Traore","Clint Hill","Nedum Onuoha","Michael Harriman","Shaun Derry","Park Ji-Sung","Andros Townsend","Stéphane M'Bia","Loïc Remy","Bobby Zamora","Sebastián Coates","Fabio Borini","Suso","Esteban Granero","Jamie Mackie","David Hoilett","Hugo Lloris","Jan Vertonghen","Michael Dawson","Kyle Walker","Benoit Assou-Ekotto","Clint Dempsey","Tom Huddlestone","Aaron Lennon","Scott Parker","Gareth Bale","Emmanuel Adebayor","Simon Mignolet","Sebastian Larsson","Jack Colback","John O'Shea","Carlos Jimenez Cuellar","Alfred Ndiaye","David Vaughan","Adam Johnson","James McClean","Danny Graham","Connor Wickham","Gylfi Sigurdsson","Jermain Defoe","Mousa Dembele","Adam Mitchell","Mikael Mandron","Billy Knott","Eric Lichaj","Christian Benteke","John Terry","Ramires","Eden Hazard","Kieran Richardson","Aaron Hughes","Andre Wisdom","Jonjo Shelvey","Mladen Petric","Conor Coady","José Bosingwa","Jermaine Jenas","Robert Elliot","Michael Williamson","Fabio","Adel Taarabt","James Perch","Gabriel Obertan","David De Gea","Patrice Evra","Nemanja Vidic","Danny Welbeck","Gerhard Tremmel","Dwight Tiendalli","Asmir Begovic","Robert Huth","Marc Wilson","Ryan Shawcross","Ryan Shotton","Steven Nzonzi","Charlie Adam","Dean Whitehead","Jonathan Walters","Matthew Etherington","Peter Crouch","Steven Caulker","Andy Wilkinson","Geoff Cameron","Cameron Jerome","Sebastien Bassong","Steven Reid","Goran Popov","Peter Odemwingie","Leon Osman","Jussi Jaaskelainen","Winston Reid","Joey O'Brien","James Collins","Guy Demel","Kevin Nolan","Matthew Jarvis","Jack Collison","Mohamed Diame","Gary O'Neil","Andrew Carroll","Tony Hibbert","Bryan Oviedo","Mark Noble","Joe Cole","Carlton Cole","Joel Robles","Antolín Alcaraz","Callum McManaman","Thomas Vermaelen","Franco Di Santo","Tal Ben Haim","Nacho Monreal","Mark Bunn","Simeon Jackson","Kei Kamara","Brett Holman","Rafael","Wayne Rooney","Daniel Agger","Steven Gerrard","Vincent Kompany","Gaël Clichy","Matija Nastasic","Gareth Barry","Luke Moore","Ricardo Vaz Te","Danny Simpson","Matthew Taylor","Dan Gosling","Shola Ameobi","Danny Rose","Craig Gardner","Phillip Bardsley","Kenwyne Jones","Jean Beausejour","Ronnie Stam","Jerome Thomas","Isaiah Brown","Stanislav Manolev","Ross  Barkley","Massadio Haidara","Moussa Sissoko","Nani","Gervinho","Glenn Whelan","Stephane Sessegnon","Ki Sung-Yueng","Maynor Figueroa","Kyle Naughton","Lewis Holtby","Kolo Touré","Javi Garcia","Steve Sidwell","Kerim Frei","Charles N'Zogbia","Ciaran Clark","Karim El Ahmadi","Luis Suárez","Ryan Bertrand","John Mikel Obi","Yossi Benayoun","Abdou Kader Mangane","Scott Sinclair","Christopher Samba","Jay Bothroyd","Gary Caldwell","Michael Owen","Lukasz Fabianski","Michael Turner","David Fox","Júlio César","Samba Diakité","Tim Krul","Garry Monk","Boaz Myhill","Craig Dawson","Gabriel Tamas","Maicon","Abdul Razak","Francis Coquelin","Michael Kightly","Thomas Carroll","Davide Santon","Ashley Young","Matthew Kilgallon","Lee Camp","Roland Lamah","James Tomkins","Oussama Assaidi","Emanuel Pogatetz","Barry Bannan","Raheem Sterling","Titus Bramble","Chris Smalling","Gael Bigirimana","Ashkan Dejagah","Brad Friedel","George McCartney","Carl Jenkinson","Abou Diaby","Jan Mucha","Steven Fletcher","Shaun Wright-Phillips","Brad Jones","Jake Livermore","Joe Allen","William Gallas","Brek Shea","Chris Baird","Kyle Bartley","Lee Cattermole","Ignasi Miquel","Phil Neville","Marko Marin","David Jones","George Thorne","Marouane Chamakh","André Santos","Ryan Nelsen","Alejandro Damian Faurlin","Andrei Arshavin","Matthew Briggs","Mauro Boselli","Ahmed Elmohamady","Mario Balotelli","Apostolos Vellios","Sandro","Daniel Potts","Alou Diarra","James McFadden","Ivan Ramis","Enda Stevens","Chris Herd","Marc Albrighton","Sammy Ameobi","Nile Ranger","Zoltan Gera","David Stockdale","Harry Kane","Jordan Spence","Modibo Maíga","Ross Turnbull","Kieron Courtney Dyer","Fraizer Campbell","Thomas Hitzlsperger","Djibril Cissé","Steve Morison","James Tavernier","Shane Ferguson","Stephen Ireland","Darren Fletcher","Anton Ferdinand","Lucas Piazon","Shane Duffy","Stephen Kelly","Adrián López Rodríguez","Oriol Romeu","Louis Saha","Leon Barnett","Yago Falqué","Derrick Williams","Mahamadou Diarra","Nick Powell","Wilson Palacios","Ryo Miyaichi","Vito Mannone","Nuri Sahin","Magaye Gueye","Serge Gnabry","Gonzalo Jara","Maurice Edu","Andrew Surman","Alan Tate","Martin Kelly","David Meyler","Andrew Johnson","Alex Smith","Pajtim Kasami","Robert Hall","Jermaine Pennant","Shay Given","Nathan Delfouneso","Nigel De Jong","Raul Meireles","Ryan Taylor","Chris Martin","Rafael Van der Vaart","Marc Tierney","Mark Gower","Younes Kaboul","Alex McCarthy","Chris Gunter","Sean Morrison","Kaspars Gorkss","Jem Karacan","Jobi McAnuff","Garath McCleary","Hal Robson-Kanu","Danny Guthrie","Pavel Pogrebnyak","Adam Le Fondre","Nick Blackman","Adrian Mariappa","Daniel Carriço","Ian Harte","Noel Hunt","Stuart Taylor","Nicky Shorey","Alex Pearce","Mikele Leigertwood","Hope Akpan","Jimmy Kebe","Adam Federici","Karim Rekik","Jay Tabb","Shaun Cummings","Jason Roberts","Dominic Samuel","Rory Delap","Kelvin Davis","Nathaniel Clyne","Jos Hooiveld","Jose Fonte","Luke Shaw","Morgan Schneiderlin","Steven Davis","Jay Rodriguez","Jack  Cork","Adam Lallana","Rickie Lambert","James Ward-Prowse","Jason Puncheon","Emmanuel Mayuka","Artur Boruc","Guilherme Do Prado","Maya Yoshida","Daniel Fox","Gaston Ramirez","Frazer Richardson","Steve  De Ridder","Matthew Upson","Richard Chaplow","Paulo Gazzaniga","Ben Reeves","Billy Sharp"]
teams = ["Arsenal","Aston Villa","Birmingham City","Blackburn Rovers","Blackpool","Bolton Wanderers","Burnley","Charlton Athletic","Chelsea","Crystal Palace","Derby County","Everton","Fulham","Hull City","Ipswich Town","Leeds United","Leicester City","Liverpool","Manchester City","Manchester United","Middlesbrough","Newcastle United","Norwich City","Portsmouth","Queens Park Rangers","Reading","Sheffield United","Southampton","Stoke City","Sunderland","Swansea City","Tottenham Hotspur","Watford","West Bromwich Albion","West Ham United","Wigan Athletic","Wolverhampton Wanderers"]


data = [
	 ('goals scored by Gareth Bale', 'player'),
	 ('top goal scorer', 'non-player'),
	 ('top away goal scorer', 'non-player'),
	 ('top home goal scorer', 'non-player'),
	 ('goals scored against Arsenal by Wayne Rooney', 'player'),
	 ('goals scored by Steven Gerrard in evening kick offs', 'player'),
	 ('top scoring team', 'non-player'),
	 ('players who scored and got a yellow card in the same game', 'non-player'),
	 ('players who scored and got a yellow card', 'non-player'),
	 ('players who scored and got booked', 'non-player'),
	 ('scored and got sent off', 'non-player'),
	 ('yellow cards received by Wayne Rooney', 'player'),
	 ('red cards for Lee Cattermole', 'player'),
	 ('second half red cards for John Terry', 'player'),
	 ('goals scored by Wayne Rooney in the second half against Arsenal', 'player'),
	 ('red cards for Manchester United', 'non-player'),
	 ('teams with the most red cards', 'non-player'),
]

split = len(data) // 2
random.shuffle(data)

cl = NaiveBayesClassifier(data[split:])
cl.classify("games Steven Gerrard played in")

cl.accuracy(data[:split])

cl2 = NaiveBayesClassifier(data[split:], feature_extractor=word_extractor)
cl2.accuracy(data[:split])

# break_down("goals scored by Gareth Bale")
# [('goals', u'NNS'), ('scored', u'VBD'), ('by', u'IN'), ('Gareth', u'NNP'), ('Bale', u'NNP')]	

# ->  MATCH (p:Player)-[:played]->(stats)
# 	  WHERE p.name = "Gareth Bale",
# 	  RETURN SUM(stats.goals) AS goals

# Extract the proper nouns

# 1. Classify two types of queries
#	query about players
#	query not about players

# goals scored by Gareth Bale, player
# top goal scorer, no-player
# top away goal scorer, no-player
# top home goal scorer, no-player