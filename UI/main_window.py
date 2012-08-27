# This file is part of Monte Carlo Simulations of Electron Scattering Experiments.

# Monte Carlo Simulations of Electron Scattering Experiments is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Monte Carlo Simulations of Electron Scattering Experiments is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Monte Carlo Simulations of Electron Scattering Experiments.  If not, see <http://www.gnu.org/licenses/>.


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Tue Apr 03 12:26:14 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(302, 504)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayout_4 = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.gasJetDiameter = QtGui.QLineEdit(self.groupBox_2)
        self.gasJetDiameter.setObjectName(_fromUtf8("gasJetDiameter"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.gasJetDiameter)
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_11)
        self.gasJetCosineSquaredDistribution = QtGui.QCheckBox(self.groupBox_2)
        self.gasJetCosineSquaredDistribution.setText(_fromUtf8(""))
        self.gasJetCosineSquaredDistribution.setObjectName(_fromUtf8("gasJetCosineSquaredDistribution"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.gasJetCosineSquaredDistribution)
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_12)
        self.gasJetIntersectionDistance = QtGui.QLineEdit(self.groupBox_2)
        self.gasJetIntersectionDistance.setObjectName(_fromUtf8("gasJetIntersectionDistance"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.gasJetIntersectionDistance)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout_3 = QtGui.QFormLayout(self.groupBox)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label)
        self.electronBeamDiameter = QtGui.QLineEdit(self.groupBox)
        self.electronBeamDiameter.setObjectName(_fromUtf8("electronBeamDiameter"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.electronBeamDiameter)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_2)
        self.electronsCount = QtGui.QLineEdit(self.groupBox)
        self.electronsCount.setObjectName(_fromUtf8("electronsCount"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.electronsCount)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.formLayout_5 = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout_5.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.laserBeamDiameter = QtGui.QLineEdit(self.groupBox_3)
        self.laserBeamDiameter.setObjectName(_fromUtf8("laserBeamDiameter"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.FieldRole, self.laserBeamDiameter)
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.laserBeamIntersectionDistance = QtGui.QLineEdit(self.groupBox_3)
        self.laserBeamIntersectionDistance.setObjectName(_fromUtf8("laserBeamIntersectionDistance"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.FieldRole, self.laserBeamIntersectionDistance)
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_6)
        self.laserBeamApexLength = QtGui.QLineEdit(self.groupBox_3)
        self.laserBeamApexLength.setObjectName(_fromUtf8("laserBeamApexLength"))
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.FieldRole, self.laserBeamApexLength)
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_5.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_7)
        self.laserBeamWavelength = QtGui.QLineEdit(self.groupBox_3)
        self.laserBeamWavelength.setObjectName(_fromUtf8("laserBeamWavelength"))
        self.formLayout_5.setWidget(4, QtGui.QFormLayout.FieldRole, self.laserBeamWavelength)
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_5.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_8)
        self.laserBeamElectronEnergy = QtGui.QLineEdit(self.groupBox_3)
        self.laserBeamElectronEnergy.setObjectName(_fromUtf8("laserBeamElectronEnergy"))
        self.formLayout_5.setWidget(5, QtGui.QFormLayout.FieldRole, self.laserBeamElectronEnergy)
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_5.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_9)
        self.laserBeamPower = QtGui.QLineEdit(self.groupBox_3)
        self.laserBeamPower.setObjectName(_fromUtf8("laserBeamPower"))
        self.formLayout_5.setWidget(6, QtGui.QFormLayout.FieldRole, self.laserBeamPower)
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_5.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_10)
        self.laserBeamGaussianDistribution = QtGui.QCheckBox(self.groupBox_3)
        self.laserBeamGaussianDistribution.setEnabled(True)
        self.laserBeamGaussianDistribution.setText(_fromUtf8(""))
        self.laserBeamGaussianDistribution.setTristate(False)
        self.laserBeamGaussianDistribution.setObjectName(_fromUtf8("laserBeamGaussianDistribution"))
        self.formLayout_5.setWidget(7, QtGui.QFormLayout.FieldRole, self.laserBeamGaussianDistribution)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.graphBins = QtGui.QPushButton(self.centralwidget)
        self.graphBins.setAutoDefault(True)
        self.graphBins.setObjectName(_fromUtf8("graphBins"))
        self.verticalLayout_2.addWidget(self.graphBins)
        self.graphIntegrals = QtGui.QPushButton(self.centralwidget)
        self.graphIntegrals.setObjectName(_fromUtf8("graphIntegrals"))
        self.verticalLayout_2.addWidget(self.graphIntegrals)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 302, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Gas Jet", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Diameter (m):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Cosine-Squared Distribution:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Intersection Distance (m):", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Electron Beam", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Diameter (m):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Number of Electrons:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Laser Beam", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Diameter (m):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Intersection Distance (m):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Focal Length (m):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Wavelength (microns):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Electron Energy (eV):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Power (W):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Gaussian Beam:", None, QtGui.QApplication.UnicodeUTF8))
        self.graphBins.setText(QtGui.QApplication.translate("MainWindow", "Energy Spectrum", None, QtGui.QApplication.UnicodeUTF8))
        self.graphIntegrals.setText(QtGui.QApplication.translate("MainWindow", "Graph Polarization Angles and Integrals", None, QtGui.QApplication.UnicodeUTF8))

