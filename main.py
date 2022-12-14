from os import getenv

import uvicorn
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    HOST = getenv("HOST")
    PORT = getenv("PORT")
    uvicorn.run("app.routes:app", host=HOST, port=int(PORT), reload=True)
