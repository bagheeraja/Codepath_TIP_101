def sleep_assistant(hours: int):
    messages = ["Oof, go back to bed!",
                "You got a good night's rest!",
                "You're a sleep prodigy!"]
    
    if hours < 8:
        return(messages[0])
    elif 8 <= hours <= 10:
        return(messages[1])
    elif hours > 10:
        return(messages[2])
    else:
        return([])
    

print(sleep_assistant(8.00))
