import sys
import csv
import json


# redirect print statement outputs to file

orig_stdout = sys.stdout
f = open('CGST_out_V2.txt', 'w')
sys.stdout = f


# importing zone preferences data

filename = 'all_data.csv'

data = []

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        # print(row)
        data.append(row)

# print(data)

data[0].append('form_filled_flag')
data[0].append('provisional_joining_flag')

data[0].append('Alloted Zone')
data[0].append('Alloted Zone Code')
data[0].append('Alloted Zone Cat')

data[0].append('Possible Zone Allocation from UR')
data[0].append('Possible Zone Allocation from UR')
data[0].append('Preference Number if Alloted from UR')

data[0].append('Possible Zone Allocation from CAT-1')
data[0].append('Possible Zone Allocation from CAT-1 code')
data[0].append('Preference Number if Alloted from Cat-1')

data[0].append('Possible Zone Allocation from WITHOUT Provisional Status')
data[0].append('Possible Zone Allocation from WITHOUT Provisional Status Code')
data[0].append('Preference Number if Alloted WITHOUT Provisional Status')

data[0].append('Possible Zone Allocation from with Provisional Status')
data[0].append('Possible Zone Allocation from with Provisional Status Code')
data[0].append('Preference Number if Alloted with Provisional Status')

print(data[0])


