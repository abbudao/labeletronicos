from math import log10
while (True):
    i = input()
    o = input()
    print("V_Input:" + i + "V_Output" + o)
    print("Ganho V/V:" + str(float(o) / float(i)))
    print("Ganho em dB:" + str(20 * log10(float(o) / float(i))))
