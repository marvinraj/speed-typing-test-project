import time


def main():

    to_start = input("press enter to start!")
    
    # start timer
    start = time.time()
    user_input = input("enter your name now: ")
    end = time.time()
    # end timer

    # calculate time taken to type out the sentence
    time_taken = end - start    
    print("time taken : " + str(time_taken))

    # calculate the wpm/speed 
    wpm = len(user_input)*60/(5*time_taken)
    print("wpm : " + str(wpm))

if __name__ == "__main__":
    main()
