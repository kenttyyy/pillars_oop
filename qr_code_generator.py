# Import the needed module
import qrcode
from pathlib import Path

class QRCodeGenerator:

    def __init__(self, content: str, filename: str = "qr.png") -> None:
        self.__content = content
        self.__filename = filename

    def generate(self) -> Path:
        img = qrcode.make(self.__content)
        out_path = Path(self.__filename).with_suffix(".png")
        img.save(out_path)
        return out_path

# Colored Qr Code
class StyledQRCode(QRCodeGenerator):

    def __init__(
        self,
        content: str,
        filename: str = "qr_styled.png",
        fg_color: str = "#023047",
        bg_color: str = "#ffffff",
    ) -> None:
        super().__init__(content, filename)
        self.fg_color, self.bg_color = fg_color, bg_color