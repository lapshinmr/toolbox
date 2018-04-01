import os
import re
import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger


def remake_pdf(pdf_from, pdf_to):
    input_handler = PdfFileReader(open(pdf_from, "rb"))
    output_handler = PdfFileWriter()
    for page_idx in range(input_handler.getNumPages()):
        output_handler.addPage(input_handler.getPage(page_idx))
    output_handler.write(open(pdf_to, "wb"))
    print('Remake completed')


class RangeError(Exception):
    pass


def make_range(range_str):
    if not range_str:
        return ()
    elif '--' in range_str:
        if re.search('\(.*\)', range_str):
            step = int(re.sub('.*\((\d+)\)', r'\1', range_str))
            range_str = re.sub('(.*)\(\d+\)', r'\1', range_str)
        else:
            step = 1
        left, right = range_str.split('--')
        if int(left) > int(right):
            raise RangeError
        return [(num, num + step) for num in range(int(left) - 1, int(right), step)]
    elif '-' in range_str:
        left, right = range_str.split('-')
        if int(left) > int(right):
            raise RangeError
        return int(left) - 1, int(right)
    else:
        return int(range_str) - 1, int(range_str)


def make_ranges(range_list):
    converted_ranges = []
    for range_str in range_list:
        converted_range = make_range(range_str)
        if isinstance(converted_range, tuple):
            converted_ranges.append(converted_range)
        elif isinstance(converted_range, list):
            converted_ranges.extend(converted_range)
    return converted_ranges


def separate(pdf_name, ranges_list):
    dir_name = os.path.splitext(pdf_name)[0]
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    source_handler = open(pdf_name, 'rb')
    for idx, pages_range in enumerate(ranges_list):
        merger = PdfFileMerger()
        merger.append(fileobj=source_handler, pages=pages_range)
        out_handler = open(os.path.join(dir_name, str(idx + 1) + '.pdf'), "wb")
        merger.write(out_handler)
        print(idx + 1, end='\r')
    print('Separate completed')


if __name__ == '__main__':

    def get_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('-l', '--list',
                            dest='list',
                            nargs='+',
                            help='Input pages list.')
        parser.add_argument('-f', '--file',
                            dest='file',
                            help='Input file.')
        return vars(parser.parse_args())

    args = get_args()
    pdf_name = args['file']
    pages_list = args['list']

    if not pages_list:
        input_handler = PdfFileReader(open(pdf_name, "rb"))
        full_page_list = [str(item) for item in range(1, input_handler.getNumPages() + 1)]
        pages_list = ' '.join(full_page_list).split()
    else:
        pages_list = pages_list[0].split()

    separate(pdf_name, make_ranges(pages_list))
