from random import random, randint

class Simulation:

	def __init__(self, num_trials, components, num_components, response):
		""" takes parameters num_trials - the number of trials to be conducted
		components - a dictionary of the components and the chances of them, for example {1: .55, 2: .45}
		num_components - the number of components in one trial
		response - evaluation function that returns True or False
		"""
		self.num_trials = num_trials
		self.components = components
		self.num_components = num_components
		self.response = response
		self.results = self.run()

	def run(self):
		""" run the simulation, return the data"""
		data = []
		for t in range(self.num_trials): # go through each trial
			trial = [] # make a new trial
			for c in range(self.num_components): # go through each component
				component = random() # make a random number

				# find out which value the random number corresponds to
				chance = 0
				for k in self.components:
					chance += self.components[k]
					if component < chance:
						value = k
						break

				trial.append(k)

			data.append(self.response(trial))

		return data

	def statistic(self, component=True):
		""" return the chance of a success or failure, takes component, which is true or false """
		return self.results.count(component)/self.num_trials

class Simulation_Marbles(Simulation):

	""" components should be the number of each one instead of the percentages, like {'red': 4, 'blue': 8} """

	def run(self):
		data = []
		for t in range(self.num_trials): # go through each trial
			trial = [] # make a new trial
			for c in range(self.num_components): # go through each component
				component = randint(1, sum(self.components.values())) # make a random number

				# find out which value the random number corresponds to
				chance = 0
				for k in self.components:
					chance += self.components[k]
					if component < chance:
						value = k
						break

				trial.append(k)

			data.append(self.response(trial))

		return data

class Simulation_N(Simulation):

	""" a simulation to determine the number of components necessary to make the response true """

	def __init__(self, num_trials, components, stop):
		""" no num_components"""
		self.num_trials = num_trials
		self.components = components
		self.stop = stop
		self.results = self.run() # the lengths of each trial

	def run(self):
		data = []
		for t in range(self.num_trials): # go through each trial
			trial = [] # make a new trial
			while not self.stop(trial): # go through each component
				component = random() # make a random number

				# find out which value the random number corresponds to
				chance = 0
				for k in self.components:
					chance += self.components[k]
					if component < chance:
						value = k
						break

				trial.append(k)

			data.append(len(trial))

		return data

	def statistic(self):
		return sum(self.results)/self.num_trials
