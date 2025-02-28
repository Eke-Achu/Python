def guessCapitals():
    countries = {"Armenia" : "Yerevan", "Bulgaria" : "Sofia", "Croatia" : "Zagreb",
        "Denmark" : "Copenhagen", "Egypt" : "Cairo", "Finland" : "Helsinki",
        "Gambia" : "Banjul", "Haiti" : "Port-au-Prince", "Indonesia" : "Jakarta",
        "Jamaica" : "Kingston", "Kuwait" : "Kuwait city", "Togo" : "Lome", "Peru": "Lima",
        "France" : "Paris", "China" : "Beijing", "Brazil" : "Brasilia", "Uganda" : "Kampala"}
    
    correct = 0

    for key in countries:
        answer = input(f"What is the capital of {key}: ")

        if answer == countries[key]:
            print("Your answer is correct")
            correct += 1
        else:
            print(f"The correct answer is {countries[key]}")

    print("The correct count is", correct)


def main():
    guessCapitals()


main()