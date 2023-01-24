# INFO: SRY FOR THE USAGE OF MIXED LANGUAGEs BETWEEN GERMAN AND ENGLISCH
try:
    from tkinter import *
    from tkinter import messagebox
    from tkinter.messagebox import showinfo
    from matplotlib.figure import Figure
    from PIL import ImageTk, Image
    import tkinter as tk
    from tkinter import ttk
    from tkinter import font as tkfont
    from paths import *

    import RechenEngines.ClassTraeger as trGr
    import RechenEngines.ClassZentral as ctr
    import RechenEngines.ClassParallel as parll

except ImportError as e:
    print(e)

# window width and heigth
WIDTH = 1100
HEIGTH = 700

###################################################################################################################################################################################################################################
# class programm for managing frames and classes


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        #tk.Tk.__init__(self, *args, **kwargs)
        super().__init__(*args, **kwargs)

        self.title('Kräfteberechnung Statik')
        self.resizable(width=False, height=False)
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()

        # calculate position
        self.x = (ws/2) - (WIDTH/2)
        self.y = (hs/3) - (HEIGTH/3)
        self.geometry('%dx%d+%d+%d' % (WIDTH, HEIGTH, self.x, self.y))
        self.title_font = tkfont.Font(
            family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        # looping trough classes and assign them as frame
        for F in (startPage, TraegerEins, TraegerZwei, ZentralEins,  ZentralZwei, ParallelEins, ParallelZwei):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        # parent represents a widget to act as the parent of the current object.
        # All widgets in tkinter except the root window require a parent (sometimes also called a master)

        # controller represents some other object that is designed to act as a common point of interaction for several pages of widgets.
        # It is an attempt to decouple the pages. That is to say,
        # each page doesn't need to know about the other pages.
        # If it wants to interact with another page, such as causing it to be visible,
        # it can ask the controller to make it visible.

        iconTmg = PhotoImage(
            file=PATH_1)
        self.iconphoto(False, iconTmg)
        self.show_frame("startPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        # stacking frame on each other, current frame will be visible
        frame.tkraise()

# no space for closing button, therefore handle close event


def on_closing():
    # returns bool wheter to close or not
    if messagebox.askokcancel("Beenden", "Möchten Sie das Programm beenden?"):
        programm.destroy()


#####################################################################################################################################################################################################################
''' 
startPage class designed with canvas 
and added images of team, tgm, etc

'''

# welcoming page


class startPage(tk.Frame, App):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # background on canvas and adding some images
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGTH)
        self.canvas.pack(fill="both", expand=True)
        img = ImageTk.PhotoImage(Image.open(PATH_2).resize(
            (WIDTH, HEIGTH), Image.Resampling.LANCZOS))

        self.canvas.background = img
        bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=img)

        self.startPageTextImg = ImageTk.PhotoImage(
            Image.open(PATH_3))
        startPageImg = self.canvas.create_image(250, 50, image=self.startPageTextImg,
                                                anchor='nw')

        self.logoTgm = ImageTk.PhotoImage(Image.open(PATH_4))
        tgmImg = self.canvas.create_image(50, 20, image=self.logoTgm,
                                          anchor='nw')

        self.auftragTgm = ImageTk.PhotoImage(Image.open(PATH_9))
        auftragImg = self.canvas.create_image(30, 5, image=self.auftragTgm,
                                              anchor='nw')

        self.speedLancerLogo = ImageTk.PhotoImage(Image.open(PATH_5))
        firmalogoImg1 = self.canvas.create_image(830, 10, image=self.speedLancerLogo,
                                                 anchor='nw')

        self.runningMan = ImageTk.PhotoImage(Image.open(PATH_6))
        firmalogoImg2 = self.canvas.create_image(900, 115, image=self.runningMan,
                                                 anchor='nw')

        self.pythonLogo = ImageTk.PhotoImage(Image.open(PATH_7))
        pythonLogoImg = self.canvas.create_image(-185, 450, image=self.pythonLogo,
                                                 anchor='nw')

        self.canvas.create_text(200, 633, text="Python",
                                fill="black", font=('Helvetica 22 bold'))

        self.canvas.create_text(1000, 630, text="Tkinter",
                                fill="black", font=('Helvetica 22 bold'))

        self.Tkinterimg = ImageTk.PhotoImage(Image.open(PATH_8))
        Tkinterimg = self.canvas.create_image(860, 470, image=self.Tkinterimg,
                                              anchor='nw')

        self.programmAuswahlTextImg = ImageTk.PhotoImage(
            Image.open(PATH_13))
        programmAuswahlImg = self.canvas.create_image(315, 480, image=self.programmAuswahlTextImg,
                                                      anchor='nw')

        # member images
        self.roland = ImageTk.PhotoImage(Image.open(PATH_10))
        rolandImg = self.canvas.create_image(250, 180, image=self.roland,
                                             anchor='nw')
        self.canvas.create_text(325, 380, text="Loulengo Roland",
                                fill="black", font=('Helvetica 17 bold'))

        self.malicia = ImageTk.PhotoImage(Image.open(PATH_11))
        maliciaImg = self.canvas.create_image(500, 200, image=self.malicia,
                                              anchor='nw')
        self.canvas.create_text(550, 380, text="Luinovic Malica",
                                fill="black", font=('Helvetica 17 bold'))

        self.jana = ImageTk.PhotoImage(Image.open(PATH_12))
        janaImg = self.canvas.create_image(670, 220, image=self.jana,
                                           anchor='nw')
        self.canvas.create_text(740, 380, text="Okoli Jana",
                                fill="black", font=('Helvetica 17 bold'))

        # buttons
        ToTraegerClassButton = tk.Button(
            self, text="Träger auf 2 Stützen", width=20, height=2, command=lambda: controller.show_frame("TraegerEins"))
        ToTraegerClassButton.place(x=325, y=600)

        ToCentralClassButton = tk.Button(
            self, text="Zentrales Kraftsystem", width=20, height=2, command=lambda: controller.show_frame("ZentralEins"))
        ToCentralClassButton.place(x=505, y=600)

        ToParallelClassButton = tk.Button(
            self, text="Paralles Kräftesystem", width=20, height=2, command=lambda: controller.show_frame("ParallelEins"))
        ToParallelClassButton.place(x=685, y=600)
