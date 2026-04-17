from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>App Docker - Fono Borel</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .card {
            background: white;
            border-radius: 20px;
            padding: 50px 40px;
            text-align: center;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 500px;
        }
        .logo { font-size: 60px; margin-bottom: 20px; }
        h1 { color: #333; font-size: 28px; margin-bottom: 10px; }
        p { color: #666; font-size: 16px; margin-bottom: 20px; }
        .badge {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 8px 20px;
            border-radius: 20px;
            font-weight: bold;
            display: inline-block;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="logo">🐳</div>
        <h1>Bonjour à tous !</h1>
        <p>Ceci est une application Flask conteneurisée avec Docker</p>
        <div class="badge">par Fono Borel</div>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
