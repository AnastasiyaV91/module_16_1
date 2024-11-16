from fastapi import FastAPI
app = FastAPI()

@app.get("/")  #  При получении в запросе "/" отрабатывает функция welcome()
async def welcome():
    return "Главная страница"    # Возвращаем сообщение

@app.get("/user")  #  При получении в запросе "/user?username='Iliya'&age=24" отрабатывает функция user_3()
async def user_3(username=str, age=int):
        return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

@app.get("/user/admin")  #  При получении в запросе "/user/admin" отрабатывает функция user_1()
async def user_1():
        return "Вы вошли как администратор"

@app.get("/user/{user_id}")  #  При получении в запросе "/user/123" отрабатывает функция user_2()
async def user_2(user_id=int):
        return f"Вы вошли как пользователь № {user_id}"


"""
  Запускаем в терминале PyCharm
python -m uvicorn module_16_1:app  
      где module_16_1 - имя файла, 
      app - объект FastAPI() в коде main1.py

Для входа в FastAPI Swagger UI вводим http://127.0.0.1:8000/docs
"""