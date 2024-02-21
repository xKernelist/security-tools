# security_tools.py
import base64


def encrypt_message(message, key):
    """
    Mesajı verilen anahtarla şifreler.

    Args:
        message (str): Şifrelenecek mesaj.
        key (int): Şifreleme anahtarı.

    Returns:
        str: Şifrelenmiş mesaj.
    """
    encrypted_bytes = bytes([ord(char) + key for char in message])
    encrypted_message = base64.b64encode(encrypted_bytes).decode('utf-8')
    return encrypted_message


def decrypt_message(encrypted_message, key):
    """
    Şifrelenmiş mesajı verilen anahtarla çözer.

    Args:
        encrypted_message (str): Şifrelenmiş mesaj.
        key (int): Şifreleme anahtarı.

    Returns:
        str: Çözülmüş mesaj.
    """
    encrypted_bytes = base64.b64decode(encrypted_message.encode('utf-8'))
    decrypted_message = ''.join([chr(byte - key) for byte in encrypted_bytes])
    return decrypted_message
