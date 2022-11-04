
from randomdata import summaryReport
from pdf import PDF
import logging


def main():
# Instantiation of inherited class
    logging.basicConfig(filename='data.log', encoding='utf-8', level=logging.DEBUG)
    pdf = PDF("L", "mm", "A4")
    pdf.printSummaryReport(summaryReport)
    

if __name__ == "__main__":
    print()
    main()