# hard-coded data (category codes and vacancy positions)
# TODO: import data from file instead of hard-coding them

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
            'UR_rendered_extra': -1,
            'OBC': 51,
            'EWS': 13,
            'SC': 38,
            'ST': 19,
            'OH': 3,
            'HH': 4,
            },
        'cutoff': {
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
            'UR_rendered_extra': -1,
            'OBC': 138,
            'EWS': 51,
            'SC': 76,
            'ST': 39,
            'OH': 8,
            'HH': 8,
        },
        'cutoff': {
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
            'UR_rendered_extra': -1,
            'OBC': 10,
            'EWS': 2,
            'SC': 2,
            'ST': 3,
            'OH': 1,
            'HH': 1,
        },
        'cutoff': {
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
            'UR_rendered_extra': -1,
            'OBC': 12,
            'EWS': 4,
            'SC': 7,
            'ST': 1,
            'OH': 1,
            'HH': 1,
        },
        'cutoff': {
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
            'UR_rendered_extra': -1,
            'OBC': 69,
            'EWS': 25,
            'SC': 38,
            'ST': 19,
            'OH': 5,
            'HH': 5,
        },
        'cutoff': {
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
            'UR_rendered_extra': -1,
            'OBC': 0,
            'EWS': 0,
            'SC': 0,
            'ST': 1,
            'OH': 0,
            'HH': 0,
        },
        'cutoff': {
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
            'UR_rendered_extra': -1,
            'OBC': 42,
            'EWS': 15,
            'SC': 22,
            'ST': 15,
            'OH': 3,
            'HH': 3,
        },
        'cutoff': {
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
            'UR_rendered_extra': -1,
            'OBC': 72,
            'EWS': 27,
            'SC': 40,
            'ST': 20,
            'OH': 4,
            'HH': 3,
        },
        'cutoff': {
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
            'UR_rendered_extra': -1,
            'OBC': 28,
            'EWS': 10,
            'SC': 15,
            'ST': 7,
            'OH': 3,
            'HH': 2,
        },
        'cutoff': {
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
            'UR_rendered_extra': -1,
            'OBC': 35,
            'EWS': 18,
            'SC': 22,
            'ST': 0,
            'OH': 2,
            'HH': 2,
        },
        'cutoff': {
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
            'UR_rendered_extra': -1,
            'OBC': 3,
            'EWS': 2,
            'SC': 7,
            'ST': 3,
            'OH': 1,
            'HH': 0,
        },
        'cutoff': {
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
            'UR_rendered_extra': -1,
            'OBC': 24,
            'EWS': 22,
            'SC': 29,
            'ST': 18,
            'OH': 4,
            'HH': 4,
        },
        'cutoff': {
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
            'UR_rendered_extra': -1,
            'OBC': 42,
            'EWS': 11,
            'SC': 20,
            'ST': 10,
            'OH': 3,
            'HH': 2,
        },
        'cutoff': {
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
            'UR_rendered_extra': -1,
            'OBC': 20,
            'EWS': 3,
            'SC': 7,
            'ST': 3,
            'OH': 1,
            'HH': 1,
        },
        'cutoff': {
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
            'UR_rendered_extra': -1,
            'OBC': 13,
            'EWS': 8,
            'SC': 13,
            'ST': 12,
            'OH': 2,
            'HH': 2,
        },
        'cutoff': {
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
            'UR_rendered_extra': -1,
            'OBC': 0,
            'EWS': 15,
            'SC': 0,
            'ST': 17,
            'OH': 1,
            'HH': 1,
        },
        'cutoff': {
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

# find index number or AIR of last candidate having `catsel=9`
air_of_last_catsel9_candidate = 0
index_of_last_catsel9_candidate = 0

for row in data[1:]:
    if row[6] == '9':
        air_of_last_catsel9_candidate = row[7]
        index_of_last_catsel9_candidate = row[0]

print("\n----------------------------------------------------------------------------\n")
print('    AIR of last candidate selected on UR Seat: ', air_of_last_catsel9_candidate)
print('    Index of last candidate selected on UR Seat: ', index_of_last_catsel9_candidate)
# print(row[int(index_of_last_catsel9_candidate)])
print("\n----------------------------------------------------------------------------\n")


# Setting Flags
# Data Cleanup: Set `form_filled_flag=True` for those who have filled form and `form_filled_flag=False` for those who havent
# Also Set `provisional_joining_flag=False` for all by default, this will be set to True for some candidates later on

print("\n\n############################################################")
print('     CANDIDATES WHO HAVE NOT FILLED PREFERENCE FORM')
print("############################################################\n")

counter = {
    'total': 0,
    'UR': 0,
    'EWS': 0,
    'OBC': 0,
    'SC' : 0,
    'ST': 0
}

for row in data[1:]:
    
    if row[8] in zone_vacancy.keys():
        # first set `form_filled_flag`
        row.append(True)
        # then set `provisional_joining_flag=False`
        row.append(False)
    else:
        print('\n ---------------------------------- \n')
        # increase counters
        counter['total'] = counter['total'] + 1
        counter[cat[row[3]]] = counter[cat[row[3]]] + 1
        # first set `form_filled_flag`
        row.append(False)
        # then set `provisional_joining_flag=False`
        row.append(False)
        # then append form status remark
        row.append('Form_Not_Filled_By_Candidate')
        print("Name: ", row[1])
        print("AIR: ", row[7])
        print("Cat 1:", cat[row[3]])
        print("Cat Sel:", cat[row[6]])
        print(row)

print("\n----------------------------------------------\n")
print('Number of candidates who have not filled data:', json.dumps(counter, indent=4))

# Allocation begins here

# first do allocation for OH and HH candidates (cat-sel = 4 or 5)

print("\n\n########################################################################")
print("      OH & HH Candidates     ")
print("########################################################################")

for row in data[1:]:
    
    alloted_zone = ''
    alloted_zone_code = ''
    alloted_from_category = ''

    # use form filled flag to do allocation for only those who have filled form
    if row[24] and (row[6] == '4' or row[6] == '5'):
        print('\n\n--------------------------------------- \n')
        print("Name: ", row[1])
        print("AIR: ", row[7])
        print("Cat 1:", cat[row[3]])
        print("Cat Sel:", cat[row[6]])
        pref = row[8:24]
        print("Preferences: ", pref)

        tracker = 0

        for i in pref:
            tracker = tracker + 1
            # check if respective category seats are available in the zone then check if horizontal reservation seats are available in the zone
            if zone_vacancy[i]['vac'][cat[row[3]]] > 0:
                if zone_vacancy[i]['vac'][cat[row[6]]] > 0:
                    
                    print("initial vacancy position")
                    print(zone_vacancy[i])

                    alloted_zone_code = i
                    alloted_zone = zone_vacancy[i]['zone']
                    alloted_from_category = cat[row[6]]

                    print('Preference Number: ', tracker)
                    print('Alloted Zone: ', alloted_zone)
                    print('Alloted from category: ', alloted_from_category)

                    # now first reduce vertical vacancy and then reduce horizontal vacancy
                    zone_vacancy[i]['vac'][cat[row[6]]] = zone_vacancy[i]['vac'][cat[row[6]]] - 1
                    zone_vacancy[i]['vac'][cat[row[3]]] = zone_vacancy[i]['vac'][cat[row[3]]] - 1

                    # now update zone cutoff
                    if zone_vacancy[i]['vac'][cat[row[6]]] == 0 and row[6] == '4':
                        zone_vacancy[i]['cutoff']['OH_cutoff'] = row[7]

                    if zone_vacancy[i]['vac'][cat[row[6]]] == 0 and row[6] == '5':
                        zone_vacancy[i]['cutoff']['HH_cutoff'] = row[7]

                    if zone_vacancy[i]['vac'][cat[row[3]]] == 0 and row[3] == '0':
                        zone_vacancy[i]['cutoff']['EWS_cutoff'] = row[7]

                    if zone_vacancy[i]['vac'][cat[row[3]]] == 0 and row[3] == '1':
                        zone_vacancy[i]['cutoff']['SC_cutoff'] = row[7]

                    if zone_vacancy[i]['vac'][cat[row[3]]] == 0 and row[3] == '2':
                        zone_vacancy[i]['cutoff']['ST_cutoff'] = row[7]

                    if zone_vacancy[i]['vac'][cat[row[3]]] == 0 and row[3] == '6':
                        zone_vacancy[i]['cutoff']['OBC_cutoff'] = row[7]

                    if zone_vacancy[i]['vac'][cat[row[3]]] == 0 and row[3] == '9':
                        zone_vacancy[i]['cutoff']['UR_cutoff'] = row[7]

                    print("after vacancy position")
                    print(zone_vacancy[i])
                
                    print(' \n ======================================================================== [loop1]\n')
                    break
        # APPEND TO ROW
        row.append(alloted_zone)
        row.append(alloted_zone_code)
        row.append(alloted_from_category)
        print(row)



# Maintain a counter to allocate fixed number provisional joining status for each category
# This number should be exactly equal to the number of candidates (for each category) who left UR seat (rendering UR seats extra) and took their respective category seat (rendering some candidates surplus)
provisional_counter = {
    'EWS': 0,
    'OBC': 0,
    'SC': 0,
    'ST': 0
}


# Then do allocation for all those selected on UR seats (cat-sel = 9) [this includes all categories selected on UR seat]

print("\n\n########################################################################")
print("      All Candidates Selected on UR Seat (CatSel=9)     ")
print("########################################################################")

for row in data[1:]:
    
    alloted_zone = ''
    alloted_zone_code = ''
    alloted_from_category = ''

    # use form filled flag to do allocation for only those who have filled form
    if row[24] and (row[6] == '9'):
        print('\n\n--------------------------------------- \n')
        print("Name: ", row[1])
        print("AIR: ", row[7])
        print("Cat 1:", cat[row[3]])
        print("Cat Sel:", cat[row[6]])
        pref = row[8:24]
        print("Preferences: ", pref)
        
        tracker = 0
        
        # for UR on UR (cat1 == catsel && catsel = 9)
        if row[3] == row[6]:
            for i in pref:
                tracker = tracker + 1
                if zone_vacancy[i]['vac'][cat[row[6]]] > 0:
                    
                    print("initial vacancy position")
                    print(zone_vacancy[i])

                    alloted_zone_code = i
                    alloted_zone = zone_vacancy[i]['zone']
                    alloted_from_category = cat[row[6]]

                    print('Preference Number: ', tracker)
                    print('Alloted Zone: ', alloted_zone)
                    print('Alloted from category: ', alloted_from_category)

                    # now first reduce vertical vacancy and then reduce horizontal vacancy
                    zone_vacancy[i]['vac'][cat[row[6]]] = zone_vacancy[i]['vac'][cat[row[6]]] - 1

                    # now update zone cutoff
                    if zone_vacancy[i]['vac'][cat[row[3]]] == 0 and row[3] == '9':
                        zone_vacancy[i]['cutoff']['UR_cutoff'] = row[7]

                    print("after vacancy position")
                    print(zone_vacancy[i])

                    # APPEND TO ROW
                    row.append(alloted_zone)
                    row.append(alloted_zone_code)
                    row.append(alloted_from_category)
                    print(row)
                
                    print(' \n ======================================================================== [loop2=>catsel=9&&cat1=catsel]\n')
                    break

        # for EWS, OBC, SC, ST on UR (cat1 != catsel && catsel == 9)
        else:
            
            possible_allocation_fromUR = ''
            possible_allocation_fromUR_code = ''
            possible_allocation_fromCat1 = ''
            possible_allocation_fromCat1_code = ''

            ur_tracker = 0
            cat_tracker = 0

            # first allocate from UR
            for i in pref:
                ur_tracker = ur_tracker + 1
                # check if ur seats are available in zone
                if zone_vacancy[i]['vac'][cat[row[6]]] > 0:
                    possible_allocation_fromUR = zone_vacancy[i]['zone']
                    possible_allocation_fromUR_code = i
                    print("Possible allocation from UR: ", possible_allocation_fromUR)
                    print("Possible preference number that can be allocated from UR: ", ur_tracker)
                    break
            
            # then allocate from respective Category
            for i in pref:
                cat_tracker = cat_tracker + 1
                # check if respective category seats are available in zone
                if zone_vacancy[i]['vac'][cat[row[3]]] > 0:
                    possible_allocation_fromCat1 = zone_vacancy[i]['zone']
                    possible_allocation_fromCat1_code = i
                    print("Possible allocation from Cat1: ", possible_allocation_fromCat1)
                    print("Possible preference number that can be allocated from Cat1: ", cat_tracker)
                    break
            
            # now we can compare the two trackers and allocate zone whichever is higher in preference
            if (cat_tracker < ur_tracker) and (cat_tracker > 0 and ur_tracker > 0):
                
                print("Allocating from cat1: ", cat[row[3]])
                print('cat tracker: ', cat_tracker)
                print('ur tracker: ', ur_tracker)
                
                alloted_zone = possible_allocation_fromCat1
                alloted_zone_code = possible_allocation_fromCat1_code
                alloted_from_category = cat[row[3]]

                print("initial vacancy position")
                print(zone_vacancy[alloted_zone_code])
                
                # now reduce vacancy position
                zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] = zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] - 1

                # this will render some candidates surplus, they will get provisional joining
                # increment counter to track number of surplus candidates of each category
                provisional_counter[cat[row[3]]] = provisional_counter[cat[row[3]]] + 1 
                
                # update zone cutoff          
                if zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] == 0 and row[3] == '0':
                    zone_vacancy[alloted_zone_code]['cutoff']['EWS_cutoff'] = row[7]
                
                if zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] == 0 and row[3] == '1':
                    zone_vacancy[alloted_zone_code]['cutoff']['SC_cutoff'] = row[7]

                if zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] == 0 and row[3] == '2':
                    zone_vacancy[alloted_zone_code]['cutoff']['ST_cutoff'] = row[7]

                if zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] == 0 and row[3] == '6':
                    zone_vacancy[alloted_zone_code]['cutoff']['OBC_cutoff'] = row[7]

                if zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] == 0 and row[3] == '9':
                    zone_vacancy[alloted_zone_code]['cutoff']['UR_cutoff'] = row[7]

                print("after vacancy position")
                print(zone_vacancy[alloted_zone_code])

                # APPEND TO ROW
                row.append(alloted_zone)
                row.append(alloted_zone_code)
                row.append(alloted_from_category)

                row.append(possible_allocation_fromUR)
                row.append(possible_allocation_fromUR_code)
                row.append(ur_tracker)

                row.append(possible_allocation_fromCat1)
                row.append(possible_allocation_fromCat1_code)
                row.append(cat_tracker)

                print(row)

                print(' \n ======================================================================== [if_cat_pref<ur_pref]\n')

            else:

                print("Allocating from unreserved cat: ", cat[row[6]])
                print('cat tracker: ', cat_tracker)
                print('ur tracker: ', ur_tracker)

                alloted_zone = possible_allocation_fromUR
                alloted_zone_code = possible_allocation_fromUR_code
                alloted_from_category = cat[row[6]]

                print("initial vacancy position")
                print(zone_vacancy[alloted_zone_code])

                # now reduce vacancy position
                zone_vacancy[alloted_zone_code]['vac'][cat[row[6]]] = zone_vacancy[alloted_zone_code]['vac'][cat[row[6]]] - 1
                # update zone cutoff          

                if zone_vacancy[alloted_zone_code]['vac'][cat[row[6]]] == 0 and row[6] == '9':
                    zone_vacancy[alloted_zone_code]['cutoff']['UR_cutoff'] = row[7]

                print("after vacancy position")
                print(zone_vacancy[alloted_zone_code])

                # APPEND TO ROW
                row.append(alloted_zone)
                row.append(alloted_zone_code)
                row.append(alloted_from_category)

                row.append(possible_allocation_fromUR)
                row.append(possible_allocation_fromUR_code)
                row.append(ur_tracker)

                row.append(possible_allocation_fromCat1)
                row.append(possible_allocation_fromCat1_code)
                row.append(cat_tracker)

                print(row)

                print(' \n ======================================================================== [if_cat_pref>ur_pref]\n')
            


