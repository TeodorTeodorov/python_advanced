def students_credits(*args):
    diyan_cradits_list = []
    course_credit = {}
    final_strings = []
    for el in args:

        course_name, credit, max_test_points, diyan_points = el.split('-')
        diyan_cradits = int(diyan_points) / int(max_test_points) * int(credit)
        diyan_cradits_list.append(diyan_cradits)
        course_credit[course_name] = diyan_cradits

    if sum(diyan_cradits_list) >= 240:
        print(f"Diyan gets a diploma with {sum(diyan_cradits_list):.1f} credits.")
    else:
        print(f"Diyan needs {(240 - sum(diyan_cradits_list)):.1f} credits more for a diploma.")

    course_credit = sorted(course_credit.items(), key=lambda x: -x[1])

    for course, points in course_credit:
        final_strings.append(f"{course} - {float(points):.1f}")
    # final_strings = str(final_strings)
    # return "\n".join(str(x) for x in final_strings)
    return "\n".join(final_strings)







print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)



