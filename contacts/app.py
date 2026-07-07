import requests
from flask import Flask, request, render_template

app = Flask(__name__)

REMOTE_HTML_URL = "https://example.com/path/to/contacts.html"

@app.route("/", methods=['GET', 'POST'])
@app.route("/<path:path>", methods=['GET'])
def contacts():
    if request.method == 'GET':
        try:
            # Загружаем HTML из удалённого репозитория
            response = requests.get(REMOTE_HTML_URL, timeout=10)
            response.raise_for_status()  # Проверяем на ошибки HTTP
            html_content = response.text

            return html_content, 200, {'Content-Type': 'text/html; charset=utf-8'}

        except requests.RequestException as e:
            print(f"Ошибка загрузки удалённого HTML: {e}")
            # Fallback: пытаемся загрузить локальную копию
            try:
                return render_template("contacts.html"), 200, {'Content-Type': 'text/html; charset=utf-8'}
            except Exception as local_error:
                return f"<h1>Ошибка загрузки страницы</h1><p>Ошибка: {local_error}</p>", 500

    elif request.method == 'POST':
        data = request.form.to_dict()
        print("Получены данные от пользователя:")
        for key, value in data.items():
            print(f"{key}: {value}")

        response = """
        <html>
        <head><title>Спасибо!</title></head>
        <body>
            <h1>Спасибо за ваше сообщение!</h1>
            <p><a href="/">Вернуться на страницу контактов</a></p>
        </body>
        </html>
        """
        return response, 200, {'Content-Type': 'text/html; charset=utf-8'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)