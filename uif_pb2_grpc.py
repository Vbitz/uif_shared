# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import uif_pb2 as uif__pb2


class UIFrameworkStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Edit = channel.unary_unary(
                '/uif.UIFramework/Edit',
                request_serializer=uif__pb2.EditReq.SerializeToString,
                response_deserializer=uif__pb2.EditResp.FromString,
                )
        self.GetEvents = channel.unary_stream(
                '/uif.UIFramework/GetEvents',
                request_serializer=uif__pb2.GetEventsReq.SerializeToString,
                response_deserializer=uif__pb2.Event.FromString,
                )
        self.GetServerProperties = channel.unary_unary(
                '/uif.UIFramework/GetServerProperties',
                request_serializer=uif__pb2.GetServerPropertiesReq.SerializeToString,
                response_deserializer=uif__pb2.GetServerPropertiesResp.FromString,
                )
        self.SetClearColor = channel.unary_unary(
                '/uif.UIFramework/SetClearColor',
                request_serializer=uif__pb2.SetClearColorReq.SerializeToString,
                response_deserializer=uif__pb2.SetClearColorResp.FromString,
                )


class UIFrameworkServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Edit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEvents(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServerProperties(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetClearColor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UIFrameworkServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Edit': grpc.unary_unary_rpc_method_handler(
                    servicer.Edit,
                    request_deserializer=uif__pb2.EditReq.FromString,
                    response_serializer=uif__pb2.EditResp.SerializeToString,
            ),
            'GetEvents': grpc.unary_stream_rpc_method_handler(
                    servicer.GetEvents,
                    request_deserializer=uif__pb2.GetEventsReq.FromString,
                    response_serializer=uif__pb2.Event.SerializeToString,
            ),
            'GetServerProperties': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServerProperties,
                    request_deserializer=uif__pb2.GetServerPropertiesReq.FromString,
                    response_serializer=uif__pb2.GetServerPropertiesResp.SerializeToString,
            ),
            'SetClearColor': grpc.unary_unary_rpc_method_handler(
                    servicer.SetClearColor,
                    request_deserializer=uif__pb2.SetClearColorReq.FromString,
                    response_serializer=uif__pb2.SetClearColorResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'uif.UIFramework', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UIFramework(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Edit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uif.UIFramework/Edit',
            uif__pb2.EditReq.SerializeToString,
            uif__pb2.EditResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/uif.UIFramework/GetEvents',
            uif__pb2.GetEventsReq.SerializeToString,
            uif__pb2.Event.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServerProperties(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uif.UIFramework/GetServerProperties',
            uif__pb2.GetServerPropertiesReq.SerializeToString,
            uif__pb2.GetServerPropertiesResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetClearColor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uif.UIFramework/SetClearColor',
            uif__pb2.SetClearColorReq.SerializeToString,
            uif__pb2.SetClearColorResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
