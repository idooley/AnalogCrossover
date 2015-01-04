#!/opt/local/bin/python3.4

# Loads some common resistor values and then exhaustively searches the space of possible combinations to find a good combination.

import re,sys,math,blist
from blist import sortedset

def convertToValue(x) :
   y = x.strip()
   if y.endswith("pF") :
      return float(y.replace("pF","")) * 0.000000000001
   if y.endswith("nF") :
      return float(y.replace("nF","")) * 0.000000001
   if y.endswith("uF") :
      return float(y.replace("uF","")) * 0.000001
   if y.endswith("mF") :
      return float(y.replace("mF","")) * 0.001
   if y.endswith("K") :
      return float(y.replace("K","")) * 1000.0
   if y.endswith("M") :
      return float(y.replace("M","")) *1000000.0
   return float(y)

def resistancesComposedOfTwoResistors(x, target) : 
   for v1 in x:
      for v2 in x:
         r = v2/v1;
         if r > 0.33 and r < 3.0:
            combined = (v1*v2)/(v1+v2)
            error = abs((combined - target)/(target))
            if error < 0.01:
               print ("" + str(combined) + " is achieved by resistors in parallel: " + str(v1) + ", " + str(v2) + " error = " + str(error))

def main() :

   resfile = open("resistor_E24_values.txt", "r")

   resValues = []
   for line in resfile.readlines():
      resValues = resValues + [convertToValue(x) for x in re.split("\s*", line) if (x is not None and x is not "")]
   resValues.sort()

   # Filter to specific ranges
   resValues = [x for x in resValues if (x >= convertToValue("100") and x <= convertToValue("100K")) ]

   resistancesComposedOfTwoResistors(resValues, float(sys.argv[1]))


if __name__ == "__main__":
    main()
