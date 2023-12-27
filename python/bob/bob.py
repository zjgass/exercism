def response(hey_bob):
    """

    :param hey_bob: string - what was said to bob
    :return: string - bob's response
    """

    response = "Whatever."
    is_question = hey_bob.strip().endswith("?")
    is_upper = hey_bob.isupper()
    is_null_or_whitespace = hey_bob.isspace() or not hey_bob or hey_bob is None

    if (is_upper and is_question):
        response = "Calm down, I know what I'm doing!"
    elif (is_question):
        response = "Sure."
    elif (is_upper):
        response = "Whoa, chill out!"
    elif (is_null_or_whitespace):
        response = "Fine. Be that way!"

    return response
