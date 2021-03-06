#!/usr/bin/env python3
import nose, logging, os
from tools import dumppdf

path = os.path.dirname(os.path.abspath(__file__)) + '/'


def run(datapath, filename, options=None):
    outputpath = '../tmp/'
    i = path + datapath + filename + '.pdf'
    o = path + outputpath + filename + '.xml'
    if options:
        s = 'dumppdf -o%s %s %s' % (o, options, i)
    else:
        s = 'dumppdf -o%s %s' % (o, i)
    dumppdf.main(s.split(' '))


class TestDumpPDF():
    def test_1(self):
        run('../samples/', 'jo', '-t -a')
        run('../samples/', 'simple1', '-t -a')
        run('../samples/', 'simple2', '-t -a')
        run('../samples/', 'simple3', '-t -a')

    def test_2(self):
        run('../samples/nonfree/', 'dmca', '-t -a')

    def test_3(self):
        run('../samples/nonfree/', 'f1040nr')

    def test_4(self):
        run('../samples/nonfree/', 'i1040nr')

    def test_5(self):
        run('../samples/nonfree/', 'kampo', '-t -a')

    def test_6(self):
        run('../samples/nonfree/', 'naacl06-shinyama', '-t -a')


if __name__ == '__main__':
    nose.runmodule()
