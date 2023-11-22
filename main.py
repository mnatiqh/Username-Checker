import requests

print("Username checker for platforms")

print("Here you can check availability of different usernames on different platforms. Just write your desired username when asked to input and found out whether your usernames are taken or not. Enter q when you don't have anymore usernames to search for.")

while True:
    username = input("Enter username or q to quit: ")

    if username == "q":
        break
    else:
        pass

    platforms = [
        "https://www.github.com",
        "https://www.instagram.com",
        "https://www.facebook.com",
        "https://www.x.com",
        "https://www.tiktok.com/en/",
        "https://www.linkedin.com"
    ]
    
    domains = []

    for i in range(len(platforms)):
        url = f"{platforms[i]}/{username}"
        print("Fetching details for ",platforms[i],"...")
        domain = platforms[i].split(".")[1]

        response = requests.get(url)

        code = response.status_code

        if ( code == 200 ):
            print("Given username not available " , platforms[i])

        else:
            print("Given username is available " , platforms[i])
            domains.append(domain)

    print("")
    print(f"Given username {username} is avaialble on follwoing platforms : ")
    for k in domains:
        print(k)
    print("")


