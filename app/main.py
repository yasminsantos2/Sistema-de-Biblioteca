from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.rotas.livro import router as livro_router

app = FastAPI(
    title="Sistema Bibliotecas API",
    description="CRM para Bibliotecas",
    version="1.0.0"
) 

app.include_router(livro_router)

@app.get("/")
async def health_check():
    return {"status": "OK"}

@app.get("/front", response_class=HTMLResponse)
async def front_page():
    html_content = """
    <html>
        <head>
            <title>Sistema Bibliotecas</title>
        </head>
        <body>
            <h1>🔪 Sistema Bibliotecas</h1>
            <p>Sistema de Gestão de Ordens de Serviço</p>
            <p>Status: <strong>Operacional</strong></p>
        </body>
    </html>
    """
    return html_content