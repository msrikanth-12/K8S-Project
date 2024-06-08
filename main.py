#uvicorn main:app --reload
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()
#templates = Jinja2Templates(directory="/code")
templates = Jinja2Templates(directory="C:/Users/Lenovo/Desktop/k8_Project")

@app.get("/mypage")
def form_post(request: Request):
    return templates.TemplateResponse('form.html', context={'request': request})
