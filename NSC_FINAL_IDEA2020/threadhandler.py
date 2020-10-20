from time import sleep
import read_mindwave_mobile 
from threading import Thread
class data :
    Delta = []
    Theta = []
    LowAlpha = []
    HighAlpha = []
    LowBeta = []
    HighBeta = []
    LowGamma = []
    MedGamma = []
    AttentionLevel = []
    MeditationLevel = []

def startallfunc() :
    thread1 = Thread(target = read_mindwave_mobile.start_measure)
    thread2 = Thread(target= wait_until_have_enough_data)
    thread1.start()
    thread2.start()
def send_kill_code() :
    read_mindwave_mobile.kill_signal = True
def wait_until_have_enough_data() :
    i = len(read_mindwave_mobile.Delta)+len(read_mindwave_mobile.Theta)+len(read_mindwave_mobile.LowAlpha)+len(read_mindwave_mobile.HighAlpha) + len(read_mindwave_mobile.LowBeta)
    i+= len(read_mindwave_mobile.HighBeta) + len(read_mindwave_mobile.MedGamma) + len(read_mindwave_mobile.AttentionLevel) + len(read_mindwave_mobile.MeditationLevel)
    while read_mindwave_mobile.kill_signal != True and i >=9:
        data.Delta += read_mindwave_mobile.Delta[-1]
        data.Theta += read_mindwave_mobile.Theta[-1]
        data.LowAlpha += read_mindwave_mobile.LowAlpha[-1]
        data.HighAlpha += read_mindwave_mobile.HighAlpha[-1]
        data.LowBeta += read_mindwave_mobile.LowBeta[-1]
        data.HighBeta += read_mindwave_mobile.HighBeta[-1]
        data.LowGamma  += read_mindwave_mobile.LowGamma[-1]
        data.HighBeta += read_mindwave_mobile.HighBeta[-1]
        data.MedGamma += read_mindwave_mobile.MedGamma[-1]
        data.AttentionLevel += read_mindwave_mobile.AttentionLevel[-1]
        data.MeditationLevel += read_mindwave_mobile.MeditationLevel[-1]
def clear_data() :
    data.Delta.clear()
    data.Theta.clear()
    data.LowAlpha.clear()
    data.HighAlpha.clear()
    data.LowBeta.clear()
    data.HighBeta.clear()
    data.LowGamma.clear()
    data.MedGamma.clear()
    data.AttentionLevel.clear()
    data.MeditationLevel.clear()
# def analyse() :