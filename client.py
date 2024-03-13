import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import grpc

from proto import helloworld_pb2, helloworld_pb2_grpc

app = FastAPI()


class NameRequest(BaseModel):
    name: str


@app.post("/greet/")
def greet(request: NameRequest):
    host = os.getenv("HOST", "localhost")
    port = os.getenv("PORT", "50051")

    with grpc.insecure_channel(f"{host}:{port}") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        try:
            response = stub.SayHello(helloworld_pb2.HelloRequest(name=request.name))
            return {"message": response.message}
        except grpc.RpcError as e:
            raise HTTPException(status_code=e.code().value[0], detail=str(e))

@app.get("/")
def root():
    return "A Dummy FastAPI service to Test Client!"



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
