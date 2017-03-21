from Tkinter import *
from tkFileDialog import *
import app
import testgui

class Application:
	def __init__(self, master):
		master.title("CS 480 Application")
		# Frame.__init__(self, master)
		self.frame = Frame(master)
		self.frame.pack()

		# self.quitbutton = Button(text='Quit', command=self.frame.quit, fg="red")
		# self.quitbutton.pack(side=TOP)

		self.label = Label(self.frame, text="DOS Scanner", font=("Helvetica", 22),pady=20)
		self.label.pack()

		self.photo = PhotoImage(file="Images/bomb.png")
		self.w = Label(self.frame, image=self.photo)
		self.w.photo = self.photo
		self.w.pack()

		self.uploadButton = Button(self.frame, text="upload", command=self.getfilepath)
		self.uploadButton.pack()

		self.uploadlabel = Label(self.frame, text="Upload File To Scan", font=("Helvetica", 9), pady=5)
		self.uploadlabel.pack()


	def say_hi(self):
		print "hi there, everyone !"
	def uploadcall(self):
		print "this is the upload call !"
	def completescan(self):
		self.completelabel = Label(self.frame, text="scan complete !", font=("Helvetica", 9))
		self.completelabel.pack()

	def getfilepath(self):
		self.options = {}
		self.options['filetypes'] = [('all files', '.*')]
		self.options['initialdir'] = [('/home/cristian/Documents/Development/CS480_Project/Python_Project/')]
		filename = askopenfilename(**self.options)

		if filename:
			app.main(filename)
			self.completescan()
			# self.windowresults()
			testgui.run()
			return filename

	def windowresults(self):
		self.top = Toplevel(self.frame)
		self.top.geometry("900x650")
		self.top.title('Scanned Results')

		self.listbox = Listbox(self.frame, selectmode=SINGLE)
		self.listbox.config(width=30)

		self.quitbutton = Button(self.top, text="Dismiss", command=self.top.destroy)
		self.quitbutton.pack()

root = Tk()
root.geometry("750x525")
application = Application(root)
root.mainloop()
# root.destroy()