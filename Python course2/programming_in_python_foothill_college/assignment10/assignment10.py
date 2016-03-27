""" Assignment #10 Submitted by Ketaki Kekatpure. Course - CS21A

"""

import tkinter

""" 
Sets up a gui that accepts the degrees in fahrenheit and converts it to celsius 
or accepts degree in celsius and converts it to fahrenheit when the appropriate
button is pressed.
"""


class TempConvert(tkinter.Frame):
	def __init__(self):
		tkinter.Frame.__init__(self)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.tempEntry_label = tkinter.Label(text = "Enter degrees in Fahrenheit: ")
		self.tempEntry = tkinter.Entry()
		self.tempEntry.delete(0, tkinter.END)
		self.tempEntry.insert(0, "0")
		self.tempEntry_label.pack(side = tkinter.LEFT)
		self.tempEntry.pack(side = tkinter.LEFT)

		self.celsButton = tkinter.Button(self)
		self.celsButton["text"] = "Convert Fahrenheit to Celsius"
		self.celsButton["command"] = self.convertocelsius
		self.celsButton.pack(side = tkinter.LEFT)
		

		self.displaycelsius = tkinter.Label(self)
		self.displaycelsius.pack(side = tkinter.LEFT)

		self.tempEntry2_label = tkinter.Label(text = "Enter degrees in Celsius: ")
		self.tempEntry2 = tkinter.Entry()
		self.tempEntry2.delete(0, tkinter.END)
		self.tempEntry2.insert(0, "0")
		self.tempEntry2_label.pack(side = tkinter.LEFT)
		self.tempEntry2.pack(side = tkinter.LEFT)

		self.fahrButton = tkinter.Button(self)
		self.fahrButton["text"] = "Convert Celsius to Fahrenheit"
		self.fahrButton["command"] = self.convertofahr
		self.fahrButton.pack(side = tkinter.LEFT)

		self.displayfahr = tkinter.Label(self)
		self.displayfahr.pack(side = tkinter.LEFT)

		self.quitButton = tkinter.Button(self)
		self.quitButton["text"] = "Quit"		
		self.quitButton["command"] = self.quit
		self.quitButton.pack(side = tkinter.LEFT)

	def convertocelsius(self):
		"""
		Accepts degrees in fahrenheit and converts it to celsius.
		"""
		c = float(self.tempEntry.get())
		self.displaycelsius["text"] = "Celsius = ", round(((5/9) * (c -32)), 2)

	def convertofahr(self):
		"""
		Accepts degrees in celsius and converts it to fahrenheit.
		"""
		f = float(self.tempEntry2.get())
		self.displayfahr["text"] = "Fahrenheit = ", round((((9/5)*f)+32), 2)

if __name__ == "__main__":
	root = tkinter.Tk()
	app = TempConvert()
	app.mainloop()
	root.destroy()
