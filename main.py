from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

STATUS_FILE = 'status.txt'

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="ru">

<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Robohand</title>

<style>
    * {
    box-sizing: border-box;
    }

body {
    height: 100vh;
    margin: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Arial, sans-serif;
    background:
    linear-gradient(90deg,
        #243454 0%,
        #001130 35%,
        #000d28 70%,
        #0a1825 100%);
    }

.card {
    width: min(420px, 100%);
    padding: 24px;
    border: 1px solid #d8d8d8;
    border-radius: 8px;
    background: #312b2b;
    text-align: center;
}

    .button {
      background:
        radial-gradient(circle,
          rgba(15, 47, 153, 0.541) 18%,
          rgba(9, 39, 90, 0.95) 45%);
      width: 240px;
      height: 90px;
      border: none;
      border-radius: 20px;
      font-size: 30px;
      color: white;
      cursor: pointer;
      border: 2px solid #b2d73d;
      transition: transform 0.15s, opacity 0.15s;
    }

    .button:active {
      transform: scale(0.96);
    }

    .button:disabled {
      opacity: 0.6;
      cursor: wait;
    }

    .status {
      margin-top: 18px;
      font-size: 28px;
      color: white;
      text-align: center;
    }

    dd {
      display: block;
      margin-inline-start: 0px;
      margin-top: 10px;
      unicode-bidi: isolate;
      justify-content: center;
    }

    .date {
      margin-top: 16px;
      font-size: 14px;
      color: #bdbdbd;
    }

    .error {
      margin-top: 16px;
      font-size: 14px;
      color: #ff3b30;
    }

.off-text {
    color: #ff3b30;
    font-weight: bold;
    }

.on-text {
    color: #34c759;
    font-weight: bold;
    }
</style>

</head>

<body>

<div class="card">
        <p>
            <a href="/?status=on">Включить (ON)</a> |
            <a href="/?status=off">Выключить (OFF)</a>
        </p>
    <div class="status">
        Текущий статус: {{status_text}}
        
    </div>

    <div id="dateText" class="date"></div>
    <div id="errorText" class="error"></div>
</div>

</body>

</html>
'''



def read_status():
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, 'r') as f:
            return f.read().strip()
    return 'OFF'


def write_status(status):
    with open(STATUS_FILE, 'w') as f:
        f.write(status)


@app.route('/')
def status():
    status_param = request.args.get('status', '').lower()

    if status_param == 'on':
        status_text = 'ON'
        write_status(status_text)
    elif status_param == 'off':
        status_text = 'OFF'
        write_status(status_text)
    else:
        status_text = read_status()

    return render_template_string(HTML_TEMPLATE, 
        status_text=status_text,
        status_file=STATUS_FILE)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)