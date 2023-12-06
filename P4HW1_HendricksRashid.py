#CTI-110
#P4HW1 - Score List
#Rashid Hendricks
#November 7, 2023
#

# Create an empty list
listOfScores = []

# Get user input for numberOfScores
numberOfScores = int(input("How many numbers you want to enter? "))

# Initialize currentNumOfScores to 0
currentNumOfScores = 0

# Loop until required number of scores have been entered
while (True):

    # Loop for user input
    while (currentNumOfScores < numberOfScores):
        scores = float(input('Enter score #{}: '.format(currentNumOfScores + 1)))

        # Prompt for user input if entered score was invalid
        while (True):
            if (scores < 0 or scores > 100):
                print("\nINVALID Score entered!!!!\nScore should be between 0 and 100")
                scores = float(input('Enter score #{} again: '.format(currentNumOfScores + 1)))

            # If valid score was entered
            else:

                # Add to the list
                listOfScores.append(scores)

                # Break out of the loop as a valid score was entered
                break

        # Count currentNumOfScores in increments of 1
        # when a valid score is entered
        currentNumOfScores += 1

        # If user entered required number of valid scores
    if (currentNumOfScores == numberOfScores):
        # Break the loop as all required input has been entered
        break

# Calculate minimum score
minElement = min(listOfScores)

# Remove min score from the list
listOfScores.remove(min(listOfScores))

# Calculate average score
average = sum(listOfScores) / len(listOfScores)

# Calculate grade based on the average score
if (average >= 90 and average <= 100):
    grade = 'A'

elif (average >= 80 and average <= 89.9):
    grade = 'B'

elif (average >= 70 and average <= 79.9):
    grade = 'C'

elif (average >= 60 and average <= 69.9):
    grade = 'D'

else: (average < 59.9)
grade = 'F'

# Display result on the console
print("--------------------Results----------------------")
print("Lowest Score  :", minElement)
print("Modified List :", listOfScores)
print("Scores Average:", average)
print("Grade         :", grade)
print("-------------------------------------------------")
