from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def sing():
    """Render the song with optimized client-side animation."""
    lyrics = [
        ("Do you think I have forgotten?", 0.05),
        ("Do you think I have forgotten?", 0.05),
        ("Do you think I have forgotten", 0.05),
        ("about you?", 0.1),
        ("There was something bout you that now I cant remember", 0.04),
        ("Its the same damn thing that made my heart surrender", 0.05),
        ("And I miss you on a train, I miss you in the morning", 0.05),
        ("I never know what to think about", 0.05),
        ("I think about youuuuuuuuuuuuuuuuuuuuuuuuuuu", 0.05)
    ]
    
    lyrics_json = []
    delays = [0.3, 5.0, 10.0, 15.0, 20.3, 25.0, 27.0, 30.2, 33.3]
    
    for i, (lyric, speed) in enumerate(lyrics):
        lyrics_json.append({
            'text': lyric,
            'delay': delays[i],
            'speed': speed
        })
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>About You</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            body {{
                font-family: 'Courier New', monospace;
                background: linear-gradient(135deg, #0a0e27 0%, #1a1a3a 100%);
                color: #00ff00;
                padding: 40px;
                min-height: 100vh;
                overflow-x: hidden;
            }}
            #lyrics {{
                font-size: 20px;
                line-height: 1.8;
                white-space: pre-wrap;
                word-wrap: break-word;
                min-height: 400px;
                text-shadow: 0 0 10px rgba(0, 255, 0, 0.5);
                letter-spacing: 1px;
            }}
            .lyric-line {{
                margin: 12px 0;
                min-height: 24px;
                animation: fadeIn 0.3s ease-in;
            }}
            @keyframes fadeIn {{
                from {{
                    opacity: 0;
                    text-shadow: 0 0 0px rgba(0, 255, 0, 0);
                }}
                to {{
                    opacity: 1;
                    text-shadow: 0 0 10px rgba(0, 255, 0, 0.5);
                }}
            }}
            .cursor {{
                display: inline-block;
                width: 2px;
                height: 1em;
                background-color: #00ff00;
                margin-left: 2px;
                animation: blink 0.7s infinite;
            }}
            @keyframes blink {{
                0%, 49% {{ opacity: 1; }}
                50%, 100% {{ opacity: 0; }}
            }}
        </style>
    </head>
    <body>
        <div id="lyrics"></div>
        
        <script>
            const lyricsData = {json.dumps(lyrics_json)};
            
            async function animateLyrics() {{
                const lyricsDiv = document.getElementById('lyrics');
                
                for (let lyricData of lyricsData) {{
                    // Wait for the delay
                    await new Promise(resolve => setTimeout(resolve, lyricData.delay * 1000));
                    
                    // Create a new line
                    const lineDiv = document.createElement('div');
                    lineDiv.className = 'lyric-line';
                    lyricsDiv.appendChild(lineDiv);
                    
                    // Animate text character by character
                    const text = lyricData.text;
                    const speed = lyricData.speed * 50; // Optimize speed
                    
                    for (let i = 0; i < text.length; i++) {{
                        lineDiv.textContent = text.substring(0, i + 1);
                        await new Promise(resolve => setTimeout(resolve, speed));
                    }}
                }}
                
                // Add cursor at the end
                const cursor = document.createElement('span');
                cursor.className = 'cursor';
                lyricsDiv.appendChild(cursor);
            }}
            
            // Start animation when page loads
            window.addEventListener('load', animateLyrics);
        </script>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
