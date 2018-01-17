### THIS FILE IS AUTOGENERATED. DO NOT EDIT THIS FILE DIRECTLY ###
from . import log_pb2_grpc
import log_pb2
from .log_pb2 import *
from minknow.rpc._support import MessageWrapper, ArgumentError

__all__ = [
    "LogService",
    "GetUserMessagesRequest",
    "UserMessage",
    "SendUserMessageRequest",
    "SendUserMessageResponse",
    "SendPingRequest",
    "SendPingResponse",
    "Severity",
    "MESSAGE_SEVERITY_TRACE",
    "MESSAGE_SEVERITY_INFO",
    "MESSAGE_SEVERITY_WARNING",
    "MESSAGE_SEVERITY_ERROR",
]

class LogService(object):
    def __init__(self, channel):
        self._stub = LogServiceStub(channel)
        self._pb = log_pb2

    def get_user_messages(self, message=None, **kwargs):
        """
        Get a stream of user messages, updated with new messages as the are emitted in minknow.

        Since 1.11

        :param include_old_messages:
            If set, any messages which have already been sent to listeners
            will be sent to the new stream again, before new messages are sent.

            If not specified - the default will not send messages that were sent previously.

            note: there is a limit on how many messages are recorded for replay.
        :rtype: UserMessage
        """
        if message is not None:
            return MessageWrapper(self._stub.get_user_messages(message), unwraps=[])

        unused_args = set(kwargs.keys())

        message = GetUserMessagesRequest()

        if 'include_old_messages' in kwargs:
            unused_args.remove('include_old_messages')
            message.include_old_messages = kwargs['include_old_messages']

        if len(unused_args) > 0:
            raise ArgumentError("get_user_messages got unexpected keyword arguments '{}'".format("', '".join(unused_args)))
        return MessageWrapper(self._stub.get_user_messages(message), unwraps=[])

    def send_user_message(self, message=None, **kwargs):
        """
        Send a log message to any listeners of messages (see get_user_messages)

        Any historical user messages are first sent to the caller,

        Since 1.11

        :param severity: (required)
            The severity of the message to send

            note: TRACE messages cannot be sent using this interface (will generate an error).
        :param user_message: (required)
            The user message to send to any listeners.
        :rtype: SendUserMessageResponse
        """
        if message is not None:
            return MessageWrapper(self._stub.send_user_message(message), unwraps=[])

        unused_args = set(kwargs.keys())

        message = SendUserMessageRequest()

        if 'severity' in kwargs:
            unused_args.remove('severity')
            message.severity = kwargs['severity']
        else:
            raise ArgumentError("send_user_message requires a 'severity' argument")

        if 'user_message' in kwargs:
            unused_args.remove('user_message')
            message.user_message = kwargs['user_message']
        else:
            raise ArgumentError("send_user_message requires a 'user_message' argument")

        if len(unused_args) > 0:
            raise ArgumentError("send_user_message got unexpected keyword arguments '{}'".format("', '".join(unused_args)))
        return MessageWrapper(self._stub.send_user_message(message), unwraps=[])

    def send_ping(self, message=None, **kwargs):
        """
        Send a ping to the configured ping server (see system config for ping server url)

        The tracking_id and context_data section of the ping are filled in automatically by MinKNOW.

        The ping is queued internally for sending immediately, if MinKNOW fails to send the message it
        stores the message to send when possible.

        Since 1.11

        :param ping_data: (required)
            The json data to send as a ping.

            note: if this string is not a valid json object, an error will be raised.
        :rtype: SendPingResponse
        """
        if message is not None:
            return MessageWrapper(self._stub.send_ping(message), unwraps=[])

        unused_args = set(kwargs.keys())

        message = SendPingRequest()

        if 'ping_data' in kwargs:
            unused_args.remove('ping_data')
            message.ping_data = kwargs['ping_data']
        else:
            raise ArgumentError("send_ping requires a 'ping_data' argument")

        if len(unused_args) > 0:
            raise ArgumentError("send_ping got unexpected keyword arguments '{}'".format("', '".join(unused_args)))
        return MessageWrapper(self._stub.send_ping(message), unwraps=[])


