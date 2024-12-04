# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from weaviate.proto.v1 import batch_delete_pb2 as v1_dot_batch__delete__pb2
from weaviate.proto.v1 import batch_pb2 as v1_dot_batch__pb2
from weaviate.proto.v1 import search_get_pb2 as v1_dot_search__get__pb2
from weaviate.proto.v1 import tenants_pb2 as v1_dot_tenants__pb2

GRPC_GENERATED_VERSION = "1.68.1"
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower

    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f"The grpc package installed is at version {GRPC_VERSION},"
        + f" but the generated code in v1/weaviate_pb2_grpc.py depends on"
        + f" grpcio>={GRPC_GENERATED_VERSION}."
        + f" Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}"
        + f" or downgrade your generated code using grpcio-tools<={GRPC_VERSION}."
    )


class WeaviateStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Search = channel.unary_unary(
            "/weaviate.v1.Weaviate/Search",
            request_serializer=v1_dot_search__get__pb2.SearchRequest.SerializeToString,
            response_deserializer=v1_dot_search__get__pb2.SearchReply.FromString,
            _registered_method=True,
        )
        self.BatchObjects = channel.unary_unary(
            "/weaviate.v1.Weaviate/BatchObjects",
            request_serializer=v1_dot_batch__pb2.BatchObjectsRequest.SerializeToString,
            response_deserializer=v1_dot_batch__pb2.BatchObjectsReply.FromString,
            _registered_method=True,
        )
        self.BatchDelete = channel.unary_unary(
            "/weaviate.v1.Weaviate/BatchDelete",
            request_serializer=v1_dot_batch__delete__pb2.BatchDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_batch__delete__pb2.BatchDeleteReply.FromString,
            _registered_method=True,
        )
        self.TenantsGet = channel.unary_unary(
            "/weaviate.v1.Weaviate/TenantsGet",
            request_serializer=v1_dot_tenants__pb2.TenantsGetRequest.SerializeToString,
            response_deserializer=v1_dot_tenants__pb2.TenantsGetReply.FromString,
            _registered_method=True,
        )


class WeaviateServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Search(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def BatchObjects(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def BatchDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def TenantsGet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_WeaviateServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Search": grpc.unary_unary_rpc_method_handler(
            servicer.Search,
            request_deserializer=v1_dot_search__get__pb2.SearchRequest.FromString,
            response_serializer=v1_dot_search__get__pb2.SearchReply.SerializeToString,
        ),
        "BatchObjects": grpc.unary_unary_rpc_method_handler(
            servicer.BatchObjects,
            request_deserializer=v1_dot_batch__pb2.BatchObjectsRequest.FromString,
            response_serializer=v1_dot_batch__pb2.BatchObjectsReply.SerializeToString,
        ),
        "BatchDelete": grpc.unary_unary_rpc_method_handler(
            servicer.BatchDelete,
            request_deserializer=v1_dot_batch__delete__pb2.BatchDeleteRequest.FromString,
            response_serializer=v1_dot_batch__delete__pb2.BatchDeleteReply.SerializeToString,
        ),
        "TenantsGet": grpc.unary_unary_rpc_method_handler(
            servicer.TenantsGet,
            request_deserializer=v1_dot_tenants__pb2.TenantsGetRequest.FromString,
            response_serializer=v1_dot_tenants__pb2.TenantsGetReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "weaviate.v1.Weaviate", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers("weaviate.v1.Weaviate", rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class Weaviate(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Search(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/weaviate.v1.Weaviate/Search",
            v1_dot_search__get__pb2.SearchRequest.SerializeToString,
            v1_dot_search__get__pb2.SearchReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def BatchObjects(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/weaviate.v1.Weaviate/BatchObjects",
            v1_dot_batch__pb2.BatchObjectsRequest.SerializeToString,
            v1_dot_batch__pb2.BatchObjectsReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def BatchDelete(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/weaviate.v1.Weaviate/BatchDelete",
            v1_dot_batch__delete__pb2.BatchDeleteRequest.SerializeToString,
            v1_dot_batch__delete__pb2.BatchDeleteReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def TenantsGet(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/weaviate.v1.Weaviate/TenantsGet",
            v1_dot_tenants__pb2.TenantsGetRequest.SerializeToString,
            v1_dot_tenants__pb2.TenantsGetReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )
