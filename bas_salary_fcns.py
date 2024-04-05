def bas(basics):
    ta=0.1*basics
    da=0.12*basics
    gross=basic+ta+da
    print(gross)
basic=int(input("Enter the salary: "))
print(bas(basic))
