### THIS FILE IS AUTOGENERATED. DO NOT EDIT THIS FILE DIRECTLY ###
from . import instance_pb2_grpc
import instance_pb2
from .instance_pb2 import *
from minknow.rpc._support import MessageWrapper, ArgumentError

__all__ = [
    "InstanceService",
    "GetVersionInfoRequest",
    "GetVersionInfoResponse",
    "GetOutputDirectoriesRequest",
    "OutputDirectories",
    "GetDefaultOutputDirectoriesRequest",
    "SetOutputDirectoryRequest",
    "SetOutputDirectoryResponse",
    "FilesystemDiskSpaceInfo",
    "GetDiskSpaceInfoRequest",
    "GetDiskSpaceInfoResponse",
    "GetMachineIdRequest",
    "GetMachineIdResponse",
]

class InstanceService(object):
    def __init__(self, channel):
        self._stub = InstanceServiceStub(channel)
        self._pb = instance_pb2

    def get_version_info(self, message=None, **kwargs):
        """
        Current version information includes:
        - Minknow version
        - Protocols version

        :rtype: GetVersionInfoResponse
        """
        if message is not None:
            return MessageWrapper(self._stub.get_version_info(message), unwraps=[])

        unused_args = set(kwargs.keys())

        message = GetVersionInfoRequest()

        if len(unused_args) > 0:
            raise ArgumentError("get_version_info got unexpected keyword arguments '{}'".format("', '".join(unused_args)))
        return MessageWrapper(self._stub.get_version_info(message), unwraps=[])

    def get_output_directories(self, message=None, **kwargs):
        """
        Returns various directory locations where minknow is outputting data. The paths are absolute paths, 
        local to the machine where minknow is installed

        the `output` base directory can be changed internally
        the `logs` directory will not be changed and can be stored
        the `reads` directory is determined  by the read writer config

        :rtype: OutputDirectories
        """
        if message is not None:
            return MessageWrapper(self._stub.get_output_directories(message), unwraps=[])

        unused_args = set(kwargs.keys())

        message = GetOutputDirectoriesRequest()

        if len(unused_args) > 0:
            raise ArgumentError("get_output_directories got unexpected keyword arguments '{}'".format("', '".join(unused_args)))
        return MessageWrapper(self._stub.get_output_directories(message), unwraps=[])

    def get_default_output_directories(self, message=None, **kwargs):
        """
        See `get_output_directories`, but this will always return the paths that are defined in the config when the instance
        of minknow has started

        Since 1.11

        :rtype: OutputDirectories
        """
        if message is not None:
            return MessageWrapper(self._stub.get_default_output_directories(message), unwraps=[])

        unused_args = set(kwargs.keys())

        message = GetDefaultOutputDirectoriesRequest()

        if len(unused_args) > 0:
            raise ArgumentError("get_default_output_directories got unexpected keyword arguments '{}'".format("', '".join(unused_args)))
        return MessageWrapper(self._stub.get_default_output_directories(message), unwraps=[])

    def set_output_directory(self, message=None, **kwargs):
        """
        Set the base directory to where all data will be output. Must be an absolute directory

        Fails with INVALID_ARGUMENT if `value` is not absolute.
        Fails with FAILED_PRECONDITION if this is called during acquisition

        Since 1.11

        :param value:
        :rtype: SetOutputDirectoryResponse
        """
        if message is not None:
            return MessageWrapper(self._stub.set_output_directory(message), unwraps=[])

        unused_args = set(kwargs.keys())

        message = SetOutputDirectoryRequest()

        if 'value' in kwargs:
            unused_args.remove('value')
            message.value = kwargs['value']

        if len(unused_args) > 0:
            raise ArgumentError("set_output_directory got unexpected keyword arguments '{}'".format("', '".join(unused_args)))
        return MessageWrapper(self._stub.set_output_directory(message), unwraps=[])

    def get_disk_space_info(self, message=None, **kwargs):
        """
        Returns information about the amount of disk space available, how much
        space is needed to stop an experiment cleanly and if MinKNOW thinks
        that the free disk-space is approaching or past this limit

        Since 1.11

        :rtype: GetDiskSpaceInfoResponse
        """
        if message is not None:
            return MessageWrapper(self._stub.get_disk_space_info(message), unwraps=[])

        unused_args = set(kwargs.keys())

        message = GetDiskSpaceInfoRequest()

        if len(unused_args) > 0:
            raise ArgumentError("get_disk_space_info got unexpected keyword arguments '{}'".format("', '".join(unused_args)))
        return MessageWrapper(self._stub.get_disk_space_info(message), unwraps=[])

    def get_machine_id(self, message=None, **kwargs):
        """
        Find the machine id MinKNOW uses for this machine.

        This is expected to be a descriptive string for the machine, MinKNOW currently uses the network hostname.

        note: This is the identifier used when sending telemetry data for this instance.

        Since 1.11

        :rtype: GetMachineIdResponse
        """
        if message is not None:
            return MessageWrapper(self._stub.get_machine_id(message), unwraps=[])

        unused_args = set(kwargs.keys())

        message = GetMachineIdRequest()

        if len(unused_args) > 0:
            raise ArgumentError("get_machine_id got unexpected keyword arguments '{}'".format("', '".join(unused_args)))
        return MessageWrapper(self._stub.get_machine_id(message), unwraps=[])


