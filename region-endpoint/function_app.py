import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="latency", auth_level=func.AuthLevel.ANONYMOUS)
def latency(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Latency request received.')
    return func.HttpResponse("OK", status_code=200)

@app.route(route="health", auth_level=func.AuthLevel.ANONYMOUS)
def health(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Healthy request received.')
    return func.HttpResponse("Healthy", status_code=200)