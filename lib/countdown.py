# your code goes here!
def countdown(n):
    while n > 0:
        print(f"{n} SECOND(S)!")
        n -= 1
    print("HAPPY NEW YEAR!")


def countdown_with_sleep(n):
    import time 
    while n > 0:
        print(f"{n} SECOND(S)!")
        time.sleep(1)
        n -= 1
    print("HAPPY NEW YEAR!")
