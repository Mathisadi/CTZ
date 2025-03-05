from main import app

@app.get("/build/route/{item_id}/{item_property}")
def build_route():
    
    return {"Hello my name is moi"}
