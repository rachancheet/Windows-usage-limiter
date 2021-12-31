import os
import time
import tkinter as tk

countdown_min = 5
countdown_sec = 0

root=tk.Tk()
root.title('Productivity Bitch')

root.geometry("400x50")

num_var=tk.StringVar()

def submit(s):
	def countdown(min,sec):
		label['text'] = f'{min} : {sec}'
		if (min+sec) == 0 :
			root2.destroy()
		if sec==0:  
			if (min+sec) !=0:
				min=min-1
				sec=60
		if (min+sec) > 0:
			root2.after(1000, countdown, min,sec-1)

	warning.grid(row=0,column=2)
	num=num_var.get()
	if int(num)<5:
		warning['text'] = 'Time must be greater than 5 min'
		root.geometry("500x50")
		submit('d')
	root.destroy()
	time.sleep((int(num)-countdown_min)*60)
	root2 = tk.Tk()
	root2.title('💀')
	root2.config(bg='Black')
	root2.geometry('200x125')

	label = tk.Label(root2,bg='Black',fg='White',font=('calibre',50))
	label.pack()
	countdown(countdown_min,countdown_sec)
	root2.mainloop()
	os.system("shutdown /s /t 1")
	exit()


num_label = tk.Label(root, text = 'Time Intent(min):   ', font=('calibre',10, 'bold'))

num_entry = tk.Entry(root,textvariable = num_var, font=('calibre',10,'normal'))
num_entry.focus()
warning = tk.Label( text = '',font=('calibre',10, 'bold'))
root.bind('<Return>',submit)

num_label.grid(row=0,column=0)
num_entry.grid(row=0,column=1)

root.mainloop()


