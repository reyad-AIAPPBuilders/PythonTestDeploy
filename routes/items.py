from fastapi import APIRouter
from typing import Optional
from services.item_services import get_available_doctors

router = APIRouter()

@router.get("/")
def begin():
    return "Welcome to our services."

@router.get("/items/")
def get_items(q: Optional[str] = None):
    return {"query": q}

@router.get("/doctors/")
def get_doctors(numberOfDoc: int = 1):
    doc_list = get_available_doctors(int(numberOfDoc))
    return {
        "Available Doctors": doc_list
    }
