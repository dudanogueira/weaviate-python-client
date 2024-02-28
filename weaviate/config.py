from dataclasses import dataclass, field
from typing import Optional, Tuple, Union

from pydantic import BaseModel, Field


@dataclass
class ConnectionConfig:
    session_pool_connections: int = 20
    session_pool_maxsize: int = 100
    session_pool_max_retries: int = 3

    def __post_init__(self) -> None:
        if not isinstance(self.session_pool_connections, int):
            raise TypeError(
                f"session_pool_connections must be {int}, received {type(self.session_pool_connections)}"
            )
        if not isinstance(self.session_pool_maxsize, int):
            raise TypeError(
                f"session_pool_maxsize must be {int}, received {type(self.session_pool_maxsize)}"
            )
        if not isinstance(self.session_pool_max_retries, int):
            raise TypeError(
                f"session_pool_max_retries must be {int}, received {type(self.session_pool_max_retries)}"
            )


# used in v3 only
@dataclass
class Config:
    grpc_port_experimental: Optional[int] = None
    grpc_secure_experimental: bool = False
    connection_config: ConnectionConfig = field(default_factory=ConnectionConfig)

    def __post_init__(self) -> None:
        if self.grpc_port_experimental is not None and not isinstance(
            self.grpc_port_experimental, int
        ):
            raise TypeError(
                f"grpc_port_experimental must be {int}, received {type(self.grpc_port_experimental)}"
            )
        if not isinstance(self.grpc_secure_experimental, bool):
            raise TypeError(
                f"grpc_secure_experimental must be {bool}, received {type(self.grpc_secure_experimental)}"
            )


class Timeout(BaseModel):
    query: int = Field(default=30, ge=0)
    insert: int = Field(default=90, ge=0)
    init: int = Field(default=1, ge=0)


class AdditionalConfig(BaseModel):
    connection: ConnectionConfig = Field(default_factory=ConnectionConfig)
    proxies: Union[dict, str, None] = Field(default=None)
    timeout_: Union[Tuple[int, int], Timeout] = Field(default_factory=Timeout, alias="timeout")
    trust_env: bool = Field(default=False)

    @property
    def timeout(self) -> Timeout:
        if isinstance(self.timeout_, tuple):
            return Timeout(query=self.timeout_[0], insert=self.timeout_[1])
        return self.timeout_
