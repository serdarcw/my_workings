cigar = input("Are you a cigarette addict older than 75 years old? (True or False): ")
severe = input("Do you have a severe chronic disease? (True or False) : ")
immune = input("Is your immune system too weak? (True or False): ")
if cigar == 'True' or severe == 'True' or immune == 'True':
    print("You are in risky group")
else:
    print("You are not in risky group")