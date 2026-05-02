def calculate_tip(bill: float, service_quality: str):
    tip_values = [0.10, 0.15, 0.20, None]

    if service_quality == "poor": 
        return(bill * tip_values[0])
    elif service_quality == "average":
        return(bill * tip_values[1])
    elif service_quality == "excellent":
        return(bill * tip_values[2])
    else:
        return(tip_values[3])
    
print(calculate_tip(150, "excellent"))