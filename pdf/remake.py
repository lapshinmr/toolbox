import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger


def remake_pdf(pdf_from, pdf_to):
    input_handler = PdfFileReader(open(pdf_from, "rb"))
    output_handler = PdfFileWriter()
    for page_idx in range(input_handler.getNumPages()):
        output_handler.addPage(input_handler.getPage(page_idx))
    output_handler.write(open(pdf_to, "wb"))
    print('Remake completed')


if __name__ == '__main__':

    def get_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--input',
                            help='Input pdf file name.')
        parser.add_argument('-o', '--output',
                            help='Output pdf file name.')
        return vars(parser.parse_args())

    args = get_args()
    remake_pdf(args['input'], args['output'])