## Now a few UR seats will be left unfilled, as some OBC EWS SC ST candidates selected on UR seats will take seats from their own category
print("\n\n###################################################################################")
print("     NUMBER OF CANDIDATES FROM EACH CATEGORY WHO WILL GET PROVISIONAL JOINING ")
print("###################################################################################\n")
print(json.dumps(provisional_counter, sort_keys=False, indent=4))

# Transfer unfilled UR seats to `UR_rendered_extra` for each category so that they can be used to allot provisional seats
print("\n\n############################################################")
print("     TRANSFERING UNFILLED UR SEATS TO `UR_rendered_extra`")
print("############################################################")

for zone_code in zone_vacancy:
    print('\n\n------------------------------------')
    print(zone_vacancy[zone_code]['zone'])
    print('Unfilled UR Vacancies in zone: ', zone_vacancy[zone_code]['vac']['UR'])
    # if unfilled UR vacancies then transfer to `UR_rendered_extra`
    if zone_vacancy[zone_code]['vac']['UR'] > 0:
        print("TRANSFERRED to `UR_rendered_extra`")
        zone_vacancy[zone_code]['vac']['UR_rendered_extra'] = zone_vacancy[zone_code]['vac']['UR']
        zone_vacancy[zone_code]['vac']['UR'] = -zone_vacancy[zone_code]['vac']['UR']

