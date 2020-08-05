#######################################
# @date:- 8/5/2020 11:03 PM			  #
# @author:- @Nomz#2168	  (discord)	  #
#######################################


############## IMPORTS #################
from uiSetup import *				   #
from subprocess import check_call	   #
import sys							   #
import hashlib						   #
import pyperclip					   #
########################################


toggle = True

class My_Window(Ui_MainWindow):
############################### MAIN FUNCTIONS #################################
	def __init__(self, window): # Initialize
		self.setupUi(window)
		self.Generate.clicked.connect(self.generate)
		self.HideShow.clicked.connect(self.hideShow)
		self.Copy.clicked.connect(self.copyToClipboard)
		
	def generate(self): # Generate the password
		algorithmInput = self.Algorithms.currentText()
		userInput = self.UserInput.text()
		self.checkIfExist(algorithmInput)
		valueCheck = self.checkIfExist(algorithmInput)
		hexifyBoolean = self.hexify.isChecked()
		hexCheck = False
		if hexifyBoolean:
			hexCheck = True
		else:
			hexCheck = False
			
		if valueCheck is True:
			self.generatePasscode(algorithmInput, userInput, hexCheck)
		
		
	def hideShow(self): # Toggle between showing or hiding the password encryption
		global toggle
		
		if toggle is False:
			toggle = True
			self.HideShow.setIcon(QtGui.QIcon("Assets//EYECLOSE.png"))
			self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
		else:
			toggle = False 
			self.HideShow.setIcon(QtGui.QIcon("Assets//EYEOPEN.png"))
			self.Password.setEchoMode(QtWidgets.QLineEdit.Normal)
			
	def copyToClipboard(self): # Function to copy the password encryption to your clipboard.
		text = self.Password.text()
		pyperclip.copy(text)
##############################################################################
	
############################### SUB FUNCTIONS #################################

	def checkIfExist(self, choice): # @params:- if the choice is available in the supported hashlib algorithms?
		availables = hashlib.algorithms_available
		for v in availables:
			if choice == v:
				return True
				
	def generatePasscode(self, algorithm, userinput, hexCheck): # @params:- Algorithm Type, Input String, is hexify button checked?
		encodedInput = userinput.encode('utf-8')
								
		if algorithm == 'sha256':
			m = hashlib.sha256()
		elif algorithm == 'sha1':
			m = hashlib.sha1()
		elif algorithm == 'sha224':
			m = hashlib.sha224()
		elif algorithm == 'md5':
			m = hashlib.md5()
		elif algorithm == 'sha512':
			m = hashlib.sha512()
		
		m.update(encodedInput)
		if hexCheck:
			hexDigested = m.hexdigest()
			self.Password.setText(hexDigested)
		else:
			digested = m.digest()
			finalText = repr(digested)[2:-1]
			self.Password.setText(finalText)
##############################################################################


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	
	ui = My_Window(MainWindow)
	
	MainWindow.show()
	app.exec_()
