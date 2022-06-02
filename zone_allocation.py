import sys

orig_stdout = sys.stdout
f = open('temp_out.txt', 'w')
sys.stdout = f


import csv

filename = 'all_data.csv'

data = []

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        # print(row)
        data.append(row)

# print(data)

data[0].append('alloted_zone')
data[0].append('alloted_zone_code')
data[0].append('alloted_from_category')

data[0].append('possible_Zone_allocation_fromUR')
data[0].append('possible_Zone_allocation_fromUR_Code')
data[0].append('possible_Zone_allocation_fromUR_preferenceNumber')

data[0].append('possible_Zone_allocation_fromCat1')
data[0].append('possible_Zone_allocation_fromCat1_Code')
data[0].append('possible_Zone_allocation_fromCat1_preferenceNumber')

print(data[0])


cat = {
    '0' : 'EWS',
    '1' : 'SC',
    '2' : 'ST',
    '3' : 'ESM',
    '4' : 'OH',
    '5' : 'HH',
    '6' : 'OBC',
    '7' : 'VH',
    '8' : 'Other-PWD',
    '9' : 'UR',
}

zone_vacancy = {
    'Q' : {
        'zone': 'Vadodara',
        'vac': {
          'UR': 52,
          'OBC': 51,
          'EWS': 13,
          'SC': 38,
          'ST': 19,
          'OH': 3,
          'HH': 4,
          'UR_cutoff': -1,
          'OBC_cutoff': -1,
          'EWS_cutoff': -1,
          'SC_cutoff': -1,
          'ST_cutoff': -1,
          'OH_cutoff': -1,
          'HH_cutoff': -1
        }
    },
    'M' : {
        'zone': 'Mumbai',
        'vac': {
          'UR': 199,
          'OBC': 138,
          'EWS': 51,
          'SC': 76,
          'ST': 39,
          'OH': 8,
          'HH': 8,
          'UR_cutoff': -1,
          'OBC_cutoff': -1,
          'EWS_cutoff': -1,
          'SC_cutoff': -1,
          'ST_cutoff': -1,
          'OH_cutoff': -1,
          'HH_cutoff': -1
        }
    },
    'G' : {
        'zone': 'Goa',
        'vac': {
          'UR': 4,
          'OBC': 10,
          'EWS': 2,
          'SC': 2,
          'ST': 3,
          'OH': 1,
          'HH': 1,
          'UR_cutoff': -1,
          'OBC_cutoff': -1,
          'EWS_cutoff': -1,
          'SC_cutoff': -1,
          'ST_cutoff': -1,
          'OH_cutoff': -1,
          'HH_cutoff': -1
        }
    },
    'J' : {
        'zone': 'Jaipur',
        'vac': {
          'UR': 16,
          'OBC': 12,
          'EWS': 4,
          'SC': 7,
          'ST': 1,
          'OH': 1,
          'HH': 1,
          'UR_cutoff': -1,
          'OBC_cutoff': -1,
          'EWS_cutoff': -1,
          'SC_cutoff': -1,
          'ST_cutoff': -1,
          'OH_cutoff': -1,
          'HH_cutoff': -1
        }
    },
    'F' : {
        'zone': 'Delhi',
        'vac': {
          'UR': 105,
          'OBC': 69,
          'EWS': 25,
          'SC': 38,
          'ST': 19,
          'OH': 5,
          'HH': 5,
          'UR_cutoff': -1,
          'OBC_cutoff': -1,
          'EWS_cutoff': -1,
          'SC_cutoff': -1,
          'ST_cutoff': -1,
          'OH_cutoff': -1,
          'HH_cutoff': -1
        }
    },
    'I' : {
        'zone': 'Hyderabad',
        'vac': {
          'UR': 1,
          'OBC': 0,
          'EWS': 0,
          'SC': 0,
          'ST': 1,
          'OH': 0,
          'HH': 0,
          'UR_cutoff': -1,
          'OBC_cutoff': -1,
          'EWS_cutoff': -1,
          'SC_cutoff': -1,
          'ST_cutoff': -1,
          'OH_cutoff': -1,
          'HH_cutoff': -1
        }
    },
    'A' : {
        'zone': 'Bangalore',
        'vac': {
          'UR': 65,
          'OBC': 42,
          'EWS': 15,
          'SC': 22,
          'ST': 15,
          'OH': 3,
          'HH': 3,
          'UR_cutoff': -1,
          'OBC_cutoff': -1,
          'EWS_cutoff': -1,
          'SC_cutoff': -1,
          'ST_cutoff': -1,
          'OH_cutoff': -1,
          'HH_cutoff': -1
        }
    },
    'D' : {
        'zone': 'Chandigarh',
        'vac': {
          'UR': 107,
          'OBC': 72,
          'EWS': 27,
          'SC': 40,
          'ST': 20,
          'OH': 4,
          'HH': 3,
          'UR_cutoff': -1,
          'OBC_cutoff': -1,
          'EWS_cutoff': -1,
          'SC_cutoff': -1,
          'ST_cutoff': -1,
          'OH_cutoff': -1,
          'HH_cutoff': -1
        }
    },
    'B' : {
        'zone': 'Bhopal',
        'vac': {
          'UR': 46,
          'OBC': 28,
          'EWS': 10,
          'SC': 15,
          'ST': 7,
          'OH': 3,
          'HH': 2,
          'UR_cutoff': -1,
          'OBC_cutoff': -1,
          'EWS_cutoff': -1,
          'SC_cutoff': -1,
          'ST_cutoff': -1,
          'OH_cutoff': -1,
          'HH_cutoff': -1
        }
    },
    'L' : {
        'zone': 'Lucknow',
        'vac': {
          'UR': 60,
          'OBC': 35,
          'EWS': 18,
          'SC': 22,
          'ST': 0,
          'OH': 2,
          'HH': 2,
          'UR_cutoff': -1,
          'OBC_cutoff': -1,
          'EWS_cutoff': -1,
          'SC_cutoff': -1,
          'ST_cutoff': -1,
          'OH_cutoff': -1,
          'HH_cutoff': -1
        }
    },
    'P' : {
        'zone': 'Thiruvananthapuram',
        'vac': {
          'UR': 14,
          'OBC': 3,
          'EWS': 2,
          'SC': 7,
          'ST': 3,
          'OH': 1,
          'HH': 0,
          'UR_cutoff': -1,
          'OBC_cutoff': -1,
          'EWS_cutoff': -1,
          'SC_cutoff': -1,
          'ST_cutoff': -1,
          'OH_cutoff': -1,
          'HH_cutoff': -1
        }
    },
    'E' : {
        'zone': 'Chennai',
        'vac': {
          'UR': 128,
          'OBC': 24,
          'EWS': 22,
          'SC': 29,
          'ST': 18,
          'OH': 4,
          'HH': 4,
          'UR_cutoff': -1,
          'OBC_cutoff': -1,
          'EWS_cutoff': -1,
          'SC_cutoff': -1,
          'ST_cutoff': -1,
          'OH_cutoff': -1,
          'HH_cutoff': -1
        }
    },
    'C' : {
        'zone': 'Bhubaneshwar',
        'vac': {
          'UR': 50,
          'OBC': 42,
          'EWS': 11,
          'SC': 20,
          'ST': 10,
          'OH': 3,
          'HH': 2,
          'UR_cutoff': -1,
          'OBC_cutoff': -1,
          'EWS_cutoff': -1,
          'SC_cutoff': -1,
          'ST_cutoff': -1,
          'OH_cutoff': -1,
          'HH_cutoff': -1
        }
    },
    'O' : {
        'zone': 'Ranchi',
        'vac': {
          'UR': 2,
          'OBC': 20,
          'EWS': 3,
          'SC': 7,
          'ST': 3,
          'OH': 1,
          'HH': 1,
          'UR_cutoff': -1,
          'OBC_cutoff': -1,
          'EWS_cutoff': -1,
          'SC_cutoff': -1,
          'ST_cutoff': -1,
          'OH_cutoff': -1,
          'HH_cutoff': -1
        }
    },
    'K' : {
        'zone': 'Kolkata',
        'vac': {
          'UR': 43,
          'OBC': 13,
          'EWS': 8,
          'SC': 13,
          'ST': 12,
          'OH': 2,
          'HH': 2,
          'UR_cutoff': -1,
          'OBC_cutoff': -1,
          'EWS_cutoff': -1,
          'SC_cutoff': -1,
          'ST_cutoff': -1,
          'OH_cutoff': -1,
          'HH_cutoff': -1
        }
    },
    'H' : {
        'zone': 'Guwahati',
        'vac': {
          'UR': 44,
          'OBC': 0,
          'EWS': 15,
          'SC': 0,
          'ST': 17,
          'OH': 1,
          'HH': 1,
          'UR_cutoff': -1,
          'OBC_cutoff': -1,
          'EWS_cutoff': -1,
          'SC_cutoff': -1,
          'ST_cutoff': -1,
          'OH_cutoff': -1,
          'HH_cutoff': -1
        }
    }
}

