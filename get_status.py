def get_status(success):
    if success:
        msg = "It worked!"
    else:
        msg = None
    return "Status: " + msg