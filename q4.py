import numpy as np

hours = np.array([5, 3, 7, 2, 8, 4, 6, 1, 9, 5])
attend = np.array([90, 75, 95, 60, 98, 80, 85, 55, 99, 88])
prev_score = np.array([65, 58, 80, 45, 88, 62, 74, 40, 91, 70])
final_score = np.array([70, 60, 85, 50, 91, 66, 78, 44, 95, 76])

print("hours shape", hours.shape, hours.dtype)
print("attend shape", attend.shape, attend.dtype)
print("prev_score shape", prev_score.shape, prev_score.dtype)
print("final_score shape", final_score.shape, final_score.dtype)

print("mean:", final_score.mean())
print("max:", final_score.max())
print("min:", final_score.min())
print("std:", final_score.std())

bonus = final_score + 5
print("with bonus:", bonus)

passed = final_score >= 75
print("passed bool:", passed)
print("scores >= 75:", final_score[passed])
