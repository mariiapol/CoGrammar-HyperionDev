swimming = int(input("Please write swimming time in min: "))
cycling = int(input("Please write cycling time in min: "))
running = int(input("Please write running time in min: "))

total = swimming + cycling + running
print(f"Total time: {total}")

if total <= 100:
    print("Provincial Colours")

elif total < 106:    
    print("Provincial Half Colours")

elif total < 111:
    print("Provincial Scroll")

else:
    print("No Award")
