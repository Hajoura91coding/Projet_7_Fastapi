import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile

import numpy as np
import pickle
from pydantic import BaseModel
import pandas as pd
import numpy as np

pickle_in = open('lgb_model_auc.pkl', 'rb')
clf = pickle.load(pickle_in)

data_test = pd.read_csv('test_selec_boost.csv')
data_test.set_index('SK_ID_CURR', inplace=True)
from fastapi import Request, status

from fastapi import  Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()



@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}

class irequest(BaseModel):
    id: int
class iresponse(BaseModel):
    prediction: int

@app.post("/predict", response_model=iresponse)
def get_predict(request:irequest):
    client = data_test[data_test.index == request.id]
    # prédiction
    new_proba_pred = clf.predict_proba(client)[:,1]
    print(new_proba_pred)
    if new_proba_pred > 0.22:
        pred = 1
        print(pred)
    else :
        pred = 0
        print(pred)
    return  iresponse( prediction=pred)

if __name__ == '__main__':
    uvicorn.run(main, host='127.0.0.1', port=8000, reload = True)
# uvicorn main:app --reload
