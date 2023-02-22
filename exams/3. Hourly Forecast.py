def forecast(*args):
    result = []
    keys = ["Sunny", "Cloudy", "Rainy"]
    args = sorted(args, key=lambda x: (keys.index(x[1]), x[0]))
    for city in args:

        result.append(f"{city[0]} - {city[1]}")

    return '\n'.join(result)


print(forecast(
("Beijing", "Sunny"),
("Hong Kong", "Rainy"),
("Tokyo", "Sunny"),
("Sofia", "Cloudy"),
("Peru", "Sunny"),
("Florence", "Cloudy"),
("Bourgas", "Sunny")))