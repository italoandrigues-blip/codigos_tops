for i in range(10):   
    n = (input("n: "))
   
    try: 
        n = int(n)
    except:
        try:
            n = float(n)
        except:
            try:
                n = complex(n)
            except:
                continue

    print(n)
    print(type(n))
