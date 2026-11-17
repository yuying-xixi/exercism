"""
To encrypt plaintext by the Caesar cipher
"""
def rotate(text, key):
    """
    :param text:str -需要加密的明文
    :param key:int -加密的key
    :return cipher:str -返回密文
    """

    # 存储密文
    cipher_text = ""

    for letter in text:
        plaintext = letter
        if plaintext.isalpha():
            if plaintext.islower():
                plaintext = chr((ord(plaintext) + key - ord('a')) % 26 + ord('a'))
            else:
                plaintext = chr((ord(plaintext) + key - ord('A')) % 26 + ord('A'))

        cipher_text += plaintext

    return cipher_text
        