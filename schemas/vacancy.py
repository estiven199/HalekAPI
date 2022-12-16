def VacancyEntity(vacantyJson) -> dict:
    return {
        "VacancyId": vacantyJson["VacancyId"],
        "PositionName": vacantyJson["PositionName"],
        "CompanyName": vacantyJson["CompanyName"],
        "Salary": vacantyJson["Salary"],
        "Currency": vacantyJson["Currency"],
        "VacancyLink": vacantyJson["VacancyLink"],
        "RequiredSkills": vacantyJson["RequiredSkills"]
    }


def VacanciesEntity(entity) -> list:
    return [VacancyEntity(vacancy) for vacancy in entity]
