# main.py
from fastapi import FastAPI
from controllers.loginController import router as login_router
from controllers.tasksController import router as tasks_router

app = FastAPI(title="FastAPI", version="1.0.0")

app.include_router(login_router)
app.include_router(tasks_router)

@app.get("/")
def root():
    print("Hello Worlds")
    return {"message": "Hello World!!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)