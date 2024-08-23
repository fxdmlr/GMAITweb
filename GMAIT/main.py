'''
General Mathematical Ability Index Test.

Author : -----------
This is a tool to asses one's general 
mathematical aptitude. 

'''

import math
import random
import time
import utils
import multgame
import matrixgames
import os

def static():
    os.system("cls")
    print("\n")
    choice = int(input("Enter the desired mode :\n1-regMul\n2-polyMul\n3-RegDet\n4-PolyDet\n5-regMatMul\n6-polyMatMul\n7-polyEval\n8-evalRoot\n9-evalRootPoly\n10-surdGame\n11-divGame\n12-polyDiv\n13-EigenGame\n14-RootGame\n15-DiscGame\n16-Quit\n"))
    if choice == 1:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        float_mode = int(input("Float mode ? (1 yes/0 no)"))
        a_fl = 0
        if float_mode:
            a_fl = int(input("Digits after floating point : "))
        
        os.system("cls")
        stats = multgame.regMulGame(number_of_rounds=rounds, nrange=ranges, float_mode=float_mode, after_float_point=a_fl)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 2:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        max_deg = int(input("Maximum degree : "))
        os.system("cls")
        stats = multgame.polyMulGame(number_of_rounds=rounds, max_deg=max_deg, nrange=ranges[:])
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 3:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        dims = int(input("Dim : "))
        os.system("cls")
        stats = matrixgames.regDetGame(number_of_rounds=rounds, dims=dims, nrange=ranges)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2])) 
    
    if choice == 4:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        dims = int(input("Dims : "))
        
        max_deg = int(input("Maximum degree : "))
        os.system("cls")
        stats = matrixgames.polyDetGame(number_of_rounds=rounds, dims=dims, nrange=ranges, max_deg=max_deg)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 5:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        dims = int(input("Dim : "))
        os.system("cls")
        stats = matrixgames.regMulGame(number_of_rounds=rounds, dims=dims, nrange=ranges)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 6:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        dims = int(input("Dims : "))
        
        max_deg = int(input("Maximum degree : "))
        os.system("cls")
        stats = matrixgames.polyMulGame(number_of_rounds=rounds, dims=dims, nrange=ranges, max_deg=max_deg)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 7:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of abs of coeffs (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        c, d = input("Range of abs of inputs (seperated by blank space): ").split(" ")
        inp_ranges = [int(c), int(d)]
        
        deg = int(input("Polynomial degree : "))
        os.system("cls")
        stats = multgame.polyEval(rounds, deg, ranges[:], inp_ranges[:])
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 8:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of surds (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        c, d = input("Range of roots: ").split(" ")
        root_ranges = [int(c), int(d)]
        ndigits = int(input("digits after floating point : "))
        os.system("cls")
        stats = multgame.evalRoot(number_of_rounds=rounds, root_range=root_ranges, ranges=ranges, ndigits=ndigits)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 9:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of surds (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        c, d = input("Range of roots: ").split(" ")
        root_ranges = [int(c), int(d)]
        ndigits = int(input("digits after floating point : "))
        e, f = input("Range of coeffs: ").split(" ")
        coeff_ranges = [int(e), int(f)]
        deg = int(input("Degree : "))
        os.system("cls")
        stats = multgame.evalRootPoly(deg, coeffs_range=coeff_ranges, number_of_rounds=rounds, root_range=root_ranges, ranges=ranges, ndigits=ndigits)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 10:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of surds (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        c, d = input("Range of roots: ").split(" ")
        root_ranges = [int(c), int(d)]
        ndigits = int(input("digits after floating point : "))
        os.system("cls")
        stats = multgame.surdGame(number_of_rounds=rounds, root_range=root_ranges, ranges=ranges, ndigits=ndigits)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 11:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        a_fl = int(input("Digits after floating point : "))
        os.system("cls")
        stats = multgame.divGame(number_of_rounds=rounds, ranges=ranges, ndigits=a_fl)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 12:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        max_deg = int(input("Maximum degree : "))
        ndigits = int(input("Digits after decimal point : "))
        os.system("cls")
        stats = multgame.polyDivGame(number_of_rounds=rounds, max_deg=max_deg, nrange=ranges[:], ndigits=ndigits)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 13:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        dims = int(input("Dim : "))
        ndigits = int(input("Digits after decimal point : "))
        os.system("cls")
        print("Enter the smallest real part of all eigen values for each matrix.")
        stats = matrixgames.eigenvalueGame(number_of_rounds=rounds, dims=dims, nrange=ranges, ndigits=ndigits)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 14:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of abs of roots (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        deg = int(input("Polynomial degree : "))
        os.system("cls")
        stats = multgame.polyroots(number_of_rounds=rounds, root_range=ranges[:], deg=deg)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 15:
        rounds = int(input("Number of rounds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        deg = int(input("Polynomial degree : "))
        os.system("cls")
        stats = multgame.polydisc(number_of_rounds=rounds, coeff_range=ranges[:], deg=deg)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 16:
        return
    
def dynamic():
    os.system("cls")
    print("\n")
    choice = int(input("Enter the desired mode :\n 1-regMul\n 2-regMulII\n 3-divGame\n 4-divGameII\n 5-MixedArr\n 6-MixedArrII\n 7-polyEval\n 8-DetGame\n 9-EigenValGame\n 10-DiscGame\n 11-rootGame\n 12-Quit\n"))
    if choice == 1:
        duration = int(input("Time in seconds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        float_mode = int(input("Float mode ? (1 yes/0 no)"))
        a_fl = 0
        if float_mode:
            a_fl = int(input("Digits after floating point : "))
        
        os.system("cls")
        stats = multgame.regMulDyn(total_time=duration, nrange=ranges, float_mode=float_mode, after_float_point=a_fl)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Alotted time : ", stats[-1])
        print("Time spent per item : ", round(stats[2]))
        
    if choice == 2:
        duration = int(input("Time in seconds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        float_mode = int(input("Float mode ? (1 yes/0 no)"))
        a_fl = 0
        if float_mode:
            a_fl = int(input("Digits after floating point : "))
        
        os.system("cls")
        stats = multgame.regMulDynII(total_time=duration, nrange=ranges, float_mode=float_mode, after_float_point=a_fl)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Alotted time : ", stats[-1])
        print("Time spent per item : ", round(stats[2]))
        
    
    if choice == 3:
        duration = int(input("Time in seconds : "))
        a, b = input("Range of numbers(seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        a_fl = int(input("Digits after floating point : "))
        os.system("cls")
        stats = multgame.divGameDyn(total_time=duration, ranges=ranges, ndigits=a_fl)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Alotted time : ", stats[-1])
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 4:
        duration = int(input("Time in seconds : "))
        a, b = input("Range of numbers(seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        a_fl = int(input("Digits after floating point : "))
        os.system("cls")
        stats = multgame.divGameDynII(total_time=duration, ranges=ranges, ndigits=a_fl)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Alotted time : ", stats[-1])
        print("Time spent per item : ", round(stats[2]))
        
    if choice == 5:
        duration = int(input("Time in seconds : "))
        a, b = input("Range of numbers for Mul(seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        c, d = input("Range of numbers for Div(seperated by blank space): ").split(" ")
        ranges_div = [int(c), int(d)]
        a_fl = int(input("Digits after floating point : "))
        os.system("cls")
        stats = multgame.mixedArithmeticDyn(total_time=duration, nrange_mul=ranges, nrange_div=ranges_div, ndigits=a_fl)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Alotted time : ", stats[-1])
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 6:
        duration = int(input("Time in seconds : "))
        a, b = input("Range of numbers for Mul(seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        c, d = input("Range of numbers for Div(seperated by blank space): ").split(" ")
        ranges_div = [int(c), int(d)]
        a_fl = int(input("Digits after floating point : "))
        os.system("cls")
        stats = multgame.mixedArithmeticDynII(total_time=duration, nrange_mul=ranges, nrange_div=ranges_div, ndigits=a_fl)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Alotted time : ", stats[-1])
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 7:
        duration = int(input("Time in seconds : "))
        a, b = input("Range of abs of coeffs (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        c, d = input("Range of abs of inputs (seperated by blank space): ").split(" ")
        inp_ranges = [int(c), int(d)]
        
        deg = int(input("Polynomial degree : "))
        os.system("cls")
        stats = multgame.polyEvalDyn(duration, deg, ranges[:], inp_ranges[:])
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Alotted time : ", stats[-1])
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 8:
        duration = int(input("Time in seconds : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        dims = int(input("Dim : "))
        os.system("cls")
        stats = matrixgames.regDetGameDyn(tot_time=duration, dims=dims, nrange=ranges)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 9:
        duration = int(input("duration : "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        dims = int(input("Dim : "))
        ndigits = int(input("Digits after decimal point : "))
        os.system("cls")
        print("Enter the smallest real part of all eigen values for each matrix.")
        stats = matrixgames.eigenvalueGameDyn(tot_time=duration, dims=dims, nrange=ranges, ndigits=ndigits)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    if choice == 10:
        duration = int(input("duration: "))
        a, b = input("Range of numbers (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        
        deg = int(input("Polynomial degree : "))
        os.system("cls")
        stats = multgame.polydiscDyn(tot_time=duration, coeff_range=ranges[:], deg=deg)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 11:
        duration = int(input("duration : "))
        a, b = input("Range of abs of roots (seperated by blank space): ").split(" ")
        ranges = [int(a), int(b)]
        deg = int(input("Polynomial degree : "))
        os.system("cls")
        stats = multgame.polyrootsDyn(tot_time=duration, root_range=ranges[:], deg=deg)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 12:
        return
          
while True:
    mode = int(input("Mode :\n 1-Static \n 2-Dynamic\n 3-Quit\n"))
    if mode == 1:
        static()
    elif mode == 2:
        dynamic()
    elif mode == 3:
        break
quit()
