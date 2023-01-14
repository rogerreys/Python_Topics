import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def get_list():
    return """
    <h1>Hello I'm Roger Reys</h1>
    <h2>Welcome</h2>
    """

@app.get("/contact")
def get_list():
    return {'name': 'roger_reys'}

def run():
    store.get_catalog()

if __name__=='__main__':
    run()