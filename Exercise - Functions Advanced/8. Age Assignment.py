def age_assignment(*names, **data):
    result = []
    for let, age in data.items():
        person_name = ''
        for name in names:
            if name.startswith(let):
                person_name = name
                break

        result.append(f"{person_name} is {age} years old.")

    return '\n'.join(sorted(result))




print(age_assignment("Peter", "George", G=26, P=19))