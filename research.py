from __future__ import division
import random, math, csv, scipy.special
import numpy

class ScatterSimulation:
	def __init__(self):
		self.electronBeamRadius = None
		self.laserBeamRadius = None
		self.laserBeamIntersectionDistance = None
		self.laserBeamApexLength = None
		self.gasJetRadius = None
		self.horizontalAngleInDegrees = None
		self.maximumBoundLength = None
		self.laserBeamWavelength = None
		self.laserBeamElectronEnergy = None
		self.laserBeamPower = None
		self.laserBeamPolarizationAngleInDegrees = None
		self.electronsCount = None
		self.displayGraph = False
		self.bins = {0: 0}

	def getIntensity(self, wavelength, fluxDensity, electronEnergy, polarizationAngle = 0):
		"""
			wavelength: microns
			fluxDensity: watts/centimeter^2
			electronEnergy: eV
		"""
		intensitySquared = 4.86 * math.pow(10, -13) * math.pow(wavelength, 4) * fluxDensity * electronEnergy * math.pow(math.cos(polarizationAngle), 2)
		return math.sqrt(intensitySquared)

	def getElectronScatterProbability(self, n, intensity = 0.35):
		if n == 0:
			return math.pow(scipy.special.jn(n, intensity * 2), 2) / 2
		else:
			return math.pow(scipy.special.jn(n, intensity * 2), 2)

	def run(self):
		if self.displayGraph:
			from mpl_toolkits.mplot3d import Axes3D
			import matplotlib.pyplot
			figure = matplotlib.pyplot.figure()
			axii = figure.add_subplot(111, projection="3d")

			completelyIntersectingPoints = []
			partiallyIntersectingPoints = []
			nonintersectingPoints = []

		horizontalAngleInRadians = self.horizontalAngleInDegrees * math.pi / 180
		laserBeamPolarizationAngleInRadians = self.laserBeamPolarizationAngleInDegrees * math.pi / 180

		if self.horizontalAngleInDegrees == 90:
			boundLength = self.electronBeamRadius * 2.0
		else:
			boundLength = (self.electronBeamRadius * 2.0 / math.sin(horizontalAngleInRadians)) + (self.laserBeamRadius * 2.0 / math.tan(horizontalAngleInRadians))

		if boundLength > self.maximumBoundLength:
			boundLength = self.maximumBoundLength

		# # # # # # # # # # electronBeamRadiusSquared = math.pow(electronBeamRadius, 2)
		laserBeamRadiusSquared = math.pow(self.laserBeamRadius, 2)
		gasJetRadiusSquared = math.pow(self.gasJetRadius, 2)

		# In centimeters for the intensity function
		laserBeamCrossSectionalAreaAtBase = math.pi * math.pow(self.laserBeamRadius * 100, 2)

		# xValues = []
		# yValues = []

		electronsCount = self.electronsCount
		while electronsCount > 0:
			electronsCount -= 1

			randomPointInBound = self.getRandomPointInCylinder(self.electronBeamRadius, boundLength)
			rotatedPointInBound = Point((randomPointInBound.coordinates[0], randomPointInBound.coordinates[2])).rotate(horizontalAngleInRadians)

			# Check electron beam intersection with gas jet
			if math.pow(rotatedPointInBound.coordinates[0], 2) + math.pow(rotatedPointInBound.coordinates[1], 2) <= gasJetRadiusSquared:
				# Check electron beam intersection with laser beam
				laserBeamRadiusAtPoint = self.laserBeamRadius / self.laserBeamApexLength * (self.laserBeamApexLength - (self.laserBeamIntersectionDistance + rotatedPointInBound.coordinates[0]))
				laserBeamRadiusSquaredAtPoint = math.pow(laserBeamRadiusAtPoint, 2)
				if math.pow(randomPointInBound.coordinates[1], 2) + math.pow(rotatedPointInBound.coordinates[1], 2) <= laserBeamRadiusSquaredAtPoint:
					# The * 10000 is for converting the area from meters^2 to centimeters^2
					laserBeamCrossSectionalAreaAtPoint = math.pi * laserBeamRadiusSquaredAtPoint * 10000
					laserBeamFluxDensityAtPoint = self.laserBeamPower / laserBeamCrossSectionalAreaAtPoint

					intensity = self.getIntensity(self.laserBeamWavelength, laserBeamFluxDensityAtPoint, self.laserBeamElectronEnergy, laserBeamPolarizationAngleInRadians)
					# xValues.append(rotatedPointInBound.coordinates[0])
					# yValues.append(intensity)
					# print intensity

					randomNumber = random.random()
					binNumber = 0
					while True:
						scatterProbability = self.getElectronScatterProbability(binNumber, intensity)
						if scatterProbability > randomNumber:
							binNumber *= -1
							break
						randomNumber -= scatterProbability

						if scatterProbability > randomNumber:
							break
						randomNumber -= scatterProbability

						binNumber += 1

					if binNumber not in self.bins:
						self.bins[binNumber] = 1
					else:
						self.bins[binNumber] += 1

					if self.displayGraph:
						completelyIntersectingPoints.append((randomPointInBound.coordinates[0], randomPointInBound.coordinates[1], randomPointInBound.coordinates[2]))
				else:
					self.bins[0] += 1

					if self.displayGraph:
						partiallyIntersectingPoints.append((randomPointInBound.coordinates[0], randomPointInBound.coordinates[1], randomPointInBound.coordinates[2]))
			elif self.displayGraph:
				nonintersectingPoints.append((randomPointInBound.coordinates[0], randomPointInBound.coordinates[1], randomPointInBound.coordinates[2]))

		# print max(yValues), min(yValues)
		# import matplotlib.pyplot
		# figure = matplotlib.pyplot.figure()
		# axii = figure.add_subplot(111)
		# axii.scatter(xValues, yValues, marker="o")
		# axii.set_xlabel('x')
		# axii.set_ylabel('Cross Sectional Area')
		# axii.set_ybound(0)
		# matplotlib.pyplot.show()

		if self.displayGraph:
			if (len(completelyIntersectingPoints)):
				xValues, yValues, zValues = zip(*completelyIntersectingPoints)
				axii.scatter(xValues, yValues, zValues, c="g", marker="o")

			if (len(partiallyIntersectingPoints)):
				xValues, yValues, zValues = zip(*partiallyIntersectingPoints)
				axii.scatter(xValues, yValues, zValues, c="y", marker="o")

			if (len(nonintersectingPoints)):
				xValues, yValues, zValues = zip(*nonintersectingPoints)
				axii.scatter(xValues, yValues, zValues, c="r", marker="o")

			axii.set_xlabel('X')
			axii.set_ylabel('Y')
			axii.set_zlabel('Z')
			matplotlib.pyplot.show()

	def getBins(self):
		return self.bins

	def resetBins(self):
		self.bins = {0: 0}

	def getRandomPoint(self, maximums):
		coordinates = []
		for maximum in maximums:
			coordinates.append(random.uniform(0, maximum))

		return Point(coordinates)

	def getRandomPointInCylinder(self, radius, height):
		# Square Root Method
		polarR = math.sqrt(random.uniform(0, math.pow(radius, 2)))
		# polarR = math.sqrt(randomLaser(math.pow(radius, 2), radius/10))
		polarTheta = random.uniform(0, 2 * math.pi)

		if height == False:
			return Point((polarR * math.cos(polarTheta), polarR * math.sin(polarTheta)))
		else:
			halfHeight = height / 2
			return Point((random.uniform(-halfHeight, halfHeight), polarR * math.cos(polarTheta), polarR * math.sin(polarTheta)))

		# Square Method
		pointInCircle = Point((random.uniform(-radius, radius), random.uniform(-radius, radius)))
		while pointInCircle.distanceTo(Point((0, 0))) > radius:
			pointInCircle = getRandomPoint((random.uniform(-radius, radius), random.uniform(-radius, radius)))

		polarR = math.sqrt(random.uniform(0, math.pow(radius, 2)))
		polarTheta = random.uniform(0, 2 * math.pi)
		return Point((random.uniform(-halfHeight, halfHeight), pointInCircle.coordinates[1], pointInCircle.coordinates[0]))

	def randomLaser(self, max, sigma):
		mu = 0

		number = random.gauss(mu, sigma)

		while math.fabs(number) > max:
			number = random.gauss(mu, sigma)

		return number

	def printBins(self):
		for binNumber, binCount in sorted(self.bins.iteritems()):
			print str(binNumber).rjust(3) +": "+ str(binCount)

	def binsToPoints(self):
		yBaseValues = []
		with open("values.csv", "rb") as csvFile:
			csvReader = csv.reader(csvFile, quoting=csv.QUOTE_NONNUMERIC)
			for (x, y) in csvReader:
				yBaseValues.append(y)

		binNumbers = self.bins.keys()
		lowestBin = min(binNumbers)
		highestBin = max(binNumbers)

		xValues = [round(x * 0.01, 2) for x in range(-1000 + (117 * lowestBin), 1001 + (117 * highestBin))]
		xZeroIndex = 1000 - (117 * lowestBin)
		yValues = [0] * len(xValues)

		for (binNumber, binCount) in self.bins.iteritems():
			xOffset = 117 * binNumber
			for (baseIndex, index) in zip(xrange(0, 2001), xrange(xZeroIndex - 1000 + xOffset, xZeroIndex + 1001 + xOffset)):
				yValues[index] += yBaseValues[baseIndex] * binCount

		return (xValues, yValues)

	def plotBins(self):
		xValues, yValues = self.binsToPoints()

		binNumbers = self.bins.keys()
		lowestBin = min(binNumbers)
		highestBin = max(binNumbers)

		import matplotlib.pyplot
		figure = matplotlib.pyplot.figure()
		axii = figure.add_subplot(111)
		axii.scatter(xValues, yValues, marker="x")
		axii.set_xlabel('Energy')
		axii.set_ylabel('Count')
		axii.set_xbound(-3.0 + (1.17 * -max([lowestBin * -1, highestBin])), 3.0 + (1.17 * max([lowestBin * -1, highestBin])))
		axii.set_ybound(0)
		axii.set_xticks([1.17 * bin for bin in xrange(-max([lowestBin * -1, highestBin]), max([lowestBin * -1, highestBin]) + 1)])
		matplotlib.pyplot.show()

	def _integratePoints(self, xValues, yValues, startX = False, stopX = False):
		"""Approximates an integral using the trapezoid rule"""
		sum = 0.0
		for i in xrange(1, len(xValues)):
			if startX is not False and xValues[i - 1] < startX:
				continue
			if stopX is not False and xValues[i] > stopX:
				break

			sum += (yValues[i] + yValues[i - 1]) / 2 * (xValues[i] - xValues[i - 1])

		return sum

	def _sumPoints(self, xValues, yValues, startX = False, stopX = False):
		"""Approximates an integral using the trapezoid rule"""
		sum = 0.0
		for i in xrange(0, len(xValues)):
			if startX is not False and xValues[i] < startX:
				continue
			if stopX is not False and xValues[i] > stopX:
				break

			sum += yValues[i]

		return sum

	def integrateBins(self, startX = False, stopX = False, scale = 1):
		xValues, yValues = self.binsToPoints()

		if not scale == 1:
			yValues = [y * scale for y in yValues]

		return self._integratePoints(xValues, yValues, startX, stopX)

	def sumBins(self, startX = False, stopX = False, scale = 1):
		xValues, yValues = self.binsToPoints()

		if not scale == 1:
			yValues = [y * scale for y in yValues]

		return self._sumPoints(xValues, yValues, startX, stopX)

class Point:
	coordinates = []
	dimensions = 0

	def __init__(self, coordinates):
		self.coordinates = coordinates
		self.dimensions = len(coordinates)

	def distanceTo(self, otherPoint):
		dimensions = min(self.dimensions, otherPoint.dimensions)
		components = []
		for i in range(dimensions):
			components.append(math.pow(self.coordinates[i] - otherPoint.coordinates[i], 2))

		return math.sqrt(sum(components))

	def rotate(self, angleInRadians):
		# Only programmed for 2 dimensions right now
		if (len(self.coordinates) != 2): return False

		x = self.coordinates[0] * math.cos(angleInRadians) - self.coordinates[1] * math.sin(angleInRadians)
		y = self.coordinates[0] * math.sin(angleInRadians) + self.coordinates[1] * math.cos(angleInRadians)

		return Point((x,y))

""" Create text based (not python based) input file """