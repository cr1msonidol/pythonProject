from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return """
<style>
.blinking{

font-size: 100pt;
font-style: bold;
    animation:blinkingText 1.2s infinite;
}
@keyframes blinkingText{
    0%{     color: #000;    }
    49%{    color: #000; }
    60%{    color: transparent; }
    99%{    color:transparent;  }
    100%{   color: #000;    }
}
</style>    
    <span class="blinking">¯\_(ツ)_/¯</span>

    
    
    """

if __name__ == '__main__':
    app.run()