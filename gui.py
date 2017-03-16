from Tkinter import *
from tkFileDialog import *
import app

class Application:
	def __init__(self, master):
		master.title("CS 480 Application")

		frame = Frame(master)
		frame.pack()

		self.label = Label(frame, text="DDOS Detector", font=("Helvetica", 22),pady=20)
		self.label.pack()

		self.uploadButton = Button(master, text="upload", command=self.getfilepath)
		self.uploadButton.pack()


	def say_hi(self):
		print "hi there, everyone !"
	def uploadcall(self):
		print "this is the upload call !"
	def getfilepath(self):
		self.options = {}
		self.options['filetypes'] = [('all files', '.*')]
		self.options['initialdir'] = [('/home/cristian/Documents/Development/CS480_Project/Python_Project/')]
		filename = askopenfilename(**self.options)

		if filename:
			app.main(filename)
			return filename

root = Tk()
root.geometry("750x525")
application = Application(root)
root.mainloop()
root.destroy()