# print information regarding vacancy position

print("\n\n############################################################")
print("     UNFILLED UR SEATS AFTER ALLOCATING CATSEL=4|5|9")
print("############################################################\n")
for i in zone_vacancy:
    if zone_vacancy[i]['vac']['UR_rendered_extra'] > 0:
        print(zone_vacancy[i]['zone'])
        print('Unfilled Vacancies of UR Cat: ', zone_vacancy[i]['vac']['UR_rendered_extra'])
        print('----------------------------------\n')

print("\n\n############################################################")
print("     VACANCY POSITION AFTER ALLOCATING CATSEL=4|5|9")
print("############################################################")
# print(zone_vacancy)
print(json.dumps(zone_vacancy, sort_keys=False, indent=4))
# print("############################################################")

# Now do allocation for all those selected on their Own category (cat-1 = 0 or 1 or 2 or 6)
## First allocate seat from their respective category
## then check if they can get better|higher preference from `UR_rendered_extra` seats, if yes allot with provisional status
## finally if all category seats are over then allot from `UR_rendered_extra` seats on basis of AIR according to their preferences

print("\n\n########################################################################")
print("      All Candidates Selected on their Own category seat (CatSel=0|1|2|6)     ")
print("########################################################################")

for row in data[1:]:
    
    alloted_zone = ''
    alloted_zone_code = ''
    alloted_from_category = ''

    possible_allocation_from_UR_extra_seats = ''
    possible_allocation_from_UR_extra_seats_code = ''
    possible_allocation_fromCat1 = ''
    possible_allocation_fromCat1_code = ''

    cat_tracker = 0
    extra_URseat_tracker = 0

    # use form filled flag to do allocation for only those who have filled form
    if row[24] and (row[6] == '0' or row[6] == '1' or row[6] == '2' or row[6] == '6'):
        print('\n\n--------------------------------------- \n')
        print("Name: ", row[1])
        print("AIR: ", row[7])
        print("Cat 1:", cat[row[3]])
        print("Cat Sel:", cat[row[6]])
        pref = row[8:24]
        print("Preferences: ", pref)

        # first allocate from category seat
        for i in pref:
            cat_tracker = cat_tracker + 1
            # check if respective category seats are available in zone
            if zone_vacancy[i]['vac'][cat[row[3]]] > 0:
                possible_allocation_fromCat1 = zone_vacancy[i]['zone']
                possible_allocation_fromCat1_code = i
                print("Possible allocation from Cat1: ", possible_allocation_fromCat1)
                print("Possible preference number that can be allocated from Cat1: ", cat_tracker)
                break            

        # then try to allot from `UR_rendered_extra` (use prov counter to check if extra UR seats available for category)

        # first check if `UR_rendered_extra` seat is available for respective category, if yes then try to allot from UR extra seats
        if provisional_counter[cat[row[3]]] > 0:
            for i in pref:
                extra_URseat_tracker = extra_URseat_tracker + 1
                # check if `UR_rendered_extra` seats are available in zone
                if zone_vacancy[i]['vac']['UR_rendered_extra'] > 0:
                    possible_allocation_from_UR_extra_seats = zone_vacancy[i]['zone']
                    possible_allocation_from_UR_extra_seats_code = i
                    print("Possible allocation from `UR_rendered_extra`: ", possible_allocation_from_UR_extra_seats)
                    print("Possible preference number that can be allocated from `UR_rendered_extra`", extra_URseat_tracker)
                    break
        
        # now compare two trackers and allot zone whichever is higher in preference
        if (extra_URseat_tracker < cat_tracker) and (cat_tracker > 0 and extra_URseat_tracker > 0):
            # first set `provisional_joining_flag=True`
            row[25] = True
            # then allocate `UR_rendered_extra` seat to this candidate
            print('Check this out')
               
            print("Allocating Provisional UR Seat from `UR_rendered_extra`")
            print('cat tracker: ', cat_tracker)
            print('UR_rendered_extra tracker: ', extra_URseat_tracker)
            
            alloted_zone = possible_allocation_from_UR_extra_seats
            alloted_zone_code = possible_allocation_from_UR_extra_seats_code
            alloted_from_category = cat[row[3]] + ' PROVISIONAL'

            print("initial vacancy position")
            print(zone_vacancy[alloted_zone_code])

            print('initial provisional counter')
            print(provisional_counter)
            
            # now reduce vacancy position
            zone_vacancy[alloted_zone_code]['vac']['UR_rendered_extra'] = zone_vacancy[alloted_zone_code]['vac']['UR_rendered_extra'] - 1

            # Reduce counter for respective category in provisional counter
            provisional_counter[cat[row[3]]] = provisional_counter[cat[row[3]]] - 1 
            
            # update zone cutoff          
            if zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] == 0 and row[3] == '0':
                zone_vacancy[alloted_zone_code]['cutoff']['EWS_cutoff'] = row[7]
            
            if zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] == 0 and row[3] == '1':
                zone_vacancy[alloted_zone_code]['cutoff']['SC_cutoff'] = row[7]

            if zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] == 0 and row[3] == '2':
                zone_vacancy[alloted_zone_code]['cutoff']['ST_cutoff'] = row[7]

            if zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] == 0 and row[3] == '6':
                zone_vacancy[alloted_zone_code]['cutoff']['OBC_cutoff'] = row[7]

            print('after provisional counter')
            print(provisional_counter)
            
            print("after vacancy position")
            print(zone_vacancy[alloted_zone_code])

            # APPEND TO ROW
            row.append(alloted_zone)
            row.append(alloted_zone_code)
            row.append(alloted_from_category)

            row.append('')
            row.append('')
            row.append('')

            row.append('')
            row.append('')
            row.append('')

            row.append(possible_allocation_fromCat1)
            row.append(possible_allocation_fromCat1_code)
            row.append(cat_tracker)

            row.append(possible_allocation_from_UR_extra_seats)
            row.append(possible_allocation_from_UR_extra_seats_code)
            row.append(extra_URseat_tracker)

            print(row)

            print(' \n ======================================================================== [if_URextra_pref<cat_pref]\n')

        else:
            print('normal case')
               
            print("Allocating from cat1: ", cat[row[3]])
            print('cat tracker: ', cat_tracker)
            print('ur tracker: ', extra_URseat_tracker)
            
            alloted_zone = possible_allocation_fromCat1
            alloted_zone_code = possible_allocation_fromCat1_code
            alloted_from_category = cat[row[3]]

            print("initial vacancy position")
            print(zone_vacancy[alloted_zone_code])
            
            # now reduce vacancy position
            zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] = zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] - 1
            
            # update zone cutoff          
            if zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] == 0 and row[3] == '0':
                zone_vacancy[alloted_zone_code]['cutoff']['EWS_cutoff'] = row[7]
            
            if zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] == 0 and row[3] == '1':
                zone_vacancy[alloted_zone_code]['cutoff']['SC_cutoff'] = row[7]

            if zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] == 0 and row[3] == '2':
                zone_vacancy[alloted_zone_code]['cutoff']['ST_cutoff'] = row[7]

            if zone_vacancy[alloted_zone_code]['vac'][cat[row[3]]] == 0 and row[3] == '6':
                zone_vacancy[alloted_zone_code]['cutoff']['OBC_cutoff'] = row[7]

            print("after vacancy position")
            print(zone_vacancy[alloted_zone_code])

            # APPEND TO ROW
            row.append(alloted_zone)
            row.append(alloted_zone_code)
            row.append(alloted_from_category)

            row.append('')
            row.append('')
            row.append('')

            row.append('')
            row.append('')
            row.append('')

            row.append(possible_allocation_fromCat1)
            row.append(possible_allocation_fromCat1_code)
            row.append(cat_tracker)

            row.append(possible_allocation_from_UR_extra_seats)
            row.append(possible_allocation_from_UR_extra_seats_code)
            row.append(extra_URseat_tracker)

            print(row)

            print(' \n ======================================================================== [if_cat_pref<URextra_pref]\n')

