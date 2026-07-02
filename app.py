from flask import Flask, render_template
import time
from threading import Thread, Lock

app = Flask(__name__)
lock = Lock()

def animate_text(text, delay=0.1):
    """Animate text with character-by-character output."""
    result = ""
    for char in text:
        result += char
        time.sleep(delay)
    return result

def render_lyrics():
    """Generate the animated lyrics as HTML."""
    lyrics = [
        ("Do you think I have forgotten?", 0.1),
        ("Do you think I have forgotten?", 0.1),
        ("Do you think I have forgotten", 0.1),
        ("about you?", 0.2),
        ("There was something bout you that now I cant remember", 0.08),
        ("Its the same damn thing that made my heart surrender", 0.1),
        ("And I miss you on a train, I miss you in the morning", 0.1),
        ("I never know what to think about", 0.1),
        ("I think about youuuuuuuuuuuuuuuuuuuuuuuuuuu", 0.1)
    ]
    
    result = ""
    for lyric, speed in lyrics:
        result += animate_text(lyric, speed) + "\n"
    
    return result

@app.route('/')
def sing():
    """Render the song with client-side animation."""
    lyrics_html = render_lyrics()
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>About You</title>
        <style>
            body {{
                font-family: monospace;
                background-color: #1a1a1a;
                color: #00ff00;
                padding: 40px;
                min-height: 100vh;
            }}
            pre {{
                font-size: 18px;
                line-height: 1.6;
                white-space: pre-wrap;
                word-wrap: break-word;
            }}
        </style>
    </head>
    <body>
        <pre>{lyrics_html}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
