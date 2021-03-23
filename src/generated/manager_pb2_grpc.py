# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import manager_pb2 as src_dot_proto_dot_manager__pb2


class ManagerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SpawnStrategy = channel.unary_unary(
                '/manager.Manager/SpawnStrategy',
                request_serializer=src_dot_proto_dot_manager__pb2.SpawnRequest.SerializeToString,
                response_deserializer=src_dot_proto_dot_manager__pb2.SpawnReply.FromString,
                )
        self.DeleteStrategy = channel.unary_unary(
                '/manager.Manager/DeleteStrategy',
                request_serializer=src_dot_proto_dot_manager__pb2.DeletionRequest.SerializeToString,
                response_deserializer=src_dot_proto_dot_manager__pb2.DeletionReply.FromString,
                )


class ManagerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SpawnStrategy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteStrategy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SpawnStrategy': grpc.unary_unary_rpc_method_handler(
                    servicer.SpawnStrategy,
                    request_deserializer=src_dot_proto_dot_manager__pb2.SpawnRequest.FromString,
                    response_serializer=src_dot_proto_dot_manager__pb2.SpawnReply.SerializeToString,
            ),
            'DeleteStrategy': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteStrategy,
                    request_deserializer=src_dot_proto_dot_manager__pb2.DeletionRequest.FromString,
                    response_serializer=src_dot_proto_dot_manager__pb2.DeletionReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'manager.Manager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Manager(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SpawnStrategy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/manager.Manager/SpawnStrategy',
            src_dot_proto_dot_manager__pb2.SpawnRequest.SerializeToString,
            src_dot_proto_dot_manager__pb2.SpawnReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteStrategy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/manager.Manager/DeleteStrategy',
            src_dot_proto_dot_manager__pb2.DeletionRequest.SerializeToString,
            src_dot_proto_dot_manager__pb2.DeletionReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)