import time
import requests


def main():
    # instructions
    print("\nType in the sentence below upon clicking enter!\n")
    # api here
    category = "happiness"
    api_url = "https://api.api-ninjas.com/v1/quotes?category={}".format(category)
    response = requests.get(api_url, headers={"X-Api-Key": "n4FilKP0NZDqYZguKKP1+Q==TePugoKqGLVK4rQJ"})

    if response.status_code == requests.codes.ok:
        data = response.json()
        print(data[0]["quote"])
    else:
        print("Error:", response.status_code, response.text)

    # q to start timer
    to_start = input("\npress enter to start!")
    
    # start timer
    start = time.time()
    user_input = input("\ntype the sentence here : ")
    end = time.time()
    # end timer

    # calculate time taken to type out the sentence
    time_taken = end - start    
    print("time taken : " + str(round(time_taken, 2)))

    # calculate the wpm/speed 
    wpm = len(user_input)*60/(5*time_taken)
    print("wpm : " + str(round(wpm, 2)))

if __name__ == "__main__":
    main()
