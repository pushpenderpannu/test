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
    [LoyaltyInfo("20203155494430", "7120122794565", "", "3910", "0", "0", "0")]
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

inferenceAboutYou = InferenceAboutYou(["InstantGratification"])
salesTransactionSummary = SalesTransactionSummary(299.67, 24.56)

summaryReport = SummaryReport(
    request,
    customerInfo,
    loyaltyInfoList,
    loyaltyOfferMadeToCustomerList,
    pSCInfo=None,
    emailSubscription=None,
    inferenceAboutYou=inferenceAboutYou,
    salesTransactionSummary=salesTransactionSummary,
)
