from xml.dom import UserDataHandler
 
def user_details():
    """
    Prompt user input
    """
    first_name = input()
    for i in first_name:
        if i.isnumeric():
           pass

    last_name = input()
    for i in last_name:
        if i.isnumeric():
            pass

    cohort = input()
    final_campus = input()
    user_campus(final_campus)


    create_user_name(first_name, last_name, cohort, final_campus)

def create_user_name(first_name, last_name, cohort, final_campus):
    """ 
    Create and return a valid username
    """
    return first_name[-3:].lower() + last_name[:3].lower() + final_campus + cohort


def user_campus(campus):
    """
    Return valid campus abbreviations
    """
    valid_campus = {"Durban":"DBN", "Cape Town":"CPT", "Johannesburg":"JHB", "Phokeng":"PHO"}
    if campus in valid_campus:
        return valid_campus[campus]



if __name__ == '__main__':
    user_details()
    