html_part_1= """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
    <style>
        body {
            font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;
            line-height: 1.6;
            color: #3e3e3e;
            background-color: #f7f3ed; /* Light parchment/cream background */
            margin: 0;
            padding: 25px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            box-sizing: border-box;
        }
        .container {
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.12);
            padding: 35px 50px;
            max-width: 650px;
            text-align: center;
            border: 1px solid #e0d9cd;
            animation: fadeIn 1.5s ease-out forwards;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        h1 {
            color: #7a5a40; /* Earthy brown for heading */
            font-size: 2.4em;
            margin-bottom: 25px;
            font-weight: normal;
            letter-spacing: 1px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.05);
        }
        .previous-action {
            font-size: 1.05em;
            color: #666;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 1px dashed #dcdcdc;
            font-style: italic;
        }
        .continuation {
            font-size: 1.3em;
            color: #4c6a49; /* Serene green for the continuation */
            margin-top: 25px;
            font-weight: bold;
        }
        .continuation p {
            margin: 0;
        }
    </style>
</head>"""

def generate_html(title, current_story,previous_action):
    html_part_2= f"""
    <body>
        <div class="container">
            <h1>{title}</h1>
            <p class="previous-action">Azione Corrente: {previous_action}.</p>
            <div class="continuation">
                <p>{current_story}</p>
            </div>
        </div>
    </body>
    </html>"""
    return html_part_1+html_part_2