# print final information of cutoff and vacancy position
print("\n\n############################################################")
print("     FINAL VACANCY POSITION")
print("############################################################")
# print(zone_vacancy)
print(json.dumps(zone_vacancy, sort_keys=False, indent=4))

print("\n\n############################################################")
print("     CUTOFF TABLE")
print("############################################################")

tuples = []
header = ['ZONE', 'UR', 'EWS', 'OBC', 'SC', 'ST', 'OH', 'HH']
tuples.append(header)

print(header)

for zone_code in zone_vacancy:
    row = []
    row.append(zone_vacancy[zone_code]['zone'])
    row.append(zone_vacancy[zone_code]['cutoff']['UR_cutoff'])
    row.append(zone_vacancy[zone_code]['cutoff']['EWS_cutoff'])
    row.append(zone_vacancy[zone_code]['cutoff']['OBC_cutoff'])
    row.append(zone_vacancy[zone_code]['cutoff']['SC_cutoff'])
    row.append(zone_vacancy[zone_code]['cutoff']['ST_cutoff'])
    row.append(zone_vacancy[zone_code]['cutoff']['OH_cutoff'])
    row.append(zone_vacancy[zone_code]['cutoff']['HH_cutoff'])
    tuples.append(row)
    print(row)

sys.stdout = orig_stdout
f.close()


writefilename = 'cgst_zone_allocation_v2.csv'
file = open(writefilename, 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(data) 