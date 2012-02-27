# Imports for PyQt
import sys
from PyQt4.QtGui import QDialog

# Dialog made in Designer
from UI.bins_dialog import Ui_Dialog

class BinsDialog(QDialog):
	def __init__(self, bins):
		QDialog.__init__(self)
		self.bins = bins

		# Set up the user interface from Designer
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

		self.addBins()
		self.show()

	def addBins(self):
		model = QAbstractItemModel()

		for binNumber, binCount in self.bins.iteritems():
			self.ui.binsTableView.setItem(row)

		self.ui.binsTableView.setItem(row)