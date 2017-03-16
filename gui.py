from Tkinter import *
from tkFileDialog import *

class App:
	def __init__(self, master):
		master.title("CS 480 Application")

		frame = Frame(master)
		frame.pack()

		self.label = Label(frame, text="DDOS Detector", font=("Helvetica", 22),pady=20)
		self.label.pack()

		self.uploadButton = Button(master, text="upload", command=self.loadFile)
		self.uploadButton.pack()


	def say_hi(self):
		print "hi there, everyone !"
	def uploadcall(self):
		print "this is the upload call !"
	def loadFile(self):
		self.options = {}
		self.options['filetypes'] = [('all files', '.*')]
		self.options['initialdir'] = [('/home/cristian/Documents/Development/CS480_Project/Python_Project/')]

		filename = askopenfilename(**self.options)

		if filename:
			print filename
			return open(filename, 'w')


root = Tk()
root.geometry("750x525")
app = App(root)

root.mainloop()
root.destroy()