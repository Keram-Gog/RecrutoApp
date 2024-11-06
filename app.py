from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    # Получаем параметры из запроса
    name = request.args.get('name', 'Recruto')  # По умолчанию 'Recruto'
    message = request.args.get('message', 'Давай дружить')  # По умолчанию 'Давай дружить'
    
    # Формируем и возвращаем ответ
    return f"Hello {name}! {message}"

if __name__ == '__main__':
    # Запускаем сервер на порту 5000
    app.run(host='0.0.0.0', port=5000)
