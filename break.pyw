import os
import time
import tkinter as tk
from playsound import playsound


root=tk.Tk()
root.title('Productivity Bitch')

root.geometry("400x75")

num_var=tk.StringVar()

def submit(s):

	num=num_var.get()
 
	root2 = tk.Tk()
	root2.title('💀')
	root2.config(bg='Black')
	root2.geometry('300x150')
	label = tk.Label(root2,bg='Black',fg='White',font=('calibre',50),pady=20)
	label.pack()
 
	def countdown(min,sec):
		if (min+sec) == 0 :
			if s == 'shut':
				os.system("shutdown /s /t 1")
			if s == 'sign':
				os.system("shutdown -l")			
		label['text'] = f'{min} : {sec}'
		if min<1:
			if sec < 30:
				root2.attributes('-topmost',True)
				playsound('C:/windows_usage_limiter/beep-07a.wav')
				root2.deiconify()
		if sec==0:  
			if (min+sec) !=0:
				min=min-1
				sec=60
		if (min+sec) > 0:
			root2.after(1000, countdown, min,sec-1)

	root.destroy()
	
	countdown(int(num),0)
	root2.mainloop()
	countdown(0,0)
	
	# root2.update_idletasks()
	# root2.update()
	# pdb.set_trace()

	# exit()


num_label = tk.Label(root, text = 'Time Intent(min):   ', font=('calibre',10, 'bold'))

num_entry = tk.Entry(root,textvariable = num_var, font=('calibre',10,'normal'))
num_entry.focus()
B1 = tk.Button(root,text='Sign out',command=lambda: submit('sign'))
B2 = tk.Button(root,text='Shutdown',command=lambda: submit('shut'))

B1.grid(row=1,column=1,pady=4)
B2.grid(row=1,column=2,pady=4)
num_label.grid(row=0,column=0,pady=2)
num_entry.grid(row=0,column=1,pady=2)
root.attributes('-topmost',True)
playsound('C:/windows_usage_limiter/beep-07a.wav')
root.deiconify()
root.mainloop()

