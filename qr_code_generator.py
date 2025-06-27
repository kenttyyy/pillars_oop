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

# override generate method
    def generate(self) -> Path:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # 30 % EC
            box_size=10,
            border=4,
        )
        # access mangled names from parent to keep data encapsulated
        qr.add_data(self._QRCodeGenerator__content)
        qr.make(fit=True)

        img = qr.make_image(fill_color=self.fg_color, back_color=self.bg_color)
        out_path = Path(self._QRCodeGenerator__filename).with_suffix(".png")
        img.save(out_path)
        return out_path