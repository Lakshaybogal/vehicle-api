from botocore.endpoint import uuid
from fastapi import Request, FastAPI, File, UploadFile, Body, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from boto3.dynamodb.conditions import Key, Attr
import base64
import boto3
from dotenv import load_dotenv
import os
load_dotenv()
app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

dynamodb = boto3.resource('dynamodb', aws_access_key_id =  os.getenv("ACCESS_KEY"),
aws_secret_access_key = os.getenv("SECRET_KEY"), region_name='ap-south-1')
table = dynamodb.Table('vehicles')

@app.get('/')
async def greet():
    return {'message': 'Jai Mata Di'}

@app.post("/upload/")
async def upload_vehicle(
    brand: str = Body(...),
    name: str = Body(...),
    type: str = Body(...),
    file_upload: UploadFile = File(...),
    image_type: str = Body(...)
):
    try:
        file_content = await file_upload.read()
        encoded_image = base64.b64encode(file_content).decode('utf-8')

        response = table.query(
            Select='COUNT',
            KeyConditionExpression=Key('vehicle_id').eq('vehicle_id')
        )
        vehicle_no = response['Count'] + 1
        vehicle_id = str(uuid.uuid4())

        table.put_item(
            Item={
                'vehicle_id': vehicle_id,
                'vehicle_no': vehicle_no,
                'vehicle_model': name.lower(),
                'vehicle_image': encoded_image,
                'vehicle_brand': brand.lower(),
                'vehicle_type': type.lower(),
                'image_type': image_type.lower()
            }
        )
        return {"message": "File uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/vehicle/getAll/")
async def get_all_vehicles():
    try:
        response = table.scan()
        items = response['Items']
        for item in items:
            item['vehicle_image'] = f'data:image/{item["image_type"]};base64,{item["vehicle_image"]}'
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/vehicle/{vehicle_id}")
async def get_vehicle_by_id(vehicle_id: str):
    try:
        response = table.get_item(Key={'vehicle_id': vehicle_id})
        return response.get('Item', {})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/vehicle/brand/{brand}")
async def get_vehicles_by_brand(brand: str):
    try:
        response = table.scan(FilterExpression=Attr('vehicle_brand').begins_with(brand.lower()))
        return {'data': response['Items'], 'count': len(response['Items'])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/vehicle/type/{vehicle_type}")
async def get_vehicles_by_type(vehicle_type: str):
    try:
        response = table.scan(FilterExpression=Key('vehicle_type').eq(vehicle_type.lower()))
        return {'data': response['Items'], 'count': len(response['Items'])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/vehicle/search/model/{vehicle_model}")
async def search_vehicles_by_name(vehicle_model: str):
    try:
        response = table.scan(
            FilterExpression=Attr('vehicle_model').begins_with(vehicle_model.lower())
        )
        return {'data': response['Items'], 'count': len(response['Items'])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
