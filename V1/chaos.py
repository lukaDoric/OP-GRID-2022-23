# File: chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print('This program illustrates a chaotic function')	
	x, y = eval(input("Enter two numbers between 0 and 1, separated by comma: "))
		
    for i in range(20): 
        x = 3.9 * x * (1 - x)		
		y = 3.9 * y * (1 - y)
        print(x, y)

		
main()