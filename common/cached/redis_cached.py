from common.clients import clients


def hget_verify_code(mobile):
    # clients.user_redis.hget("sms_code", "sms_{}".format(mobile)).decode("utf-8")
    return "8888"