#####################################################################################################################################################################################################################


#####################################################################################################################################################################################################################
''' 
Showing some info about 
calculating bearing forces on the first screen
'''

# interface 1 of calculations of bearing forces


class TraegerEins(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # canvas
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGTH)
        self.canvas.pack()

        img = ImageTk.PhotoImage(Image.open(BG_CALC_GUIS).resize(
            (WIDTH, HEIGTH), Image.Resampling.LANCZOS))
        # Keep a reference in case this code is put in a function.
        self.canvas.background = img
        bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=img)

        self.traegerImg = ImageTk.PhotoImage(Image.open(PATH_14))
        traegerImg = self.canvas.create_image(30, +300, image=self.traegerImg,
                                              anchor='nw')

        self.winkelCorrect = ImageTk.PhotoImage(
            Image.open(PATH_15))
        winkelCorrect = self.canvas.create_image(+640, 80, image=self.winkelCorrect,
                                                 anchor='nw')

        # adding some info text on canvas
        self.canvas.create_text(230, 40, text="Träger auf 2 Stützen",
                                fill="black", font=('Helvetica 30 bold'))
        self.canvas.create_text(350, 210, text="Lager Ⓐ sei ein Fest-Lager (nimmt Kraft in beide Richtungen auf)\n\n"
                                "und Ⓑ ein Los-Lager (nimmt Kraft in einer Richtung auf) \n\n im Abstand l. Das Koordinatensystem ist bereits vorgegeben.\n\n"
                                " Die Belastung F hat den Abstand a zum Festlager.\n\n"
                                "Gesucht sind die Auflagerreaktionen FAy, FAx und FBy", fill="black", font=('Helvetica 15 bold'))
        self.canvas.create_text(320, 535, text="Erforderliche Eingabe für die Berechnung",
                                fill="black", font=('Helvetica 20 bold'))
        self.canvas.create_text(320, 620, text="Die Länge des Balkens, Die Beträge der Kräfte in Newton\n\n"
                                "Die Winkeln und Abstände der Kräfte zum Festlager Ⓐ.", fill="black", font=('Helvetica 15 bold'))
        self.canvas.create_text(860, 50, text="Hinweis zum Winkel",
                                fill="black", font=('Helvetica 22 bold'))
        self.canvas.create_text(880, 430, text="Zum eingegebenen Winkel alpha strich\n\n"
                                "muss man also 180° dazu rechnen !",
                                fill="black", font=('Helvetica 15 bold'))

        # buttons
        TotraegerGUI_Teil1 = tk.Button(
            self, text="Startbildschirm", width=20, height=2,  command=lambda: controller.show_frame("startPage"))
        TotraegerGUI_Teil1.place(x=720, y=600)
        TotraegerGUI_Teil2 = tk.Button(
            self, text="Beispiel starten", width=20, height=2,  command=lambda: controller.show_frame("TraegerZwei"))
        TotraegerGUI_Teil2.place(x=900, y=600)
#####################################################################################################################################################################################################################


#####################################################################################################################################################################################################################
''' 
Actual class Traeger for 
calculation of bearing forces
'''


