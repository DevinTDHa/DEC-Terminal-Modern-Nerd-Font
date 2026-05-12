import fontforge
import sys

if len(sys.argv) != 4:
    print("Usage: fontforge -script process_font.py <input.ttf> <output.ttf> <scale_factor>")
    sys.exit(1)

input_font = sys.argv[1]
output_font = sys.argv[2]
scale_factor = float(sys.argv[3])

font = fontforge.open(input_font)

font.familyname = "DEC Terminal Modern Scaled"
font.fontname = "DECTerminalModernScaled-Regular"
font.fullname = "DEC Terminal Modern Scaled"

for glyph in font.glyphs():
    glyph.width = int(round(glyph.width * scale_factor))
    glyph.vwidth = int(round(glyph.vwidth * scale_factor))

font.generate(output_font)
font.close()

print(f"Scaled width by {scale_factor}x: {input_font} -> {output_font}")