print("########################################################################")
print("      OH & HH Candidates     ")
print("########################################################################")

# first do zone allocation for hh and oh candidates
for row in data[1:]:

  alloted_zone = ''
  alloted_zone_code = ''
  alloted_from_category = ''
  
  if row[6] == '4' or row[6] == '5':
    print("Name: ", row[1])
    print("AIR: ", row[7])
    print("Cat 1:", cat[row[3]])
    print("Cat Sel:", cat[row[6]])
    pref = row[8:24]
    print("Preferences: ", pref)
    tracker = 0
    for i in pref:
      if i in zone_vacancy.keys():
        tracker = tracker + 1
        # check if respected category seats are available in zone then check if horizontal reservation seats are available
        if zone_vacancy[i]['vac'][cat[row[3]]] > 0:
          if zone_vacancy[i]['vac'][cat[row[6]]] > 0:
            # print("initial vacancy position")
            # print(zone_vacancy[i])
            alloted_zone_code = i
            alloted_zone = zone_vacancy[i]['zone']
            alloted_from_category = row[6]
            print('Preference Number: ', tracker)
            print('Alloted Zone: ', alloted_zone)
            print('Alloted from category: ', cat[alloted_from_category])
            
            # now first reduce vertical vacancy and then reduce horizontal vacancy
            zone_vacancy[i]['vac'][cat[row[6]]] = zone_vacancy[i]['vac'][cat[row[6]]] - 1
            zone_vacancy[i]['vac'][cat[row[3]]] = zone_vacancy[i]['vac'][cat[row[3]]] - 1

            # update zone cutoff
            if zone_vacancy[i]['vac'][cat[row[6]]] == 0 and row[6] == '4':
              zone_vacancy[i]['vac']['OH_cutoff'] = row[7]
            
            if zone_vacancy[i]['vac'][cat[row[6]]] == 0 and row[6] == '5':
              zone_vacancy[i]['vac']['HH_cutoff'] = row[7]
            
            if zone_vacancy[i]['vac'][cat[row[3]]] == 0 and row[3] == '0':
              zone_vacancy[i]['vac']['EWS_cutoff'] = row[7]
            
            if zone_vacancy[i]['vac'][cat[row[3]]] == 0 and row[3] == '1':
              zone_vacancy[i]['vac']['SC_cutoff'] = row[7]

            if zone_vacancy[i]['vac'][cat[row[3]]] == 0 and row[3] == '2':
              zone_vacancy[i]['vac']['ST_cutoff'] = row[7]

            if zone_vacancy[i]['vac'][cat[row[3]]] == 0 and row[3] == '6':
              zone_vacancy[i]['vac']['OBC_cutoff'] = row[7]

            if zone_vacancy[i]['vac'][cat[row[3]]] == 0 and row[3] == '9':
              zone_vacancy[i]['vac']['UR_cutoff'] = row[7]


            # print("after vacancy position")
            # print(zone_vacancy[i])

            print(' \n ======================================================================== [loop1]\n')
            break
    # APPEND TO ROW
    row.append(alloted_zone)
    row.append(alloted_zone_code)
    row.append(cat[alloted_from_category])
    print(row)

