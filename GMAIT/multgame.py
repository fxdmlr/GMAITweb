import math
import random
import time
import utils

def regMulGame(number_of_rounds=5, nrange=[100, 10000], float_mode=0, after_float_point=0):
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        n1 = random.randint(nrange[0], nrange[1]) + float_mode*round(random.random(), after_float_point)
        n2 = random.randint(nrange[0], nrange[1]) + float_mode*round(random.random(), after_float_point)
        entry = int(input("%d * %d = "%(n1, n2))) if not float_mode else float(input("%f * %f = "%(n1, n2)))
        if entry == n1 * n2:
            print("Correct.")
            pts += 1
        
        else:
            print("Incorrect. The answer was : %f \n" % (n1 * n2))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]

def polyMulGame(number_of_rounds=5, max_deg=5, nrange=[10, 100]):
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        p1 = utils.poly.rand(random.randint(1, max_deg), coeff_range=nrange[:]) 
        p2 = utils.poly.rand(random.randint(1, max_deg), coeff_range=nrange[:]) 
        wentry = input("(%s) * (%s) = "%(str(p1), str(p2))).split(" ") 
        entry = [int(i) for i in wentry]
        entry.reverse()
        entry_poly = utils.poly(entry[:]) 
        if entry_poly == p1 * p2:
            print("Correct.")
            pts += 1
        
        else:
            print("Incorrect. The answer was : %s \n" % str(p1 * p2))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]

def polyEval(number_of_rounds, deg, coeffs_range, input_range):
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        p = utils.poly.rand(deg, coeff_range=coeffs_range)
        x = (-1) ** random.randint(1, 10) * random.randint(input_range[0], input_range[1])
        entry = int(input("%s\t at x = %d : \n"%(str(p), x)))
        if entry == p(x):
            print("Correct.")
            pts += 1
        else:
            print("Incorrect. The answer was : %d"%p(x))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]

def evalRoot(number_of_rounds=5,root_range=[2, 5], ranges=[100, 1000], ndigits = 2):
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        p = utils.AlgebraicReal.randpurer(1, nrange_surd=ranges[:], nrange_root=root_range[:])
        entry = float(input(str(p) + " = "))
        if entry == round(p(), ndigits=ndigits):
            print("Correct.")
            pts += 1
        else:
            print("Incorrect. The answer was : %f"%round(p(), ndigits=ndigits))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]  

def evalRootPoly(deg, coeffs_range = [10, 100], number_of_rounds=5,root_range=[2, 5], ranges=[100, 1000], ndigits = 2):
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        r = utils.AlgebraicReal.randpurer(1, nrange_surd=ranges[:], nrange_root=root_range[:])
        p = utils.poly.rand(deg, coeff_range=coeffs_range)
        entry = float(input(str(p) + "\n at x = \n" + str(r)))
        if entry == round(p(r()), ndigits=ndigits):
            print("Correct.")
            pts += 1
        else:
            print("Incorrect. The answer was : %f"%round(p(r()), ndigits=ndigits))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]   

def surdGame(number_of_rounds=5, root_range=[2, 5], ranges=[100, 1000], ndigits = 2):
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        n = random.randint(root_range[0], root_range[1])
        p = utils.AlgebraicReal([0, [random.randint(ranges[0], ranges[1]), random.randint(ranges[0], ranges[1]), 2], [random.randint(ranges[0], ranges[1]), random.randint(ranges[0], ranges[1]), 2]])
        entry = float(input("%d root of \n%s : "%(n, str(p))))
        if entry == round(p() ** (1/n), ndigits=ndigits):
            print("Correct.")
            pts += 1
        else:
            print("Incorrect. The answer was : %f"%round(p() ** (1/n), ndigits=ndigits))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]  

def divGame(number_of_rounds=5, ranges=[100, 1000], ndigits=5):
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        n = utils.rational.rand(nrange=ranges[:])
        string = utils.strpprint(utils.connect(n.pprint(), [["   "], [" = "], ["   "]]))
        entry = float(input("%s \n\t"%string))
        if entry == round(n(), ndigits=ndigits):
            print("Correct.")
            pts += 1
        else:
            print("Incorrect. The answer was : %f"%round(n(), ndigits=ndigits))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]

def polyDivGame(number_of_rounds=5, max_deg=5, nrange=[10, 100], ndigits = 2):
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        p1 = utils.poly.rand(random.randint(1, max_deg), coeff_range=nrange[:]) 
        p2 = utils.poly.rand(random.randint(1, p1.deg), coeff_range=nrange[:]) 
        wentry = input("%s \n%s \n > "%(str(p1), str(p2))).split(" ") 
        entry = [float(i) for i in wentry]
        entry.reverse()
        entry_poly = utils.poly(entry[:]) 
        if entry_poly == round(p1 / p2, ndigits=ndigits):
            print("Correct.")
            pts += 1
        
        else:
            print("Incorrect. The answer was : %s \n" % str(round(p1 / p2, ndigits=ndigits)))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]

