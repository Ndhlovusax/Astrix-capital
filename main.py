from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(title='Astrix Capital API (skeleton)')
class Health(BaseModel):
    status: str
@app.get('/health', response_model=Health)
def health():
    return {'status':'ok'}
@app.get('/v1/astrix/{symbol}')
def astrix_read(symbol: str):
    return {'symbol': symbol.upper(), 'bias': 'Bullish', 'confidence': 72.4}
