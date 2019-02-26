import matplotlib.pyplot as plotter
import math
import csv
import os

old_game_data = open("gamedata.csv", "w")
old_game_data.truncate()
old_game_data.close()

old_game_data = open("madeshots.csv", "w")
old_game_data.truncate()
old_game_data.close()

#old_game_data = open("missedshots.csv", "w")
#old_game_data.truncate()
#old_game_data.close()


# open x-values file, define x-values list
x_values_file = open("data/X Values.txt","r")
x_values_list = []

# open y-values file, define y-values list
y_values_file = open("data/Y Values.txt","r")
y_values_list = []

# open made-values file, define made-values list
made_values_file = open("data/Made.txt","r")
made_values_list = []

# open game-info file, define game info list
game_info_file = open("data/GameInformation.txt","r")
game_info_list = []

made_data_list = [[]]
missed_data_list = [[]]

# read in the x values into a list
for line in x_values_file:
    x_values_list.append(float(line.strip('\n')))

# read in the y values into a list
for line in y_values_file:
    y_values_list.append(float(line.strip('\n')))

# read in the made values into a list
for line in made_values_file:
    made_values_list.append(float(line.strip('\n')))

# read in the game info into a list
for line in game_info_file:
    game_info_list.append(line.strip('\n'))

# create and open a new csv file
with open('gamedata.csv',mode="w") as csv_file:
    writer = csv.writer(csv_file)
    # iterate through the game information and output it to a csv
    for i in range(len(game_info_list)):
        current_row = []
        current_row.extend((game_info_list[i],x_values_list[i],y_values_list[i],made_values_list[i]))
        writer.writerow(current_row)

#with open('gamedata.csv') as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',')
#    line_count = 0
#    with open('madeshots.csv',mode="w") as made_file:
#        with open('missedshots.csv',mode="w") as missed_file:

#            made_writer = csv.writer(made_file)
 #           missed_writer = csv.writer(missed_file)
  #          for row in csv_reader:
   #             if len(row) > 0:
    #                if row[3] == 1:
     #                   made_writer.writerow(row)
      #              else:
       #                 missed_writer.writerow(row)


for x in range(len(x_values_list)):
    if made_values_list[x] == 1:
        print("X")
print(made_data_list)        
plotter.scatter(made_data_list[0][1],made_data_list[0][2])
plotter.show()
