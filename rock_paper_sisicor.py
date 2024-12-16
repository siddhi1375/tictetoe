print("press 1 for rock :")
print("press 2 for siscor :")
print("press 3 for paper :")
choice1=int(input("enter a choice1 :"))
choice2=int(input("enter a choice2 :"))
if choice1==choice2 :
	print("tie")
elif choice1==1 and choice2==2 :
	print("player 1 is winner")
elif choice1==2 and choice2==1:
	print("player2 is winner")
elif choice1==2 and choice2==3:
	print("player 1 is winner")
elif choice1==3 and choice2==2:
	print("player 2 is winner")
elif choice1==1 and choice2==3:
	print("player 2 is winner")
elif choice1==3 and choice2==1:
	print("player 1 is winner")
else:
	print("invalid choices")