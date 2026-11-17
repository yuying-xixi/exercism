def response(hey_bob):
    """
    :param hey_bob:str -向bob打招呼
    :return ：str -bob的回应
    """
    
    trimmed = hey_bob.strip()
    
    isQuestion = trimmed.endswith("?")
    haveLetter = any(word.isalpha() for word in trimmed)
    isYell = haveLetter and trimmed.isupper()
    
    #  This is how bob responds to silence. 
    if not trimmed:
        return "Fine. Be that way!"
    
    if isQuestion and isYell:
        return "Calm down, I know what I'm doing!"
    
    if isYell:
        return "Whoa, chill out!"
    
    if isQuestion:
        return "Sure."

    return "Whatever." 
