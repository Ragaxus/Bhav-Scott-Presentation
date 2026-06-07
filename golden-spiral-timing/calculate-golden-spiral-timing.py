spiral_total_time = 4.00 # sec

def fib(n):
	if n == 1:
		return [1,1]
	else:
		return next_fib(fib(n-1))
def next_fib(current_fib_arr):
	current_fib_arr.append(current_fib_arr[-2] + current_fib_arr[-1])
	return current_fib_arr

if __name__ == "__main__":
	fib_list = fib(7)
	total = sum(fib_list)
	times = [spiral_total_time * sum(fib_list[:idx+1])/total for idx in range(len(fib_list))]
	print(times)	
		
