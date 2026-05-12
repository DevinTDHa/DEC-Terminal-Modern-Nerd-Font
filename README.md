# DEC Terminal Modern Nerd Font

Vintage font from Digital Electronics Corp (DEC) VT220 terminals for your terminal emulator. 
Now patched to include [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts).

This repo contains a patch for [DEC Terminal Modern](https://www.dafont.com/dec-terminal-modern.font). It adds Nerd Fonts glyphs
and width adjustments. I can't find the author but huge thanks to whoever uploaded this!

When using this font however, it appears too thin for my eyes. After reading the wonderful blog post [Raster CRT Typography (According to DEC)](https://www.masswerk.at/nowgobang/2019/dec-crt-typography), I did a very scientific test by checking the pixel differences in Photopea to stretch the font by 9%. Now it's nice.

> ![terminal](attachments/term.png)
> Wezterm running the font with the gruvbox color scheme.

You can find the standard and stretched version in the [releases](releases).

> ![NOTE]
>
> Some icons will be a bit iffy, but most of them should look ok.

## Requirements

- The [DEC Terminal Modern](https://www.dafont.com/dec-terminal-modern.font) ttf font file
- font-patcher from the [nerd-fonts](https://github.com/ryanoasis/nerd-fonts#font-patcher) repo
  - The nerd-fonts repo will also provide instructions on how to get and run fontforge for the script below

## Steps

1. **Scale font width by 9%** and rename to *DEC Terminal Modern Scaled*:
   ```sh
   ./FontForge-2025-10-09-Linux-x86_64.AppImage \
     -script $PWD/process_font.py \
     $PWD/dec_terminal_modern/_decterm.ttf \
     $PWD/out/_decterm_scaled.ttf \
     1.09
   ```

2. **Run Nerd Fonts patcher** with complete + monospace glyph set:
   ```sh
   ./FontForge-2025-10-09-Linux-x86_64.AppImage \
     -script $PWD/font_patcher/font-patcher \
     --complete --mono \
     --outputdir $PWD/out \
     --extension ttf \
     $PWD/out/_decterm_scaled.ttf
    ```

## CLI Reference — `process_font.py`

```shell
fontforge -script process_font.py <input.ttf> <output.ttf> <scale_factor>
```

Scales font width by `scale_factor` (e.g. `1.09` for 9% wider) and renames the font family to *DEC Terminal Modern Scaled*.

## Output

`DECTerminalModernScaledNerdFontMono-Regular.ttf` — use this anywhere you wish.

