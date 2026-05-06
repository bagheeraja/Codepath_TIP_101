def calculate_gpa(report_card: dict[str,str]) -> float:
    grades = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
    total = 0

    for grade in report_card.values():
        total += grades[grade]

    return total/len(report_card)

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))