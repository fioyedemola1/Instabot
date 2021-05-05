# draw
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********

# |||
# ||||||
# |||||||||
# ||||||||||||
# |||||||||||||||
# ||||||||||||||||||
# |||||||||||||||||||||
# ||||||||||||||||||||||||
# |||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||




# Implement the function unique_in_order which takes as argument a sequence 
# and returns a list of items without any elements with the same value next 
# to each other and preserving the original order of elements.

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]


dict_items = {"songs": [], "name": [], "length": []}
a = ["Madonna","song_name_1", "3:12"]
b = ["U2","song_name_2","3:14"]
c = ["Prince","song_name_3","4:23"]




keys=[
    {
        "link": "www.xxxxxxxxxxx.com",  
        "key": '34243242354354'
    },
    {
        "link": "www.xxxxxxxxxxx.com",
        "key": '432432534534534'
    },
    {
        "link": "www.xxxxxxxxxxx.com",
        "key": '423455345734'
    },
    {
        "link": "www.xxxxxxxxxxx.com",
        "key": '423459534534'
    },
    {
        "link": "www.xxxxxxxxxxx.com",
        "key": '423459534534'
    },
    {
        "link": "www.xxxxxxxxxxx.com",
        "key": '423459534534'
    }
]


question = ['To repeat a statement multiple times.', 
                'To decompose a program into several small subroutines.', 
                'To determine the execution time of a program.', 
                'To interrupt the execution of a program.'
            ]
# print it out like below
# 1. To repeat a statement multiple times.
# 2. To decompose a program into several small subroutines.
# 3. To determine the execution time of a program.
# 4. To interrupt the execution of a program.



'tHE Man tOLd mE a SToRy abOut lIFe'  -> # 'T h e   m A N   T o l D   M e   A   s t O r Y   A B o U T   L i f E'
'tHe QuiCK brOWn fOx juMps ovEr THe lAZY dOG' --> # 'T h E   q U I c k   B R o w N   F o X   J U m P S   O V e R   t h E   L a z y   D o g'