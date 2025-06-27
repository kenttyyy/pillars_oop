# Import the needed module
import qrcode
from pathlib import Path

class QRCodeGenerator:
    def __init__(self, content: str, filename: str = "qr.png") -> None:
        self.__content = content
        self.__filename = filename