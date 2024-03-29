import os
import numpy as np
import re
# from datetime import datetime
from Analysis import Analysis
import matplotlib.pyplot as plt

def function(dir, wlen):
    timelistc = []
    ratelistc1 = []
    ratelistc6 = []

    timelisto = []
    ratelisto1 = []
    ratelisto6 = []

    channelID = [1, 2, 4, 5, 6]

    for filename in os.listdir(dir):
        # Finds time in seconds from first timestamp

        # filename = "Test"+"_"+Wavelength+"-"+Run+"_2023-10-03"+"_"+Hour+"-"+Minute+"-"+Second+".csv"
        # match = re.search(r'\d{2}-\d{2}-\d{2}', filename)
        # date = datetime.strptime(match.group(), '%H:%M:%S').date()

        t = re.split("_", filename)

        if t[1][:6] == 'closed':
            time = (int(t[3][0:2]))*3600 + int(t[3][3:5])*60 + int(t[3][6:8])
            timelistc.append(time)

            # date_object = datetime.strptime(t[2][2:10]+' '+t[3][:8], "%y-%m-%d %H-%M-%S")
            # timelistc.append(date_object)

            # Finds Trigger Rate
            ana = Analysis(wlen)
            df = ana.import_file("C:/Users/lzvio/-bkgd/"+filename, [])
            ratelistc1.append(ana.trig_rate(df, channelID)[0])
            ratelistc6.append(ana.trig_rate(df, channelID)[4])
    
        else:
            time = (int(t[3][0:2]))*3600 + int(t[3][3:5])*60 + int(t[3][6:8])
            timelisto.append(time)

            # Finds Trigger Rate
            ana = Analysis(wlen)
            df = ana.import_file("C:/Users/lzvio/-bkgd/"+filename, [])
            ratelisto1.append(ana.trig_rate(df, channelID)[0])
            ratelisto6.append(ana.trig_rate(df, channelID)[4])

    background = [(sum(ratelistc1[i:i+2])/2) for i in range(0, len(ratelistc1), 2)]
    # print(background)
    for i in range(len(ratelisto1)):
        ratelisto1[i] = ratelisto1[i] - background[i//3]
        ratelisto6[i] = ratelisto6[i] - background[i//3]

    # time_newc = np.array(timelistc) - min(timelistc)

    # time_newc, ratelistc1, ratelistc6 = zip(*sorted(zip(time_newc, ratelistc1, ratelistc6)))

    # plt.scatter(time_newc, ratelistc1, c='b', label='Ch 1')
    # plt.scatter(time_newc, ratelistc6, c='r', label='Ch 6')
    # plt.legend()
    # plt.title('Closed')
    # plt.xlabel('Time (s)')
    # plt.ylabel('Trigger Rate (Hz)')
    # plt.ylim(0, 200)
    # plt.grid()
    # plt.show()
    
    time_newo = np.array(timelisto) - min(timelisto)

    # time_newo, ratelisto1, ratelisto6 = zip(*sorted(zip(time_newo, ratelisto1, ratelisto6)))

    plt.scatter(time_newo, ratelisto1, c='b', label='Ch 1')
    plt.scatter(time_newo, ratelisto6, c='r', label='Ch 6')
    plt.legend()
    plt.title('Open')
    plt.xlabel('Time (s)')
    plt.ylabel('Trigger Rate (Hz)')
    plt.ylim(0, 300)
    plt.grid()
    plt.show()
    
function("C:/Users/lzvio/-bkgd", 1280)



































def function(dir, wlen):
    #closed
    timelistc = []
    ratelistc1 = []
    ratelistc2 = []
    ratelistc6 = []

    #128 nm
    timelisto = []
    ratelisto1 = []
    ratelisto2 = []
    ratelisto6 = []

    #170 nm
    timelisto1 = []
    ratelisto11 = []
    ratelisto21 = []
    ratelisto61 = []

    channelID = [1, 2, 4, 5, 6]

    for filename in os.listdir(dir):
        # Finds time in seconds from first timestamp

        t = re.split("_", filename)

        #Closed
        if t[1][:6] == 'closed':
            time = (int(t[3][0:2]))*3600 + int(t[3][3:5])*60 + int(t[3][6:8])
            timelistc.append(time)

            # Finds Trigger Rate
            ana = Analysis(wlen)
            df = ana.import_file("C:/Users/lzvio/-bkgd/"+filename, [])
            ratelistc1.append(ana.trig_rate(df, channelID)[0])
            ratelistc2.append(ana.trig_rate(df, channelID)[1])
            ratelistc6.append(ana.trig_rate(df, channelID)[4])
                # date_object = datetime.strptime(t[2][2:10]+' '+t[3][:8], "%y-%m-%d %H-%M-%S")
                # timelistc.append(date_object)

        #128 nm
        if t[1][:6] == '1280A3':
            time = (int(t[3][0:2]))*3600 + int(t[3][3:5])*60 + int(t[3][6:8])
            timelisto.append(time)

            # Finds Trigger Rate
            ana = Analysis(wlen)
            df = ana.import_file("C:/Users/lzvio/-bkgd/"+filename, [])
            ratelisto1.append(ana.trig_rate(df, channelID)[0])
            ratelisto2.append(ana.trig_rate(df, channelID)[1])
            ratelisto6.append(ana.trig_rate(df, channelID)[4])

        #170 nm
        if t[1][:6] == '1700A3':
            time = (int(t[3][0:2]))*3600 + int(t[3][3:5])*60 + int(t[3][6:8])
            timelisto1.append(time)

            # Finds Trigger Rate
            ana = Analysis(wlen)
            df = ana.import_file("C:/Users/lzvio/-bkgd/"+filename, [])
            ratelisto11.append(ana.trig_rate(df, channelID)[0])
            ratelisto21.append(ana.trig_rate(df, channelID)[1])
            ratelisto61.append(ana.trig_rate(df, channelID)[4])

    # Closed
    time_newc = np.array(timelistc) - min(timelistc)
    plt.scatter(time_newc, ratelistc1, c='b', label='Ch 1')
    plt.scatter(time_newc, ratelistc2, c='g', label='Ch 2')
    plt.scatter(time_newc, ratelistc6, c='r', label='Ch 6')
    plt.legend(loc='upper left')
    plt.title('Closed')
    plt.xlabel('Time (s)')
    plt.ylabel('Trigger Rate (Hz)')
    plt.ylim(0, 175)
    plt.grid()
    plt.show()
    
    #128 nm
    time_newo = np.array(timelisto) - min(timelisto)
    plt.scatter(time_newo, ratelisto1, c='b', label='Ch 1')
    plt.scatter(time_newo, ratelisto2, c='g', label='Ch 2')
    plt.scatter(time_newo, ratelisto6, c='r', label='Ch 6')
    plt.legend(loc='upper left')
    plt.title('128 nm')
    plt.xlabel('Time (s)')
    plt.ylabel('Trigger Rate (Hz)')
    plt.ylim(0, 600)
    plt.grid()
    plt.show()

    #170 nm
    time_newo1 = np.array(timelisto1) - min(timelisto1)
    plt.scatter(time_newo1, ratelisto11, c='b', label='Ch 1')
    plt.title('170 nm Ch 1')
    plt.xlabel('Time (s)')
    plt.ylabel('Trigger Rate (Hz)')
    plt.ylim(0, 1750)
    plt.grid()
    plt.show()
    #plot Ch 1 separately from other channels
    plt.scatter(time_newo1, ratelisto21, c='g', label='Ch 2')
    plt.scatter(time_newo1, ratelisto61, c='r', label='Ch 6')
    plt.legend(loc='upper left')
    plt.title('170 nm')
    plt.xlabel('Time (s)')
    plt.ylabel('Trigger Rate (Hz)')
    plt.ylim(0, 250)
    plt.grid()
    plt.show()
    
function("C:/Users/lzvio/-bkgd", 1280)