print("########################################################################")
print("      All Other Candidates     ")
print("########################################################################")

# then do zone allocation for rest

for row in data[1:]:

  alloted_zone = ''
  alloted_zone_code = ''
  alloted_from_category = ''

  # for normal candidated selected in his own category
  if row[3] == row[6]:
    print("Name: ", row[1])
    print("AIR: ", row[7])
    print("Cat 1:", cat[row[3]])
    print("Cat Sel:", cat[row[6]])
    pref = row[8:24]
    print("Preferences: ", pref)
    tracker = 0

    for i in pref:
      if i in zone_vacancy.keys():
        tracker = tracker + 1
        # check if respected category seats are available in zone
        if zone_vacancy[i]['vac'][cat[row[6]]] > 0:

          print("initial vacancy position")
          print(zone_vacancy[i])

          alloted_zone_code = i
          alloted_zone = zone_vacancy[i]['zone']
          alloted_from_category = row[6]

          print('Preference Number: ', tracker)
          print('Alloted Zone: ', alloted_zone)
          print('Alloted from category: ', cat[alloted_from_category])

          # now reduce horizontal vacancy
          zone_vacancy[i]['vac'][cat[row[6]]] = zone_vacancy[i]['vac'][cat[row[6]]] - 1

          # update zone cutoff          
          if zone_vacancy[i]['vac'][cat[row[3]]] == 0 and row[3] == '0':
            zone_vacancy[i]['vac']['EWS_cutoff'] = row[7]
          
          if zone_vacancy[i]['vac'][cat[row[3]]] == 0 and row[3] == '1':
            zone_vacancy[i]['vac']['SC_cutoff'] = row[7]

          if zone_vacancy[i]['vac'][cat[row[3]]] == 0 and row[3] == '2':
            zone_vacancy[i]['vac']['ST_cutoff'] = row[7]

          if zone_vacancy[i]['vac'][cat[row[3]]] == 0 and row[3] == '6':
            zone_vacancy[i]['vac']['OBC_cutoff'] = row[7]

          if zone_vacancy[i]['vac'][cat[row[3]]] == 0 and row[3] == '9':
            zone_vacancy[i]['vac']['UR_cutoff'] = row[7]

          print("after vacancy position")
          print(zone_vacancy[i])

          # APPEND TO ROW
          row.append(alloted_zone)
          row.append(alloted_zone_code)
          row.append(cat[alloted_from_category])
          print(row)

          print(' \n ======================================================================== [loop2-cat1=catsel]\n')
          break
      else:
        print(row)
        print("Form not filled by candidate")
        # APPEND TO ROW
        row.append('Form Not Filled By Candidate')
        row.append('Form Not Filled By Candidate')
        row.append('Form Not Filled By Candidate')
        print(row)

        print(' \n ======================================================================== [if_cond_formfill_check]\n')
        break
    
    if alloted_zone == '' and tracker >= 16:
      print("Candidate could not be alloted zone in respective category due to own merit student adjustments")
      # APPEND TO ROW
      row.append('Could not be allocated zone due to own merit adjustment')
      row.append('Could not be allocated zone due to own merit adjustment')
      row.append('Could not be allocated zone due to own merit adjustment')
      print(row)

      print(' \n ======================================================================== [own_merit_check]\n')
  
  # else:
  #   print(row)
  #   print(row[3])
  #   print(row[6])

  # for reserved but selected as UR
  if row[3] != row[6] and row[6] == '9':

    # print("initial vacancy position")
    # print(zone_vacancy[i])

    possible_allocation_fromUR = ''
    possible_allocation_fromUR_code = ''
    possible_allocation_fromCat1 = ''
    possible_allocation_fromCat1_code = ''

    print("Name: ", row[1])
    print("AIR: ", row[7])
    print("Cat 1:", cat[row[3]])
    print("Cat Sel:", cat[row[6]])
    pref = row[8:24]
    print("Preferences: ", pref)
    ur_tracker = 0
    cat_tracker = 0
    # first allocate from UR
    for i in pref:  
      if i in zone_vacancy.keys():
        ur_tracker = ur_tracker + 1
        # check if ur seats are available in zone
        if zone_vacancy[i]['vac'][cat[row[6]]] > 0:
          possible_allocation_fromUR = zone_vacancy[i]['zone']
          possible_allocation_fromUR_code = i
          print("Possible allocation from UR: ", possible_allocation_fromUR)
          print("Possible preference number that can be allocated from UR: ", ur_tracker)
          break
      else:
        print(row)
        print("Form not filled by candidate")
        # APPEND TO ROW
        row.append('Form Not Filled By Candidate')
        row.append('Form Not Filled By Candidate')
        print(row)
        print(' \n ======================================================================== [formfill_check_cat1!=catsel_part1]\n')
        break
 
    # then allocate from category
    for i in pref:  
      if i in zone_vacancy.keys():
        cat_tracker = cat_tracker + 1
        # check if ur seats are available in zone
        if zone_vacancy[i]['vac'][cat[row[3]]] > 0:
          possible_allocation_fromCat1 = zone_vacancy[i]['zone']
          possible_allocation_fromCat1_code = i
          print("Possible allocation from Cat1: ", possible_allocation_fromCat1)
          print("Possible preference number that can be allocated from Cat1: ", cat_tracker)
          break
      else:
        print(row)
        print("Form not filled by candidate")
        # APPEND TO ROW
        row.append('Form Not Filled By Candidate')
        print(row)
        print(' \n ======================================================================== [formfill_check_cat1!=catsel_part2]\n')
        break

    # compare two trackers and allocate whichever is lower
    if cat_tracker < ur_tracker:
      print("Allocating from cat1: ", row[3])
      print('cat tracker: ', cat_tracker)
      print('ur tracker: ', ur_tracker)
      alloted_zone = possible_allocation_fromCat1
      alloted_zone_code = possible_allocation_fromCat1_code
      alloted_from_category = row[3]
      # now reduce vacancy position
      zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] = zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] - 1
      # update zone cutoff          
      if zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] == 0 and row[3] == '0':
        zone_vacancy[alloted_zone_code]['vac']['EWS_cutoff'] = row[7]
      
      if zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] == 0 and row[3] == '1':
        zone_vacancy[alloted_zone_code]['vac']['SC_cutoff'] = row[7]

      if zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] == 0 and row[3] == '2':
        zone_vacancy[alloted_zone_code]['vac']['ST_cutoff'] = row[7]

      if zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] == 0 and row[3] == '6':
        zone_vacancy[alloted_zone_code]['vac']['OBC_cutoff'] = row[7]

      if zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] == 0 and row[3] == '9':
        zone_vacancy[alloted_zone_code]['vac']['UR_cutoff'] = row[7]

      # print("after vacancy position")
      # print(zone_vacancy[alloted_zone_code])

      # APPEND TO ROW
      row.append(alloted_zone)
      row.append(alloted_zone_code)
      row.append(cat[alloted_from_category])

      row.append(possible_allocation_fromUR)
      row.append(possible_allocation_fromUR_code)
      row.append(ur_tracker)

      row.append(possible_allocation_fromCat1)
      row.append(possible_allocation_fromCat1_code)
      row.append(cat_tracker)

      print(row)

      print(' \n ======================================================================== [if_cat_pref<ur_pref]\n')
      # break

    else:
      print("Allocating from unreserved cat: ", row[6])
      print('cat tracker: ', cat_tracker)
      print('ur tracker: ', ur_tracker)
      alloted_zone = possible_allocation_fromUR
      alloted_zone_code = possible_allocation_fromUR_code
      alloted_from_category = row[6]
      # now reduce vacancy position
      zone_vacancy[alloted_zone_code]['vac'][cat[row[6]]] = zone_vacancy[alloted_zone_code]['vac'][cat[row[6]]] - 1
      # update zone cutoff          

      if zone_vacancy[alloted_zone_code]['vac'][cat[row[6]]] == 0 and row[6] == '9':
        zone_vacancy[alloted_zone_code]['vac']['UR_cutoff'] = row[7]

      # print("after vacancy position")
      # print(zone_vacancy[alloted_zone_code])

      # APPEND TO ROW
      row.append(alloted_zone)
      row.append(alloted_zone_code)
      row.append(cat[alloted_from_category])

      row.append(possible_allocation_fromUR)
      row.append(possible_allocation_fromUR_code)
      row.append(ur_tracker)

      row.append(possible_allocation_fromCat1)
      row.append(possible_allocation_fromCat1_code)
      row.append(cat_tracker)

      print(row)

      print(' \n ======================================================================== [if_cat_pref>ur_pref]\n')
      # break

  # row.append(alloted_zone)
  # row.append(alloted_zone_code)
  # row.append(alloted_from_category)


print(zone_vacancy)

sys.stdout = orig_stdout
f.close()


writefilename = 'output.csv'

# with open(writefilename, 'r') as csvfile:
#     datareader = csv.reader(csvfile)
#     for row in datareader:
#         # print(row)
#         data.append(row)

file = open(writefilename, 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(data) 