import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Arc, RegularPolygon
from numpy import radians as rad
from tkinter import ttk
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class traeger():
    def __init__(self, length, a):
        self.root = tk.Tk(className="") 
        self.root.title("Kinematik v0.1 (c) B. Ratschiner")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.geometry("1200x750")
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid(row=0, column=0, sticky="news")

        self.label = ttk.Label(self.frm, text="Eingabe")
        self.label.grid(column=0, row=0, sticky="news")
        self.entry = ttk.Entry(self.frm)
        self.entry.insert(10, 0)
        self.entry.grid(column=1, row=0, sticky="news")
#  
    
        self.entry1 = ttk.Entry(self.frm)
        self.entry1.insert(10, 0)
        self.entry1.grid(column=0, row=0, sticky="news")
        
        self.entry2 = ttk.Entry(self.frm)
        self.entry2.insert(10, 0)
        self.entry2.grid(column=0, row=0, sticky="news") 

        # Creat Start Buttom
        self.button_start = ttk.Button(self.frm, text="Start", command=self.make_all, width = 30).grid(column=2, row=0)

        # Create Plot the subplot
        self.fig, self.ax = plt.subplots(figsize=(10, 5))
        self.fig.tight_layout()
        plt.subplots_adjust(left=0.07, bottom=0.15, right=0.975, top=None, wspace=0.3, hspace=None)

        # Laenge des Traegers
        self.len = length        

        # Kraefte und ihre Pfeile
        self.forces = []

        # Traeger bauen
        self.ax.plot([0, 0], [0, 0], 'ko')
        self.ax.plot([a, a + self.len], [0, 0], 'k-')
        self.fx = []
        self.fy = []

        self.lager_arrow_props = dict(fc='r', ec='r', arrowstyle='->', connectionstyle="arc3, rad=0.0",mutation_scale=20, visible=False)
        self.belastung_arrow_props = dict(fc='k', ec='k', arrowstyle='->', connectionstyle="arc3, rad=0.0",mutation_scale=20, visible=False)
        
        # Formatierend es Plots
        self.ax.axis('equal')
        for side in ['top','right','left']:
            self.ax.spines[side].set_visible(False)
        self.ax.tick_params(axis='y',which='both',labelbottom=False,bottom=False,left=False)
        self.ax.axes.yaxis.set_visible(False)

        # creating the Tkinter canvas containing the Matplotlib figure
        self.canvas = FigureCanvasTkAgg(self.fig, self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=4, column=0, columnspan=3, sticky="news")

        # Frame for the toolbar
        self.frame_toolbar = ttk.Frame(self.root)
        self.frame_toolbar.grid(row=5, column=0, columnspan=3, sticky="news")
        self.toobar = NavigationToolbar2Tk(self.canvas, self.frame_toolbar)

        self.frm.rowconfigure(4, weight=1)
        self.frm.columnconfigure(0, weight=1)
        
        #self.frm.rowconfigure(tuple(range(5)), weight=1)
        #self.frm.columnconfigure(tuple(range(3)), weight=1)


        self.root.mainloop()
    def add_force(self, name, pos, val, ang):
        self.forces.append({'pos': pos, 'val': -val, 'ang': ang, 'typ': False, 'name': name})
    def drawCirc(self, ax, radius, centX, centY, angle_, theta2_, color_='black'):
        #========Line
        arc = Arc([centX,centY],radius,radius,angle=angle_,
              theta1=0,theta2=theta2_,capstyle='round',linestyle='-', lw=2, color=color_)
        ax.add_patch(arc)

        #========Create the arrow head
        endX=centX+(radius/2)*np.cos(rad(theta2_+angle_)) #Do trig to determine end position
        endY=centY+(radius/2)*np.sin(rad(theta2_+angle_))

        ax.add_patch(                    #Create triangle as arrow head
            RegularPolygon(
                (endX, endY),            # (x,y)
                3,                       # number of vertices
                radius/9,                # radius
                rad(angle_+theta2_),     # orientation
                color=color_
            )
        )
        ax.set_xlim([centX-radius,centY+radius]) and ax.set_ylim([centY-radius,centY+radius]) 
        # Make sure you keep the axes scaled or else arrow will distort
    def plot_traeger(self):
        for i in self.forces:
            self.make_arrows(i)

        #self.drawCirc(self.ax, 1, self.festlager[0], self.festlager[1], 0, 250, 'green')

        # Add Moment arrow
        style = "Simple, tail_width=0.5, head_width=4, head_length=8"
        kw = dict(arrowstyle=style, color="g")
        #a3 = FancyArrowPatch((self.festlager[0]+0.6, self.festlager[1]+0.4), (self.festlager[0]-0.6, self.festlager[1]+0.4),
        #                     connectionstyle="arc3,rad=.6", **kw)
        # self.ax.add_patch(a3)

        # Plot xlim and ylim

        #ax_x_max = np.max(self.fx)
        #ax_x_min = np.min(self.fx)
        #ax_y_max = np.max(self.fy)
        #ax_y_min = np.min(self.fy)
        #print('xmax', ax_x_max, 'xmin', ax_x_min, 'ymax', ax_y_max, 'ymin', ax_y_min)

        #ax_x = [np.min(self.x_check) + np.min(self.fx), np.max(self.x_check) + np.max(self.fx)] # self.lenx + 
        #ax_y = [np.min(self.y_check) + np.min(self.fy), np.max(self.y_check) + np.max(self.fy)] # self.leny +

        #print(ax_x, ax_y)

        # self.ax.axis(ax_x + ax_y)
        #self.ax.set(xlim=ax_x, ylim=ax_y)

        #figManager = plt.get_current_fig_manager()
        #figManager.window.showMaximized()
        self.canvas.draw_idle()
        self.canvas.flush_events()
        #plt.show()
 
    def make_all(self):
        self.forces = []
        self.add_force("F1", [1, 0], 10, np.pi / 2.)
        self.add_force("F2", [1, 0], 20, np.pi / 2. )
        self.add_force("F3", [2, 0], 15, np.pi /2.)
        self.add_force("F3", [1, 0], 18, np.pi /2.)

        self.calc()
        self.plot_traeger()


if __name__ == '__main__':
    app = traeger(10., 1.)  