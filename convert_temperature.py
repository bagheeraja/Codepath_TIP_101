def convertTemp(celsius: float):
    ans = []

    kelvin = celsius + 273.15
    fahrenheit = (celsius * 1.80) + 32.00

    ans.append(round(kelvin, 2))
    ans.append(round(fahrenheit, 2))
    
    return ans

temperatures = convertTemp(23.00)

print([f"{t:.2f}" for t in temperatures])