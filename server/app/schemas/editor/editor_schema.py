from pydantic import BaseModel, Field
from typing import Optional

class EditorBase(BaseModel):
    issue_id: int 
    firstname_en: str
    firstname_mn: str
    firstname_tr: str

    middlename_en: Optional[str] = None
    middlename_mn: Optional[str] = None
    middlename_tr: Optional[str] = None

    lastname_en: str
    lastname_mn: str
    lastname_tr: str

    role_en: str
    role_mn: str
    role_tr: str

    suffix_en: Optional[str] = None
    suffix_mn: Optional[str] = None
    suffix_tr: Optional[str] = None

class EditorCreate(EditorBase):
    pass

class EditorUpdate(BaseModel):
    firstname_en: Optional[str] = None
    firstname_mn: Optional[str] = None
    firstname_tr: Optional[str] = None

    middlename_en: Optional[str] = None
    middlename_mn: Optional[str] = None
    middlename_tr: Optional[str] = None

    lastname_en: Optional[str] = None
    lastname_mn: Optional[str] = None
    lastname_tr: Optional[str] = None

    role_en: Optional[str] = None
    role_mn: Optional[str] = None
    role_tr: Optional[str] = None

    suffix_en: Optional[str] = None
    suffix_mn: Optional[str] = None
    suffix_tr: Optional[str] = None

class EditorResponse(BaseModel):
    issue_id: int = Field(..., example=1)

    firstname_en: str = Field(..., example="Bold")
    firstname_mn: str = Field(..., example="Болд")
    firstname_tr: str = Field(..., example="Bold")

    middlename_en: Optional[str] = Field(None, example="T.")
    middlename_mn: Optional[str] = Field(None, example="T.")
    middlename_tr: Optional[str] = Field(None, example="T.")

    lastname_en: str = Field(..., example="Bat")
    lastname_mn: str = Field(..., example="Бат")
    lastname_tr: str = Field(..., example="Bat")

    role_en: str = Field(..., example="Editor")
    role_mn: str = Field(..., example="Редактор")
    role_tr: str = Field(..., example="Editor")

    suffix_en: Optional[str] = Field(None, example="Jr.")
    suffix_mn: Optional[str] = Field(None, example="Жр.")
    suffix_tr: Optional[str] = Field(None, example="Jr.")
