import json 
import csv #can write out a csv for the modes/band plans available
import tkinter #for the GUI

# different modes that can be used for transmission
mode = ["AM","FM","USB","LSB","CW", "SSB","Digital","RTTY","Various","All"]

# Essentially, I'd like to get the settings of the bands, modes and their limits.
# This would then be displayed in the GUI for what is "tuneable" based on license
# tier as well as the band that is being accessed.

tech_band_file= open('tech_bands.json')
tech_band_plan_file = open('tech_band_plans.json')
tech_band_data = json.load(tech_band_file)
tech_band_plan_data= json.load(tech_band_plan_file)

#sample band plan
print('23 CM Band plan: \n')
print(tech_band_plan_data["uhf"]["23 centimeters"])
print('\n')
print('23 CM Privileges: \n')
print(tech_band_data["uhf"]["23 Centimeters"])

with open('band_plan.csv','w', newline ='') as csv:
    fieldnames = ["UpperLimit","LowerLimit","Mode"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(tech_band_plan_data["uhf"]["23 centimeters"])



