import openai
import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
from aiohttp import ClientSession
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

openai.aiosession.set(ClientSession())

def create_prompt(question, answer):
    return f"Validate in br-portuguese if the answer {answer} for the question {question} is correct. If it's correct return 'Resposta Correta!' else if it's wrong give the right answer for the question." #Extracting important information from the answer.

@app.get("/", response_class=HTMLResponse)
def dry_run(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
async def index(request: Request, api_key: str = Form(), question: str= Form(...), answer: str = Form(...)):
    openai.api_key = api_key
    prompt = create_prompt(question, answer)
    response = await openai.Completion.acreate(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.1,
    )
    result = response.choices[0].text
    if result == "":
        result = "Alguma coisa acontece de errado. Tente novamente em alguns instantes."
    await openai.aiosession.get().close()
    return templates.TemplateResponse("index.html", {"request": request, "result": result})



if __name__ == "__main__":
    uvicorn.run('main:app', host="localhost", port=8001, reload=True)
    