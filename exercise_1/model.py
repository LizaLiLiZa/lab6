# pylint: disable=E0213
import datetime
from typing import Optional
from pydantic import BaseModel, field_validator, EmailStr

from exercise_1.validation import ValidateInfo

class PersonModel(BaseModel):
    """
        Request create person
    """
    first_name: str
    last_name: str
    middle_name:  Optional[str] = None
    birthday_at: datetime.date
    phone: int
    email: EmailStr
    password: str

    @field_validator("first_name")
    def validate_first_name(cls, value: str):
        """
            Validation first name
        """        
        value = value.capitalize()
        if ValidateInfo.validation_name(value):
            return value
        raise ValueError(detail="Неверно введено имя пользователя!")

    @field_validator("last_name")
    def validate_last_name(cls, value: str):
        """
            Validation last name
        """
        value = value.capitalize()
        if ValidateInfo.validation_name(value):
            return value
        raise ValueError(detail="Неверно введена фамилия пользователя!")

    @field_validator("middle_name")
    def validate_middle_name(cls, value: str):
        """
            Validation middle name
        """
        value = value.capitalize()
        if value is None or ValidateInfo.validation_name(value):
            return value
        raise ValueError(detail="Неверно введено отчество пользователя!")

    @field_validator("birthday_at")
    def validate_birthday_at(cls, value: datetime.date):
        """
            Validation birthday
        """
        if ValidateInfo.validation_birthday_at(value):
            return value
        raise ValueError(detail="Вам должно быть больше 12 лет и меньше 120!")

    @field_validator("phone")
    def validate_phone(cls, value: int):
        """
            Validation phone
        """
        if ValidateInfo.validate_phone(str(value)):
            return value
        raise ValueError(detail="Неверный формат телефона")

    @field_validator("password")
    def validate_password(cls, value: str):
        """
            Validate password
        """
        if ValidateInfo.validate_password(value):
            return value
        raise ValueError(detail="Неверный формат пароля")

class PersonInfoModel(BaseModel):
    """
        Get person info
    """
    id: int
    first_name: str
    last_name: str
    middle_name: str
    birthday_at: datetime.date

    @field_validator("first_name")
    def validate_first_name(cls, value: str):
        """
            Validation first name
        """        
        value = value.capitalize()
        if ValidateInfo.validation_name(value):
            return value
        raise ValueError(detail="Неверно введено имя пользователя!")

    @field_validator("last_name")
    def validate_last_name(cls, value: str):
        """
            Validation last name
        """
        value = value.capitalize()
        if ValidateInfo.validation_name(value):
            return value
        raise ValueError(detail="Неверно введена фамилия пользователя!")

    @field_validator("middle_name")
    def validate_middle_name(cls, value: str):
        """
            Validation middle name
        """
        value = value.capitalize()
        if value is None or ValidateInfo.validation_name(value):
            return value
        raise ValueError(detail="Неверно введено отчество пользователя!")

    @field_validator("birthday_at")
    def validate_birthday_at(cls, value: datetime.date):
        """
            Validation birthday
        """
        if ValidateInfo.validation_birthday_at(value):
            return value
        raise ValueError(detail="Вам должно быть больше 12 лет и меньше 120!")

class PersonPasswordModel(BaseModel):
    """
        Password person
    """
    id: int
    password: str
    new_password: str

    @field_validator("password")
    def password_validate(cls, value: str):
        if ValidateInfo.validate_password(value):
            return value
        raise ValueError(detail="Неверный формат старого пароля.")

    @field_validator("new_password")
    def new_password_validate(cls, value: str):
        if ValidateInfo.validate_password(value):
            return value
        raise ValueError(detail="Неверный формат нового пароля.")
