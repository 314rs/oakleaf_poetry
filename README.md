# Oakleaf poetry station

## Dependencies:

### FPDF

The script needs fpdf to be installed on the client computer. To install it use:

```cmd
pip install fpdf
```
or:
```cmd
python -m pip install fpdf
```
## Files

### words.txt
- put words here
- one per line

### poetry_client.py:
- choose 3 random words from '''words.txt''' (one word per line)
- save poem as .txt and .pdf in ./poems
- change the layout in line 83: ```pdf = poem_to_pdf(entry_text, mode=1, font_size=24)```
  - mode=0 : use fixed font size and line breaks
  - mode=1 : use biggest possible font size (per line) \[experimental\]
  - mode=2 : use biggest possible font size but same for all lines

### poetry_printer.py:
- choose a random PDF from ./poems
- print it using the windows-standard-printer

## Mitmachen:
https://projekt-rezepte.de/partizipation/
