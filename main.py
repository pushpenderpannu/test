
from randomdata import summaryReportData,detailReportData
from pdf import SummaryReportPDF, DetailReportPDF
import logging


def main():
# Instantiation of inherited class
    logging.basicConfig(filename='data.log', encoding='utf-8', level=logging.DEBUG)
    pdfSummary = SummaryReportPDF(summaryReportData)
    pdfSummary.printReport()
    pdfDetail = DetailReportPDF(detailReportData)
    pdfDetail.printReport()
    

if __name__ == "__main__":
    print()
    main()

