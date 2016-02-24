TOX_USER_STATUS = {
    'NONE': 0,
    'AWAY': 1,
    'BUSY': 2,
}

TOX_MESSAGE_TYPE = {
    'NORMAL': 0,
    'ACTION': 1,
}

TOX_PROXY_TYPE = {
    'NONE': 0,
    'HTTP': 1,
    'SOCKS5': 2,
}

TOX_SAVEDATA_TYPE = {
    'NONE': 0,
    'TOX_SAVE': 1,
    'SECRET_KEY': 2,
}

TOX_ERR_OPTIONS_NEW = {
    'OK': 0,
    'MALLOC': 1,
}

TOX_ERR_NEW = {
    'OK': 0,
    'NULL': 1,
    'MALLOC': 2,
    'PORT_ALLOC': 3,
    'PROXY_BAD_TYPE': 4,
    'PROXY_BAD_HOST': 5,
    'PROXY_BAD_PORT': 6,
    'PROXY_NOT_FOUND': 7,
    'LOAD_ENCRYPTED': 8,
    'LOAD_BAD_FORMAT': 9,
}

TOX_ERR_BOOTSTRAP = {
    'OK': 0,
    'NULL': 1,
    'BAD_HOST': 2,
    'BAD_PORT': 3,
}

TOX_CONNECTION = {
    'NONE': 0,
    'TCP': 1,
    'UDP': 2,
}

TOX_ERR_SET_INFO = {
    'OK': 0,
    'NULL': 1,
    'TOO_LONG': 2,
}

TOX_ERR_FRIEND_ADD = {
    'OK': 0,
    'NULL': 1,
    'TOO_LONG': 2,
    'NO_MESSAGE': 3,
    'OWN_KEY': 4,
    'ALREADY_SENT': 5,
    'BAD_CHECKSUM': 6,
    'SET_NEW_NOSPAM': 7,
    'MALLOC': 8,
}

TOX_ERR_FRIEND_DELETE = {
    'OK': 0,
    'FRIEND_NOT_FOUND': 1,
}

TOX_ERR_FRIEND_BY_PUBLIC_KEY = {
    'OK': 0,
    'NULL': 1,
    'NOT_FOUND': 2,
}

TOX_ERR_FRIEND_GET_PUBLIC_KEY = {
    'OK': 0,
    'FRIEND_NOT_FOUND': 1,
}

TOX_ERR_FRIEND_GET_LAST_ONLINE = {
    'OK': 0,
    'FRIEND_NOT_FOUND': 1,
}

TOX_ERR_FRIEND_QUERY = {
    'OK': 0,
    'NULL': 1,
    'FRIEND_NOT_FOUND': 2,
}

TOX_ERR_SET_TYPING = {
    'OK': 0,
    'FRIEND_NOT_FOUND': 1,
}

TOX_ERR_FRIEND_SEND_MESSAGE = {
    'OK': 0,
    'NULL': 1,
    'FRIEND_NOT_FOUND': 2,
    'FRIEND_NOT_CONNECTED': 3,
    'SENDQ': 4,
    'TOO_LONG': 5,
    'EMPTY': 6,
}

TOX_FILE_KIND = {
    'DATA': 0,
    'AVATAR': 1,
}

TOX_FILE_CONTROL = {
    'RESUME': 0,
    'PAUSE': 1,
    'CANCEL': 2,
}

TOX_ERR_FILE_CONTROL = {
    'OK': 0,
    'FRIEND_NOT_FOUND': 1,
    'FRIEND_NOT_CONNECTED': 2,
    'NOT_FOUND': 3,
    'NOT_PAUSED': 4,
    'DENIED': 5,
    'ALREADY_PAUSED': 6,
    'SENDQ': 7,
}

TOX_ERR_FILE_SEEK = {
    'OK': 0,
    'FRIEND_NOT_FOUND': 1,
    'FRIEND_NOT_CONNECTED': 2,
    'NOT_FOUND': 3,
    'DENIED': 4,
    'INVALID_POSITION': 5,
    'SENDQ': 6,
}

TOX_ERR_FILE_GET = {
    'OK': 0,
    'NULL': 1,
    'FRIEND_NOT_FOUND': 2,
    'NOT_FOUND': 3,
}

TOX_ERR_FILE_SEND = {
    'OK': 0,
    'NULL': 1,
    'FRIEND_NOT_FOUND': 2,
    'FRIEND_NOT_CONNECTED': 3,
    'NAME_TOO_LONG': 4,
    'TOO_MANY': 5,
}

CHUNK = {
    'OK': 0,
    'NULL': 1,
    'FRIEND_NOT_FOUND': 2,
    'FRIEND_NOT_CONNECTED': 3,
    'NOT_FOUND': 4,
    'NOT_TRANSFERRING': 5,
    'INVALID_LENGTH': 6,
    'SENDQ': 7,
    'WRONG_POSITION': 8,
}

TOX_ERR_FRIEND_CUSTOM_PACKET = {
    'OK': 0,
    'NULL': 1,
    'FRIEND_NOT_FOUND': 2,
    'FRIEND_NOT_CONNECTED': 3,
    'INVALID': 4,
    'EMPTY': 5,
    'TOO_LONG': 6,
    'SENDQ': 7,
}

TOX_ERR_GET_PORT = {
    'OK': 0,
    'NOT_BOUND': 1,
}

TOX_PUBLIC_KEY_SIZE = 32

TOX_ADDRESS_SIZE = TOX_PUBLIC_KEY_SIZE + 48

TOX_MAX_FRIEND_REQUEST_LENGTH = 1016

TOX_MAX_MESSAGE_LENGTH = 1372

TOX_MAX_NAME_LENGTH = 128

TOX_MAX_STATUS_MESSAGE_LENGTH = 1007

# -----------------------------------------------------------------------------------------------------------------
# Other enums
# -----------------------------------------------------------------------------------------------------------------


TOX_USER_CONNECTION_STATUS = {
    'ONLINE': 0,
    'AWAY': 1,
    'BUSY': 2,
    'OFFLINE': 3
}
