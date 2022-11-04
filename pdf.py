from fpdf import FPDF
import datetime
from reportdata import SummaryReport, DetailReport
import logging


class PDF(FPDF):
    report_font = "Arial"
    bullet_character = u"\u2022"
    logger = logging.getLogger(__name__)
    summaryReport: SummaryReport

    def __printTableHeader__(self, headers):

        self.set_font(self.report_font, "B", 14)
        col_width = self.epw / len(headers)
        for header in headers:
            self.multi_cell(
                w=col_width,
                h=self.font_size * 2,
                txt=header,
                border=1,
                new_y="TOP",
                new_x="RIGHT",
                fill=True,
                align="L"
            )
        self.ln(self.font_size * 4)

    def __printTableValue__(self, values):

        self.set_font(self.report_font, "", 14)
        col_width = self.epw / len(values)
        for value in values:
            self.multi_cell(
                w=col_width,
                h=self.font_size * 2,
                txt=value,
                border=1,
                new_y="TOP",
                new_x="RIGHT",
                align="L"
            )
        self.ln(self.font_size *5)

    def __printTableSection__(self, tableSectionData):
        sectionName = tableSectionData.__sectionName__
        headers = tableSectionData.__dataHeaders__
        headerKeys = headers.keys()
        dataIndexes = headers.values()
        
        entries = tableSectionData.entries

        self.set_font(self.report_font, "BU")
        self.cell(w=self.epw, h=self.font_size * 2, txt=sectionName, ln=1)
        self.__printTableHeader__(headerKeys)
        for row in entries:
            data =[]
            for dataIndex in dataIndexes:
                data.append(row[dataIndex])
            self.__printTableValue__(data)

    def __horizontalBar__(self):
        self.line(self.get_x(), self.get_y(), self.get_x() + 267, self.get_y())

    def __printHeadingAndValue__(self, header, value):
        self.set_font(self.report_font, "B", 15)
        self.cell(133, 10, txt=header)
        self.set_font(self.report_font, "", 15)
        valueCounter = 0
        if type(value) is not list:
            self.cell(133, 10, txt=value)
            self.ln()
        else:
            for val in value:
                if valueCounter > 0:
                    self.cell(133)
                self.cell(133, 10, txt=val)
                self.ln()
                valueCounter = valueCounter + 1



    ## Summary report section functions starts

    def __printCustomerInfo__(self):
        customerInfor = self.summaryReport.customer

        self.ln()
        self.set_font(self.report_font, "BU", 15)
        self.cell(133, 10, customerInfor.__sectionName__, 0, 1)
        customerKeys  = customerInfor.__keyList__
        
        for key,value in customerKeys.items():
            self.__printHeadingAndValue__(key,customerInfor[value])
        self.__horizontalBar__()

    def __printLoyaltyInfo__(self):
        tabledSection = self.summaryReport.loyatlyInformations
        self.__printTableSection__(tabledSection)
        self.__horizontalBar__()

    def __printLoyaltyOffersMadeToCustomer__(self):    
        tabledSection = self.summaryReport.loyaltyOfferMadeToCustomer
        self.__printTableSection__(tabledSection)
        self.__horizontalBar__()

    def __printPSCInformation__(self):
        pass
    def __printEmailSubscription_(self):
        pass
    def __printInferencesAboutYou__(self):
        pass
    def __printSalesTransactionSummary__(self):
        pass
    ## Summary report section functions ends

    ## Details report section functions stats
    def __printInstorePurchaes__(self):
        pass
    def __printOnlinePurchase__(self):
        pass
    def __printOnlineReturns__(self):
        pass
    def __selfPaymentDetails__(self):
        pass
    
    ## Details report section functions ends

    


    def printSummaryReport(self, SummaryReport):
        self.summaryReport = SummaryReport

        self.set_fill_color(255, 255, 0)
        self.set_margins(15, 10)
        self.add_page()

        self.__printRequestDetails__()
        self.__printCustomerInfo__()
        self.__printLoyaltyInfo__()
        self.__printLoyaltyOffersMadeToCustomer__()
        self.__printPSCInformation__()
        self.__printEmailSubscription_()
        self.__printInferencesAboutYou__()
        self.__printSalesTransactionSummary__()
        self.__printEndSection__()

        self.save("SUM_DAE_")

    def printDetailReport(self, DetailReport):
        self.set_fill_color(255, 255, 0)
        self.set_margins(15, 10)
        self.add_page()

        self.__printEndSection__()
        self.save("DET_DAE_")

    def header(self):
        # Logo
        # Todo move to resource directory
        self.image("WAG_Signature_logo_RGB.png", x=23, y=4, w=130, h=35)
        # Arial bold 15
        self.set_font(self.report_font, "B", 15)
        # Move to the right
        self.cell(153)
        # Title
        self.cell(30, 10, "Title", 1, 0, "C")
        # Line break after header has printed
        self.ln(35)
        self.logger.info("Saving file to system")

    def save(self, name):
        self.output(f'{name} - {datetime.datetime.now().strftime("%H-%M-%S")}.pdf', "F")
