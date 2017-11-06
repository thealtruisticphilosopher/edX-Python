def genPrimes():
    prime = 2
    while True:
        if prime==2:
            yield prime
            prime +=1
        else:
            for i in range(2, prime):
                if (prime % i)==0:
                    prime += 1
                    break
            else:
                yield prime
                prime += 1