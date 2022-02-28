
import stats

# component for Simulation is always a random float [0, 1)
# component for a Simulation_Marbles is always the sum of the values of the dictionary

def p15(n):
	components = {1: 0.55, 2: 0.45} # candidate 1 if c between [0, .55), candidate 2 if c between (.55, 1)
	num_components = 100 # trial is a series of 100 votes
	response = lambda t: t.count(2) > 50 # True if there are more than 50 2s
	election_sim = stats.Simulation(n, components, num_components, response)
	return election_sim.statistic()
	# According to the simulation, there is a 13.24% chance that the other candidate wins the election
	# if 100 people vote.

def p16(n):
	components = {'spades': 13, 'clubs': 13, 'hearts': 13, 'diamonds': 13} 
	# spades if [1, 13], clubs if [14, 26], hearts if [27, 39], diamonds if [40, 52]
	num_components = 5 # trial is a series of 5 cards, subtracting from the suit chosen each time
	def response(t):
		two = False
		three = False
		for c in t:
			if t.count(c) == 2:
				two = True
			if t.count(c) == 3:
				three = True
		if two and not three:
			return 2
		if three and not two:
			return 3
		return 0
	cards_sim = stats.Simulation_Marbles(n, components, num_components, response)
	return {2: cards_sim.statistic(2), 3: cards_sim.statistic(3)}
	# According to the simulation, it is more likely to draw two cards of the same suit than three in a 
	# deck of 5 cards.

def p17(n):
	components = {'Lebron James': .2, 'Danica Patrick': .3, 'Dustin Johnson': .5}
	# Lebron James if [0, .2), Danica Patrick if [.2, .5), Dustin Johnson if [.5, 1)
	num_components = 5
	response = lambda t: 'Lebron James' in t and 'Danica Patrick' in t and 'Dustin Johnson' in t
	cereal_sim = stats.Simulation(n, components, num_components, response)
	return cereal_sim.statistic()
	# According to the simulation, there is a 50.63% chance that you end up with a complete set with 5 boxes.

def p18(n):
	components = {'Lebron James': .2, 'Danica Patrick': .3, 'Dustin Johnson': .6} # Lebron James if [0, .2)
	# trial: will generate random components until finds Lebron picture
	# response: the number of boxes examined
	stop = lambda t: 'Lebron James' in t
	cereal_sim = stats.Simulation_N(n, components, stop)
	return cereal_sim.statistic()
	# According to the simulation you need to buy 6 boxes to be sure to get LeBron's card.

def p19(n):
	components = {True: .8, False: .2} # get right if [0, 0.8), boolean
	num_components = 6 # trial is series of 6 components
	response = lambda t: not False in t # whether or not there is a False in the trial
	quiz_sim = stats.Simulation(n, components, num_components, response)
	return quiz_sim.statistic()
	# According to the simulation, there is a 26.12% chance that you will get them all right

def p20(n):
	components = {True: .25, False: .75} # get right if [0, .25), boolean
	num_components = 6 # trial is a series of 6 components
	response = lambda t: not False in t
	quiz_sim = stats.Simulation(n, components, num_components, response)
	return quiz_sim.statistic()
	# I don't believe her, because according to my simulation, there is a 0.03% chance that she got them all 
	# right

if __name__ == '__main__':
	pass
