def yueshefu(total,step,rest):
    a=list(range(1,total+1))
    while len(a)>rest:
        print(f'{a[step-1]}号下船了')
        a=a[step:] + a[:step-1]
        print(a)
a=int(input('人数='))
b=int(input('步数='))
c=int(input('存活人数='))
yueshefu(a,b,c)