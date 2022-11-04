from fpdf import FPDF
import datetime
import reportdata
import logging


class PDF(FPDF):
    report_font = "Arial"
    bullet_character = "\u2022"
    logger = logging.getLogger(__name__)

    def __printTableHeader__(self, headers, widthMap):
        self.set_font(self.report_font, "B")
        total = sum(widthMap)
        counter = 0
        unit_width = self.epw / total
        for header in headers:
            self.multi_cell(
                w=unit_width * widthMap[counter],
                h=self.font_size * 4,
                max_line_height=self.font_size * 2,
                txt=header,
                border=1,
                new_y="TOP",
                new_x="RIGHT",
                fill=True,
                align="L",
            )
            counter = counter + 1
        self.ln(self.font_size * 4)

    def __printTableValue__(self, values, widthMap, alignmentMap):

        self.set_font(self.report_font, "")
        total = sum(widthMap)
        counter = 0
        unit_width = self.epw / total
        for value in values:
            self.multi_cell(
                w=unit_width * widthMap[counter],
                h=self.font_size * 2,
                max_line_height=self.font_size * 2,
                txt=value,
                border=1,
                new_y="TOP",
                new_x="RIGHT",
                align=alignmentMap[counter],
            )
            counter = counter + 1
        self.ln()

    def __printTableSection__(self, sectionName, tableSectionData):
        self.ln()
        if tableSectionData is not None:
            if (self.y + self.b_margin + self.report_font_size * 2) > 210:
                self.add_page()
            headers = tableSectionData.__headingAttributeMap__
            widthMap = list(tableSectionData.__widthMap__.values())
            
            try:
                alignmentMap = tableSectionData.__alignmentMap__
            except AttributeError:
                alignmentMap = {}

            alignmentData = []
            for header in headers:
                if alignmentMap.get(header) is not None:
                    alignmentData.append(alignmentMap.get(header))
                else:
                    alignmentData.append("L")

            if widthMap is None:
                widthMap = [1 for i in headers]
            headerKeys = headers.keys()
            dataIndexes = headers.values()
            entries = tableSectionData.entries

            self.set_font(self.report_font, "BU")
            self.cell(w=self.epw, h=self.font_size * 2, txt=sectionName, ln=1)
            self.__printTableHeader__(headerKeys, widthMap)
            for row in entries:
                data = []
                for dataIndex in dataIndexes:
                    data.append(row[dataIndex])
                self.__printTableValue__(data, widthMap, alignmentData)
            self.ln(self.font_size)
        else:
            self.set_font(self.report_font, "BU")
            self.cell(133, 10, txt=sectionName)
            self.set_font(self.report_font)
            self.cell(133, 10, txt="NA", ln=1)
        self.__horizontalBar__()

    def __horizontalBar__(self):
        self.set_line_width(0.4)
        self.line(self.get_x(), self.get_y(), self.get_x() + 267, self.get_y())
        self.set_line_width(0.2)

    def __printHeadingValueSection__(self, sectionName, sectionData):

        if sectionData is not None:
            self.set_font(self.report_font, "BU")
            self.cell(133, 10, sectionName, 0, 1)
            keys = sectionData.__headingAttributeMap__

            for key, value in keys.items():
                self.__printHeadingAndValue__(key, sectionData[value])
        else:
            self.__printHeadingAndValue__(sectionName, "NA", "BU")
        self.__horizontalBar__()

    def __printHeadingAndValue__(self, header, value, headingFontOptions="B"):
        self.set_font(self.report_font, headingFontOptions)
        self.cell(133, 10, txt=header)
        self.set_font(self.report_font)
        valueCounter = 0
        if value is None:
            self.cell(133, 10, txt="NA", ln=1)
        elif type(value) is not list:
            self.cell(133, 10, txt=value, ln=1)
        else:
            for val in value:
                if valueCounter > 0:
                    self.cell(133)
                self.cell(133, 10, txt=val, ln=1)
                valueCounter = valueCounter + 1

    def header(self):
        # Logo
        # Todo move to resource directory
        self.image("WAG_Signature_logo_RGB.png", x=23, y=4, w=130, h=35)
        # Arial bold 15
        self.set_font(self.report_font, "B")
        # Move to the right
        self.cell(153)
        # Title
        self.cell(30, 10, "Title", 1, 0, "C")
        # Line break after header has printed
        self.ln(35)
        self.logger.info("Saving file to system")

    def save(self, name):
        self.output(f'{name} - {datetime.datetime.now().strftime("%H-%M-%S")}.pdf', "F")


