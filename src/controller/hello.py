from base import app

@app.route('/hello')
async def hello():
    return {'hello': 'world'}