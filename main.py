# Imports for PyQt
import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QMessageBox

# Main window made in Designer
from UI.main_window import Ui_MainWindow

# Imports for research
from research import ScatterSimulation
import math

class Main(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)

		# Set up the user interface from Designer
		self.mainWindow = Ui_MainWindow()
		self.mainWindow.setupUi(self)

		# Change the ui
		self.setDefaultValues()
		self.setEvents()

		self.show()

	def setDefaultValues(self):
		# TODO: Make this read from a file
		self.mainWindow.gasJetDiameter.setText("1e-3")
		self.mainWindow.gasJetIntersectionDistance.setText("1e-2")

		self.mainWindow.electronBeamDiameter.setText("1e-3")
		self.mainWindow.electronsCount.setText("1e5")

		self.mainWindow.laserBeamDiameter.setText("1e-2")
		self.mainWindow.laserBeamIntersectionDistance.setText("0.13875")
		self.mainWindow.laserBeamApexLength.setText("15e-2")
		self.mainWindow.laserBeamWavelength.setText("1.064")
		self.mainWindow.laserBeamElectronEnergy.setText("100")
		self.mainWindow.laserBeamPower.setText("2e6")

	def setEvents(self):
		self.mainWindow.graphBins.clicked.connect(self.displayGraph)
		self.mainWindow.graphIntegrals.clicked.connect(self.displayPolarizationAngleVersusIntegral)

	def displayGraph(self):
		scatterSimulation = self.configureScatterSimulation(ScatterSimulation())
		if scatterSimulation is False: return

		scatterSimulation.run()

		print ''.join(['-'] * 30)
		scatterSimulation.printBins()
		print ''.join(['-'] * 30)

		scatterSimulation.plotBins()

	def displayPolarizationAngleVersusIntegral(self, startX = False, stopX = False):
		# TODO: Retrieve this from input
		startX, stopX = -1.42, -0.92

		print "----------Laser Off:----------"
		print "Integral, Error"
		laserOffSimulation = self.configureScatterSimulation(ScatterSimulation())
		if laserOffSimulation is False: return
		laserOffSimulation.laserBeamRadius = 0

		laserOffSimulation.run()

		# Computing integral for when the beam is off...   0: 84877574
		# 11178736.5941
		theoreticalRatioInIntersection = 84877574 / float(10**8)
		calculatedRatioInIntersection = sum(laserOffSimulation.getBins().values()) / laserOffSimulation.electronsCount
		scale = theoreticalRatioInIntersection / calculatedRatioInIntersection

		# TODO: Fix errors.  They are not being computed correctly.
		laserOffIntegral = laserOffSimulation.sumBins(startX, stopX, scale)
		laserOffError = 0
		laserOffP = laserOffIntegral / laserOffSimulation.sumBins(scale = scale)
		print laserOffIntegral, laserOffError
		laserOnSimulation = self.configureScatterSimulation(ScatterSimulation())
		if laserOnSimulation is False: return

		integrals = []
		errors = []
		polarizationAngles = range(0, 91)

		print
		print "----------Laser On:----------"
		print "Angle, Integral, Error, n, p, n * p"
		for polarizationAngle in polarizationAngles:
			laserOnSimulation.laserBeamPolarizationAngleInDegrees = polarizationAngle

			print polarizationAngle,
			laserOnSimulation.run()

			binsIntegral = laserOnSimulation.sumBins(startX, stopX)
			# binsIntegral = laserOnSimulation.sumBins(startX, stopX, includeUnaffected = False)
			integral = binsIntegral - laserOffIntegral
			integrals.append(integral)

			n = laserOnSimulation.affectedByLaserCount
			p = laserOnSimulation.sumBins(startX, stopX, includeUnaffected = False) / laserOnSimulation.affectedByLaserCount
			# p = binsIntegral / laserOnSimulation.affectedByLaserCount

			errors.append(math.sqrt(n * p * (1 - p)))

			print integral, errors[-1], n, p, n * p

			laserOnSimulation.reset()

		import numpy
		import matplotlib.pyplot
		figure = matplotlib.pyplot.figure()
		axii = figure.add_subplot(111)
		# axii.scatter(polarizationAngles, integrals, marker="o")
		axii.errorbar(polarizationAngles, integrals, errors)
		axii.set_xbound(0, 90)
		axii.set_xlabel("Polarization Angle (Degrees)")
		axii.set_ylabel("Integral")
		matplotlib.pyplot.show()

	def configureScatterSimulation(self, scatterSimulation):
		"""Configures the scatter simulation based on the GUI input"""
		try:
			scatterSimulation.gasJetRadius = self.__getNumericFieldValue("gasJetDiameter") / 2.0
			scatterSimulation.gasJetIntersectionDistance = self.__getNumericFieldValue("gasJetIntersectionDistance")
			scatterSimulation.gasJetCosineSquaredDistribution = self.mainWindow.gasJetCosineSquaredDistribution.isChecked()

			scatterSimulation.electronBeamRadius = self.__getNumericFieldValue("electronBeamDiameter") / 2.0
			scatterSimulation.electronsCount = self.__getNumericFieldValue("electronsCount")

			scatterSimulation.laserBeamRadius = self.__getNumericFieldValue("laserBeamDiameter") / 2.0
			scatterSimulation.laserBeamIntersectionDistance = self.__getNumericFieldValue("laserBeamIntersectionDistance")
			scatterSimulation.laserBeamApexLength = self.__getNumericFieldValue("laserBeamApexLength")
			scatterSimulation.laserBeamWavelength = self.__getNumericFieldValue("laserBeamWavelength")
			scatterSimulation.laserBeamElectronEnergy = self.__getNumericFieldValue("laserBeamElectronEnergy")
			scatterSimulation.laserBeamPower = self.__getNumericFieldValue("laserBeamPower")
			scatterSimulation.laserBeamGaussianDistribution = self.mainWindow.laserBeamGaussianDistribution.isChecked()
		except ValueError as exception:
			errorMessage = QMessageBox.critical(self, "Input Error", ('Could not understand the value of the field "%s".\n\nPlease make sure that it\'s a number.' % exception.fieldName))
			return False

		# These are not implemented yet
		scatterSimulation.horizontalAngleInDegrees = 90
		scatterSimulation.maximumBoundLength = 1e10
		scatterSimulation.laserBeamPolarizationAngleInDegrees = 0

		return scatterSimulation

	def __getNumericFieldValue(self, fieldName):
		""" Tries to get the value of fieldName and convert it to a float.  Returns ValueError on failure. """
		try:
			textInBox = vars(self.mainWindow)[fieldName].text()
			numericConversion = float(textInBox)
			return numericConversion
		except ValueError as exception:
			exception.fieldName = fieldName
			raise exception

# Create the UI
app = QtGui.QApplication(sys.argv)
main = Main()
sys.exit(app.exec_())