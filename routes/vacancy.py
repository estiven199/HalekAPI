import uuid
from bson import ObjectId
from utils.functions import requirements
from utils.functions import VerifyTokenRoute
from models.responses import VacancyResposive
from config.db import connect_to_database as ctb
from models.vacancy import Vacancy, VacancyUpdate
from schemas.vacancy import VacancyEntity, VacanciesEntity
from fastapi import APIRouter, Header, HTTPException, status

vacancy_routes = APIRouter(route_class=VerifyTokenRoute)

@vacancy_routes.get('/vacancies/{vacancy_id}', response_model=VacancyResposive, tags=["Module Vacancy"])
async def find_user(vacancy_id: str, Authorization: str = Header(None)):
    db = ctb.connect_to_mongo(Authorization)
    data_vacancy = db.vacancies.find_one({"VacancyId": vacancy_id})
    if data_vacancy == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    return {
        "code": 0,
        "message": "success",
        "data": VacancyEntity(data_vacancy)
    }


@vacancy_routes.get('/vacancies', response_model=VacancyResposive, tags=["Module Vacancy"])
async def get_vacancies(Authorization: str = Header(None)):
    db = ctb.connect_to_mongo(Authorization)
    return {
        "code": 0,
        "message": "success",
        "data": {"vacancies": VacanciesEntity(db.vacancies.find())}
    }


@vacancy_routes.post('/vacancies', response_model=VacancyResposive, tags=["Module Vacancy"])
async def create_vacancy(vacancy: Vacancy, Authorization: str = Header(None)):
    db = ctb.connect_to_mongo(Authorization)
    new_vacancy = dict(vacancy)
    id = db.vacancies.insert_one(new_vacancy).inserted_id
    vacancy = db.vacancies.update_one(
        {"_id": ObjectId(id)}, {"$set": {"VacancyId": str(uuid.uuid4())}})
    vacancy = db.vacancies.find_one({"_id": ObjectId(id)})
    return {
        "code": 0,
        "message": "The Vacancy has been created",
        "data": VacancyEntity(vacancy)
    }


@vacancy_routes.put("/vacancies/{vacancy_id}", response_model=VacancyResposive, tags=["Module Vacancy"])
async def update_vacancy(vacancy_id: str, vacancy: VacancyUpdate, Authorization: str = Header(None)):
    db = ctb.connect_to_mongo(Authorization)
    update_data = dict(vacancy)
    data_upate = {k: v for k, v in update_data.items() if v != None}
    print(data_upate)
    db.vacancies.find_one_and_update({
        "VacancyId": vacancy_id
    }, {
        "$set": data_upate
    })
    return {
        "code": 0,
        "message": "Vacancy has been updated successfully",
        "data":  VacancyEntity(db.vacancies.find_one({"VacancyId": vacancy_id}))
    }


@vacancy_routes.get("/searches_vacancies/{user_id}", tags=["Module Vacancy"])
async def searches_vacancies(user_id: str, Authorization: str = Header(None)):
    db = ctb.connect_to_mongo(Authorization)
    print(user_id)
    data_user = db.users.find_one({"UserId": user_id})
    if data_user == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    RequiredSkills = [{key: {"$exists": True}}
                      for skiil in data_user['Skills'] for key in skiil.keys()]
    inf_vacancies = [vacancy for vacancy in db.vacancies.find({"RequiredSkills": {"$all": [
        {
            "$elemMatch": {
                "$or": RequiredSkills
            }
        }
    ]
    }}) if requirements(vacancy['RequiredSkills'], data_user['Skills']) >= 0.5]

    return {
        "code": 0,
        "message": "success",
        "data":  VacanciesEntity(inf_vacancies)
    }
