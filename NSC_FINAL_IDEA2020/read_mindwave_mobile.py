import textwrap
import time
from time import sleep

import bluetooth
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader
from mindwavemobile.MindwaveDataPoints import RawDataPoint

Delta = []
Theta = []
LowAlpha = []
HighAlpha = []
LowBeta = []
HighBeta = []
LowGamma = []
MedGamma = []
AttentionLevel = []
PoorSignalLevel = []
Unknowdatapoint = []
MeditationLevel = []
timer  = 1

kill_signal = False
mindwaveDataPointReader = MindwaveDataPointReader()

def bt_init() :
   mindwaveDataPointReader.start()


def check() :
   errorgenerator = 4
   if (mindwaveDataPointReader.isConnected()):
      return True
   else :
      print("it is not connected")
      return False

def start_measure() :
   # mindwaveDataPointReader.start()
   if (mindwaveDataPointReader.isConnected()):    
        while (kill_signal == False):
            dataPoint = mindwaveDataPointReader.readNextDataPoint()
            if (not dataPoint.__class__ is RawDataPoint):
               dataPointlist = str(dataPoint).split(":")
               print(dataPointlist)
               if ('D' in dataPointlist) :
                  Delta.append(dataPointlist[1])
                  Theta.append(dataPointlist[3])
                  LowAlpha.append(dataPointlist[5])
                  HighAlpha.append(dataPointlist[7])
                  LowBeta.append(dataPointlist[9])
                  HighBeta.append(dataPointlist[11])
                  LowGamma.append(dataPointlist[13])
                  MedGamma.append(dataPointlist[15])
               elif ('UOV' in dataPointlist) :
                  Unknowdatapoint.append(dataPointlist[1])
               elif ('AL' in dataPointlist) :
                  AttentionLevel.append(dataPointlist[1])
               elif ('ML' in dataPointlist) :
                  MeditationLevel.append(dataPointlist[1])
               elif ('PSL' in dataPointlist) :
                  PoorSignalLevel.append(dataPointlist[1])
            print(Delta)
            print(Theta)
            print(LowAlpha)
            print(HighAlpha)
            print(LowBeta)
            print(HighBeta)
            print(LowGamma)
            print(MedGamma)
            print(AttentionLevel)
            print(PoorSignalLevel)
            print(Unknowdatapoint)
            print("running")
            # try :
            #    # print(MeditationLevel[-1])
            #    # if MeditationLevel[-1] > 10:
            #    # #    print("that is it")
            #    #    pyautogui.press("w")
            # except : 
            #    print("")
   else:
      print((textwrap.dedent("""\
         Exiting because the program could not connect
         to the Mindwave Mobile device.""").replace("\n", " ")))
