from dataclasses import dataclass


# Class specific to Details report
@dataclass
class InstorePurchase:
    purchaseDate: str
    productDescription: str
    totalQuantity: str
    totalSales: float
    returnQuatity: str

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class InstorePurchaseList:
    entries: list[InstorePurchase]
    __headingAttributeMap__ = {
        "Purchase Date": "purchaseDate",
        "Product Description": "productDescription",
        "Total Quantity": "totalQuantity",
        "Total Sales ($)": "totalSales",
        "Return Quatity": "returnQuatity",
    }
    __alignmentMap__ = {
        "Total Quantity ($)": "R",
        "Total Sales": "R",
        "Return Quantity": "R",
    }
    __widthMap__ = {
        "Purchase Date": 1,
        "Product Description": 2,
        "Total Quantity": 1,
        "Total Sales ($)": 1,
        "Return Quatity": 1,
    }


@dataclass
class OnlinePurchase:
    purhcaseDate: str
    productDescription: str
    totalSales: str
    unitQuantity: str

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class OnlinePurchaseList:
    entries: list[OnlinePurchase]
    __headingAttributeMap__ = {
        "Purchase Date": "purchaseDate",
        "Product Description": "productDescription",
        "Total Sales ($)": "totalSales",
        "Unit Quantity": "unitQuantity",
    }
    __alignmentMap__ = {"Total Sales ($)": "R", "Unit Quantity": "R"}
    __widthMap__ = {
        "Return Reported Date": 1,
        "Product Description": 2,
        "Return Quantity": 1,
        "Return Amount ($)": 1,
    }


@dataclass
class OnlineReturn:
    returnReportedDate: str
    productDescription: str
    qnantityToReturn: str
    totalReturnDlr: str

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class OnlinReturnList:
    entries: list[OnlineReturn]
    __headingAttributeMap__ = {
        "Return Reported Date": "returnReportedDate",
        "Product Description": "productDescription",
        "Return Quantity": "qnantityToReturn",
        "Return Amount ($)": "totalReturnDlr",
    }
    __alignmentMap__ = {"Return Quantity": "R", "Return Amount ($)": "R"}
    __widthMap__ = {
        "Return Reported Date": 1,
        "Product Description": 2,
        "Return Quantity": 1,
        "Return Amount ($)": 1,
    }


@dataclass
class PaymentDetail:
    purchaseDate: str
    paymentType: str
    tenderedAmount: str
    cardLastFourDigits: str
    purchaseType: str

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class PaymentDetailList:
    entries : list[PaymentDetail]
    __headingAttributeMap__ = {
        "Purchase Date": "purchaseDate",
        "Payment Type": "paymentType",
        "Tendered Amount ($)": "tenderedAmount",
        "Card Last 4 Digits": "cardLastFourDigits",
        "Purchase Type": "purchaseType",
    }
    __alignmentMap__ = {"Tendered Amount ($)": "R", "Card Last 4 Digits": "C"}
    __widthMap__ = {
        "Purchase Date": 1,
        "Payment Type": 1,
        "Tendered Amount ($)": 1,
        "Card Last 4 Digits": 1,
        "Purchase Type": 1,
    }


# class specific to summary


@dataclass
class SalesTransactionSummary:
    totalAmountSpend: str
    totalTaxPaid: str
    __headingAttributeMap__ = {
        "Total amount spent in last 12 months": "totalAmountSpend",
        "Total tax paid in last 12 months": "totalTaxPaid",
    }
    __alignmentMap__ = {}

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class InferenceAboutYou:
    listOfBehaviour: list[str] = None
    listOfCharacterstics: list[str] = None
    listOfPreferences: list[str] = None
    homeOwnerList: list[str] = None
    householdEduList: list[str] = None
    householdMartialStatusList: list[str] = None
    householdSize: str = None
    householdLanguageCode: str = None
    noOfChildrenInHousehold: str = None
    occupationList: list[str] = None
    targetIncomeList: list[str] = None
    childrenAgeZeroToTwoList: list[str] = None
    childrenAgeThreeToFiveList: list[str] = None
    childrenAgesixToTenList: list[str] = None
    childrenAgeElevenToFiftenList: list[str] = None
    childrenAgeSixteenToSeventeenList: list[str] = None

    __headingAttributeMap__ = {
        "Preferences": "listOfPreferences"
        ## TODO Update all
    }
    __alignmentMap__ = {}

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class EmailSubscription:
    subs: list[str]


