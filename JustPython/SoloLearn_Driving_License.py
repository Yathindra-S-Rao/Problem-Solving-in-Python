#       Driver's license
#       inputs Name, number of agents and string of other names
#       Takes 20 mins to process one application 

try:
    applicant = input("Enter the applicant's name : ")
    agents = int(input("Enter number of agents in office : "))
    other_applicants = input("Enter other applicants names : ")

    all_applicants = other_applicants.split(" ")
    all_applicants.append(applicant)
    all_applicants.sort()

    #len(all_applicants)
    applicant_pos = all_applicants.index(applicant) + 1

    time = int((applicant_pos % agents) * 20)
    print("It takes {} minutes to process {}'s license".format(time, applicant))

except:
    print("something went wrong. run the code again")


