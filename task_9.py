import time

def main():
    currentHour = time.time()
    hour1 = time.localtime(currentHour)
    leftMinutes = 60 - hour1[4]
    leftHour = 18 - hour1[3]
    isEarly = False
    if leftMinutes > 0 and leftHour >= 0:
        isEarly = True
    elif leftHour > 0:
        isEarly = True

    if isEarly:
        print("Te quedan", leftHour, "horas con", leftMinutes, "minutos de trabajo")
    else:
        print("Es hora de ir a casa")
if __name__ == "__main__":
    main()
