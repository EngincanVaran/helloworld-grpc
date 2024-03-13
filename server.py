from concurrent import futures
import grpc
import logging

from proto import helloworld_pb2, helloworld_pb2_grpc


class GreeterServicer(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        logging.info(f"Request Recieved! {request.name}")
        return helloworld_pb2.HelloReply(message=f"Hello, {request.name}!")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    port = '0.0.0.0:50051'
    server.add_insecure_port(port)

    logging.info(f"App started. Listening on {port}")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] | %(message)s",
        handlers=[logging.StreamHandler()]
    )
    logging.info("App starting...")
    serve()
