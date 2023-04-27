import os
import subprocess

IMG_FORMAT = ".png"
ICON_DIR = "."


files = os.listdir(ICON_DIR)
icon_files = [
    icon for icon in files if icon.endswith(IMG_FORMAT)
]

for icon in icon_files:
    source_file = icon
    destination_file = icon.replace(IMG_FORMAT, ".bip")
    subprocess.run(
        ["python",
         "-m",
            "t3dn_bip_converter",
         source_file,
         destination_file]
    )

print("Done!")