class TraegerZwei(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # creating new canvas
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGTH)
        self.canvas.pack()

        img = ImageTk.PhotoImage(Image.open(BG_CALC_GUIS).resize(
            (WIDTH, HEIGTH), Image.Resampling.LANCZOS))
        # Keep a reference in case this code is put in a function.
        self.canvas.background = img
        bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=img)

        # the results will be stored in these class variables
        # which we can access using self and therefore set the result on the canvas using
        # the built in function:  text.configure
        self.FAx = float(0)
        self.FAy = float(0)
        self.FBy = float(0)

        # empty lists to store user input and float for bar length
        self.forceList: list = []
        self.anglesList: list = []
        self.distanceList: list = []
        self.balk_laenge = float()

        # creating some info text
        self.canvas.create_text(230, 40, text="Träger auf 2 Stützen",
                                fill="black", font=('Helvetica 30 bold'))
        self.canvas.create_text(870, 80, text="Ergebnis der Berechnung",
                                fill="black", font=('Helvetica 18 bold'))
        self.fbyText = self.canvas.create_text(840, 160, text="FBy =  " + str(self.FBy) + "  Newton",
                                               fill="black", font=('Helvetica 18 bold'))
        self.fayText = self.canvas.create_text(840, 220, text="FAy =  " + str(self.FAy) + "  Newton",
                                               fill="black", font=('Helvetica 18 bold'))
        self.faxText = self.canvas.create_text(840, 280, text="FAx =  " + str(self.FAx) + "  Newton",
                                               fill="black", font=('Helvetica 18 bold'))

        self.canvas.create_text(150, 140, text="Kraft [F in Newton] ",
                                fill="black", font=('Helvetica 15 bold'))
        self.canvas.create_text(160, 220, text="Winkel der Kraft [in °]",
                                fill="black", font=('Helvetica 15 bold'))
        self.canvas.create_text(190, 300, text="Abstand zum Festlager A in m",
                                fill="black", font=('Helvetica 15 bold'))
        self.canvas.create_text(560, 460, text="Mehrere Kräfte?\n\nKein Problem!\n\n Wir lösen jedes Problem!\n\n Und zwar SMART!",
                                fill="black", font=('Helvetica 15 bold'))
        self.numOfForces = 0
        self.kraefteAnzahl = self.canvas.create_text(135, 648, text="Anzahl der Kräfte:   " + str(self.numOfForces),
                                                     fill="black", font=('Helvetica 15 bold'))

        self.canvas.create_text(550, 140, text="Die Balkenlänge ",
                                fill="black", font=('Helvetica 15 bold'))
        self.canvas.create_text(610, 190, text="meter",
                                fill="black", font=('Helvetica 15 bold'))

        # keep track of the number of forces entered
        self.count = 1
        self.tupleForce = tuple()

        # titles of treeview widget
        self.titles = {'Nr.': self.count, 'Kräfte in N': self.forceList,
                       'Winkel in °': self.anglesList, 'Abstände in m': self.distanceList}
        self.tableInputs = ttk.Treeview(self, selectmode='browse')

        # setting column names of treeview
        self.tableInputs["columns"] = list(
            x for x in range(len(list(self.titles.keys()))))
        self.tableInputs['show'] = 'headings'

        for x, y in enumerate(self.titles.keys()):
            self.tableInputs.column(
                x,  anchor=CENTER, stretch=NO,  width=90)
            self.tableInputs.heading(x, text=y)

        # creating treeview on canvas
        windowTableInputs = self.canvas.create_window(
            40, 380, anchor="nw", window=self.tableInputs)

        # entry boxes + validation command
        vcmd = (self.register(self.check), '%d', '%i',
                '%P', '%s', '%S', '%v', '%V', '%W')
        self.forceEntry = tk.Entry(self, validate='key', validatecommand=vcmd, font=(
            "Helvetica", 15), width=8, bd=2)
        self.angleEntry = tk.Entry(self, validate='key', validatecommand=vcmd, font=(
            "Helvetica", 15), width=8, bd=2)
        self.distanceEntry = tk.Entry(
            self, validate='key', validatecommand=vcmd, font=("Helvetica", 15), width=8, bd=2)
        self.balkEntry = tk.Entry(
            self, validate='key', validatecommand=vcmd, font=("Helvetica", 15), width=8, bd=2)

        # Add the entry boxes to the canvas
        winforceEntry = self.canvas.create_window(
            290, 125, anchor="nw", window=self.forceEntry)
        winAngleEntry = self.canvas.create_window(
            290, 205, anchor="nw", window=self.angleEntry)
        winDisEntry = self.canvas.create_window(
            350, 285, anchor="nw", window=self.distanceEntry)
        winBalkL = self.canvas.create_window(
            475, 175, anchor="nw", window=self.balkEntry)

        # buttons and adding them to canvas, although we could just use pack or place
        addForce = tk.Button(
            self, text="Kraft hinzufügen und berechnen", width=25, height=2, command=self.addForce)
        addForceWindow = winDisEntry = self.canvas.create_window(
            430, 580, anchor="nw", window=addForce)

        removeForce = tk.Button(
            self, text="Kraft löschen", width=15, height=2, command=self.remForce)
        removeForceWindow = winDisEntry = self.canvas.create_window(
            630, 580, anchor="nw", window=removeForce)

        TotraegerGUI_Teil1 = tk.Button(
            self, text="Zurück zur Erklärung", width=20, height=2, command=self.resetInputs_Ifok)
        buttonTotraegerGUI_Teil1 = winDisEntry = self.canvas.create_window(
            760, 580, anchor="nw", window=TotraegerGUI_Teil1)

    # only floats or ints, plus max number of 5 decimals and after "." only 2 decimals allowed

    def check(self, d, i, P, s, S, v, V, W):
        text = P  # e.get()
        #print('text:', text)
        parts = text.split('.')
        parts_number = len(parts)
        if parts_number > 2:
            #print('too much dots')
            return False
        if parts_number > 1 and parts[1]:  # don't check empty string
            if not parts[1].isdecimal() or len(parts[1]) > 2:
                #print('wrong second part')
                return False
        if parts_number > 0 and parts[0]:  # don't check empty string
            if not parts[0].isdecimal() or len(parts[0]) > 4:
                #print('wrong first part')
                return False
        return True

    # reset values when returning to previous window

    def resetInputs_Ifok(self):

        if len(self.forceList) != 0 and len(self.distanceList) != 0:
            MsgBox = messagebox.askquestion(
                'Zurück', 'Ihre Änderungen gehen verloren, \n\nMöchten Sie fortfahren?', icon='warning')

            if MsgBox == 'yes':
                # clearing entries
                self.forceEntry.delete(0, END)
                self.angleEntry.delete(0, END)
                self.distanceEntry.delete(0, END)
                self.balkEntry.configure(state="normal")
                self.balkEntry.delete(0, END)

                self.tableInputs.delete(*self.tableInputs.get_children())
                self.forceList.clear()
                self.anglesList.clear()
                self.distanceList.clear()
                self.calc()
                self.numOfForces = 0
                self.canvas.itemconfigure(
                    self.kraefteAnzahl, text="Anzahl der Kräfte:   " + str(self.numOfForces))
                self.controller.show_frame("TraegerEins")

        else:
            self.forceEntry.delete(0, END)
            self.angleEntry.delete(0, END)
            self.distanceEntry.delete(0, END)
            self.balkEntry.configure(state="normal")
            self.balkEntry.delete(0, END)
            self.controller.show_frame("TraegerEins")

    # method to add force

    def addForce(self):
        if self.forceEntry.get() == "" or self.angleEntry.get() == "" or self.distanceEntry.get() == "" or self.balkEntry.get() == "":
            messagebox.showinfo(title="No Data", message=("Du musst die Kraft, den Winkel, den Abstand\n\n"
                                "sowie die Balkenlänge eingeben!"))
        else:
            # wenn der abstand größer als die balkenlänge ist
            if float(self.distanceEntry.get()) > float(self.balkEntry.get()):
                messagebox.showwarning(title="Wrong data", message=(
                    "Der Abstand der Kraft zum Lager A darf \n\n nicht größer sein als die Balkenlänge!"))
            else:
                self.balkEntry.configure(state="disabled")
                # inserting values in treeview
                self.tableInputs.insert(parent='', index='end', text='', values=(
                    self.count, self.forceEntry.get(), self.angleEntry.get(), self.distanceEntry.get()))

                # getting values and adding them to lists
                force = float(self.forceEntry.get())
                angle = float(self.angleEntry.get())
                distance = float(self.distanceEntry.get())
                self.balk_laenge = float(self.balkEntry.get())

                self.forceList.append(force)
                self.anglesList.append(angle)
                self.distanceList.append(distance)

                # updating force number on canvas
                self.count += 1
                self.numOfForces += 1
                self.canvas.itemconfigure(
                    self.kraefteAnzahl, text="Anzahl der Kräfte:   " + str(self.numOfForces))
                self.calc()

                # clearing entries
                self.forceEntry.delete(0, END)
                self.angleEntry.delete(0, END)
                self.distanceEntry.delete(0, END)

    # method to remove force

    def remForce(self):
        # selected item
        curItem = self.tableInputs.focus()
        # if item is selected we get True
        if bool(curItem):
            x = self.tableInputs.selection()[0]
            self.tableInputs.delete(x)

            # removing force inputs from list
            self.forceList.pop()
            self.anglesList.pop()
            self.distanceList.pop()

            # setting current force number - 1 and configuring canvas text
            self.count -= 1
            self.numOfForces -= 1
            self.canvas.itemconfigure(
                self.kraefteAnzahl, text="Anzahl der Kräfte:   " + str(self.numOfForces))
            self.calc()

            # reseting values
            if self.numOfForces == 0:
                self.FAx = 0.0
                self.FAy = 0.0
                self.FBy = 0.0
                self.balkEntry.configure(state="normal")
                self.balkEntry.delete(0, END)
        else:
            # if lists for storing inputs are still empty
            if len(self.forceList) == 0 or len(self.distanceList) == 0:
                messagebox.showerror(
                    title="No Data", message="Noch keine Einträge vorhanden!")

            # if values exist but nothing is selected, to avoid error: tuple index out of range
            if len(self.forceList) != 0 or len(self.distanceList) != 0 and not bool(curItem):
                messagebox.showerror(
                    title="No Data selected", message="Zum löschen bitte zuerst einen Eintrag wählen!")


    # calculation with Class PorterOnTwoSupport
    def calc(self):
        traegerClass = trGr.PorterOnTwoSupport(
            self.forceList, self.anglesList, self.distanceList, self.balk_laenge)
        self.tupleForce = traegerClass.calcBearingForces()

        self.FAy = self.tupleForce[0]
        self.FAx = self.tupleForce[1]
        self.FBy = self.tupleForce[2]

        # updating values
        self.canvas.itemconfigure(
            self.fayText, text="FAy =  " + str(self.FAy) + "  Newton",)
        self.canvas.itemconfigure(
            self.faxText, text="FAx =  " + str(self.FAx) + "  Newton",)
        self.canvas.itemconfigure(
            self.fbyText, text="FBy =  " + str(self.FBy) + "  Newton",)

