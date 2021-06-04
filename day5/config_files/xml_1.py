Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: /Users/shobhit/Desktop/tsip/day5/misc/one.py ===========
>>> id(varx)
4336635984
>>> id(vary)
4336636144
>>> id(varz)
4336635984
>>> import sys
>>> sys.version
'3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) \n[Clang 6.0 (clang-600.0.57)]'
>>> 
========= RESTART: /Users/shobhit/Desktop/tsip/day5/excptions/one.py =========
enter the index:
4
lista[i] = xx
>>> 
========= RESTART: /Users/shobhit/Desktop/tsip/day5/excptions/one.py =========
enter the index:
12
Traceback (most recent call last):
  File "/Users/shobhit/Desktop/tsip/day5/excptions/one.py", line 5, in <module>
    print("lista[i] =", lista[i])
IndexError: list index out of range
>>> 
========= RESTART: /Users/shobhit/Desktop/tsip/day5/excptions/one.py =========
enter the index:
3
lista[i] = ww
code continues
>>> 
========= RESTART: /Users/shobhit/Desktop/tsip/day5/excptions/one.py =========
enter the index:
12
Traceback (most recent call last):
  File "/Users/shobhit/Desktop/tsip/day5/excptions/one.py", line 5, in <module>
    print("lista[i] =", lista[i])
IndexError: list index out of range
>>> 
========= RESTART: /Users/shobhit/Desktop/tsip/day5/excptions/one.py =========
enter the index:
12
wrong index entered, defaulting to zero
lista[i] = tt
code continues
>>> 
========= RESTART: /Users/shobhit/Desktop/tsip/day5/excptions/one.py =========
enter the index:
4
lista[i] = xx
code continues
>>> 
========== RESTART: /Users/shobhit/Desktop/tsip/day5/excptions/2.py ==========
enter the index:
23.4
Traceback (most recent call last):
  File "/Users/shobhit/Desktop/tsip/day5/excptions/2.py", line 4, in <module>
    i = int(input("enter the index:\n"))
ValueError: invalid literal for int() with base 10: '23.4'
>>> 
========== RESTART: /Users/shobhit/Desktop/tsip/day5/excptions/2.py ==========
enter the index:
34.7
Traceback (most recent call last):
  File "/Users/shobhit/Desktop/tsip/day5/excptions/2.py", line 4, in <module>
    i = int(input("enter the index:\n"))
ValueError: invalid literal for int() with base 10: '34.7'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/shobhit/Desktop/tsip/day5/excptions/2.py", line 10, in <module>
    except valueError:
NameError: name 'valueError' is not defined
>>> 
========== RESTART: /Users/shobhit/Desktop/tsip/day5/excptions/2.py ==========
enter the index:
13.78
should have ntered only integers, defaulting to zero
lista[i] = tt
code continues
>>> 
========== RESTART: /Users/shobhit/Desktop/tsip/day5/excptions/3.py ==========
enter the index:
3
Traceback (most recent call last):
  File "/Users/shobhit/Desktop/tsip/day5/excptions/3.py", line 5, in <module>
    print("lista[i] =", listb[i])
NameError: name 'listb' is not defined
>>> 
========== RESTART: /Users/shobhit/Desktop/tsip/day5/excptions/3.py ==========
enter the index:
5
something went wrong
code continues
>>> 
========== RESTART: /Users/shobhit/Desktop/tsip/day5/excptions/4.py ==========
enter the index:
5
Traceback (most recent call last):
  File "/Users/shobhit/Desktop/tsip/day5/excptions/4.py", line 6, in <module>
    print("lista[i] =", listb[i])
NameError: name 'listb' is not defined

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/shobhit/Desktop/tsip/day5/excptions/4.py", line 15, in <module>
    except ex:
