# Imports for PyQt
import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QMessageBox

# Main window made in Designer
from UI.main_window import Ui_MainWindow

# Dialogs
from bins import BinsDialog

# Imports for research
from research import ScatterSimulation
import math

class Main(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)

		# Set up the user interface from Designer
		self.mainWindow = Ui_MainWindow()

		# Set it up
		self.mainWindow.setupUi(self)

		# Change the ui
		self.setDefaultValues()
		self.setEvents()

		self.show()

	def setDefaultValues(self):
		############################
		# MAKE THIS READ FROM FILE
		############################
		self.mainWindow.gasJetDiameter.setText("1e-3")

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
		# RETRIEVE THIS FROM INPUT
		startX, stopX = -1.42, -0.92

		print "Computing integral for when the beam is off...",
		laserOffSimulation = self.configureScatterSimulation(ScatterSimulation())
		if laserOffSimulation is False: return
		laserOffSimulation.laserBeamRadius = 0

		laserOffSimulation.run()

		# Computing integral for when the beam is off...   0: 84877574
		# 11178736.5941
		theoreticalRatioInIntersection = 84877574 / float(10**8)
		calculatedRatioInIntersection = sum(laserOffSimulation.getBins().values()) / laserOffSimulation.electronsCount
		scale = theoreticalRatioInIntersection / calculatedRatioInIntersection

		laserOffIntegral = laserOffSimulation.integrateBins(startX, stopX, scale)
		laserOffError = 0 # math.sqrt(sum(laserOffSimulation.getBins()))
		print laserOffIntegral

		laserOnSimulation = self.configureScatterSimulation(ScatterSimulation())
		if laserOnSimulation is False: return

		integrals = []
		errors = []
		polarizationAngles = range(0, 91)

		for polarizationAngle in polarizationAngles:
			laserOnSimulation.laserBeamPolarizationAngleInDegrees = polarizationAngle

			# print "Computing integral for polarization angle %s degrees..." % polarizationAngle,
			print polarizationAngle,
			laserOnSimulation.run()

			binsIntegral = laserOnSimulation.integrateBins(startX, stopX)
			integral = binsIntegral - laserOffIntegral
			integrals.append(integral)

			laserOnError = math.sqrt(binsIntegral)
			errors.append(math.sqrt(laserOffError ** 2 + laserOnError ** 2))

			print integral, errors[-1]

			laserOnSimulation.resetBins()

		print "Integrals:"
		print integrals

		print "Errors:"
		print errors

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
		try:
			scatterSimulation.gasJetRadius = self.__getNumericFieldValue("gasJetDiameter") / 2.0

			scatterSimulation.electronBeamRadius = self.__getNumericFieldValue("electronBeamDiameter") / 2.0
			scatterSimulation.electronsCount = self.__getNumericFieldValue("electronsCount")

			scatterSimulation.laserBeamRadius = self.__getNumericFieldValue("laserBeamDiameter") / 2.0
			scatterSimulation.laserBeamIntersectionDistance = self.__getNumericFieldValue("laserBeamIntersectionDistance")
			scatterSimulation.laserBeamApexLength = self.__getNumericFieldValue("laserBeamApexLength")
			scatterSimulation.laserBeamWavelength = self.__getNumericFieldValue("laserBeamWavelength")
			scatterSimulation.laserBeamElectronEnergy = self.__getNumericFieldValue("laserBeamElectronEnergy")
			scatterSimulation.laserBeamPower = self.__getNumericFieldValue("laserBeamPower")
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