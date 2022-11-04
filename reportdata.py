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
class OnlinePurchase:
    purhcaseDate: str
    productDescription: str
    totalSales: float
    unitQuantity: str

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class OnlineReturn:
    productDescription: str
    totalReturnDlr: str
    qnantityToReturn: str
    returnReportedDate: str

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class PaymentDetail:
    accountNumber: str
    purchaseDate: str
    paymentType: str
    tenderedAmount: float
    cardLastFourDigits: str
    purchaseType: str

    def __getitem__(self, item):
        return getattr(self, item)


# class specific to summary


@dataclass
class SalesTransactionSummary:
    totalAmountSpend: float
    totalTaxPaid: float
    __sectionName__ = "Sales Transaction Summary"
    __dataHeaders__ = {
        "Total amount spent in last 12 months": "totalAmountSpend",
        "Total tax paid in last 12 months": "totalTaxPaid",
    }


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

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class EmailSubscription:
    subs: list[str]


@dataclass
class PSCInfo:
    psdMembershipId: str
    pscCardId: str
    name: str
    email: str
    postalAddress: str
    telephoneNumber: str
    dateOfBirth: str
    createDate: str
    endDate: str
    memberShipCategory: str
    __sectionName__ = "PSC Information"
    __dataHeaders__ = {
        "Loyalty Member Id": "psdMembershipId",
        "Loyalty Card Number": "pscCardId",
        "Enrollment Date": "name",
        "Enrollment Channel": "email",
        "Current Point Balance": "postalAddress",
        "Lifetime Points Earned": "telephoneNumber",
        "Lifetime Points Redemmed": "dateOfBirth",
        "Lifetime Points Redemmed": "createDate",
        "Lifetime Points Redemmed": "endDate"
    }

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
    entries : list[LoyaltyOfferMadeToCustomer]
    __sectionName__ = "Loyalty Offers Made To Customer"
    __dataHeaders__ = {
        "Loyalty Member Id": "loyaltyMemberId",
        "Loyalty Offer": "loyaltyOffer",
        "Offer Opt In Date": "offerOptInDate",
        "Offer Opt Out Date": "offerOptOutDate",
        "Date Opt In": "dateOptIn",
        "Date Opt Out": "dateOptOut"
    }

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
    entries : list[LoyaltyInfo]
    __sectionName__ = "Loyalty Information"
    __dataHeaders__ = {
        "Loyalty Member Id": "loyaltyMemberId",
        "Loyalty Card Number": "loyaltyCardNumber",
        "Enrollment Date": "enrollmentDate",
        "Enrollment Channel": "enrollmentChannel",
        "Current Point Balance": "currentPointBalance",
        "Lifetime Points Earned": "lifetimePointsEarnerd",
        "Lifetime Points Redemmed": "lifeTimePointsRedemmed",
    }

@dataclass
class Customer:
    name: str
    birthDate: str
    gender: str
    emailAddresses: list[str]
    contacts: list[str]
    postalAddresses: list[str]
    __sectionName__ ="Customer Information"
    __keyList__ = {
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