#####################################################################################################################################################################################################################


#####################################################################################################################################################################################################################
class ZentralEins(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGTH)
        self.canvas.pack()

        img = ImageTk.PhotoImage(Image.open(BG_CALC_GUIS).resize(
            (WIDTH, HEIGTH), Image.Resampling.LANCZOS))
        # Keep a reference in case this code is put in a function.
        self.canvas.background = img
        bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=img)


        self.zentralImg = ImageTk.PhotoImage(Image.open(PATH_16))
        zentralImg = self.canvas.create_image(550, 250, image=self.zentralImg,
                                              anchor='nw')

        self.zentralImg2 = ImageTk.PhotoImage(
            Image.open(PATH_17))
        zentralimg = self.canvas.create_image(670, 50, image=self.zentralImg2,
                                                 anchor='nw')
        
        # adding some info text on canvas
        self.canvas.create_text(250, 40, text="Zentrales Kraftsystem",
                                fill="black", font=('Helvetica 30 bold'))
        
        
        self.canvas.create_text(380, 260, text="Hier greifen gleichzeitig Kräfte, auf einem Punkt A \n\n"
                                "an einem Bauteil an. Die Wirklinien aller Kräfte schneiden sich in \n\neinem"
                                " gemeinsamen Punkt. Man nennt diesen Schnittpunkt \n\nden Zentralpunkt"
                                "A des Kräftesystems. Lt Längsverschiebungssatz \n\nkönnen alle Kräfte auf ihren Wirklinien im  Punkt A verschoben werden.\n\n"
                                "Man kann den Körper nur verschieben, aber nicht drehen.\n\n"
                                "Ein ZS ist im Gleichgewicht,"
                                "wenn sich das Krafteck schließt."
                                , fill="black", font=('Helvetica 15 bold'))
        
        
        self.canvas.create_text(320, 510, text="Erforderliche Eingabe für die Berechnung",
                                fill="black", font=('Helvetica 20 bold'))
        self.canvas.create_text(200, 600, text="Die Beträge der Kräfte in Newton\n\n"
                                "Die Winkeln der Kräfte in ° Grad.", fill="black", font=('Helvetica 15 bold'))
        
        
        
        # Add other tkinter widgets.
        Towelcome = tk.Button(
            self, text="Startbildschirm", width=20, height=2,  command=lambda: controller.show_frame("startPage"))
        Towelcome.place(x=720, y=625)
        #button.grid(row=0, column=0)

        # Add other tkinter widgets.
        ToZentral2 = tk.Button(
            self, text="Beispiel starten", width=20, height=2,  command=lambda: controller.show_frame("ZentralZwei"))
        ToZentral2.place(x=900, y=625)
        #button.grid(row=0, column=0)