def regMulDyn(total_time=600, nrange=[100, 10000], float_mode=0, after_float_point=0):
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time() - start < total_time:
        n1 = random.randint(nrange[0], nrange[1]) + float_mode*round(random.random(), after_float_point)
        n2 = random.randint(nrange[0], nrange[1]) + float_mode*round(random.random(), after_float_point)
        number_of_rounds += 1
        entry = int(input("%d * %d = "%(n1, n2))) if not float_mode else float(input("%f * %f = "%(n1, n2)))
        end = time.time()
        if time.time() - start > total_time:
            print("Time Elapsed before entry.")
            return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
        if entry == n1 * n2:
            print("Correct.")
            pts += 1
        
        else:
            print("Incorrect. The answer was : %f \n" % (n1 * n2))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
def regMulDynII(total_time=600, nrange=[100, 10000], float_mode=0, after_float_point=0):
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time() - start < total_time:
        n1 = random.randint(nrange[0], nrange[1]) + float_mode*round(random.random(), after_float_point)
        n2 = random.randint(nrange[0], nrange[1]) + float_mode*round(random.random(), after_float_point)
        n3 = random.randint(nrange[0], nrange[1]) + float_mode*round(random.random(), after_float_point)
        n4 = random.randint(nrange[0], nrange[1]) + float_mode*round(random.random(), after_float_point)
        number_of_rounds += 1
        entry = int(input("%d * %d + %d * %d = "%(n1, n2, n3, n4))) if not float_mode else float(input("%f * %f + %f * %f = "%(n1, n2, n3, n4)))
        end = time.time()
        if time.time() - start > total_time:
            print("Time Elapsed before entry.")
            return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
        if entry == n1 * n2 + n3 * n4:
            print("Correct.")
            pts += 1
        
        else:
            print("Incorrect. The answer was : %f \n" % (n1 * n2 + n3 * n4))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
def polyEvalDyn(total_time, deg, coeffs_range, input_range):
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time() - start < total_time:
        p = utils.poly.rand(deg, coeff_range=coeffs_range)
        x = (-1) ** random.randint(1, 10) * random.randint(input_range[0], input_range[1])
        number_of_rounds += 1
        entry = int(input("%s\t at x = %d : \n"%(str(p), x)))
        end = time.time()
        if time.time() - start > total_time:
            print("Time Elapsed before entry.")
            return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
        if entry == p(x):
            print("Correct.")
            pts += 1
        else:
            print("Incorrect. The answer was : %d"%p(x))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]

def divGameDyn(total_time=600, ranges=[100, 1000], ndigits=5):
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time() - start < total_time:
        n = utils.rational.rand(nrange=ranges[:])
        string = utils.strpprint(utils.connect(n.pprint(), [["   "], [" = "], ["   "]]))
        number_of_rounds += 1
        entry = float(input("%s \n\t"%string))
        end = time.time()
        if time.time() - start > total_time:
            print("Time Elapsed before entry.")
            return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
        if entry == round(n(), ndigits=ndigits):
            print("Correct.")
            pts += 1
        else:
            print("Incorrect. The answer was : %f"%round(n(), ndigits=ndigits))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]

def divGameDynII(total_time=600, ranges=[100, 1000], ndigits=5):
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time() - start < total_time:
        n = utils.rational.rand(nrange=ranges[:])
        m = utils.rational.rand(nrange=ranges[:])
        string = utils.strpprint(utils.connect(utils.connect(utils.connect(n.pprint(), [["   "], [" + "], ["   "]]), m.pprint()), [["   "], [" = "], ["   "]]))
        number_of_rounds += 1
        entry = float(input("%s \n\t"%string))
        end = time.time()
        if time.time() - start > total_time:
            print("Time Elapsed before entry.")
            return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
        if entry == round(n() + m(), ndigits=ndigits):
            print("Correct.")
            pts += 1
        else:
            print("Incorrect. The answer was : %f"%round(n() + m(), ndigits=ndigits))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]

def mixedArithmeticDyn(total_time, nrange_mul=[100, 1000], nrange_div=[10, 100],  ndigits=5):
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time() - start < total_time:
        x = random.randint(1, 10)
        if x%2 == 0:
            n1 = random.randint(nrange_mul[0], nrange_mul[1]) 
            n2 = random.randint(nrange_mul[0], nrange_mul[1]) 
            number_of_rounds += 1
            entry = int(input("%d * %d = "%(n1, n2)))
            end = time.time()
            if time.time() - start > total_time:
                print("Time Elapsed before entry.")
                return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
            if entry == n1 * n2:
                print("Correct.")
                pts += 1
            
            else:
                print("Incorrect. The answer was : %f \n" % (n1 * n2))
        else:
            n = utils.rational.rand(nrange=nrange_div[:])
            string = utils.strpprint(utils.connect(n.pprint(), [["   "], [" = "], ["   "]]))
            number_of_rounds += 1
            entry = float(input("%s \n\t"%string))
            end = time.time()
            if time.time() - start > total_time:
                print("Time Elapsed before entry.")
                return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
            if entry == round(n(), ndigits=ndigits):
                print("Correct.")
                pts += 1
            else:
                print("Incorrect. The answer was : %f"%round(n(), ndigits=ndigits))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]

