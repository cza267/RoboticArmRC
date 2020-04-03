import tkinter as tk

window = tk.Tk()
window.title("Robotic Arm RC")

'''     LEFT RIGHT BUTTON       '''

labelARM_LR=tk.Label(window,background="light steel blue",font=('System',10),text ="ARM RIGHT-LEFT") #Text above L/R box
labelARM_LR.place(x=70,y=0)                                                                          #Location in GUI screen where (0,0) is upper left most corner.
labelARM_UD=tk.Label(window, background="light steel blue", font=('System',10),text="ARM UP-DOWN")   #Text above L/R box
labelARM_UD.place(x=280, y=0)                                                                        #Location in GUI screen where (0,0) is upper left most corner.                                                             

buttonLeftMove=tk.Button(window,bd=3,text="Arm-Left")                                                #Button for Left
buttonLeftMove.bind('<Button-1>', lambda event, arg=1:callback(0,1))                                 #Allows for Left mouse click button to activate the function
buttonLeftMove.place(x=40,y=50) 

buttonRightMove=tk.Button(window,bd=3,text="Arm-Right")
buttonRightMove.bind('<Button-1>', lambda event, arg=1:callback(0,1))
buttonRightMove.place(x=140,y=50) 

textBoxLR=tk.Text(window, height=1, width=3,bd=2)
textBoxLR.place(x=110,y=22)
textBoxLR.insert(tk.INSERT,0)

'''     UP DOWN BUTTON       '''
buttonUpMove=tk.Button(window,bd=3,text="Arm Up")
buttonUpMove.bind('<Button-1>',lambda event,arg=1:callback(0,2))
buttonUpMove.place(x=310,y=50)

buttonDownMove=tk.Button(window,bd=3,text="Arm Down")
buttonDownMove.bind('<Button-1>',lambda event, arg=1:callback(0,-2))
buttonDownMove.place(x=300,y=90)

textBoxUD=tk.Text(window, height=1, width=3,bd=2)
textBoxUD.place(x=320,y=22)
textBoxUD.insert(tk.INSERT,0)

'''      RESET, AUTO, RANDOM       '''
labelMode=tk.Label(window,background="light steel blue", font=('System',10),text="MODE")
labelMode.place(x=205,y=109)

buttonArmReset=tk.Button(window,bd=3,text="Reset Arm")
buttonArmReset.bind('<Button-1>',lambda event, arg=1:callback(0,3))
buttonArmReset.place(x=190,y=240)

buttonArmAuto=tk.Button(window,bd=3,text="Auto Sweep")
buttonArmAuto.bind('<Button-1>',lambda event, arg=1:callback(0,4))
buttonArmAuto.place(x=190,y=160)

buttonArmAuto=tk.Button(window,bd=3,text="Random Scan")
buttonArmAuto.bind('<Button-1>',lambda event, arg=1:callback(0,5))
buttonArmAuto.place(x=185,y=200)












window.mainloop()