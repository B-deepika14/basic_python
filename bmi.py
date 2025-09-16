weight=54
height=60
bmi=round(weight/height**2)
if bmi<24:
    print("normal range")
elif bmi<29:
    print("over weight(pre-obese)")
elif bmi<34:
    print("obese(class I)")
elif bmi<39:
    print("obese(class II)")
else:
    print("obese(class III)")
