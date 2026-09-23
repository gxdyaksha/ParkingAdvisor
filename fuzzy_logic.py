import numpy as np
import skfuzzy as fuzz


def calculate_parking_suitability(crowd_level, parking_space):
    # Input ranges
    crowd = np.arange(0, 11, 1)
    space = np.arange(0, 11, 1)

    # Output range
    suitability = np.arange(0, 101, 1)

    # Membership functions for crowd
    crowd_low = fuzz.trimf(crowd, [0, 0, 5])
    crowd_medium = fuzz.trimf(crowd, [0, 5, 10])
    crowd_high = fuzz.trimf(crowd, [5, 10, 10])

    # Membership functions for parking space
    space_small = fuzz.trimf(space, [0, 0, 5])
    space_medium = fuzz.trimf(space, [0, 5, 10])
    space_large = fuzz.trimf(space, [5, 10, 10])

    # Membership functions for suitability
    suitability_poor = fuzz.trimf(suitability, [0, 0, 50])
    suitability_moderate = fuzz.trimf(suitability, [25, 50, 75])
    suitability_good = fuzz.trimf(suitability, [50, 100, 100])

    # Fuzzification
    crowd_low_level = fuzz.interp_membership(
        crowd, crowd_low, crowd_level
    )
    crowd_medium_level = fuzz.interp_membership(
        crowd, crowd_medium, crowd_level
    )
    crowd_high_level = fuzz.interp_membership(
        crowd, crowd_high, crowd_level
    )

    space_small_level = fuzz.interp_membership(
        space, space_small, parking_space
    )
    space_medium_level = fuzz.interp_membership(
        space, space_medium, parking_space
    )
    space_large_level = fuzz.interp_membership(
        space, space_large, parking_space
    )

    # Fuzzy rules
    rule_poor = max(
        min(crowd_high_level, space_small_level),
        min(crowd_high_level, space_medium_level),
        min(crowd_medium_level, space_small_level)
    )

    rule_moderate = max(
        min(crowd_medium_level, space_medium_level),
        min(crowd_low_level, space_small_level)
    )

    rule_good = max(
        min(crowd_low_level, space_large_level),
        min(crowd_low_level, space_medium_level),
        min(crowd_medium_level, space_large_level)
    )

    # Apply rules to output membership functions
    poor_result = np.fmin(rule_poor, suitability_poor)
    moderate_result = np.fmin(rule_moderate, suitability_moderate)
    good_result = np.fmin(rule_good, suitability_good)

    # Combine all rule results
    combined_result = np.fmax(
        poor_result,
        np.fmax(moderate_result, good_result)
    )

    # Defuzzification
    if np.sum(combined_result) == 0:
        return 0

    score = fuzz.defuzz(
        suitability,
        combined_result,
        "centroid"
    )

    return round(score, 2)