NameError: name 'ex' is not defined
>>> 
========== RESTART: /Users/shobhit/Desktop/tsip/day5/excptions/4.py ==========
enter the index:
10
something went wrong,  name 'listb' is not defined
code continues
>>> 
============= RESTART: /Users/shobhit/Desktop/tsip/day5/re/1.py =============
enter the string: 
heel
right swipe
>>> 
============= RESTART: /Users/shobhit/Desktop/tsip/day5/re/1.py =============
enter the string: 
hel
no match
>>> 
============= RESTART: /Users/shobhit/Desktop/tsip/day5/re/1.py =============
enter the string: 
heeel
no match
>>> 
============= RESTART: /Users/shobhit/Desktop/tsip/day5/re/1.py =============
enter the string: 
hiit
no match
>>> 
============= RESTART: /Users/shobhit/Desktop/tsip/day5/re/2.py =============
['2', '3', '4', '3', '5', '7', '4', '3', '6', '7', '3', '4', '1', '4', '5', '8', '4', '5']
>>> 
============= RESTART: /Users/shobhit/Desktop/tsip/day5/re/2.py =============
['23', '435', '7', '4367', '341', '458', '45']
>>> 
============= RESTART: /Users/shobhit/Desktop/tsip/day5/re/2.py =============
['435', '436', '341', '458']
>>> 
============= RESTART: /Users/shobhit/Desktop/tsip/day5/re/3.py =============
['23', '435', '4367', '341', '458', '45']
>>> 
============= RESTART: /Users/shobhit/Desktop/tsip/day5/re/4.py =============
['hell', 'hell', 'heal', 'heel']
>>> 
============= RESTART: /Users/shobhit/Desktop/tsip/day5/re/5.py =============
['hell', 'hell', 'heal', 'heel', 'HEll']
>>> 
============= RESTART: /Users/shobhit/Desktop/tsip/day5/re/6.py =============
['hello ', ' hi ', ' great 7\nexample ', ' \t\tbasic ', '\nprinting ', '\tdrive\t', '\nA hello heals the heel\nso does a HEllo\n']
>>> 
============= RESTART: /Users/shobhit/Desktop/tsip/day5/re/6.py =============
['hello', '23', 'hi', '435', 'great', '7', 'example', '4367', '', '', 'basic', '341', 'printing', '458', 'drive', '45', 'A', 'hello', 'heals', 'the', 'heel', 'so', 'does', 'a', 'HEllo', '']
>>> 
============= RESTART: /Users/shobhit/Desktop/tsip/day5/re/6.py =============
['hello', '23', 'hi', '435', 'great', '7\nexample 4367 \t\tbasic 341\nprinting 458\tdrive\t45\nA hello heals the heel\nso does a HEllo\n']
>>> 
============= RESTART: /Users/shobhit/Desktop/tsip/day5/re/7.py =============
hello_23_hi_435_great_7_example_4367___basic_341_printing_458_drive_45_A_hello_heals_the_heel_so_does_a_HEllo_
>>> 
============= RESTART: /Users/shobhit/Desktop/tsip/day5/re/8.py =============
hello_23_hi_435_great_7_example_4367_basic_341_printing_458_drive_45_A_hello_heals_the_heel_so_does_a_HEllo_
>>> 
============= RESTART: /Users/shobhit/Desktop/tsip/day5/re/9.py =============
hello ## hi ## great ##
example ## 		basic ##
printing ##	drive	##
A hello heals the heel
so does a HEllo

>>> 
============= RESTART: /Users/shobhit/Desktop/tsip/day5/re/10.py =============
('hello ## hi ## great ##\nexample ## \t\tbasic ##\nprinting ##\tdrive\t##\nA hello heals the heel\nso does a HEllo\n', 7)
>>> 
====== RESTART: /Users/shobhit/Desktop/tsip/day5/config_files/json_1.py ======
65
>>> stra[0:23]
'{\n    "fruit": "Apple",'
>>> 
====== RESTART: /Users/shobhit/Desktop/tsip/day5/config_files/json_1.py ======
>>> print(type(stra))
<class 'dict'>
>>> stra
{'fruit': 'Apple', 'size': 'Large', 'color': 'Red'}
>>> stra['fruit']
'Apple'
>>> stra.keys()
dict_keys(['fruit', 'size', 'color'])
>>> list(stra.keys())
['fruit', 'size', 'color']
>>> 
====== RESTART: /Users/shobhit/Desktop/tsip/day5/config_files/json_2.py ======
>>> dictb
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    dictb
NameError: name 'dictb' is not defined
>>> dicta
{'quiz': {'sport': {'q1': {'question': 'Which one is correct team name in NBA?', 'options': ['New York Bulls', 'Los Angeles Kings', 'Golden State Warriros', 'Huston Rocket'], 'answer': 'Huston Rocket'}}, 'maths': {'q1': {'question': '5 + 7 = ?', 'options': ['10', '11', '12', '13'], 'answer': '12'}, 'q2': {'question': '12 - 8 = ?', 'options': ['1', '2', '3', '4'], 'answer': '4'}}}}
>>> dicta['quiz']['maths']['q2']['question'][-1]
'?'
>>> 
====== RESTART: /Users/shobhit/Desktop/tsip/day5/config_files/json_3.py ======
>>> 
====== RESTART: /Users/shobhit/Desktop/tsip/day5/config_files/json_3.py ======
>>> 
====== RESTART: /Users/shobhit/Desktop/tsip/day5/config_files/json_3.py ======
>>> 
====== RESTART: /Users/shobhit/Desktop/tsip/day5/config_files/xml_1.py ======
catalog
>>> 
====== RESTART: /Users/shobhit/Desktop/tsip/day5/config_files/xml_2.py ======
catalog
{}
>>> 
====== RESTART: /Users/shobhit/Desktop/tsip/day5/config_files/xml_3.py ======
book
{'id': 'bk101'}
>>> 
====== RESTART: /Users/shobhit/Desktop/tsip/day5/config_files/xml_4.py ======
{}
Gambardella, Matthew
{}
XML Developer's Guide
{}
Computer
{}
44.95
{}
2000-10-01
{}
An in-depth look at creating applications
      with XML.
