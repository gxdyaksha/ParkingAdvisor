from gemini_advisor import get_parking_advice


situation = "The parking area is crowded and the parking space is small."

crowd_level = 8
parking_space = 3
score = 31.66


advice = get_parking_advice(
    situation,
    crowd_level,
    parking_space,
    score
)


print("Parking Advice:")
print(advice)