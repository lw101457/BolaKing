from datetime import datetime
import hashlib
import random
import time

try:
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    import warnings

    warnings.warn('A secure pseudo-random number generator is not available '
                  'on your user. Falling back to Mersenne Twister.')
    using_sysrandom = False


def id_generator(t: datetime, shard_id=0, seq=0):
    start_epoch = 1562300506835
    return int(datetime.timestamp(t) * 1000 - start_epoch) << 23 | shard_id << 11 | seq


def default_name_gen(t: datetime):
    start_epoch = 1564024430
    uid = int((datetime.timestamp(t) - start_epoch) * 100)
    return "球迷-{}".format(uid), str(uid)


def get_random_string(length=12,
                      allowed_chars='abcdefghijklmnopqrstuvwxyz'
                                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    """
    Return a securely generated random string.

    The default length of 12 with the a-z, A-Z, 0-9 character set returns
    a 71-bit value. log_2((26+26+10)^12) =~ 71 bits
    """
    if not using_sysrandom:
        import settings

        random.seed(
            hashlib.sha256(
                ('%s%s%s' % (random.getstate(), time.time(), settings.TOKEN_SECRET_KEY)).encode()
            ).digest()
        )
    return ''.join(random.choice(allowed_chars) for i in range(length))


if __name__ == '__main__':
    print(default_name_gen(datetime.now()))
