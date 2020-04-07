import tkinter as tk

window = tk.Tk()
window.title("Robotic Arm RC")

'''     LEFT RIGHT BUTTON       '''  ## calback() is a function that runs thru the matrix or data arra for info of x y z dimensions

labelARM_LR=tk.Label(window, font=('System',10),text ="ARM RIGHT-LEFT") #Text above L/R box
labelARM_LR.place(x=70,y=0)                                                                          #Location in GUI screen where (0,0) is upper left most corner.
labelARM_UD=tk.Label(window, font=('System',10),text="ARM UP-DOWN")   #Text above L/R box
labelARM_UD.place(x=280, y=0)                                                                        #Location in GUI screen where (0,0) is upper left most corner.                                                             

buttonLeftMove=tk.Button(window,bd=3,text="Arm-Left")                                                #Button for Left
#buttonLeftMove.bind('<Button-1>', lambda event, arg=1:callback(0,1))                                 #Allows for Left mouse click button to activate the function
buttonLeftMove.place(x=40,y=50) 

buttonRightMove=tk.Button(window,bd=3,text="Arm-Right")
buttonRightMove.place(x=140,y=50) 

textBoxLR=tk.Text(window, height=1, width=3,bd=2)
textBoxLR.place(x=110,y=22)
textBoxLR.insert(tk.INSERT,0)

'''     UP DOWN BUTTON       '''
buttonUpMove=tk.Button(window,bd=3,text="Arm Up")
buttonUpMove.place(x=310,y=50)

buttonDownMove=tk.Button(window,bd=3,text="Arm Down")
buttonDownMove.place(x=300,y=90)

textBoxUD=tk.Text(window, height=1, width=3,bd=2)
textBoxUD.place(x=320,y=22)
textBoxUD.insert(tk.INSERT,0)

'''      RESET, AUTO, RANDOM       '''
labelMode=tk.Label(window, font=('System',10),text="MODE")
labelMode.place(x=205,y=109)

buttonArmReset=tk.Button(window,bd=3,text="Reset Arm")
buttonArmReset.place(x=190,y=240)

buttonArmAuto=tk.Button(window,bd=3,text="Auto Sweep")
buttonArmAuto.place(x=190,y=160)

buttonArmAuto=tk.Button(window,bd=3,text="Random Scan")
buttonArmAuto.place(x=185,y=200)

textOnOff= tk.Text(window, height=1, width =3, bd=2)
textOnOff.place(x=210,y =130)
textOnOff.insert(tk.INSERT,'OFF')

'''     DEGREE SELECTION    '''
buttonRadioLabel= tk.Label (window, font=("System,10",10), text = "DEGREE\nSELECTION")
buttonRadioLabel.place(x=300,y=165)

buttonRadio5=tk.Radiobutton(window,value=5,text = "5 deg")
buttonRadio5.place(x=305,y=200)

buttonRadio10=tk.Radiobutton(window, value=10,text = " 10 deg")
buttonRadio10.place(x=305,y=225)

buttonRadio15=tk.Radiobutton(window, value=15,text = " 15 deg")
buttonRadio15.place(x=305,y=250)


'''   ARM DEGREES  '''
labelArm=tk.Label(window, font=("System", 10), text= "ARM\nDegrees")
labelArm.place(x=100, y=120)

labelBase=tk.Label(window,text="Base")
labelBase.place(x=40,y=160)
textBox90=tk.Text(window, height=1, width=3, bd=2)
textBox90.place(x=120, y=160)
textBox90.insert(tk.INSERT,'90')

labelShoulder=tk.Label(window,text="Shoulder")
labelShoulder.place(x=40,y=190)
textBox165=tk.Text(window, height=1, width=3, bd=2)
textBox165.place(x=120, y=190)
textBox165.insert(tk.INSERT,'165')

labelElbow=tk.Label(window,text="Elbow")
labelElbow.place(x=40,y=220)
textBox0=tk.Text(window, height=1, width=3, bd=2)
textBox0.place(x=120, y=220)
textBox0.insert(tk.INSERT,'0')

labelWrist=tk.Label(window,text="Wrist")
labelWrist.place(x=40,y=250)
textBox0=tk.Text(window, height=1, width=3, bd=2)
textBox0.place(x=120, y=250)
textBox0.insert(tk.INSERT,'0')

window.mainloop()