@dataclass
class PSCInfo:
    psdMembershipId: str
    name: str
    dateOfBirth: str
    pscCardId: str
    memberShipCategory: str
    createDate: str
    endDate: str
    phoneNo: str
    email: str
    postalAddress: str
    __sectionName__ = "PSC Information"
    __headingAttributeMap__ = {
        "Member Id": "psdMembershipId",
        "Name": "name",
        "Birth Date": "dateOfBirth",
        "Psc Card Id": "pscCardId",
        "Membership Type": "memberShipCategory",
        "Start Date": "createDate",
        "End Date": "endDate",
        "Phone Number": "phoneNo",
        "Email": "email",
        "Postal Address": "postalAddress",
    }
    __widthMap__ = {
        "Member Id": 6,
        "Name": 3,
        "Birth Date": 3,
        "Psc Card Id": 4,
        "Membership Type": 3,
        "Start Date": 3,
        "End Date": 3,
        "Phone Number": 4,
        "Email": 3,
        "Postal Address": 5,
    }
    __alignmentMap__ = {}

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class LoyaltyOfferMadeToCustomer:
    loyaltyMemberId: str
    loyaltyOffer: str
    offerOptInDate: str
    offerOptOutDate: str
    dateOptIn: str
    dateOptOut: str

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class LoyaltyOfferMadeToCustomerList:
    entries: list[LoyaltyOfferMadeToCustomer]
    __headingAttributeMap__ = {
        "Loyalty Member Id": "loyaltyMemberId",
        "Loyalty Offer": "loyaltyOffer",
        "Offer Opt In Date": "offerOptInDate",
        "Offer Opt Out Date": "offerOptOutDate",
        "Date Opt In": "dateOptIn",
        "Date Opt Out": "dateOptOut",
    }
    __widthMap__ = {
        "Loyalty Member Id": 4,
        "Loyalty Offer": 6,
        "Offer Opt In Date": 3,
        "Offer Opt Out Date": 3,
        "Date Opt In": 3,
        "Date Opt Out": 3,
    }
    __alignmentMap__ = {}


@dataclass
class LoyaltyInfo:
    loyaltyMemberId: str
    loyaltyCardNumber: str
    enrollmentDate: str
    enrollmentChannel: str
    currentPointBalance: str
    lifetimePointsEarnerd: str
    lifeTimePointsRedemmed: str

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class LoyatlyInfoList:
    entries: list[LoyaltyInfo]
    __headingAttributeMap__ = {
        "Loyalty Member Id": "loyaltyMemberId",
        "Loyalty Card Number": "loyaltyCardNumber",
        "Enrollment Date": "enrollmentDate",
        "Enrollment Channel": "enrollmentChannel",
        "Current Point Balance": "currentPointBalance",
        "Lifetime Points Earned": "lifetimePointsEarnerd",
        "Lifetime Points Redemmed": "lifeTimePointsRedemmed",
    }
    __widthMap__ = {
        "Loyalty Member Id": 4,
        "Loyalty Card Number": 4,
        "Enrollment Date": 3,
        "Enrollment Channel": 3,
        "Current Point Balance": 3,
        "Lifetime Points Earned": 3,
        "Lifetime Points Redemmed": 3,
    }
    __alignmentMap__ = {}


@dataclass
class Customer:
    name: str = None
    birthDate: str = None
    gender: str = None
    emailAddresses: list[str] = None
    contacts: list[str] = None
    postalAddresses: list[str] = None
    __headingAttributeMap__ = {
        "Name": "name",
        "Birth Date": "birthDate",
        "Gender": "gender",
        "Email Addresses": "emailAddresses",
        "Contact": "contacts",
        "Postal Address": "postalAddresses",
    }

    def __getitem__(self, item):
        return getattr(self, item)


# class common to both


@dataclass
class Request:
    requesterId: str
    requesterName: str
    reportDate: str


@dataclass
class DetailReport:
    request: Request
    instorePurchases: list[InstorePurchase] = None
    onlinePurcahses: list[OnlinePurchase] = None
    onlineReturns: list[OnlineReturn] = None
    paymentDetails: list[PaymentDetail] = None

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class SummaryReport:
    request: Request
    customer: Customer
    loyatlyInformations: LoyatlyInfoList = None
    loyaltyOfferMadeToCustomer: LoyaltyOfferMadeToCustomerList = None
    pSCInfo: PSCInfo = None
    emailSubscription: EmailSubscription = None
    inferenceAboutYou: InferenceAboutYou = None
    salesTransactionSummary: SalesTransactionSummary = None

    def __getitem__(self, item):
        return getattr(self, item)
