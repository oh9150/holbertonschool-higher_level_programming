#!/usr/bin/python3
def remove_chat_at(str, n):
    if (n <= 0):
        return (str)
    return (str[:n] + str[n + 1:])
