# importing modules
try:
    from cmath import cos, sin
    from numpy import radians as rad
    import numpy as np
    from sympy.solvers import solve
    from sympy import Symbol
    import json
    import itertools
    from path import *
    

except ImportError as e:
    print(e)

# Class Porter
class PorterOnTwoSupport:
    def __init__(self, forces, angles, distances, barLength):
        super().__init__()
        self.forces: list = forces
        self.angles: list = angles
        self.distances: list = distances
        self.barLength: float = barLength

        # empty lists to append forces and torques
        self.forceY: list = []
        self.forceX: list = []
        self.torques: list = []
        
        # to check if lists are passed and also if the list values are floats or ints
        try:
            if not all(isinstance(i, list) for i in [forces, angles, distances]):raise Exception("\nLists must be provided!")
            if all(isinstance(i, list) for i in [forces, angles, distances]):
                for eingabeAlsTuple in itertools.zip_longest(forces, angles, distances):
                    for value in eingabeAlsTuple:
                        if not isinstance(value, (float, int)):raise Exception("\nList values mus be float or integers!")
                        if value == True or value == False:
                            print(
                                "\nBooleans are subtypes of strings, that means\nif you type True for your list value, it equals = 1, when passing False it is 0!\n")
            if not isinstance(barLength, (float, int)):
                print("\nThe bar length must be a float or integer!")
        except ValueError as e:
            print(e)
        #self.calcBearingForces()

        # Bearing reaction forces
        # fixed bearing force in point A, consisting of an x and y
        # component and a loose bearing in point B with the bearing force F_By
        self.F_Ay = float()
        self.F_Ax = float()
        self.F_By = float()

    # method to calculate the bearing forces
    def calcBearingForces(self) -> tuple[float, float, float]:
        try:
            FA_y_calculated = float()
            F_Ax_calculated = float()
            F_By_calculated = float()
            carrier_Example_Dict = dict()

            # iterating through 3 lists and zipping their values together, like coordinates
            for force, angle, distance in zip(self.forces, self.angles, self.distances):

                # adding 180° to get the correct angle of the force and multiplying
                # the value with sin(angle) to get the y component of the force or with cos(angle) to get the x component of the force
                angle = rad(angle + 180)
                force_x = np.real(force*(cos(angle)))
                force_y = np.real(force*(sin(angle)))
                torque = force_y*distance

                # appending the calculated forces (in x and y) and the torques in lists
                self.forceX.append(round((force_x), 2))
                self.forceY.append(round((force_y), 2))
                self.torques.append(round((torque), 2))

            # using python implemented solve function for solving math equations
            # you can think of the expressions below being written this way: 2x + 45+  2 = 0
            # whereas x is the unknown variable or in our case: F_By, F_Ax, F_Ay
            F_By = Symbol("F_By")
            F_By_calculated = solve(
                (sum(self.torques) + F_By*self.barLength), F_By)
            F_By_calculated = round(
                (float(' '.join(map(str, F_By_calculated)))), 2)
            #print("\n1. Auflagerkraft F_By = ", F_By_calculated)
            
           

            F_Ax = Symbol("F_Ax")
            F_Ax_calculated = solve((sum(self.forceX) + F_Ax), F_Ax)
            F_Ax_calculated = round(
                (float(' '.join(map(str, F_Ax_calculated)))), 2)
            #print("\n2. Auflagerkraft F_Ax =", F_Ax_calculated)
            
            

            F_Ay = Symbol("F_Ay")
            FA_y_calculated = solve(
                (sum(self.forceY) + F_Ay + F_By_calculated), F_Ay)
            FA_y_calculated = round(
                (float(' '.join(map(str, FA_y_calculated)))), 2)
            #print("\n3. Auflagerkraft F_Ay = ", FA_y_calculated)
            #print("\n")
            numOf_forces = len(self.forceX) + len(self.forceY)
            
            
            # self.result.append(F_By_calculated)
            # self.result.append(FA_y_calculated)
            # self.result.append(F_Ax_calculated)
            #print("hallo")
                        
            # F_By_calculated, F_Ax_calculated and FA_y_calculated are returned as lists
            # why? because in math, sometimes functions may return more than one solutions, e.g. quadratic functions
            # Because the result is returned as a list I had to convert it to a string first and then to a float

            # we initialize the constructor variables
            # then another class can access it, using inheritance or super init method
            self.F_Ay = FA_y_calculated
            self.F_Ax = F_Ax_calculated
            self.F_By = F_By_calculated

            # dictionary to save an example,
            # with an key "Example" and a value which is an
            # array of 2 dictionaries, with the second dictionary in the array
            # having a key of "solution" and a value of an dictionary with key value pairs
            carrier_Example_Dict = {
                "Example": [
                    {
                        "Number of forces": numOf_forces,
                        "Bar length": self.barLength,
                        "Forces along the Y Axis": self.forceY,
                        "Forces along the X Axis": self.forceX,
                        "angles": self.angles
                    },
                    {
                        "solution": {
                            "F_By": F_By_calculated,
                            "F_Ay": FA_y_calculated,
                            "F_Ax": F_Ax_calculated
                        }
                    }
                ]
            }

            # store in json file
            #print(carrier_Example_Dict)
            with open(PATH_TRAEGER_JSON, "w") as outfile:
                json.dump(carrier_Example_Dict, outfile, indent=4)

        except ValueError as e:
            print(e)
        finally:
            return self.F_Ay, self.F_Ax, self.F_By
            
#initializing the class
# PorterExample = PorterOnTwoSupport(
# [200, 100, 50], [120, 250, 405], [10, 245, 34], 540)



