Tensorflow Doc Pdf
===================

As i cannot find pdf version of tensorflow documentation,
i write a script to do this.

1. transform ipynb/md to html
python nbmd2html.py

2. transform html to pdf
use https://html2pdf.com/ 

3. add TOC for pdf
i use https://github.com/chroming/pdfdir.

some problems:
* orginization is done by os.walk.
* not fully automatic
** html2pdf with human/url, as pdfkit.from_file fail with image.
** TOC page num with human, as pdf gen and merge is not manchine-auto.
