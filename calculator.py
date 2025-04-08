# Program to create a calculator 

import kivy 
from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Config.set('graphics', 'resizable', 1)


# Creating Layout class
class CalcGridLayout(GridLayout):

	# Function called when equals is pressed
	def calculate(self, calculation):
		if not calculation:
			self.display.text = "Error"
			return
		try:
			result = eval(calculation)
			# Convert result to int if it is a whole number (i.e., no decimal part)
			if isinstance(result, float) and result.is_integer():
				result = int(result)
			self.display.text = str(result)
		except Exception:
			self.display.text = "Error"

	# def calculate(self, calculation):
	# 	if calculation:
	# 		try:
	# 			self.display.text = str(eval(calculation))
	# 		except Exception:
	# 			self.display.text = "Error"

# Creating App class
class CalculatorApp(App):

	def build(self):
		return CalcGridLayout()

# creating object and running it 
if __name__ == '__main__':
    calcApp = CalculatorApp()
    calcApp.run()
