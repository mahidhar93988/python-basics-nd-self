n = int(input())

for i in range(n):
	x,y = map (int, input().split())
	
	if x > 0 and y > 0 :
		print("Q1")
	if x < 0 and y > 0 :
		print("Q2")
	if x < 0 and y < 0 :
		print("Q3")
	if x > 0 and y < 0 :
		print("Q4")

     # Predict the Quadrent