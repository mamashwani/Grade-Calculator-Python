# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 18:38:25 2018
Muhammad Mashwnai 
PeopleSoft ID: 1378052
COSC 1430 
Assignment 3
"""
def get_better_grade(average):
    if average >= 92:
        print("You have an A so there is no higher grade")
    elif average >= 88:
        value = 92 - average
        print("You are "+str(value)+" points away from an A")
    elif average >= 84:
        value = 88 - average
        print("You are "+str(value)+" points away from an A-")
    elif average >= 80:
        value = 84 - average
        print("You are "+str(value)+" points away from a B+")
    elif average >= 76:
        value = 80 - average
        print("You are "+str(value)+" points away from a B")
    elif average >= 72:
        value = 76 - average
        print("You are "+str(value)+" points away from a B-")
    elif average >= 68:
        value = 72 - average
        print("You are "+str(value)+" points away from a C+")
    elif average >= 64:
        value = 68 - average
        print("You are "+str(value)+" points away from a C")
    elif average >= 60:
        value = 64 - average
        print("You are "+str(value)+" points away from a C-")
    elif average >= 56:
        value = 60 - average
        print("You are "+str(value)+" points away from a D+")
    elif average < 56:
        value = 56 - average
        print("You are "+str(value)+" points away from a D")
        
def get_letter_grade(average):
    if average  >= 92:
        return "A"
    elif average >= 88:
        return "A-"
    elif average >= 84:
        return "B+"
    elif average >= 80:
        return "B"
    elif average >= 76:
        return "B-"
    elif average >= 72:
        return "C+"
    elif average >= 68:
        return "C"
    elif average >= 64:
        return "C-"
    elif average >= 60:
        return "D+"
    elif average >= 56:
        return "D"
    elif average < 56:
        return "F"
        

average = float(input("Please enter a final average: "))
letter = get_letter_grade(average)
print()
print()
print("Congratulations, you earned a/an ",letter)
get_better_grade(average)
print()
print("="*40)
