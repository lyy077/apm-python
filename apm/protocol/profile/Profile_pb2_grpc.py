# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ..common import Common_pb2 as common_dot_Common__pb2
from ..profile import Profile_pb2 as profile_dot_Profile__pb2


class ProfileTaskStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getProfileTaskCommands = channel.unary_unary(
                '/apm.v3.ProfileTask/getProfileTaskCommands',
                request_serializer=profile_dot_Profile__pb2.ProfileTaskCommandQuery.SerializeToString,
                response_deserializer=common_dot_Common__pb2.Commands.FromString,
                )
        self.collectSnapshot = channel.stream_unary(
                '/apm.v3.ProfileTask/collectSnapshot',
                request_serializer=profile_dot_Profile__pb2.ThreadSnapshot.SerializeToString,
                response_deserializer=common_dot_Common__pb2.Commands.FromString,
                )
        self.reportTaskFinish = channel.unary_unary(
                '/apm.v3.ProfileTask/reportTaskFinish',
                request_serializer=profile_dot_Profile__pb2.ProfileTaskFinishReport.SerializeToString,
                response_deserializer=common_dot_Common__pb2.Commands.FromString,
                )


class ProfileTaskServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getProfileTaskCommands(self, request, context):
        """query all sniffer need to execute profile task commands
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def collectSnapshot(self, request_iterator, context):
        """collect dumped thread snapshot
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def reportTaskFinish(self, request, context):
        """report profiling task finished
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProfileTaskServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getProfileTaskCommands': grpc.unary_unary_rpc_method_handler(
                    servicer.getProfileTaskCommands,
                    request_deserializer=profile_dot_Profile__pb2.ProfileTaskCommandQuery.FromString,
                    response_serializer=common_dot_Common__pb2.Commands.SerializeToString,
            ),
            'collectSnapshot': grpc.stream_unary_rpc_method_handler(
                    servicer.collectSnapshot,
                    request_deserializer=profile_dot_Profile__pb2.ThreadSnapshot.FromString,
                    response_serializer=common_dot_Common__pb2.Commands.SerializeToString,
            ),
            'reportTaskFinish': grpc.unary_unary_rpc_method_handler(
                    servicer.reportTaskFinish,
                    request_deserializer=profile_dot_Profile__pb2.ProfileTaskFinishReport.FromString,
                    response_serializer=common_dot_Common__pb2.Commands.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'apm.v3.ProfileTask', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProfileTask(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getProfileTaskCommands(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/apm.v3.ProfileTask/getProfileTaskCommands',
            profile_dot_Profile__pb2.ProfileTaskCommandQuery.SerializeToString,
            common_dot_Common__pb2.Commands.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def collectSnapshot(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/apm.v3.ProfileTask/collectSnapshot',
            profile_dot_Profile__pb2.ThreadSnapshot.SerializeToString,
            common_dot_Common__pb2.Commands.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def reportTaskFinish(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/apm.v3.ProfileTask/reportTaskFinish',
            profile_dot_Profile__pb2.ProfileTaskFinishReport.SerializeToString,
            common_dot_Common__pb2.Commands.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)