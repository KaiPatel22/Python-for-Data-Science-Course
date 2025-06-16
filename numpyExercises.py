import numpy as np

stepsArray = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [6012, 7079, 6886, 7230, 598, 5564, 6971, 7763, 8032, 9569]])
print(stepsArray)
additionalSteps = np.array([[0], [2000]])
newStepsArray = np.add(stepsArray, additionalSteps)
print(f"Steps with additional steps: {newStepsArray}")
stepIndexWithCondition = np.where(newStepsArray > 9000)[1]
print(f"Indices of steps greater than 9000: {stepIndexWithCondition}")
stepsWithCondition = newStepsArray[:, stepIndexWithCondition]
print(f"Steps greater than 9000: {stepsWithCondition}")
sortedSteps = np.sort(newStepsArray)
print(f"Sorted steps: {sortedSteps}")