def mixedArithmeticDynII(total_time, nrange_mul=[100, 1000], nrange_div=[10, 100],  ndigits=5):
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time() - start < total_time:
        x = random.randint(1, 10)
        if x%2 == 0:
            n1 = random.randint(nrange_mul[0], nrange_mul[1]) 
            n2 = random.randint(nrange_mul[0], nrange_mul[1]) 
            n3 = random.randint(nrange_mul[0], nrange_mul[1]) 
            n4 = random.randint(nrange_mul[0], nrange_mul[1])
            number_of_rounds += 1
            entry = int(input("%d * %d + %d * %d = "%(n1, n2, n3, n4)))
            end = time.time()
            if time.time() - start > total_time:
                print("Time Elapsed before entry.")
                return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
            if entry == n1 * n2 + n3 * n4:
                print("Correct.")
                pts += 1
            
            else:
                print("Incorrect. The answer was : %f \n" % (n1 * n2 + n3 * n4))
        else:
            start = time.time()
            pts = 0
            number_of_rounds = 0
            n = utils.rational.rand(nrange=nrange_div[:])
            m = utils.rational.rand(nrange=nrange_div[:])
            string = utils.strpprint(utils.connect(utils.connect(utils.connect(n.pprint(), [["   "], [" + "], ["   "]]), m.pprint()), [["   "], [" = "], ["   "]]))
            number_of_rounds += 1
            entry = float(input("%s \n\t"%string))
            end = time.time()
            if time.time() - start > total_time:
                print("Time Elapsed before entry.")
                return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]
            if entry == round(n() + m(), ndigits=ndigits):
                print("Correct.")
                pts += 1
            else:
                print("Incorrect. The answer was : %f"%round(n() + m(), ndigits=ndigits))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds, total_time]

def polyroots(number_of_rounds=5, root_range=[1, 10], deg=3):
    print("Enter the result of a^n + b^(n-1) + c^(n-2) + ... \nwhere a < b < c < ... \nand a,b,c etc. are the roots of the polynomial and n is the degree.")
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        z = utils.poly([1])
        rarray = []
        for j in range(deg):
            q = (-1)**(random.randint(1, 10)) * random.randint(root_range[0], root_range[1])
            rarray.append(-q)
            z *= utils.poly([q, 1])
        print(z)
        m = int(input("Answer : "))
        narr = list(sorted(rarray))
        res = sum([narr[i] ** (deg - i) for i in range(deg)])
        if m == res:
            print("Correct.")
            pts += 1
        
        else:
            print("Incorrect. The answer was: %d"%res)
            print("The roots were : ", " , ".join([str(i) for i in narr]))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]

def polyrootsDyn(tot_time=600, root_range=[1, 10], deg=3):
    print("Enter the result of a^n + b^(n-1) + c^(n-2) + ... \nwhere a < b < c < ... \nand a,b,c etc. are the roots of the polynomial and n is the degree.")
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time()-start <= tot_time:
        z = utils.poly([1])
        rarray = []
        for j in range(deg):
            q = (-1)**(random.randint(1, 10)) * random.randint(root_range[0], root_range[1])
            rarray.append(-q)
            z *= utils.poly([q, 1])
        print(z)
        m = int(input("Answer : "))
        number_of_rounds += 1
        narr = list(sorted(rarray))
        res = sum([narr[i] ** (deg - i) for i in range(deg)])
        if time.time() - start > tot_time:
            print("Time elapsed before entry.")
            return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]
        
        if m == res:
            print("Correct.")
            pts += 1
        
        else:
            print("Incorrect. The answer was: %d"%res)
            print("The roots were : ", " , ".join([str(i) for i in narr]))
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]

def polydisc(number_of_rounds=5, coeff_range=[1, 10], deg=3):
    start = time.time()
    pts = 0
    for i in range(number_of_rounds):
        z = utils.poly.rand(deg, coeff_range=coeff_range[:])
        print(z)
        m = int(input("Discriminant : "))
        res = z.disc()
        if m == res:
            print("Correct.")
            pts += 1
        
        else:
            print("Incorrect. The answer was: %d"%res)
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]

def polydiscDyn(tot_time=600, coeff_range=[1, 10], deg=3):
    start = time.time()
    pts = 0
    number_of_rounds = 0
    while time.time()-start <= tot_time:
        z = utils.poly.rand(deg, coeff_range=coeff_range[:])
        number_of_rounds += 1
        print(z)
        m = int(input("Discriminant : "))
        res = z.disc()
        end = time.time()
        if time.time() - start > tot_time:
            print("Time elapsed before entry.")
            return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]
        
        if m == res:
            print("Correct.")
            pts += 1
        
        else:
            print("Incorrect. The answer was: %d"%res)
    
    end = time.time()
    return [pts / number_of_rounds * 100, end - start, (end - start) / number_of_rounds]