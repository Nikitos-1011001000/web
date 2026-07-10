import os
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# 1. Находим папку, где лежит этот скрипт (app.py)
base_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(base_dir, 'templates', 'contacts.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_data = request.form.to_dict()

        print(f"\n✅ Получены данные от пользователя: {form_data}\n")

        return """
            <html>
              <head><meta charset="utf-8"></head>
              <body style="text-align:center; padding:50px; font-family:Arial;">
                <h1 style="color:green;">✅ Спасибо за ваше сообщение!</h1>
                <p>Данные успешно получены сервером.</p>
                <a href="/" style="text-decoration:none; color:#007bff;">← Вернуться к форме</a>
              </body>
            </html>
            """, 200, {'Content-Type': 'text/html; charset=utf-8'}

    # 2. Если это обычный заход на страницу (GET) — отдаём contacts.html
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read(), 200, {'Content-Type': 'text/html; charset=utf-8'}


    except Exception as e:
        return f"<h1>Ошибка чтения: {str(e)}</h1>", 500

if __name__ == '__main__':
    app.run(debug=True)