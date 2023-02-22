def students_credits(*args):
    credits_dict = {}
    result = []
    course_credit_sorted = {}
    for i in args:
        credit = i.split('-')
        credits_dict[credit[0]] = []
        credits_dict[credit[0]] = (int(credit[3])/int(credit[2])*int(credit[1]))

    sum_credits = 0
    for v in credits_dict.values():
        sum_credits += v
    if sum_credits >= 240:
        result.append(f"Diyan gets a diploma with {sum_credits:.1f} credits.")
    else:
        diff = 240-sum_credits
        result.append(f"Diyan needs {diff:.1f} credits more for a diploma.")
    course_credit_sorted = sorted(credits_dict.items(), key=lambda x: -x[1])
    for k, v in course_credit_sorted:
        result.append(f"{k} - {v:.1f}")

    return "\n".join(str(x) for x in result)



print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