#####################################################################################################################################################################################################################


####################################################################################################################################################################################################################
# class central gui
class ZentralZwei(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGTH)
        self.canvas.pack()

        img = ImageTk.PhotoImage(Image.open(BG_CALC_GUIS).resize(
            (WIDTH, HEIGTH), Image.Resampling.LANCZOS))
        # Keep a reference in case this code is put in a function.
        self.canvas.background = img
        bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=img)

        self.canvas.create_text(250, 40, text="Zentrales Kraftsystem",
                                fill="black", font=('Helvetica 30 bold'))

        # the results will be stored in these class variables
        # which we can access using self and therefore set the result on the canvas using
        # the built in function:  text.configure
        self.F_res_angle = float(0)
        self.F_res = float(0)

        self.fres_text = self.canvas.create_text(820, 160, text="Resultierende =  " + str(self.F_res) + "  Newton",
                                                 fill="black", font=('Helvetica 18 bold'))
        self.fres_angle_text = self.canvas.create_text(820, 220, text="Winkel der Resultierende =  " + str(self.F_res_angle) + " ° Grad",
                                                       fill="black", font=('Helvetica 18 bold'))
        self.canvas.create_text(190, 185, text="Kraft [F in Newton] ",
                                fill="black", font=('Helvetica 15 bold'))
        self.canvas.create_text(200, 265, text="Winkel der Kraft [in °]",
                                fill="black", font=('Helvetica 15 bold'))
        self.canvas.create_text(560, 460, text="Mehrere Kräfte?\n\nKein Problem!\n\n Wir lösen jedes Problem!\n\n Und zwar SMART!",
                                fill="black", font=('Helvetica 15 bold'))
        self.numOfForces = 0
        self.kraefteAnzahl = self.canvas.create_text(180, 648, text="Anzahl der Kräfte:   " + str(self.numOfForces),
                                                     fill="black", font=('Helvetica 15 bold'))

        # empty lists to store user input and float for bar length
        self.forceList: list = []
        self.anglesList: list = []

        # keep track of the number of forces entered, empty tuple for function results
        self.count = 1
        self.tupleForce = tuple()

        # titles of treeview widget
        self.titles = {'Nr.': self.count, 'Kräfte in N': self.forceList,
                       'Winkel in °': self.anglesList}
        self.tableInputs = ttk.Treeview(self, selectmode='browse')

        # setting column names of treeview
        self.tableInputs["columns"] = list(
            x for x in range(len(list(self.titles.keys()))))
        self.tableInputs['show'] = 'headings'

        for x, y in enumerate(self.titles.keys()):
            self.tableInputs.column(
                x,  anchor=CENTER, stretch=NO,  width=90)
            self.tableInputs.heading(x, text=y)

        # creating treeview on canvas
        windowTableInputs = self.canvas.create_window(
            80, 380, anchor="nw", window=self.tableInputs)

        # entry boxes and validation command
        vcmd = (self.register(self.check), '%d', '%i',
                '%P', '%s', '%S', '%v', '%V', '%W')
        self.forceEntry = tk.Entry(self, validate='key', validatecommand=vcmd, font=(
            "Helvetica", 15), width=7, bd=2)
        self.angleEntry = tk.Entry(self, validate='key', validatecommand=vcmd,  font=(
            "Helvetica", 15), width=7, bd=2)

        # Add the entry boxes to the canvas
        winforceEntry = self.canvas.create_window(
            350, 170, anchor="nw", window=self.forceEntry)
        winAngleEntry = self.canvas.create_window(
            350, 250, anchor="nw", window=self.angleEntry)

        # buttons and adding them to canvas, although we could just use pack or place
        addForce = tk.Button(
            self, text="Kraft hinzufügen und berechnen", width=25, height=2, command=self.addForce)
        addForceWindow = winDisEntry = self.canvas.create_window(
            430, 580, anchor="nw", window=addForce)

        removeForce = tk.Button(
            self, text="Kraft löschen", width=15, height=2, command=self.remForce)
        removeForceWindow = winDisEntry = self.canvas.create_window(
            630, 580, anchor="nw", window=removeForce)

        ToZentralEinsButton = tk.Button(
            self, text="Zurück zur Erklärung", width=20, height=2, command=self.resetInputs_Ifok)
        winToZentralEinsButton = self.canvas.create_window(
            760, 580, anchor="nw", window=ToZentralEinsButton)

    # reset values when returning to previous window
    def resetInputs_Ifok(self):

        if len(self.forceList) != 0:
            MsgBox = messagebox.askquestion(
                'Zurück', 'Ihre Änderungen gehen verloren, \n\nMöchten Sie fortfahren?', icon='warning')

            if MsgBox == 'yes':
                # clearing entries
                self.forceEntry.delete(0, END)
                self.angleEntry.delete(0, END)

                self.tableInputs.delete(*self.tableInputs.get_children())
                self.forceList.clear()
                self.anglesList.clear()
                self.calc()
                self.numOfForces = 0
                self.canvas.itemconfigure(
                    self.kraefteAnzahl, text="Anzahl der Kräfte:   " + str(self.numOfForces))
                self.controller.show_frame("ZentralEins")

        else:
            self.forceEntry.delete(0, END)
            self.angleEntry.delete(0, END)
            self.controller.show_frame("ZentralEins")

    # only floats or ints, plus max number of 5 decimals and after "." only 2 decimals allowed
    def check(self, d, i, P, s, S, v, V, W):
        text = P  # e.get()
        #print('text:', text)
        parts = text.split('.')
        parts_number = len(parts)
        if parts_number > 2:
            #print('too much dots')
            return False
        if parts_number > 1 and parts[1]:  # don't check empty string
            if not parts[1].isdecimal() or len(parts[1]) > 2:
                #print('wrong second part')
                return False
        if parts_number > 0 and parts[0]:  # don't check empty string
            if not parts[0].isdecimal() or len(parts[0]) > 4:
                #print('wrong first part')
                return False
        return True

    # method to add force
    def addForce(self):
        if self.forceEntry.get() == "" or self.angleEntry.get() == "":
            messagebox.showinfo(title="No Data", message=(
                "Du musst die Kraft und den Winkel eingeben!"))
        else:
            # inserting values in treeview
            self.tableInputs.insert(parent='', index='end', text='', values=(
                self.count, self.forceEntry.get(), self.angleEntry.get()))

            # getting values and adding them to lists
            force = float(self.forceEntry.get())
            angle = float(self.angleEntry.get())

            self.forceList.append(force)
            self.anglesList.append(angle)

            # updating force number on canvas
            self.count += 1
            self.numOfForces += 1
            self.canvas.itemconfigure(
                self.kraefteAnzahl, text="Anzahl der Kräfte:   " + str(self.numOfForces))
            self.calc()

            # clearing entries
            self.forceEntry.delete(0, END)
            self.angleEntry.delete(0, END)

    # method to remove force

    def remForce(self):
        # selected item
        curItem = self.tableInputs.focus()
        # if item is selected we get True
        if bool(curItem):
            x = self.tableInputs.selection()[0]
            self.tableInputs.delete(x)

            # removing force inputs from list
            self.forceList.pop()
            self.anglesList.pop()

            # setting current force number - 1 and configuring canvas text
            self.count -= 1
            self.numOfForces -= 1
            self.canvas.itemconfigure(
                self.kraefteAnzahl, text="Anzahl der Kräfte:   " + str(self.numOfForces))
            self.calc()

            # reseting values
            if self.numOfForces == 0:
                self.F_res = 0.0
                self.F_res_angle = 0.0

        else:
            # if lists for storing inputs are still empty
            if len(self.forceList) == 0 or len(self.anglesList) == 0:
                messagebox.showerror(
                    title="No Data", message="Noch keine Einträge vorhanden!")

            # if values exist but nothing is selected, to avoid error: tuple index out of range
            if len(self.forceList) != 0 or len(self.anglesList) != 0 and not bool(curItem):
                messagebox.showerror(
                    title="No Data selected", message="Zum löschen bitte einen Eintrag wählen!")

    # calculation with Class PorterOnTwoSupport
    def calc(self):
        traegerClass = ctr.CentralForce(
            self.forceList, self.anglesList)

        self.tupleForce = traegerClass.calcResultantForce()
        self.F_res = self.tupleForce[0]
        self.F_res_angle = self.tupleForce[1]

        # for result in tupleForce:
        self.canvas.itemconfigure(
            self.fres_text, text="Resultierende =  " + str(self.F_res) + "  Newton",)
        self.canvas.itemconfigure(
            self.fres_angle_text, text="Winkel der Resultierende =  " + str(self.F_res_angle) + " ° Grad",)
