from random import random, randint

class Simulation:

	def __init__(self, num_trials, components, num_components, rule):
		""" takes parameters num_trials - the number of trials to be conducted
		components - a dictionary of the components and the chances of them, for example {1: .55, 2: .45}
		num_components - the number of components in one trial
		rule - evaluation function that returns True or False
		"""
		self.num_trials = num_trials
		self.components = components
		self.num_components = num_components
		self.rule = rule
		self.results = self.run()

	def run(self):
		""" run the simulation, return the data"""
		data = []
		for t in range(self.num_trials): # go through each trial
			trial = [] # make a new trial
			for c in range(self.num_components): # go through each component
				rand = random() # make a random number

				# find out which value the random number corresponds to
				chance = 0
				for k in self.components:
					chance += self.components[k]
					if rand < chance:
						value = k
						break

				trial.append(k)

			data.append(self.rule(trial))

		return data

	def chance(self, component=True):
		""" return the chance of a success or failure, takes component, which is true or false """
		return self.results.count(component)/self.num_trials

class Simulation_Marbles(Simulation):

	""" components should be the number of each one instead of the percentages, like {'red': 4, 'blue': 8} """

	def run(self):
		data = []
		for t in range(self.num_trials): # go through each trial
			trial = [] # make a new trial
			for c in range(self.num_components): # go through each component
				rand = randint(1, sum(self.components.values())) # make a random number

				# find out which value the random number corresponds to
				chance = 0
				for k in self.components:
					chance += self.components[k]
					if rand < chance:
						value = k
						break

				trial.append(k)

			data.append(self.rule(trial))

		return data

class Simulation_N(Simulation):

	""" a simulation to determine the number of components necessary to make the rule true """

	def __init__(self, num_trials, components, rule):
		""" no num_components"""
		self.num_trials = num_trials
		self.components = components
		self.rule = rule
		self.results = self.run() # the lengths of each trial

	def run(self):
		data = []
		for t in range(self.num_trials): # go through each trial
			trial = [] # make a new trial
			while not self.rule(trial): # go through each component
				rand = random() # make a random number

				# find out which value the random number corresponds to
				chance = 0
				for k in self.components:
					chance += self.components[k]
					if rand < chance:
						value = k
						break

				trial.append(k)

			data.append(len(trial))

		return data

	def average(self):
		return sum(self.results)/self.num_trials


def p15(n):
	rule = lambda t: t.count(2) > 50
	election_sim = Simulation(n, {1: 0.55, 2: 0.45}, 100, rule)
	return election_sim.chance()

def p16(n):

	def rule(t):
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

	deck = {'spades': 13, 'clubs': 13, 'hearts': 13, 'diamonds': 13}

	cards_sim = Simulation_Marbles(n, deck, 5, rule)
	return {2: cards_sim.chance(2), 3: cards_sim.chance(3)}

def p17(n):
	rule = lambda t: 'Lebron James' in t and 'Danica Patrick' in t and 'Dustin Johnson' in t
	cereal_sim = Simulation(n, {'Lebron James': .2, 'Danica Patrick': .3, 'Dustin Johnson': .6}, 5, rule)
	return cereal_sim.chance()

def p18(n):
	rule = lambda t: 'Lebron James' in t
	cereal_sim = Simulation_N(n, {'Lebron James': .2, 'Danica Patrick': .3, 'Dustin Johnson': .6}, rule)
	return cereal_sim.average()

def p19(n):
	rule = lambda t: not False in t
	quiz_sim = Simulation(n, {True: .8, False: .2}, 6, rule)
	return quiz_sim.chance()

def p20(n):
	rule = lambda t: not False in t
	quiz_sim = Simulation(n, {True: .25, False: .75}, 6, rule)
	return quiz_sim.chance()

print(p17(1000))