from reportdata import *

request = Request("NX83B2L3H9", "Anshul Jain", "2022-10-22")
customerInfo = Customer(
    "Anshul Jain",
    "1981-01-01",
    "Male",
    ["anshul.email@gmail.com", "another@gmial.com"],
    ["4082040385", "8477546241"],
    ["00000 000", "3036 Village Green Blvd"],
)
loyaltyInfoList = LoyatlyInfoList(
    [
        LoyaltyInfo(
            "20203155494430", "7120122794565", "2021-02-11", "3910", "0", "0", "0"
        )
    ]
)
loyaltyOfferMadeToCustomerList = LoyaltyOfferMadeToCustomerList(
    [
        LoyaltyOfferMadeToCustomer(
            "20203155494430",
            "Add Everyday Points Perk",
            "2015-05-17",
            "2021-12-31",
            "2016-04-16",
            "",
        ),
        LoyaltyOfferMadeToCustomer(
            "20203155494430",
            "Beauty Enthusiast",
            "2016-08-30",
            "2020-08-31",
            "2016-01-20",
            "",
        ),
    ]
)

inferenceAboutYou = InferenceAboutYou(listOfPreferences=["Instant Gratification"])
salesTransactionSummary = SalesTransactionSummary("$299.67", "$24.56")

summaryReportData = SummaryReport(
    request,
    customerInfo,
    loyaltyInfoList,
    loyaltyOfferMadeToCustomerList,
    pSCInfo=None,
    emailSubscription=None,
    inferenceAboutYou=inferenceAboutYou,
    salesTransactionSummary=salesTransactionSummary,
)

detailReportData = DetailReport(
    request,
    InstorePurchaseList(
        [InstorePurchase("2020-12-05", "N/B GNKO BLBA 100S", "2", "18.99", "0")]
    ),
    None,
    None,
    PaymentDetailList(
        [PaymentDetail("2021-03-02", "Credit Card", "10.98", "6278", "In Stores")]
    ),
)
