import os
import time
import tkinter as tk
from playsound import playsound


root=tk.Tk()
root.title('Productivity Bitch')

root.geometry("400x70")

num_var=tk.StringVar()

def submit(s):
	def countdown(min,sec):
		if (min+sec) == 0 :
			if s == 'shut':
				print('shut')
				os.system("shutdown /s /t 1")
			if s == 'sign':
				print('sign')
				os.system("shutdown -l")			
		label['text'] = f'{min} : {sec}'
		if min<1:
			if sec < 5:
				playsound('C:/Users/RAXXS/Music/beep-07a.wav')
			if sec < 30:
				root2.deiconify()
		if sec==0:  
			if (min+sec) !=0:
				min=min-1
				sec=60
		if (min+sec) > 0:
			root2.after(1000, countdown, min,sec-1)

	if s=='yes':
		countdown(0,0)

	warning.grid(row=0,column=2)
	num=num_var.get()
	if int(num)<3:
		warning['text'] = 'Time must be greater than 3 min'
		root.geometry("500x50")
		submit('d')
	root.destroy()
	time.sleep((int(num)-3)*60)
 
	root2 = tk.Tk()
	root2.title('💀')
	root2.config(bg='Black')
	root2.geometry('200x125')
	label = tk.Label(root2,bg='Black',fg='White',font=('calibre',50))
	label.pack()
 
	countdown(3,0)
	root2.mainloop()
	countdown(0,0)
	
	# root2.update_idletasks()
	# root2.update()
	# pdb.set_trace()

	# exit()


num_label = tk.Label(root, text = 'Time Intent(min):   ', font=('calibre',10, 'bold'))

num_entry = tk.Entry(root,textvariable = num_var, font=('calibre',10,'normal'))
num_entry.focus()
warning = tk.Label( text = '',font=('calibre',10, 'bold'))
# root.bind('<Return>',submit)
B1 = tk.Button(root,text='Sign out',command=lambda: submit('sign'))
B2 = tk.Button(root,text='Shutdown',command=lambda: submit('shut'))

B1.grid(row=1,column=1,pady=4)
B2.grid(row=1,column=2,pady=4)
num_label.grid(row=0,column=0,pady=2)
num_entry.grid(row=0,column=1,pady=2)
root.deiconify()
root.mainloop()
submit('yes')