>>> 
====== RESTART: /Users/shobhit/Desktop/tsip/day5/config_files/xml_4.py ======
author = Gambardella, Matthew
title = XML Developer's Guide
genre = Computer
price = 44.95
publish_date = 2000-10-01
description = An in-depth look at creating applications
      with XML.
>>> 
====== RESTART: /Users/shobhit/Desktop/tsip/day5/config_files/xml_5.py ======
<Element 'book' at 0x7fe65037c778>
<Element 'book' at 0x7fe6503a1e58>
<Element 'book' at 0x7fe6503a50e8>
<Element 'book' at 0x7fe6503a5318>
<Element 'book' at 0x7fe6503a5598>
<Element 'book' at 0x7fe6503a14f8>
<Element 'book' at 0x7fe650395728>
<Element 'book' at 0x7fe6503a58b8>
<Element 'book' at 0x7fe6503a5ae8>
<Element 'book' at 0x7fe6503a5d18>
<Element 'book' at 0x7fe6503a5f48>
<Element 'book' at 0x7fe6503b6228>
>>> 
====== RESTART: /Users/shobhit/Desktop/tsip/day5/config_files/xml_5.py ======
book
book
book
book
book
book
book
book
book
book
book
book
>>> 
====== RESTART: /Users/shobhit/Desktop/tsip/day5/config_files/xml_6.py ======
>>> print(titles)
["XML Developer's Guide", 'Midnight Rain', 'Maeve Ascendant', "Oberon's Legacy", 'The Sundered Grail', 'Lover Birds', 'Splish Splash', 'Creepy Crawlies', 'Paradox Lost', 'Microsoft .NET: The Programming Bible', 'MSXML3: A Comprehensive Guide', 'Visual Studio 7: A Comprehensive Guide']
>>> 
====== RESTART: /Users/shobhit/Desktop/tsip/day5/config_files/xml_6.py ======
>>> fa.close()
>>> 
===== RESTART: /Users/shobhit/Desktop/tsip/day5/concurrency/threads_1.py =====
task A will exit in 6 seconds
task A will exit in 5 seconds
task A will exit in 4 seconds
task A will exit in 3 seconds
task A will exit in 2 seconds
task A will exit in 1 seconds
task B will exit in 9 seconds
task B will exit in 8 seconds
task B will exit in 7 seconds
task B will exit in 6 seconds
task B will exit in 5 seconds
task B will exit in 4 seconds
task B will exit in 3 seconds
task B will exit in 2 seconds
task B will exit in 1 seconds
task Main will exit in 3 seconds
task Main will exit in 2 seconds
task Main will exit in 1 seconds
>>> 
===== RESTART: /Users/shobhit/Desktop/tsip/day5/concurrency/threads_2.py =====
task A will exit in 6 seconds
task A will exit in 5 seconds
task A will exit in 4 seconds
task A will exit in 3 seconds
task A will exit in 2 seconds
task A will exit in 1 seconds
task B will exit in 9 seconds
task B will exit in 8 seconds
task B will exit in 7 seconds
task B will exit in 6 seconds
task B will exit in 5 seconds
task B will exit in 4 seconds
task B will exit in 3 seconds
task B will exit in 2 seconds
task B will exit in 1 seconds
task A will exit intask B will exit intask Main will exit in   693   secondssecondsseconds


task A will exit in 5task B will exit in  seconds8task Main will exit in
  seconds2
 seconds
task A will exit in 4task B will exit in  seconds7
task Main will exit in  seconds1
 seconds
task A will exit in 3 seconds
task B will exit in 
>>> 6 seconds
task A will exit in 2 seconds
task B will exit in 5 seconds
task A will exit in 1 seconds
task B will exit in 4 seconds
task B will exit in 3 seconds
task B will exit in 2 seconds
task B will exit in 1 seconds
task Main will exit in  seconds1
SyntaxError: invalid syntax
>>> 
