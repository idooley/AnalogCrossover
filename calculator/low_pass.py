#!/opt/local/bin/python3.4
# Loads some common capacitor and resistor values and then exhaustively searches the space of possible combinations to find a good combination.

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

def resistancesComposedOfTwoResistors(x) : 
   results = sortedset()
#   for v in x:
#      results.add(v)

   for v1 in x:
      for v2 in x:
         r = v2/v1;
         if r > 0.7 and r < 1.0/(0.7):
            results.add((v1*v2)/(v1+v2))
   
   return results

def main() :
   if len(sys.argv) != 2:
      sys.stderr.write ("usage: " + sys.argv[0] + " frequency")
      sys.exit(1)

   capfile = open("capacitorValues.txt", "r")
   resfile = open("resistor_E24_values.txt", "r")

   capValues = []
   for line in capfile.readlines():
      capValues = capValues + [convertToValue(x) for x in re.split("\s*", line) if (x is not None and x is not "")]
   capValues.sort()

   resValues = []
   for line in resfile.readlines():
      resValues = resValues + [convertToValue(x) for x in re.split("\s*", line) if (x is not None and x is not "")]
   resValues.sort()

   # Filter to specific ranges
   resValues = [x for x in resValues if (x >= convertToValue("200") and x <= convertToValue("4K")) ]
   capValues = [x for x in capValues if (x >= convertToValue("200nF") and x <= convertToValue("600nF")) ]

   qTol = 0.0005
   qExpected = 1.0 / math.sqrt(2.0)
   fTol = 2.0
   fExpected = float(sys.argv[1]) # target frequency

   print ("num resistor values: ", len(resValues))
   expandedResValues = resistancesComposedOfTwoResistors(resValues)
   
   print ("num resistor pair values: ", len(expandedResValues))

   resValues1 = expandedResValues
#   resValues2 = resValues
   resValues2 = expandedResValues

   for R1 in resValues1:
      for R2 in resValues2:
         for C2 in capValues:
            C1 = 2.0* C2
            try:
               q = math.sqrt(C1*C2*R1*R2)/(C2*(R1+R2))
               if abs(q - qExpected) < qTol:
                  f = 1.0/(2.0*3.1415927*math.sqrt(C1*C2*R1*R2))
                  if abs(f - fExpected) < fTol:
                     print (R1, R2, C1, C2)
                     print ("q=", q)
                     print ("f=", f)
            except:
               pass
                  
if __name__ == "__main__":
    main()
