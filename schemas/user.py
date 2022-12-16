
def userEntity(userJson) -> dict:
    return {
        "UserId": userJson["UserId"],
        "FirstName": userJson["FirstName"],
        "LastName": userJson["LastName"],
        "Email": userJson["Email"],
        "YearsPreviousExperience": userJson["Email"],
        "Skills": userJson["Skills"],
    }

def usersEntity(entity) -> list:
    return [userEntity(user) for user in entity]