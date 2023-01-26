#Import the Counter and defaultdict modules

from collections import Counter, defaultdict

# Color of shirts worn by each staffs in a week

Bincom_staffs = {
    'Monday': {
        'staff_1':{
            'shirt_worn':'blue'
        },
        'staff_2':{
            'shirt_worn':'orange'
        },
        'staff_3':{
            'shirt_worn':'white'
        },
         'staff_4':{
            'shirt_worn':'orange'
        },
         'staff_5':{
            'shirt_worn':'brown'
        },

    },

    'Tuesday': {
        'staff_1':{
            'shirt_worn':'white'
        },
        'staff_2':{
            'shirt_worn':'green'
        },
        'staff_3':{
            'shirt_worn':'blue'
        },
         'staff_4':{
            'shirt_worn':'green'
        },
         'staff_5':{
            'shirt_worn':'purple'
        },

    },

    'wednesday': {
        'staff_1':{
            'shirt_worn':'purple'
        },
        'staff_2':{
            'shirt_worn':'brown'
        },
        'staff_3':{
            'shirt_worn':'red'
        },
         'staff_4':{
            'shirt_worn':'black'
        },
         'staff_5':{
            'shirt_worn':'green'
        },
    },
    'Thursday': {
        'staff_1':{
            'shirt_worn':'orange'
        },
        'staff_2':{
            'shirt_worn':'white'
        },
        'staff_3':{
            'shirt_worn':'blue'
        },
         'staff_4':{
            'shirt_worn':'cream'
        },
         'staff_5':{
            'shirt_worn':'red'
        },
    },

    'Friday': {
        'staff_1':{

            'shirt_worn':'yellow'
        },
        'staff_2':{
            'shirt_worn':'brown'
        },
        'staff_3':{
            'shirt_worn':'black'
        },
         'staff_4':{
            'shirt_worn':'white'
        },
         'staff_5':{
            'shirt_worn':'orange'
        },
    },
}

# Setting defaultdict to return back an int

shirt_count = defaultdict(int)

for day, staffs in Bincom_staffs.items():

    for staff, details in staffs.items():

        shirt_color = details['shirt_worn']

        shirt_count[shirt_color] += 1

print(shirt_count)

# mean color

total_number_of_shirt_colors_worn = sum(shirt_count.values())

mean_value = total_number_of_shirt_colors_worn / len(shirt_count)

print('The mean value is ', mean_value)


# Determine the color of shirt worn most

Shirt_worn_most = max(shirt_count, key=shirt_count.get)

print('The color of shirt worn most Throughout the week is ' + Shirt_worn_most)

# The median value of colors worn that week

sorted_count = sorted(shirt_count.values())

median_index = len(sorted_count) // 2

if len(sorted_count) % 2 == 0:

    median_count = (sorted_count[median_index] + sorted_count[median_index - 1]) / 2

else:
    median_count = sorted_count[median_index]

print('The median value is ', median_count )


# Probability of picking red color

expected_outcome = shirt_count['red']

total_number_of_outcomes = sum(shirt_count.values())

Probability_of_picking_red = expected_outcome / total_number_of_outcomes

print('The probability of wearing a red shirt for the week is ',  Probability_of_picking_red)

# The variance

# Save to postgresql

import psycopg2

DB_HOST = "http://127.0.0.1:52274/browser/"
DB_NAME = "PYTHON"
DB_USER = "postgres"
DB_PASS = "kingsman11"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

conn.close()

# print(variance)
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# sum = 0
# for i in range(1, 51):
#     sum += fibonacci(i)

# print("The sum of the first 50 Fibonacci numbers is:", sum)