# yapdfminer (Yet Another PDFMiner fork)

PDFMiner is a great Python tool that had apparently been abandoned by its original author
[Yusuke Shinyama](https://github.com/euske) in 2016.
Ever since, it got forked and re-forked time and time again but never maintained for long.

## Goals

I created this fork in order to better service the requirements of my own project from PDF analysis:
1. Apply multiple pull requests that languish on the original repository, that **solve some bugs** that I ran into.
1. Target **Python 3.7**.
There will be no attempt to maintain backwards compatibility to older versions of Python.
1. Generate a **smaller distribution package** (I'm running on AWS Lambda, where RAM is at a premium),
at the cost of **dropping support for Chinese, Japanese and Korean** PDFs.

If you require Asian language support, it should be simple enough to re-enable it by building with the resource
files in `cmaprsrc`.

Other than the issues mentioned above, I do strive to make this library drop-in compatible with the original PDFMiner,
including for example the package name (which pdfminer3 had changed).


**Lineage:**
- This is a fork of [gwk/pdfminer3](https://github.com/gwk/pdfminer3/).
- gwk/pdfminer3 was forked from [pdfminer/pdfminer.six](https://github.com/pdfminer/pdfminer.six)
- pdfminer.six was forked from the original [pdfminer](https://github.com/euske/pdfminer)


## About

PDFMiner is a pure Python tool for extracting information from PDF documents.

Its focus is on PDF content retrieval and analysis.

Please refer to the original repo for more information: https://github.com/euske
