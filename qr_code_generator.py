# Import the needed module
import qrcode
from qrcode import QRCode
from pathlib import Path

try:
    from PIL import Image   # noqa: F401  (import just for the test)
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

if not HAS_PIL:
    from qrcode.image.svg import SvgImage

class QRCodeGenerator:

    def __init__(self, content: str, filename: str = "qr") -> None:
        self.__content = content
        self.__filename_stem = filename

    def generate(self) -> Path:
        if HAS_PIL:
            img = qrcode.make(self.__content)  # PNG path
            out_path = Path(f"{self.__filename_stem}.png")
        else:
            img = qrcode.make(self.__content, image_factory=SvgImage)
            out_path = Path(f"{self.__filename_stem}.svg")

        img.save(out_path)
        return out_path

    def _get_content(self) -> str:
        return self.__content

    def _get_filename_stem(self) -> str:
        return self.__filename_stem

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

    def generate(self) -> Path:  # polymorphic override
        if not HAS_PIL:
            print("⚠️  Pillow not found. Falling back to monochrome SVG.")
            return super().generate()

        # 🔄 CHANGED — use the imported class directly
        qr = QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(self._get_content())
        qr.make(fit=True)

        img = qr.make_image(fill_color=self.fg_color, back_color=self.bg_color)
        out_path = Path(f"{self._get_filename_stem()}.png")
        img.save(out_path)
        return out_path

# Build main demo
if __name__ == "__main__":
    print("╭────────────────────────────────────────────────────────────╮")
    print("│  Python QR Code Generator                                 │")
    print("╰────────────────────────────────────────────────────────────╯\n")

    text = input("Enter the text / URL to encode: ").strip()
    style = input("Generate coloured QR? [Yes/No]: ").lower() == "y"

    # [5] apply polymorphic logic
    generator = StyledQRCode(text) if style else QRCodeGenerator(text)
    saved_file = generator.generate()     # one call, many forms

    # [6] polish user output
    print(f"\n✅  QR code saved to → {saved_file.resolve()}")
    print("   Open the PNG file to view or scan it with your phone!")