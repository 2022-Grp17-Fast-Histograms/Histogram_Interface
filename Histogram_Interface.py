import PySimpleGUI as ui
import matplotlib.pyplot as plt
import csv
import numpy as np

layout = [
                [ui.Text("Average", size= 80, justification= 'center'),
                 ui.Text("Variance", size= 80, justification= 'center')],     # Part 2 - The Layout
                [ui.Image(filename= "y_avg_frame1.png", key= 'prev'),
                 ui.Image(filename="y_var_frame1.png", key= 'curr')],
                [ui.Button("Previous", size= 80, ),
                 ui.Button("Next", size= 80)]

             ]

window = ui.Window('window', layout, resizable= True)

y_avg = [[], [], [], [], [], [], [], [], [], []]
u_avg = [[], [], [], [], [], [], [], [], [], []]
v_avg = [[], [], [], [], [], [], [], [], [], []]
y_var = [[], [], [], [], [], [], [], [], [], []]
u_var = [[], [], [], [], [], [], [], [], [], []]
v_var = [[], [], [], [], [], [], [], [], [], []]

w = 0.2
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
bar1 = np.arange(len(x))
bar2 = [i+w for i in bar1]
bar3 = [i+w for i in bar2]

with open('AVERAGE_HISTOGRAM_Y.csv') as y_avg_val:
   y_avg_r = csv.reader(y_avg_val)
   num = 0
   for val in y_avg_r:
       y_avg[num].extend(val)
       num += 1

   for frame in range(len(y_avg)):
       for i in range(len(y_avg[frame])):
           y_avg[frame][i] = int(y_avg[frame][i])

#print(y_avg)
with open('AVERAGE_HISTOGRAM_U.csv') as u_avg_val:
    u_avg_r = csv.reader(u_avg_val)
    num = 0
    for val in u_avg_r:
        u_avg[num].extend(val)
        num += 1

    for frame in range(len(u_avg)):
        for i in range(len(u_avg[frame])):
            u_avg[frame][i] = int(u_avg[frame][i])

with open('AVERAGE_HISTOGRAM_V.csv') as v_avg_val:
    v_avg_r = csv.reader(v_avg_val)
    num = 0
    for val in v_avg_r:
        v_avg[num] = val
        num += 1

    for frame in range(len(v_avg)):
        for i in range(len(v_avg[frame])):

            v_avg[frame][i] = int(v_avg[frame][i])

        plt.bar(bar1, y_avg[frame], w, label="y")
        plt.bar(bar2, u_avg[frame], w, label="u")
        plt.bar(bar3, v_avg[frame], w, label="v")
        plt.title("Avg Frame " + str(frame + 1))
        plt.legend()

        plt.savefig('y_avg_frame' + str(frame + 1) + '.png')
        plt.figure()

with open('VARIANCE_HISTOGRAM_Y.csv') as y_var_val:
    y_var_r = csv.reader(y_var_val)
    num = 0
    for val in y_var_r:
        y_var[num] = val
        num += 1

    for frame in range(len(y_var)):
        for i in range(len(y_var[frame])):
            y_var[frame][i] = int(y_var[frame][i])
with open('VARIANCE_HISTOGRAM_U.csv') as u_var_val:
    u_var_r = csv.reader(u_var_val)
    num = 0
    for val in u_var_r:
        u_var[num] = val
        num += 1

    for frame in range(len(u_var)):
        for i in range(len(u_var[frame])):
            u_var[frame][i] = int(u_var[frame][i])

with open('VARIANCE_HISTOGRAM_V.csv') as v_var_val:
    v_var_r = csv.reader(v_var_val)
    num = 0
    for val in v_var_r:
        v_var[num] = val
        num += 1

    for frame in range(len(v_var)):
        for i in range(len(v_var[frame])):
            v_var[frame][i] = int(v_var[frame][i])

        plt.bar(bar1, y_var[frame], w, label="y")
        plt.bar(bar2, u_var[frame], w, label="u")
        plt.bar(bar3, v_var[frame], w, label="v")

        plt.title('Var Frame ' + str(frame + 1))
        plt.legend()
        plt.savefig('y_var_frame' + str(frame + 1) + '.png')
        plt.figure()

plt.bar(bar1, y_avg[0], w, label = "y")
plt.bar(bar2, u_avg[0], w, label = "u")
plt.bar(bar3, v_avg[0], w, label = "v")
plt.title("Avg Frame 1")
plt.legend()

plt.savefig('y_avg_frame1.png')
plt.figure()

plt.bar(bar1, y_var[0], w, label = "y")
plt.bar(bar2, u_var[0], w, label = "u")
plt.bar(bar3, v_var[0], w, label = "v")
plt.title("Var Frame 1")
plt.legend()
plt.savefig('y_var_frame1.png')
plt.figure()

#plt.show()
frames = 1
frame = 1

while True:
    event, value = window.read()

    if event == 'Exit' or event == ui.WIN_CLOSED:
        break
    elif event == 'Next':

        if frame < 10:
            window['prev'].update(filename='y_avg_frame' + str(frame + 1) + '.png', visible=True)
            window['curr'].update(filename='y_var_frame' + str(frame + 1) + '.png', visible=True)

            window.refresh()
            frame += 1
            print(frame)
        else:
            print()


    elif event == 'Previous':
        #plt.clf()
        if frames < 0:
            window['prev'].update(filename='y_avg_frame' + str(frame - 1) + '.png', visible=True)
            window['curr'].update(filename='y_var_frame' + str(frame - 1) + '.png', visible=True)
            window.refresh()
            frame -= 1
            #frames -= 1

        else:
            print()


window.close()