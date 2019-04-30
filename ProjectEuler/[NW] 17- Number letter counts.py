def writeUnderHundred (i):
    if i == 0: return ''
    if 9 < i < 20:
        return tunit [i - 10]
    return (tens [i//10] + " " + unit[i%10]).strip()
    

def writeUnderThousand (i):
    s = writeUnderHundred (i%100)
    if i < 100:
        return s.strip()
    else:
        return (str(unit[i//100]) + ' Hundred ' + s).strip()
    
def writeWord (i):
    s = writeUnderThousand (i%1000)
    if i < 1000:
        return s.strip()
    k = writeUnderThousand((i%1000000)//1000)
    if k != '':
        s = k + ' Thousand ' + s
    if i < 1000000:
        return s.strip()
    k = writeUnderThousand((i%1000000000)//1000000)
    if k != '':
        s =  k + ' Million ' + s
    if i < 1000000000:
        return s.strip()
    k = writeUnderThousand((i%1000000000000)//1000000000)
    if k != '':
    	s = k + ' Billion ' + s
    if i < 1000000000000:
    	return s.strip()
    else:
    	return unit[i//1000000000000] + ' Trillion ' + s


unit = [ "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
tunit = ["Ten","Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ['', '', "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

# T = int(input())
# for t0 in range(T):
#     n = int(input())

#     print(writeWord(n))

print(writeWord(1000010000))