####################################################################################################################################################################################################################


####################################################################################################################################################################################################################
class ParallelEins(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGTH)
        self.canvas.pack()

        img = ImageTk.PhotoImage(Image.open(BG_CALC_GUIS).resize(
            (WIDTH, HEIGTH), Image.Resampling.LANCZOS))
        # Keep a reference in case this code is put in a function.
        self.canvas.background = img
        bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=img)

        self.canvas.create_text(265, 40, text="Paralleles Kräftesystem",
                                fill="black", font=('Helvetica 30 bold'))

        self.parallel_1 = ImageTk.PhotoImage(
            Image.open(PATH_18))
        parallelImg = self.canvas.create_image(660, 80, image=self.parallel_1,
                                               anchor='nw')

        self.parallel_2 = ImageTk.PhotoImage(
            Image.open(PATH_19))
        parallelImg = self.canvas.create_image(760, 300, image=self.parallel_2,
                                               anchor='nw')

        self.canvas.create_text(340, 250, text="Auf dem rechten oberen Bild sind die Kräfte F1=10N, \n\n"
                                "F2=20N, F3=15N und F4=18N abgebildet, die alle parallel \n\n"
                                "zueinander sind und auf den gewichtslosen Balken wirken.\n\n"
                                " Es stellt sich die Frage, wie groß die Haltekraft H sein muss,\n\n"
                                "damit der Balken im Gleichgewicht ist. Es wird insbesondere"
                                "\n\nder Punkt gesucht in dem die Haltekraft angreifen muss.", fill="black", font=('Helvetica 15 bold'))
        self.canvas.create_text(320, 510, text="Erforderliche Eingabe für die Berechnung",
                                fill="black", font=('Helvetica 20 bold'))

        self.canvas.create_text(225, 600, text="Die Beträge der Kräfte in Newton\n\n"
                                "Die Abstände der Kräfte zum Punkt A.", fill="black", font=('Helvetica 15 bold'))

        # Add other tkinter widgets.
        TotraegerGUI_Teil1 = tk.Button(
            self, text="Startbildschirm", width=20, height=2,  command=lambda: controller.show_frame("startPage"))
        TotraegerGUI_Teil1.place(x=720, y=600)
        #button.grid(row=0, column=0)

        # Add other tkinter widgets.
        TotraegerGUI_Teil2 = tk.Button(
            self, text="Beispiel starten", width=20, height=2,  command=lambda: controller.show_frame("ParallelZwei"))
        TotraegerGUI_Teil2.place(x=900, y=600)
        #button.grid(row=0, column=0)

