from dataclasses import dataclass


# Class specific to Details report
@dataclass
class InstorePurchase:
    purchaseDate: str
    productDescription: str
    totalQuantity: int
    totalSales: float
    returnQuatity: int


@dataclass
class OnlinePurchase:
    purhcaseDate: str
    productDescription: str
    totalSales: float
    unitQuantity: int


@dataclass
class OnlineReturn:
    productDescription: str
    totalReturnDlr: str
    qnantityToReturn: int
    returnReportedDate: str


@dataclass
class PaymentDetail:
    accountNumber: str
    purchaseDate: str
    paymentType: str
    tenderedAmount: float
    cardLastFourDigits: int
    purchaseType: str


# class specific to summary


@dataclass
class SalesTransactionSummary:
    totalAmountSpend: float
    totalTaxPaid: float


@dataclass
class InferenceAboutYou:
    listOfBehaviour: list[str] = None
    listOfCharacterstics: list[str] = None
    listOfPreferences: list[str] = None
    homeOwnerList: list[str] = None
    householdEduList: list[str] = None
    householdMartialStatusList: list[str] = None
    householdSize: int = None
    householdLanguageCode: str = None
    noOfChildrenInHousehold: int = None
    occupationList: list[str] = None
    targetIncomeList: list[str] = None
    childrenAgeZeroToTwoList: list[str] = None
    childrenAgeThreeToFiveList: list[str] = None
    childrenAgesixToTenList: list[str] = None
    childrenAgeElevenToFiftenList: list[str] = None
    childrenAgeSixteenToSeventeenList: list[str] = None


@dataclass
class EmailSubscription:
    subs: list[str]


@dataclass
class PSCInfo:
    psdMembershipId: str
    pscCardId: str
    name: str
    email: str
    postalAddresS: str
    telephoneNumber: str
    dateOfBirth: str
    createDate: str
    endDate: str
    memberShipCategory: str


@dataclass
class LoyaltyOfferMadeToCustomer:
    loyaltyMemberId: str
    loyaltyOffer: str
    offerOptInDate: str
    offerOptOutDate: str
    dateOptIn: str
    dateOptOut: str


@dataclass
class LoyaltyInfo:
    loyaltyMemberId: str
    loyaltyCardNumber: str
    enrollmentDate: str
    enrollmentChannel: str
    currentPointBalance: int
    lifetimePointsEarnerd: int
    lifeTimePointsRedemmed: int


@dataclass
class Customer:
    name: str
    birthDate: str
    gender: str
    emailAddresses: list[str]
    contacts: list[str]
    postalAddresses: list[str]

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

@dataclass
class SummaryReport:
    request: Request
    customer: Customer
    loyatlyInformations: list[LoyaltyInfo] = None
    loyaltyOfferMadeToCustomer: list[LoyaltyOfferMadeToCustomer] = None
    pSCInfo:PSCInfo = None
    emailSubscription: EmailSubscription = None
    inferenceAboutYou: InferenceAboutYou = None
    salesTransactionSummary: SalesTransactionSummary = None
