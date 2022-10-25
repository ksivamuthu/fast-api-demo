import logging
import sys
from fastapi import FastAPI, Request

import uvicorn
sys.path.append('..')

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get('/healthz')
async def health():
    return { 'status': 'ok' }

# Add health check endpoint to call it from robot.
@app.post('/trigger')
async def trigger(request: Request):
    data = await request.json()
    ## TODO: Add the trigger logic from the robot
    return { 'status': 'ok' } 

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000)