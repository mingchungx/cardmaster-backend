import pandas as pd, csv

"""
CSV Format

username,travelFreq,travelInterest,occupation,income,creditScore,budget
"""

# Similarity of users
"""
Data representation:
travel freq: bool
travel interest: bool
occupations- student, early professional, mid-career, business owner, freelance, executive, unemployed 
credit score- poor, fair, good, great, excellent
income
budget
tags

liked cards
disliked cards
"""

"""student - occupation:student"""
"""business - occupation:business owner,freelance,executive"""
"""travel - moderate-high travel freq; moderate-high travel interest"""
"""elite - occupation:mid-career,business owner,executive ; credit score: great,exellent ; income:100 000+ ; budget:100+"""
users = pd.read_csv("users.csv")
fobj = open("bin_users.csv", "w")
fieldnames = [
    "username",
    "fingerprint",
]  # TODO fill this in
refined_users = csv.DictWriter(fobj, fieldnames=fieldnames)
refined_users.writeheader()
occupations = [
    "student",
    "earlyProfessional",
    "midCareer",
    "businessOwner",
    "freelance",
    "executive",
    "unemployed",
]
credit_ranges = ["poor", "fair", "good", "great", "excellent"]


def userToBin(occupation, travelFrequency, travelInterest, creditScore, income, budget):
    user_fingerprint = ""
    user_fingerprint += str(int(occupation == occupations[0]))
    user_fingerprint += str(int(occupation in occupations[3:6]))
    user_fingerprint += str(int(travelFrequency or travelInterest))
    user_fingerprint += str(
        int(
            (occupation in occupations[2:4] + [occupations[5]])
            or creditScore in credit_ranges[3:]
            or income >= 100000
            or budget >= 100
        )
    )
    return user_fingerprint


for (
    idx,
    row,
) in users.iterrows():
    # Binary representation of user's associated tags
    # [student,business,travel,elite]
    user_fingerprint = userToBin(
        row["occupation"],
        row["travelFrequency"],
        row["travelInterest"],
        row["creditScore"],
        row["income"],
        row["budget"],
    )
    # Dump into another csv file
    refined_users.writerow([row["username"], user_fingerprint])

fobj.close()
# occupation:mid-career,business owner,executive ; credit score: great,exellent ; income:100 000+ ; budget:100+

# Tags: student (based on occupation),
# business (based on occupation),
# travels (based on travel freq and travel interest),
# cash back (everyone),
# elite (based on occupations, credit score, income, budget),
# store (recommended to everyone; user filters out whether or not they want to see it)


# Card recommendations based on similar users
