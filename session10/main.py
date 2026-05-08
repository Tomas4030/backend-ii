import uvicorn
from app.api import api

def main():
    uvicorn.run(api, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