class ReportPDF(PDF):
    report_font_size = 12

    def __init__(self, report):
        super().__init__(orientation="L", unit="mm", format="A4")
        self.report = report
        self.set_font_size(self.report_font_size)
        self.set_fill_color(255, 255, 0)
        self.set_margins(15, 10)
        self.add_page()
        self.__printRequestDetails__()

    def __printRequestDetails__(self):
        request: reportdata.Request = self.report.request

        self.set_font("Arial", "B")
        self.cell(133, h=10, txt="Request Id", border="T,L")
        self.set_font("Arial", "")
        self.cell(133, h=10, txt=request.requesterId, border="T,R", ln=1)
        self.set_font("Arial", "B")
        self.cell(133, h=10, txt="Requester Name", border="L")
        self.set_font("Arial", "")
        self.cell(133, h=10, txt=request.requesterName, border="R", ln=1)
        self.set_font("Arial", "B")
        self.cell(133, h=10, txt="Report Date", border="B,L")
        self.set_font("Arial", "")
        self.cell(133, h=10, txt=request.reportDate, border="B,R", ln=1)

    def __printEndSection__(self):
        pass


class SummaryReportPDF(ReportPDF):
    def __init__(self, summaryReport):
        super().__init__(summaryReport)
        self.summaryReport: reportdata.SummaryReport = summaryReport

    def __printCustomerInfo__(self):
        sectionName = "Customer Information"
        sectionData = self.summaryReport.customer
        self.__printHeadingValueSection__(sectionName, sectionData)

    def __printLoyaltyInfo__(self):
        sectionName = "Loyalty Information"
        tabledSection = self.summaryReport.loyatlyInformations
        self.__printTableSection__(sectionName, tabledSection)

    def __printLoyaltyOffersMadeToCustomer__(self):
        sectionName = "Loyalty Offers Made To Customer"
        tabledSection = self.summaryReport.loyaltyOfferMadeToCustomer
        self.__printTableSection__(sectionName, tabledSection)

    def __printPSCInformation__(self):
        sectionName = "PSC Information"
        tabledSection = self.summaryReport.pSCInfo
        if tabledSection is not None:
            self.__printTableSection__(sectionName, tabledSection)
        else:
            self.set_font(self.report_font, "BU")
            self.cell(133, 10, txt=sectionName)
            self.set_font(self.report_font)
            self.ln()
            self.__printHeadingAndValue__("Membership Id", "NA")
            self.__horizontalBar__()

    def __printEmailSubscription_(self):
        sectionName = "Email Subscription"
        sectionData = self.summaryReport.emailSubscription
        self.__printHeadingValueSection__(sectionName, sectionData)

    def __printInferencesAboutYou__(self):
        sectionName = "Inferences About You"
        sectionData = self.summaryReport.inferenceAboutYou
        self.__printHeadingValueSection__(sectionName, sectionData)

    def __printSalesTransactionSummary__(self):
        sectionName = "Sales Transaction Summary"
        sectionData = self.summaryReport.salesTransactionSummary
        self.__printHeadingValueSection__(sectionName, sectionData)

    def __save__(self):
        self.__printEndSection__()
        self.save("SUM_DAE_")

    def printReport(self):
        self.__printCustomerInfo__()
        self.__printLoyaltyInfo__()
        self.__printLoyaltyOffersMadeToCustomer__()
        self.__printPSCInformation__()
        self.__printEmailSubscription_()
        self.__printInferencesAboutYou__()
        self.__printSalesTransactionSummary__()
        self.__save__()


class DetailReportPDF(ReportPDF):
    def __init__(self, detailreport):
        super().__init__(detailreport)
        self.detailreport: reportdata.DetailReport = detailreport


    def __save__(self):
        self.__printEndSection__()
        self.save("DET_DAE_")

    def __printInstorePurchaes__(self):
        sectionName = "Instore Purcahses"
        tabledSection = self.detailreport.instorePurchases
        self.__printTableSection__(sectionName, tabledSection)

    def __printOnlinePurchase__(self):
        sectionName = "Online Purcahses"
        tabledSection = self.detailreport.onlinePurcahses
        self.__printTableSection__(sectionName, tabledSection)

    def __printOnlineReturns__(self):
        sectionName = "Online Returns"
        tabledSection = self.detailreport.onlineReturns
        self.__printTableSection__(sectionName, tabledSection)

    def __printPaymentDetails__(self):
        sectionName = "Payment Details"
        tabledSection = self.detailreport.paymentDetails
        self.__printTableSection__(sectionName, tabledSection)

    def printReport(self):
        self.__printInstorePurchaes__()
        self.__printOnlinePurchase__()
        self.__printOnlineReturns__()
        self.__printPaymentDetails__()
        self.__save__()
