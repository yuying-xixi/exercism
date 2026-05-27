def response(hey_bob):
    """
    :param hey_bob:str -向bob打招呼
    :return -bob的回应
    """
    
    trimmed = hey_bob.strip()
    
    is_question = trimmed.endswith("?")
    have_letter = any(word.isalpha() for word in trimmed)
    is_yell = have_letter and trimmed.isupper()
    
    #  This is how bob responds to silence. 
    if not trimmed:
        return "Fine. Be that way!"
    
    if is_question and is_yell:
        return "Calm down, I know what I'm doing!"
    
    if is_yell:
        return "Whoa, chill out!"
    
    if is_question:
        return "Sure."

    return "Whatever." 
