# importing modules



try:
    from cmath import cos, sin, atan
    from numpy import radians as rad
    import numpy as np
    from sympy.solvers import solve
    from sympy import Symbol
    import json
    import itertools
    from sympy import symbols, Eq, solve
    import sys
    import math
    from path import *

    
except ImportError as e:
    print(e)

        #Klasse für parallele Kräfte
class ParallelForce:
        #Methode Konstruktor
    def __init__(self, forces, distance):
        super().__init__()
        #erstellen Liste für Kräfte
        self.forces: list = forces
        #erstellen Liste für Abstände von dem Punkt A
        self.distance: list = distance
        
        # leere Listen to append forces and moment
        self.moments: list = []
        self.forces_H: list = []
        self.m_A :  list = []
        
        self.F_halteKraft = float()
        self.F_hk_abstand = float()

        #Überprüfung der Listen und ob die Werte float oder integer sind
        try:
            if not all(isinstance(i, list) for i in [forces, distance]): raise Exception("\nLists must be provided!")
            if all(isinstance(i, list) for i in [forces, distance]):
                for eingabeAlsTuple in itertools.zip_longest(forces, distance):
                    for value in eingabeAlsTuple:
                        if not isinstance(value, (float, int)): raise Exception("\nList values mus be float or integers!")
                        if value == True or value == False:
                            print(
                                "\nBooleans are subtypes of strings, that means\nif you type True for your list value, it equals = 1, when passing False it is 0!\n")
        except ValueError as e:
            print(e)
        self.calcHoldingForce()
        
        #Methode für Berechnung der Momenten, Haltekraft und Position der Haltekraft vom Punkt A        
    def calcHoldingForce(self):
        F_H = float()
        
        try:
            for forces, distance in zip(self.forces, self.distance):
        #Moment berechnen, als Produkt der Kraft und des Abstands               
                m_A = np.real(forces * distance)

        #Haltekraft berechnen, als Summe aller Kräften
                F_H = sum(self.forces)
                self.moments.append(m_A)
                self.forces_H.append(F_H)
                MA_summe : float
        #Summe der Momenten berechnen
                MA_summe = sum(self.moments)
        #Division von Summer der Momemnten und der Haltekraft ergibt die Position der Haltekraft von dem Punkt A
                r_A = MA_summe/F_H
                
            numOf_forces = len(self.forces_H) 
            # print("Der Moment beträgt: ", MA , "Nm")
            #print("Die Haltekraft beträgt: ", "%.2f" %F_H , "N")
            #print("Position der Halterkraft bezüglich des Punktes A : ","%.2f" % r_A , "m")
            
            #Dictionary - JSON File - speichert die Werte und Ergebnisse
            
            self.F_halteKraft = round((F_H), 2) 
            self.F_hk_abstand = round((r_A), 2) 
            
            parallelForcesExampleDict = {
                    "Example": [
                        {
                            "Anzahl der Kraeften": numOf_forces,
                            "Kraefte in N" : self.forces, 
                            "Abstaende in m"  : self.distance,
                            "Momente in Nm": self.moments
                        },
                        {
                            "Ergebnisse": {
                                "Halterkraft in N": "%.2f" % F_H ,
                                "Abstand der Halterkraft von dem Punkt A in m": "%.2f" % r_A 
                            }
                        }
                    ]
                }

                # store in json file
                #print(parallelForcesExampleDict)
            with open(PATH_PARALLEL_JSON, "w") as outfile:
                    json.dump(parallelForcesExampleDict, outfile, indent=4)
            
            
        except ValueError as e:
                    print(e)
        finally: return    self.F_halteKraft, self.F_hk_abstand
            
#Objekt Parallele Kräfte erzeugen    
#ParallelForceObject = ParallelForce([10, 20, 15, 100], [10, 2, 4, 5])
            
            