from fpdf import FPDF
import datetime
from reportdata import SummaryReport, DetailReport
import logging


class PDF(FPDF):

    logger = logging.getLogger(__name__)
    summaryReport: SummaryReport

    def __horizontalBar__(self):
        self.line(self.get_x(), self.get_y(), self.get_x()+267, self.get_y())
    
    def __printHeadingAndValue__(self, header, value):
        self.set_font("Arial", "B", 15)
        self.cell(133, 10, txt=header)
        self.set_font("Arial", "", 15)
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

    def __printRequestDetails__(self):
        request = self.summaryReport.request

        self.set_font("Arial", "B", 15)
        self.cell(133, h=10, txt="Request Id", border="T,L")
        self.set_font("Arial", "", 15)
        self.cell(133, h=10, txt=request.requesterId, border="T,R", ln=1)
        self.set_font("Arial", "B", 15)
        self.cell(133, h=10, txt="Requester Name", border="L")
        self.set_font("Arial", "", 15)
        self.cell(133, h=10, txt=request.requesterName, border="R", ln=1)
        self.set_font("Arial", "B", 15)
        self.cell(133, h=10, txt="Report Date", border="B,L")
        self.set_font("Arial", "", 15)
        self.cell(133, h=10, txt=request.reportDate, border="B,R", ln=1)

    def __printCustomerInfo__(self):
        customerInfor = self.summaryReport.customer
        keyList = {
            "Name": "name",
            "Birth Date": "birthDate",
            "Gender": "gender",
            "Email Addresses": "emailAddresses",
            "Contact": "contacts",
            "Postal Address": "postalAddresses",
        }
        self.ln()
        self.set_font("Arial", "BU", 15)
        self.cell(133, 10, "Customer Information", 0, 1)
        for key in keyList.keys():
            self.__printHeadingAndValue__(key, customerInfor[keyList[key]])

    def __printLoayaltyInfo__(self):
        loyaltyInformation = self.summaryReport.loyatlyInformations
        
        keyList = {
            "Name": "name",
            "Birth Date": "birthDate",
            "Gender": "gender",
            "Email Addresses": "emailAddresses",
            "Contact": "contacts",
            "Postal Address": "postalAddresses",
        }
        self.ln()
        self.set_font("Arial", "BU", 15)
        self.cell(133, 10, "Customer Information", 0, 1)
        for key in keyList.keys():
            self.__printHeadingAndValue__(key, customerInfor[keyList[key]])

    def printSummaryReport(self, SummaryReport):
        self.summaryReport = SummaryReport
        self.set_margins(15, 10)
        self.add_page()
        self.__printRequestDetails__()
        self.__printCustomerInfo__()
        self.__horizontalBar__()
        
        self.save("SUM_DAE_")

    def printDetailReport(self, DetailReport):
        self.add_page()
        self.save("DET_DAE_")

    def header(self):
        # Logo
        # Todo move to resource directory
        self.image("WAG_Signature_logo_RGB.png", x=23, y=4, w=130, h=35)
        # Arial bold 15
        self.set_font("Arial", "B", 15)
        # Move to the right
        self.cell(153)
        # Title
        self.cell(30, 10, "Title", 1, 0, "C")
        # Line break after header has printed
        self.ln(35)
        self.logger.info("Saving file to system")

    def save(self, name):
        self.output(f'{name} - {datetime.datetime.now().strftime("%H-%M-%S")}.pdf', "F")
