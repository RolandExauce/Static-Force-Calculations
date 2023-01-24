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

      # Klasse für Zentralkraftsystem
class CentralForce:
      
      #Methode Konstruktor
    def __init__(self, forces, angles):
        super().__init__()
        self.forces: list = forces
        self.angles: list = angles

        # empty lists to append forces 
        self.forceY: list = []
        self.forceX: list = []
        
        #Überprüfung der Listen und ob die Werte float oder integer sind
        try:
            if not all(isinstance(i, list) for i in [forces, angles]): raise Exception("\nLists must be provided!")
            if all(isinstance(i, list) for i in [forces, angles]):
                for eingabeAlsTuple in itertools.zip_longest(forces, angles):
                    for value in eingabeAlsTuple:
                        if not isinstance(value, (float, int)): raise Exception("\nList values mus be float or integers!")
                        if value == True or value == False:
                            print(
                                "\nBooleans are subtypes of strings, that means\nif you type True for your list value, it equals = 1, when passing False it is 0!\n")
        except ValueError as e:
            print(e)
        self.calcResultantForce()
                
        # self.F_res_Angle = float()
        # self.F_Res = float()
        
    # Methode für Berechnung der resultierenden Kraft 
    def calcResultantForce(self)->tuple[float, float]:
        
        Fx = float()
        Fy = float()
        F_res = float()
        F_res_angle = float()
        
        try:
            for force, angle in zip(self.forces, self.angles):
                # Kräfte zur Achse X und Y berechnen
                fx = force *np.real(cos(rad(angle)))
                fy = force *np.real( sin( rad(angle)))
                self.forceY.append(fy)
                self.forceX.append(fx)
                
              
                
            #Summe aller Kräften zur Achse X und Y berechnen
                Fx = sum(self.forceX)
                Fy = sum(self.forceY)
            #Resultierenden Winkel berechnen    
            F_res_angle =   round((math.degrees(math.atan(Fy/Fx))), 2)
            #Resultierende Kraft berechnen
            #math.degrees((np.arctan(Fx/Fy)).real)
            F_res = round((math.sqrt(pow(Fx, 2)+  pow(Fy, 2))), 2)
            numOf_forces = len(self.forces)
            #Ergebnisse ausgeben
            # print("\nDas ist die resultierende Kraft: ","%.2f" % F_res)
            # print("\n")
            # print("Winkel der resultierenden Kraft","%.2f" % F_res_angle)
            # print("\n")
            
            
            # self.F_Res = F_res
            # self.F_res_Angle = F_res_angle

            # print( self.Fres)
            # print(self.Fres_angle)
            
            # Dictionary für JSON erstellen, hier werden die Eingaben und Ergebnisse gespeichert
            centralForcesExampleDict = {
                    "Example": [
                        {
                            "Anzahl der Kreaeften": numOf_forces,
                            " Kraefte " : self.forces,
                            "Kraefte zu Y Achse": self.forceY,
                             "Kraefte zu X Achse": self.forceX,
                             "Winkeln": self.angles
                            
                        },
                        {
                            "Ergebnis": {
                                "Resultierende Kraft": "%.2f" % F_res,
                                "Winkel der Resultierende": "%.2f" % F_res_angle
                            }
                        }
                    ]
                }

            # print JSON Dictionary
            with open(PATH_ZENTRAL_JSON, "w") as outfile:
                    json.dump(centralForcesExampleDict, outfile, indent=4)

        except ValueError as e:
                    print(e)
        finally: return   F_res, F_res_angle 
            # Objekt erzeugen und Werten in Listen eingeben       
#CentralForceObject = CentralForce([400,500,350,450], [45,90,75,130])


