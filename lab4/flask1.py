from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/solve', methods=['POST'])
def solve():
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    # Вычисление дискриминанта
    D = b ** 2 - 4 * a * c
    # Проверка дискриминанта
    if D > 0:
        # Два различных корня
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        result = f"Корни уравнения: x1 = {x1}, x2 = {x2}"
    elif D == 0:
        # Один корень
        x = -b / (2 * a)
        result = f"Уравнение имеет один корень: x = {x}"
    else:
        # Два комплексных корня
        kom1 = -b / (2 * a)
        kom2=  (-D) ** 0.5 / (2 * a)
        result = f"Корни уравнения: x1 = {kom1} + {kom2}i, x2 = {kom1} - {kom2}i"
    return render_template('result.html', result=result)
if __name__ == '__main__':
    app.run()
