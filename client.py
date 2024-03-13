import grpc
from proto import helloworld_pb2, helloworld_pb2_grpc


def run():
    # Create an insecure channel with the server's URL and port
    with grpc.insecure_channel(
        'grpc-server-engincanvaran-dev.apps.sandbox-m3.1530.p1.openshiftapps.com:50051'
    ) as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='world'))
        print("Greeter client received: " + response.message)

if __name__ == '__main__':
    run()
