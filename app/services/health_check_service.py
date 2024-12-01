from fastapi import APIRouter
from ..utils.es_utils import check_es_health

healthrouter = APIRouter()

@healthrouter.get("/")
def health_check():
    if check_es_health():
        return {"status": "success", "message": "Elasticsearch is running"}
    else:
        return {"status": "failure", "message": "Elasticsearch is down"}
