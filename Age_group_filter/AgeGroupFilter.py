
def main():

    # print("Current working directory:", os.getcwd())
    # Get file names and age threshold from input
    names_file = input("Enter the names file name: ")
    ages_file = input("Enter the ages file name: ")
    threshold_age = int(input("Enter the threshold age: "))

    # Create empty name and age lists
    names = []
    ages = []

    # Read in the data from the names file and store each name in the names list
    with open(names_file, 'r') as names_file:
        names = names_file.read().splitlines()

    # Read in the data from the ages file and store each age in the ages list
    with open(ages_file, 'r') as ages_file:
        ages = list(map(int, ages_file.read().splitlines()))

    # Create empty lists for above and below the threshold
    above_threshold = []
    below_threshold = []

    # Loop through the lists and check if the age is at or above the threshold
    for i in range(len(names)):
        if ages[i] >= threshold_age:
            above_threshold.append(names[i])
        else:
            below_threshold.append(names[i])

    # Print out people above the age threshold
    print(f'The people above or at the age of {threshold_age} are:')
    for person in above_threshold:
        print(person)

    # Print out people below the age threshold
    print(f'\nThe people below the age of {threshold_age} are:')
    for person in below_threshold:
        print(person)

if __name__ == "__main__":
    main()
