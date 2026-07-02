from flask import Flask

app = Flask(__name__)

@app.route('/')
def sing():
    """Render the song with client-side animation."""
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
            body {{
                font-family: monospace;
                background-color: #1a1a1a;
                color: #00ff00;
                padding: 40px;
                min-height: 100vh;
                margin: 0;
            }}
            #lyrics {{
                font-size: 18px;
                line-height: 1.6;
                white-space: pre-wrap;
                word-wrap: break-word;
                min-height: 400px;
            }}
            .lyric-line {{
                margin: 10px 0;
                min-height: 20px;
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
                    for (let char of lyricData.text) {{
                        lineDiv.textContent += char;
                        await new Promise(resolve => setTimeout(resolve, lyricData.speed * 100));
                    }}
                }}
            }}
            
            // Start animation when page loads
            animateLyrics();
        </script>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