####################################################################################################################################################################################################################


####################################################################################################################################################################################################################
class ParallelZwei(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGTH)
        self.canvas.pack()

        img = ImageTk.PhotoImage(Image.open(BG_CALC_GUIS).resize(
            (WIDTH, HEIGTH), Image.Resampling.LANCZOS))
        # Keep a reference in case this code is put in a function.
        self.canvas.background = img
        bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=img)

        self.canvas.create_text(265, 40, text="Paralleles Kräftesystem",
                                fill="black", font=('Helvetica 30 bold'))

        # the results will be stored in these class variables
        # which we can access using self and therefore set the result on the canvas using
        # the built in function:  text.configure
        self.F_hk = float(0)
        self.F_hk_abstand = float(0)
        # empty lists to store user input and float for bar length
        self.forceList: list = []
        self.distanceList: list = []

        self.canvas.create_text(730, 80, text="Ergebnis der Berechnung",
                                fill="black", font=('Helvetica 18 bold'))
        self.f_hk_Text = self.canvas.create_text(710, 160, text="Haltekraft =  " + str(self.F_hk) + "  Newton",
                                                 fill="black", font=('Helvetica 18 bold'))

        self.f_dis_Text = self.canvas.create_text(780, 220, text="Abstand der HK zum Punkt A =  " + str(self.F_hk_abstand) + "  meter",
                                                  fill="black", font=('Helvetica 18 bold'))

        self.canvas.create_text(160, 210, text="Kraft [F in Newton] ",
                                fill="black", font=('Helvetica 15 bold'))

        self.canvas.create_text(140, 300, text="Abstand in m",
                                fill="black", font=('Helvetica 15 bold'))

        self.canvas.create_text(560, 460, text="Mehrere Kräfte?\n\nKein Problem!\n\n Wir lösen jedes Problem!\n\n Und zwar SMART!",
                                fill="black", font=('Helvetica 15 bold'))
        self.numOfForces = 0
        self.kraefteAnzahl = self.canvas.create_text(170, 648, text="Anzahl der Kräfte:   " + str(self.numOfForces),
                                                     fill="black", font=('Helvetica 15 bold'))

        # keep track of the number of forces entered
        # empty tuple to store result of method, which is coming from class parallel
        self.count = 1
        self.tupleForce_Parallell = tuple()

        # titles of treeview widget
        self.titles = {'Nr.': self.count, 'Kräfte in N': self.forceList,
                       'Abstände in m': self.distanceList}
        self.tableInputs = ttk.Treeview(self, selectmode='browse')

        # setting column names of treeview
        self.tableInputs["columns"] = list(
            x for x in range(len(list(self.titles.keys()))))
        self.tableInputs['show'] = 'headings'

        for x, y in enumerate(self.titles.keys()):
            self.tableInputs.column(
                x,  anchor=CENTER, stretch=NO,  width=90)
            self.tableInputs.heading(x, text=y)

        # creating treeview on canvas
        windowTableInputs = self.canvas.create_window(
            80, 380, anchor="nw", window=self.tableInputs)

        # entry boxes and validation command
        vcmd = (self.register(self.check), '%d', '%i',
                '%P', '%s', '%S', '%v', '%V', '%W')
        self.forceEntry = tk.Entry(self, validate='key', validatecommand=vcmd, font=(
            "Helvetica", 15), width=7, bd=2)
        self.distanceEntry = tk.Entry(
            self, validate='key', validatecommand=vcmd,  font=("Helvetica", 15), width=7, bd=2)

        # Add the entry boxes to the canvas
        winforceEntry = self.canvas.create_window(
            280, 200, anchor="nw", window=self.forceEntry)
        winDisEntry = self.canvas.create_window(
            230, 285, anchor="nw", window=self.distanceEntry)

        # buttons and adding them to canvas, although we could just use pack or place
        addForce = tk.Button(
            self, text="Kraft hinzufügen und berechnen", width=25, height=2, command=self.addForce)
        addForceWindow = winDisEntry = self.canvas.create_window(
            430, 580, anchor="nw", window=addForce)

        removeForce = tk.Button(
            self, text="Kraft löschen", width=15, height=2, command=self.remForce)
        removeForceWindow = winDisEntry = self.canvas.create_window(
            630, 580, anchor="nw", window=removeForce)

        ToParallelGUI_Teil1 = tk.Button(
            self, text="Zurück zur Erklärung", width=20, height=2, command=self.resetInputs_Ifok)
        winToParallelGUI_Teil1 = self.canvas.create_window(
            760, 580, anchor="nw", window=ToParallelGUI_Teil1)

    # only floats or ints, plus max number of 5 decimals and after "." only 2 decimals allowed

    def check(self, d, i, P, s, S, v, V, W):
        text = P  # e.get()
        #print('text:', text)
        parts = text.split('.')
        parts_number = len(parts)
        if parts_number > 2:
            #print('too much dots')
            return False
        if parts_number > 1 and parts[1]:  # don't check empty string
            if not parts[1].isdecimal() or len(parts[1]) > 2:
                #print('wrong second part')
                return False
        if parts_number > 0 and parts[0]:  # don't check empty string
            if not parts[0].isdecimal() or len(parts[0]) > 4:
                #print('wrong first part')
                return False
        return True

    # reset values when returning to previous window
    def resetInputs_Ifok(self):
        if len(self.forceList) != 0:
            MsgBox = messagebox.askquestion(
                'Zurück', 'Ihre Änderungen gehen verloren, \n\nMöchten Sie fortfahren?', icon='warning')

            if MsgBox == 'yes':
                # clearing entries
                self.forceEntry.delete(0, END)
                self.distanceEntry.delete(0, END)

                self.tableInputs.delete(*self.tableInputs.get_children())
                self.forceList.clear()
                self.distanceList.clear()

                self.numOfForces = 0
                self.calc()
                self.canvas.itemconfigure(
                    self.kraefteAnzahl, text="Anzahl der Kräfte:   " + str(self.numOfForces))
                self.controller.show_frame("ParallelEins")
        else:
            self.forceEntry.delete(0, END)
            self.distanceEntry.delete(0, END)
            self.controller.show_frame("ParallelEins")

    # method to add force
    def addForce(self):
        if self.forceEntry.get() == "" or self.distanceEntry.get() == "":
            messagebox.showinfo(title="No Data", message=("Du musst die Kraft und\n\n"
                                " den Abstand zum Punkt A eingeben!"))
        else:

            # inserting values in treeview
            self.tableInputs.insert(parent='', index='end', text='', values=(
                self.count, self.forceEntry.get(), self.distanceEntry.get()))

            # getting values and adding them to lists
            force = float(self.forceEntry.get())
            distance = float(self.distanceEntry.get())
            self.forceList.append(force)
            self.distanceList.append(distance)

            # updating force number on canvas
            self.count += 1
            self.numOfForces += 1

            self.canvas.itemconfigure(
                self.kraefteAnzahl, text="Anzahl der Kräfte:   " + str(self.numOfForces))
            self.calc()
            # clearing entries
            self.forceEntry.delete(0, END)
            self.distanceEntry.delete(0, END)

    # method to remove force
    def remForce(self):
        # selected item
        curItem = self.tableInputs.focus()
        # if item is selected we get True
        if bool(curItem):
            x = self.tableInputs.selection()[0]
            self.tableInputs.delete(x)

            # removing force inputs from list
            self.forceList.pop()
            self.distanceList.pop()

            # setting current force number - 1 and configuring canvas text,
            # updating both, on canvas and Treeview
            self.count -= 1
            self.numOfForces -= 1
            self.canvas.itemconfigure(
                self.kraefteAnzahl, text="Anzahl der Kräfte:   " + str(self.numOfForces))
            self.calc()

            if self.numOfForces == 0:
                self.F_hk = 0.0
                self.F_hk_abstand = 0.0
        else:
            if len(self.forceList) == 0 or len(self.distanceList) == 0:
                messagebox.showerror(
                    title="No Data", message="Noch keine Einträge vorhanden!")

            if len(self.forceList) != 0 or len(self.distanceList) != 0 and not bool(curItem):
                messagebox.showerror(
                    title="No Data selected", message="Zum löschen bitte einen Eintrag wählen!")

    # calculation with Class ParallelForce
    def calc(self):
        parallelClass = parll.ParallelForce(
            self.forceList, self.distanceList)
        self.tupleForce_Parallell = parallelClass.calcHoldingForce()
        self.F_hk = self.tupleForce_Parallell[0]
        self.F_hk_abstand = self.tupleForce_Parallell[1]

        # configuring canvas to updated values
        self.canvas.itemconfigure(
            self.f_hk_Text, text="Haltekraft =  " + str(self.F_hk) + "  Newton")
        self.canvas.itemconfigure(
            self.f_dis_Text, text="Abstand der HK zum Punkt A =  " + str(self.F_hk_abstand) + "  meter",)

####################################################################################################################################################################################################################


# running the main app
if __name__ == "__main__":
    programm = App()

    # handling closing button x
    programm.protocol("WM_DELETE_WINDOW", on_closing)
    programm.mainloop()
####################################################################################################################################################################################################################
