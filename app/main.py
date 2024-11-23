from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.llama_handler import query_model

# Инициализация приложения
app = FastAPI()

# Модель данных для запросов
class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate(prompt_request: PromptRequest):
    """
    Получает запрос с текстом и передает его в модель.
    Возвращает ответ модели.
    """
    try:
        response = query_model(prompt_request.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
