from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
currency_list = [('Rupees', 'Rupees'),
                 ('Dollor', 'Dollor'), ('Pound', 'Pound')]

prefix_type = [('PatientID', 'PatientID'), ('EncounterID', 'EncounterID'), ('Counter Sale', 'Counter Sale'), ('Counter Return', 'Counter Return'), ('Pharmacy Sale', 'Pharmacy Sale'), ('Pharmacy return', 'Pharmacy return'), ('Deposit', 'Deposit'), ('Purchases', 'Purchases'), ('Purchases Return', 'Purchases Return'), ('SampleID', 'SampleID'), ('Demand', 'Demand'), ('Supply', 'Supply'),
               ('IpNo', 'IpNo'), ('dakhila', 'dakhila'), ('StockOut', 'StockOut'), ('Booking', 'Booking'), ('Pharmacy Deposit', 'Pharmacy Deposit'), ('CashPaymentVoucher', 'CashPaymentVoucher'), ('FixedAssets', 'FixedAssets'), ('PurchaseOrder', 'PurchaseOrder'), ('MembershipCode', 'MembershipCode'), ('DischargeMapping', 'DischargeMapping')]

status = [('Active', 'Active'), ('Inactive', 'Inactive')]

date_type = [('All days', 'All days'), ('Specific', 'Specific'), ('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday',
                                                                                                              'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')]

schedule_type = [('Zero', 'Zero'), ('Unlimited',
                                    'Unlimited'), ('Fixed', 'Fixed')]

billing_mode_type = [('General', 'General'), ('Insurance', 'Insurance'), ('Government', 'Government'),
                     ('Transportation', 'Transportation'), ('Organization', 'Organization'), ('Co-operate', 'Co-operate')]


department_type = [('Consultation', 'Consultation'), (
    'Department', 'Department'), ('PatientWard', 'PatientWard'), ('Clinical', 'Clinical')]

service_group_under = [('General service', 'General service'), ('Pathology', 'Pathology'), ('Radiology', 'Radiology'), ('AMBULANCE', 'AMBULANCE'), ('BED CHARGE', 'BED CHARGE'), ('BODY FLUID', 'BODY FLUID'), ('CARDIAC SURGERY', 'CARDIAC SURGERY'), ('DENTAL', 'DENTAL'), ('DERMATOLOGY', 'DERMATOLOGY'), ('ECG', 'ECG'), ('ENT', 'ENT'), ('EYE', 'EYE'), ('FORENSIC', 'FORENSIC'), ('GENERAL PROCEDURE', 'GENERAL PROCEDURE'), ('GENERAL STORE INCOME', 'GENERAL STORE INCOME'), ('GET PASS', 'GET PASS'), (
    'GYNAECOLOGY AND OBSTETRICS', 'GYNAECOLOGY AND OBSTETRICS'), ('MEDICAL', 'MEDICAL'), ('MEDICAL OPD', 'MEDICAL OPD'), ('MISCELLANEOUS', 'MISCELLANEOUS'), ('MONI PATI', 'MONI PATI'), ('OMR', 'OMR'), ('ORTHOPEDIC OPERATION CHARGE', 'ORTHOPEDIC OPERATION CHARGE'), ('OXYGEN', 'OXYGEN'), ('PHARMACY', 'PHARMACY'), ('PHOTOTHERAPY', 'PHOTOTHERAPY'), ('PHYSIOTHERAPY', 'PHYSIOTHERAPY'), ('PSYCHIATRY', 'PSYCHIATRY'), ('SALLON', 'SALLON'), ('VENTILATER CHARGE', 'VENTILATER CHARGE'), ('ER PROCEDURE', 'ER PROCEDURE')]

service_type = [('Target', 'Target'), ('Unit', 'Unit')]

tax = [('N/A', 'N/A'), ('HST', 'HST'), ('VAT', 'VAT')]
service_cost_target = [('', '')]
service_cost_unit = [('', '')]
therapeutic = [('N/A', 'N/A'), ('ANAESTHETICS', 'ANAESTHETICS'), ('ANALGESIC', 'ANALGESIC'), ('ANTHELMINTIC', 'ANTHELMINTIC'), ('ANTI DIARRHEAL',
                                                                                                                                'ANTI DIARRHEAL'), ('ANTIANGINAL/CORONARY VASODILATOR', 'ANTIANGINAL/CORONARY VASODILATOR'), ('ANTIARRYTHMIC', 'ANTIARRYTHMIC'), ('ANTIARTHRITICS', 'ANTIARTHRITICS'), ('ANTIASTHMATIC', 'ANTIASTHMATIC'), ('ANTIBIOTIC', 'ANTIBIOTIC'), ('ANTICOAGULANT', 'ANTICOAGULANT'), ('ANTICONVULSANT', 'ANTICONVULSANT'), ('ANTIDEPRESSANT', 'ANTIDEPRESSANT'), ('ANTIDOTES', 'ANTIDOTES'), ('ANTIEMETIC', 'ANTIEMETIC'), ('ANTIFUNGAL', 'ANTIFUNGAL'), ('ANTIGOUT', 'ANTIGOUT'), ('ANTIHAEMORRHAGIC', 'ANTIHAEMORRHAGIC'), ('ANTIHISTAMINE', 'ANTIHISTAMINE'), ('ANTIHYPERTENSIVE', 'ANTIHYPERTENSIVE'), ('ANTIMALARIAL', 'ANTIMALARIAL'), ('ANTIMICROBIAL', 'ANTIMICROBIAL'), ('ANTIMIGRAINE', 'ANTIMIGRAINE'), ('ANTINEOPLASTIC', 'ANTINEOPLASTIC'), ('ANTIPSYCHOTIC', 'ANTIPSYCHOTIC'), ('ANTIRHEUMATOID', 'ANTIRHEUMATOID'), ('ANTIPASMODIC', 'ANTIPASMODIC'), ('ANTIULCER', 'ANTIULCER'), ('ANTIVIRAL', 'ANTIVIRAL'), ('ANXIOLYTIC/SEDATIVE', 'ANXIOLYTIC/SEDATIVE'), ('AYURVEDIC', 'AYURVEDIC'), ('CHF DRUGS', 'CHF DRUGS'), ('CNS', 'CNS'), ('CONTRAST MEDIA', 'CONTRAST MEDIA'), ('CORTICOSTEROID', 'CORTICOSTEROID'), ('COUGH PREPARATION', 'COUGH PREPARATION'), ('DECONGESTANT', 'DECONGESTANT'), ('DIABETIC', 'DIABETIC'), ('DIURETICS', 'DIURETICS'), ('EAR/EYE PREP', 'EAR/EYE PREP'), ('ELECTORLYTES', 'ELECTORLYTES'), ('ENZYME/CARMINATIVE', 'ENZYME/CARMINATIVE'), ('GARGLES/MOUTH WASH', 'GARGLES/MOUTH WASH'), ('GASTROINTESTINAL', 'GASTROINTESTINAL'), ('GERMAN', 'GERMAN'), ('GERMAN', 'GERMAN'), ('GI RELAXANT/PROKINETICS', 'GI RELAXANT/PROKINETICS'), ('GROWTH DISORDER', 'GROWTH DISORDER'), ('HAEMATOPOIETIC GROWTH FACTOR', 'HAEMATOPOIETIC GROWTH FACTOR'), ('HEPATOBILIARY PREPARATION', 'HEPATOBILIARY PREPARATION'), ('HORMONE/STEROID PREP', 'HORMONE/STEROID PREP'), ('I/V SALINE', 'I/V SALINE'), ('IMMUNOGLOBIN', 'IMMUNOGLOBIN'), ('IODINE', 'IODINE'), ('LAXATIVE/PURGATIVE', 'LAXATIVE/PURGATIVE'), ('LIPID LOWERING AGENT', 'LIPID LOWERING AGENT'), ('METABOLISM', 'METABOLISM'), ('MISCELLANEOUS', 'MISCELLANEOUS'), ('MOOD ELEVATOR', 'MOOD ELEVATOR'), ('MUCOLYTICS AND PROKINETICS', 'MUCOLYTICS AND PROKINETICS'), ('MUSCLE RELAXANT', 'MUSCLE RELAXANT'), ('NASAL PREPARATION', 'NASAL PREPARATION'), ('NEUROMUSCULAR BLOCKER', 'NEUROMUSCULAR BLOCKER'), ('NON USE', 'NON USE'), ('NSAID', 'NSAID'), ('NUTRITION', 'NUTRITION'), ('OPOID', 'OPOID'), ('ORAL PRODUCT', 'ORAL PRODUCT'), ('THYROIDS+ANTITHYROID', 'THYROIDS+ANTITHYROID'), ('TOPICAL PREPARATION', 'TOPICAL PREPARATION'), ('UROGENITAL DRUGS', 'UROGENITAL DRUGS'), ('VASODILATOR AND VASOCONSTRICTORS', 'VASODILATOR AND VASOCONSTRICTORS'), ('VIT/NUTRITION SUPP', 'VIT/NUTRITION SUPP')]
diff = [('Yes', 'Yes'), ('No', 'No')]
route = [('N/A', 'N/A'), ('ID(intra deomen)', 'ID(intra deomen)'), ('IM (intra masular)', 'IM (intra masular)'), ('Inhale', 'Inhale'), ('IO (intra osees)', 'IO (intra osees)'), ('IV (intra venous)', 'IV (intra venous)'),
         ('Nebuliser', 'Nebuliser'), ('PO (per oral)', 'PO (per oral)'), ('PR (per reatal)', 'PR (per reatal)'), ('PU (per vasinal)', 'PU (per vasinal)'), ('SC (sub cutaneous)', 'SC (sub cutaneous)'), ('sublingual', 'sublingual')]
medicine_type = [('Consumable', 'Consumable'),
                 ('Non-Consumable', 'Non-Consumable')]
applyFor = [('Medicine', 'Medicine'), ('Surgical', 'Surgical')]
discountType = [('Custom', 'Custom'), ('Full', 'Full')]
patientStatus = [('Both', 'Both'), ('OPD', 'OPD'), ('IPD', 'IPD')]
service_package_type = [
    ('Service Package', 'Service Package'), ('Service Group', 'Service Group')]
packageName = [('CR AND CAST APPLIED IN HEMATOMA BLOCK', 'CR AND CAST APPLIED IN HEMATOMA BLOCK'), ('"ADNEXAL OPERATIONS - INCLUDING OVARIAN CYSTECTOMY ( OR SALPINGECTOMY PHORECTOMY (ECTOPIC)', 'ADNEXAL OPERATIONS - INCLUDING OVARIAN CYSTECTOMY ( OR SALPINGECTOMY PHORECTOMY (ECTOPIC)'), ('"LAPAROSCOPIC DIAGNOSTIC LAP WITH BLUE TEST (DYE INCLUDED) (CHROMOTUBATION)', '"LAPAROSCOPIC DIAGNOSTIC LAP WITH BLUE TEST (DYE INCLUDED) (CHROMOTUBATION)'), ('(FEM - POP BYPASS , LLIAC SURGERY)',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                 '(FEM - POP BYPASS , LLIAC SURGERY)'), ('15 MM STRAIGHT PLATE', '15 MM STRAIGHT PLATE'), ('24 HOUR URINARY POTASSIUM', '24 HOUR URINARY POTASSIUM'), ('24 HOUR URINARY SODIUM', '24 HOUR URINARY SODIUM'), ('24 HOUR URINE CALCIUM', '24 HOUR URINE CALCIUM'), ('24 HOUR URINE GLUCOSE', '24 HOUR URINE GLUCOSE'), ('24 HOUR URINE OSMOLALITY', '24 HOUR URINE OSMOLALITY'), ('24 HOUR URINE PHOSPHOROUS', '24 HOUR URINE PHOSPHOROUS'), ('24 HOUR URINE PROTEIN EXCRETION', '24 HOUR URINE PROTEIN EXCRETION')]

under = [('Home', 'Home'), ('Master', 'Master'), ('Account', 'Account'), ('Cashier', 'Cashier'), ('Laboratory', 'Laboratory'), ('Pharmacy', 'Pharmacy'), ('Store', 'Store'), ('Setting', 'Setting'), ('Report', 'Report'), ('Financial Report', 'Financial Report'), ('EMR', 'EMR'), ('Log', 'Log'), ('Budget', 'Budget'), ('Radiology', 'Radiology'), ('Thirdparty Report', 'Thirdparty Report'), ('Booking Report', 'Booking Report'), ('Insurance Cost', 'Insurance Cost'), ('Insurance Billing', 'Insurance Billing'), ('Product Rate', 'Product Rate'), ('Insurance Billing', 'Insurance Billing'), ('HMS Report', 'HMS Report'), ('Daily Billing', 'Daily Billing'), ('Bill by User', 'Bill by User'), ('Collection Report', 'Collection Report'), ('Patient Deposit Report', 'Patient Deposit Report'), ('Period Purchase Report', 'Period Purchase Report'), ('Sales Book Report', 'Sales Book Report'), ('Demand Package', 'Demand Package'), ('Cash Payment Voucher', 'Cash Payment Voucher'), ('Default Insurance Ledger',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          'Default Insurance Ledger'), ('Overall Collection', 'Overall Collection'), ('Cash Reciept Payment Report', 'Cash Reciept Payment Report'), ('Medicine Package', 'Medicine Package'), ('Rack', 'Rack'), ('HMIS setting', 'HMIS setting'), ('Rack Management', 'Rack Management'), ('Pharmacy Due Clearance', 'Pharmacy Due Clearance'), ('Pharmacy Deposit Return', 'Pharmacy Deposit Return'), ('Medication Report', 'Medication Report'), ('ICU 1', 'ICU 1'), ('Group Wise Report', 'Group Wise Report'), ('Cashflow', 'Cashflow'), ('LabReport Verify', 'LabReport Verify'), ('Mapping', 'Mapping'), ('Custom Report', 'Custom Report'), ('HMIS', 'HMIS'), ('Feedback', 'Feedback'), ('Questionnaire List', 'Questionnaire List'), ('Patient Feedback List', 'Patient Feedback List'), ('List', 'List'), ('Insurance', 'Insurance'), ('Radiology Report Verify', 'Radiology Report Verify'), ('Emergency', 'Emergency'), ('Billing Draft', 'Billing Draft'), ('Gynaecology', 'Gynaecology'), ('OT/Procedure', 'OT/Procedure'), ('ECHO', 'ECHO'), ('OT Setting', 'OT Setting'), ('Primary', 'Primary')]

inoutType = [('Percentage', 'Percentage'), ('Amount', 'Amount')]

tpName = [('Choose TP Name', 'Choose TP Name'), ('HIB', 'HIB'), ('SSF', 'SSF'),
          ('Yatayat Prali', 'Yatayat Prali'), ('UN staff', 'UN staff'), ('Cash', 'Cash')]

patientType = [('Select Patient Type', 'Select Patient Type'), ('GENERAL', 'GENERAL'), ('LAND DONAR', 'LAND DONAR'), ('ANC', 'ANC'), ('DH KUSMS STUDENT', 'DH KUSMS STUDENT'), ('GOVERNMENT INSURANCE', 'GOVERNMENT INSURANCE'), ('EYE CAMP', 'EYE CAMP'), ('SCHEER MEMORIAL HOSPITAL', 'SCHEER MEMORIAL HOSPITAL'), ('NEW BORN', 'NEW BORN'), ('Bahunepati H.C', 'Bahunepati H.C'), ('DH STAFF', 'DH STAFF'), ('BALUWA H.C', 'BALUWA H.C'), ('KU-STAFF', 'KU-STAFF'), ('DH-FAMILY', 'DH-FAMILY'), ('KUHS-STAFF', 'KUHS-STAFF'), ('KAVRE BUS PVT. LTD', 'KAVRE BUS PVT. LTD'), ('MATRON DISCOUNT', 'MATRON DISCOUNT'), ('GOVT. FREE TREATMENT-DHO', 'GOVT. FREE TREATMENT-DHO'), ('SURGICAL CAMP', 'SURGICAL CAMP'), ('SPONSOR PATIENT', 'SPONSOR PATIENT'), ('CAMP EXPENSES', 'CAMP EXPENSES'), ('RAN AWAY', 'RAN AWAY'), ('DHULIKHEL DRINKING WATER COMMUNITY', 'DHULIKHEL DRINKING WATER COMMUNITY'), ('Surgical Ward', 'Surgical Ward'), ('Medical Ward', 'Medical Ward'), ('SENIOR CITIZEN', 'SENIOR CITIZEN'), ('DH-FRIEND', 'DH-FRIEND'), ('OCMC(ONE-STOP CRISIS MANAGEMENT CENTER)', 'OCMC(ONE-STOP CRISIS MANAGEMENT CENTER)'), ('VANDOL', 'VANDOL'), ('CARDIAC CAMP', 'CARDIAC CAMP'), ('GNC', 'GNC'), ('PG EXAM', 'PG EXAM'), ('SUBIDHA CARD', 'SUBIDHA CARD'), ('ECDC', 'ECDC'), ('KU-STAFF FAMILY', 'KU-STAFF FAMILY'), ('KU-STUDENT', 'KU-STUDENT'), ('KUHS-STAFF FAMILY', 'KUHS-STAFF FAMILY'), ('KUHS-STUDENT', 'KUHS-STUDENT'), ('SEAP', 'SEAP'), ('BIPANNA NAGARIK', 'BIPANNA NAGARIK'), ('EXECUTIVE BOARD MEMBER / FAMILY', 'EXECUTIVE BOARD MEMBER / FAMILY'), ('SIKHAR INSURANCE', 'SIKHAR INSURANCE'), ('FOOD POISON KAVRE', 'FOOD POISON KAVRE'), ('ACADEMIC PURPOSE', 'ACADEMIC PURPOSE'), ('BOARD MEMBER (FAMILY)', 'BOARD MEMBER (FAMILY)'), ('SECOND OT', 'SECOND OT'), ('SINDHU HELAMBU YATAYAT SEWA P.LTD', 'SINDHU HELAMBU YATAYAT SEWA P.LTD'), ('GANESH HIMAL YATAYAT SEWA CO.PVT LTD', 'GANESH HIMAL YATAYAT SEWA CO.PVT LTD'), ('IVI-T003', 'IVI-T003'), ('NAMASTE STIFTUNG', 'NAMASTE STIFTUNG'), ('JYOTI BUDATHOKI', 'JYOTI BUDATHOKI'), ('CHIEF MINISTRY HEALTH PROGRAM', 'CHIEF MINISTRY HEALTH PROGRAM'), ('KATHMANDU UNIVERSITY', 'KATHMANDU UNIVERSITY'), ('IMMUNIZATION RESPONSE (DHO)', 'IMMUNIZATION RESPONSE (DHO)'), ('BHOMI HOSPITAL', 'BHOMI HOSPITAL'), ('PURBA ARANIKO YATAYAT PVT.LTD', 'PURBA ARANIKO YATAYAT PVT.LTD'), ('METABOLIC SYNDROME', 'METABOLIC SYNDROME'), ('RED PAGODA', 'RED PAGODA'), ('JANTRA', 'JANTRA'), ('MATRON DISCOUNT(IPD)', 'MATRON DISCOUNT(IPD)'), ('VANDOL(IPD)', 'VANDOL(IPD)'), ('MI KUSMS STUDENT', 'MI KUSMS STUDENT'), ('BOLDE PHEDICHE HEALTH CEN', 'BOLDE PHEDICHE HEALTH CEN'), ('KATTIKE DEURALI H.C', 'KATTIKE DEURALI H.C'), ('DOLAKHA HOSPITAL', 'DOLAKHA HOSPITAL'), ('ENT WARD', 'ENT WARD'), ('ENT WARD NEW', 'ENT WARD NEW'), ('PSYCHIATRIC WARD', 'PSYCHIATRIC WARD'), ('PNC WARD', 'PNC WARD'), ('REWARD', 'REWARD'), ('ORTHOPEDIC WARD',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        'ORTHOPEDIC WARD'), ('CARDIO PULMONARY OPD', 'CARDIO PULMONARY OPD'), ('CORESMA PROJECT', 'CORESMA PROJECT'), ('MANEKHARKA H.C', 'MANEKHARKA H.C'), ('WARD', 'WARD'), ('BALARA H.C', 'BALARA H.C'), ('CHHATRA DEURALI H.C', 'CHHATRA DEURALI H.C'), ('DHUNGKHARKA H.C', 'DHUNGKHARKA H.C'), ('DORPU H.C', 'DORPU H.C'), ('DUMJA H.C', 'DUMJA H.C'), ('KIRNETAR H.C', 'KIRNETAR H.C'), ('MANIKHARKA H.C', 'MANIKHARKA H.C'), ('DERMATOLOGY WARD', 'DERMATOLOGY WARD'), ('DENTAL WARD', 'DENTAL WARD'), ('EMERGENCY ROOM', 'EMERGENCY ROOM'), ('ENDOSCOPY', 'ENDOSCOPY'), ('ENT OPD', 'ENT OPD'), ('GYNE OPD', 'GYNE OPD'), ('HEMATOLOGY', 'HEMATOLOGY'), ('HEMO DIALYSIS', 'HEMO DIALYSIS'), ('HIGH DEPENDANCY UNIT', 'HIGH DEPENDANCY UNIT'), ('IMMUNIZATION F/P', 'IMMUNIZATION F/P'), ('LUNDRY', 'LUNDRY'), ('MEDICINE OPD', 'MEDICINE OPD'), ('MICROBIOLOGY', 'MICROBIOLOGY'), ('NEONATAL', 'NEONATAL'), ('OPD', 'OPD'), ('OPERATION THEATER', 'OPERATION THEATER'), ('ORTHO OPD / PR', 'ORTHO OPD / PR'), ('OT GYANE', 'OT GYANE'), ('PEDRATIC OPD', 'PEDRATIC OPD'), ('PHYSIOTHERAPY', 'PHYSIOTHERAPY'), ('RADIOLOGY', 'RADIOLOGY'), ('SEAP II', 'SEAP II'), ('SURGERY OPD', 'SURGERY OPD'), ('SYAHAR', 'SYAHAR'), ('WHCPP (WH-NP)', 'WHCPP (WH-NP)'), ('PROSTHO DENTAL', 'PROSTHO DENTAL'), ('PERIPDONTICS DENTAL', 'PERIPDONTICS DENTAL'), ('ORTHODONTICS DENTAL', 'ORTHODONTICS DENTAL'), ('GYANE LABOUR ROOM II', 'GYANE LABOUR ROOM II'), ('CANTEEN', 'CANTEEN'), ('DH RTA(2022-05-04)', 'DH RTA(2022-05-04)'), ('RTA BA 3 KHHA 2643', 'RTA BA 3 KHHA 2643'), ('RTA BA2 KHHA 5778', 'RTA BA2 KHHA 5778'), ('NAWAKANTIPUR BHALAI TATHA COMPANY PVT BALAJU', 'NAWAKANTIPUR BHALAI TATHA COMPANY PVT BALAJU'), ('DH RTA (JA-4009)', 'DH RTA (JA-4009)'), ('AARSHU KAFLE', 'AARSHU KAFLE'), ('BLOOD BANK', 'BLOOD BANK'), ('HRDC', 'HRDC'), ('SURGERY WARD', 'SURGERY WARD'), ('SOCIAL SECURTIY FUND', 'SOCIAL SECURTIY FUND'), ('STAFF', 'STAFF'), ('UN STAFF', 'UN STAFF'), ('DAPCHA H.C', 'DAPCHA H.C'), ('PHALEBAS H.C', 'PHALEBAS H.C'), ('POST OP WARD', 'POST OP WARD'), ('PEDODENTIC DENTAL', 'PEDODENTIC DENTAL'), ('MGDM', 'MGDM'), ('GYANE EMERGENCY', 'GYANE EMERGENCY'), ('OMR DENTAL', 'OMR DENTAL'), ('HINDI H.C', 'HINDI H.C'), ('SOLAMBU H.C', 'SOLAMBU H.C'), ('THANGSING H.C', 'THANGSING H.C'), ('PUTTAR HEALTH CENTER', 'PUTTAR HEALTH CENTER'), ('EYE WARD', 'EYE WARD'), ('OPD EYE', 'OPD EYE'), ('SURGERY DENTAL', 'SURGERY DENTAL'), ('PROCEDURE ROOM', 'PROCEDURE ROOM'), ('CT SCAN', 'CT SCAN'), ('SICU WARD', 'SICU WARD'), ('ICU PEDRATIC WARD', 'ICU PEDRATIC WARD'), ('CATH LAB', 'CATH LAB'), ('PEDIATRIC WARD', 'PEDIATRIC WARD'), ('CSSD', 'CSSD'), ('FORENSIC', 'FORENSIC'), ('MRI', 'MRI'), ('URO OPD', 'URO OPD'), ('INTENSIVE CARE UNIT', 'INTENSIVE CARE UNIT'), ('LABOR ROOM', 'LABOR ROOM'), ('LABORATORY', 'LABORATORY'), ('PEDIATRIC HDU', 'PEDIATRIC HDU'), ('ULTRASOUND DEPT', 'ULTRASOUND DEPT'), ('CONS & ENDO DENTAL', 'CONS & ENDO DENTAL')]

accountGroupNature = [('Select Nature', 'Select Nature'), ('N/A', 'N/A'), ('Income', 'Income'),
                      ('Expenses', 'Expenses'), ('Liabilities', 'Liabilities'), ('Assets', 'Assets')]


accountGroupUnder = [('Select Group', 'Select Group'), ('Bank Account', 'Bank Account'), ('Bank OD A/C', 'Bank OD A/C'), ('Branch/Divisions', 'Branch/Divisions'), ('Capital Account', 'Capital Account'), ('Cash in Hand', 'Cash in Hand'), ('Current Assets', 'Current Assets'), ('Current Liabilities', 'Current Liabilities'), ('Deposits (Assets)', 'Deposits (Assets)'), ('Direct Expenses', 'Direct Expenses'), ('Direct Income', 'Direct Income'), ('Duties & Taxes', 'Duties & Taxes'), ('Employee A/C', 'Employee A/C'), ('Fixed Assets', 'Fixed Assets'), ('Indirect Expenses', 'Indirect Expenses'), ('Indirect Income', 'Indirect Income'), ('Investments', 'Investments'),
                     ('Loans & Advances(Asset)', 'Loans & Advances(Asset)'), ('Loans (Liability)', 'Loans (Liability)'), ('Misc.Expenses (Asset)', 'Misc.Expenses (Asset)'), ('Pharmacy Suppliers', 'Pharmacy Suppliers'), ('Primary', 'Primary'), ('Provisions', 'Provisions'), ('Purchase Account', 'Purchase Account'), ('Reserves & Surplus', 'Reserves & Surplus'), ('Sales Account', 'Sales Account'), ('Secured Loans', 'Secured Loans'), ('Service Account', 'Service Account'), ('Stock-in-Hand', 'Stock-in-Hand'), ('Sundry Creditors', 'Sundry Creditors'), ('Sundry Debtors', 'Sundry Debtors'), ('Suspense A/C', 'Suspense A/C'), ('Unsecured Loans', 'Unsecured Loans')]

account_debit_credit = [('Dr.', 'Dr.'), ('Cr.', 'Cr.')]

debit_credit = [('Debit', 'Debit'), ('Credit', 'Credit')]

account_ledger_type = [('Both', 'Both'), ('Sub ledger',
                                          'Sub ledger'), ('Main ledger', 'Main ledger')]

journalVoucherType = [('Expenditure', 'Expenditure'), ('Income', 'Income')]

subLedger = [('Select Sub Ledger', 'Select Sub Ledger'), ('Cash', 'Cash'), ('Pharmacy Sales', 'Pharmacy Sales'), ('Fixed Assets Purchase', 'Fixed Assets Purchase'), ('ABC Company Pvt.Ltd', 'ABC Company Pvt.Ltd'), ('CheckName', 'CheckName'), ('Check2', 'Check2'), ('Dhulikhel Hospital', 'Dhulikhel Hospital'), ('New Supplier', 'New Supplier'), ('Ambulance Income', 'Ambulance Income'), ('Bed Charge Income', 'Bed Charge Income'), ('BIOCHEMISTRY INCOME', 'BIOCHEMISTRY INCOME'), ('BLOOD BANK INCOME',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              'BLOOD BANK INCOME'), ('BODY FLUID INCOME', 'BODY FLUID INCOME'), ('CARDIAC SURGERY INCOME', 'CARDIAC SURGERY INCOME'), ('CARDIOLOGY INCOME', 'CARDIOLOGY INCOME'), ('CT SCAN INCOME', 'CT SCAN INCOME'), ('CTVS INCOME', 'CTVS INCOME'), ('CYTOPATHOLOGY INCOME', 'CYTOPATHOLOGY INCOME'), ('DENTAL INCOME', 'DENTAL INCOME'), ('DEPT OF MEDICINE INCOME', 'DEPT OF MEDICINE INCOME'), ('DERMATOLOGY INCOME', 'DERMATOLOGY INCOME'), ('ECG INCOME', 'ECG INCOME'), ('ENDOSCOPY INCOME', 'ENDOSCOPY INCOME'), ('ENT INCOME',)]

reference = [('Against', 'Against')]

chequeDate = [('AD', 'AD')]

pdc = [('Choose Type', 'Choose Type'), ('Payabale',
                                        'Payabale'), ('Recievable', 'Recievable')]
pdcClearance = [('Choose Type', 'Choose Type'), ('PDC Payabale',
                                                 'PDC Payabale'), ('PDC Recievable', 'PDC Recievable')]
pdcClearanceStatus = [('Choose Status', 'Choose Status'), ('Return', 'Return'),
                      ('Cleared', 'Cleared'), ('Bounced', 'Bounced'), ('Cancelled', 'Cancelled')]

budgetCategoryUnder = [
    ('Select Category', 'Select Category'), ('Primary', 'Primary')]

budgetTitle = [('Select Ledger', 'Select Ledger'), ('Salary', 'Salary'), ('Discount Allowed', 'Discount Allowed'),
               ('Custom', 'Custom'), ('Purchase CC Charge', 'Purchase CC Charge'), ('Purchase Adjustment', 'Purchase Adjustment')]

budgetIssueType = [('Choose Issue Type', 'Choose Issue Type'), ('Monthly', 'Monthly'), ('One third',
                                                                                        'One third'), ('Quaterly', 'Quaterly'), ('Half Yearly', 'Half Yearly'), ('Yearly', 'Yearly')]

relation = [('MOTHER', 'MOTHER'), ('HUSBAND', 'HUSBAND'), ('FATHER', 'FATHER'), ('WIFE', 'WIFE'), ('SON', 'SON'), ('DAUGHTER', 'DAUGHTER'), ('OTHER', 'OTHER'), ('C/O', 'C/O'), ('BROTHER', 'BROTHER'), ('SISTER', 'SISTER'), ('UNCLE', 'UNCLE'), ('CHILD', 'CHILD'), ('COUSIN', 'COUSIN'), ('DAUGHTER IN-LAW', 'DAUGHTER IN-LAW'), ('SISTER IN-LAW', 'SISTER IN-LAW'),
            ('FRIENDS', 'FRIENDS'), ('GRANDSON', 'GRANDSON'), ('GRANDDAUGHTER', 'GRANDDAUGHTER'), ('GRANDFATHER', 'GRANDFATHER'), ('GRANDMOTHER', 'GRANDMOTHER'), ('MOTHER IN-LAW', 'MOTHER IN-LAW'), ('BROTHER IN-LAW', 'BROTHER IN-LAW'), ('SON IN-LAW', 'SON IN-LAW'), ('FATHER IN-LAW', 'FATHER IN-LAW'), ('NIECE', 'NIECE'), ('NEPHEW', 'NEPHEW'), ('AUNTY', 'AUNTY')]

gender = [('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')]

deposit_mode = [('Deposit', 'Deposit'), ('Return', 'Return')]

patientStatus = [('Registered', 'Registered'), ('Admitted', 'Admitted')]

billing_def_ledger_Type = [('Cash', 'Cash'), ('Credit', 'Credit')]

in_outType = [('Percentage', 'Percentage'), ('Amount', 'Amount')]

budgetCategoryUnder = [('Primary', 'Primary')]
# Master


class BillingMode(models.Model):
    billingmode = models.CharField(max_length=50, null=True, blank=True)
    modeType = models.CharField(
        max_length=50, choices=billing_mode_type, null=True, blank=True)
    active = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.billingmode


# Master


class Department(models.Model):
    department_type = models.CharField(
        max_length=50, choices=department_type, null=True, blank=True)
    icon = models.ImageField(null=True, blank=True)
    hod = models.CharField(max_length=100, null=True,
                           blank=True, default='N/A')
    department_name = models.CharField(max_length=100, null=True, blank=True)
    department_status = models.CharField(
        max_length=50, choices=status, null=True, blank=True)

    def __str__(self):
        return self.department_name


class Room(models.Model):
    room_no = models.IntegerField()
    # If the room has no number and only name then.
    roomName = models.CharField(max_length=100, null=True, blank=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.room_no)

# Master


class ConsultantType(models.Model):
    type_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.type_name
# Master


class Consultant(models.Model):
    nmc_no = models.IntegerField(null=True, blank=True, default='N/A')
    post = models.CharField(max_length=50, null=True,
                            blank=True, default='N/A')
    consultant_type = models.ForeignKey(
        'ConsultantType', on_delete=models.CASCADE, null=True, blank=True)
    e_mail = models.EmailField(
        unique=True, null=True, blank=True, default='N/A')
    profile = models.CharField(
        max_length=50, null=True, blank=True, default='N/A')
    department = models.ForeignKey(
        'Department', on_delete=models.CASCADE, null=True, blank=True)
    upload_image = models.ImageField(null=True, blank=True)
    dr_name = models.CharField(
        max_length=50, null=True, blank=True, default='N/A')
    mobile = models.BigIntegerField(null=True, blank=True)
    address = models.CharField(
        max_length=50, null=True, blank=True, default='N/A')
    avg_consultant_time = models.IntegerField(null=True, blank=True)
    doctor_order = models.CharField(
        max_length=20, default='null', null=True, blank=True)
    active = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.dr_name


# Home
class Company(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_no = models.BigIntegerField(null=True, blank=True)
    web = models.CharField(max_length=50, null=True, blank=True, default='N/A')
    pincode = models.IntegerField(null=True, blank=True)
    PAN_No = models.IntegerField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    mailing_name = models.CharField(
        max_length=100, default='N/A', null=True, blank=True)
    mobileNo = models.BigIntegerField(null=True, blank=True)
    country = models.CharField(
        max_length=100, null=True, blank=True, default='N/A')
    currency = models.CharField(
        choices=currency_list, max_length=100, null=True, blank=True)
    cst_no = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    e_mail = models.EmailField(unique=True, null=True, blank=True)
    state = models.CharField(max_length=50, null=True,
                             blank=True, default='N/A')
    tin_no = models.IntegerField(null=True, blank=True)
    chs_code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

# Home


class FiscalYear(models.Model):
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)
    shortname = models.CharField(
        max_length=20, null=True, blank=True, default='N/A')

    def __str__(self):
        return str(self.startdate)

# Home


class Prefix(models.Model):
    fiscalYear = models.ForeignKey(
        'FiscalYear', on_delete=models.CASCADE, null=True, blank=True)
    startIndex = models.IntegerField(null=True, blank=True)
    startDate = models.DateField(null=True, blank=True)
    suffix = models.CharField(max_length=50, null=True,
                              blank=True, default='N/A')
    prefix_type = models.CharField(
        choices=prefix_type, max_length=50, null=True, blank=True)
    prefix = models.CharField(max_length=50, null=True,
                              blank=True, default='N/A')
    endDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.prefix_type

# Home


class Role(models.Model):
    roleName = models.CharField(max_length=50, null=True, blank=True)
    role_status = models.CharField(
        choices=status, max_length=50, null=True, blank=True)

    def __str__(self):
        return self.roleName

# Home


class DoctorSchedule(models.Model):
    dateType = models.CharField(
        max_length=50, choices=date_type, default='N/A', null=True, blank=True)
    doctor = models.ForeignKey(
        'Consultant', on_delete=models.CASCADE, null=True, blank=True)  # Master - consultant
    registration_start_time = models.TimeField(null=True, blank=True)
    registration_days = models.IntegerField(default=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    schedule_type = models.CharField(
        max_length=50, choices=schedule_type, default='N/A', null=True, blank=True)
    registration_end_time = models.TimeField(null=True, blank=True)
    booking_days = models.IntegerField(default=100, null=True, blank=True)
    mode = models.ForeignKey(
        'BillingMode', on_delete=models.CASCADE, null=True, blank=True)  # Master-billing mode
    regd = models.IntegerField(null=True, blank=True)
    booking_start_time = models.TimeField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    department = models.ForeignKey(
        'Department', on_delete=models.CASCADE, null=True, blank=True)
    booking = models.IntegerField(null=True, blank=True)
    booking_end_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.dateType

# Home


class DoctorMapping(models.Model):
    #     # user = relation
    consultant_doctor = models.OneToOneField(
        'Consultant', on_delete=models.CASCADE)
    # status =

    def __str__(self):
        return self.consultant_doctor


# Home
class Holiday(models.Model):
    from_date = models.DateField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.from_date)

# Master


class ServiceGroup(models.Model):
    group_name = models.CharField(
        max_length=100, default='N/A', null=True, blank=True)
    under = models.CharField(
        max_length=50, choices=service_group_under, null=True, blank=True)
    service_group_type = models.CharField(
        max_length=50, choices=service_type, null=True, blank=True)
    active = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.group_name

# Master


class ServiceCost(models.Model):
    item_name = models.CharField(
        max_length=50, null=True, blank=True, default='N/A')
    price = models.IntegerField(null=True, blank=True)
    code = models.IntegerField(null=True, blank=True)
    group = models.ForeignKey(
        'ServiceGroup', on_delete=models.CASCADE, null=True, blank=True)
    tax = models.CharField(max_length=50, choices=tax,
                           null=True, blank=True, default='N/A')
    d_qty = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(null=True, blank=True)
    target = models.CharField(
        max_length=50, choices=service_cost_target, null=True, blank=True, default='N/A')
    unit = models.CharField(
        max_length=50, choices=service_cost_unit, null=True, blank=True, default='N/A')
    fixed_rate = models.BooleanField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    interpretation = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.item_name


# Master
class ReferCorporation(models.Model):
    name = models.CharField(
        max_length=50, default='N/A', null=True, blank=True)
    contact = models.BigIntegerField(null=True, blank=True)
    address = models.CharField(
        max_length=50, null=True, blank=True, default='N/A')
    isActive = models.CharField(
        max_length=50, choices=status, null=True, blank=True, default='N/A')

    def __str__(self):
        return self.name

# Master


class Referby(models.Model):
    license_no = models.IntegerField(null=True, blank=True)
    profile = models.CharField(
        max_length=50, default='N/A', null=True, blank=True)
    mobile = models.BigIntegerField(null=True, blank=True)
    address = models.CharField(
        max_length=50, default='N/A', null=True, blank=True)
    status = models.CharField(
        max_length=10, choices=status, default='N/A', null=True, blank=True)
    doctor_name = models.CharField(
        max_length=50, default='N/A', null=True, blank=True)
    post = models.CharField(
        max_length=50, default='N/A', null=True, blank=True)
    email = models.EmailField(
        unique=True, default='N/A', null=True, blank=True)
    corporation = models.ForeignKey(
        'ReferCorporation', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.doctor_name

# Master
# Medicine item foreign model start


class Standard(models.Model):
    name = models.CharField(
        max_length=50, default='N/A', null=True, blank=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(
        max_length=50, default='N/A', null=True, blank=True)

    def __str__(self):
        return self.name


class PackSize(models.Model):
    name = models.CharField(
        max_length=50, default='N/A', null=True, blank=True)

    def __str__(self):
        return self.name


class Generic(models.Model):
    name = models.CharField(
        max_length=50, default='N/A', null=True, blank=True)
    therapeutic = models.CharField(
        max_length=50, default='N/A', null=True, blank=True, choices=therapeutic)  # choices not finished
    narcotic = models.CharField(
        max_length=10, choices=diff, null=True, blank=True)

    def __str__(self):
        return self.name


class GenericStrength(models.Model):
    genericName = models.ForeignKey(
        'Generic', on_delete=models.CASCADE, null=True, blank=True)
    route = models.CharField(
        max_length=50, choices=route, null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    strength_unit = models.CharField(max_length=50, null=True, blank=True)
    volume = models.IntegerField(null=True, blank=True)
    volumeUnit = models.CharField(max_length=50, null=True, blank=True)
    otherInfo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.genericName


class Unit(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    formalName = models.CharField(max_length=50, null=True, blank=True)
    applyFor = models.CharField(max_length=50, choices=applyFor)

    def __str__(self):
        return self.name

# Medicine item foreign models end

# Master


class Medicine(models.Model):
    brandName = models.CharField(max_length=50, null=True, blank=True)
    standard = models.ForeignKey(
        'Standard', on_delete=models.CASCADE, null=True, blank=True)
    manufacturer = models.ForeignKey(
        'Manufacturer', on_delete=models.CASCADE, null=True, blank=True)
    primaryUnit = models.IntegerField(null=True, blank=True)
    packSize = models.ForeignKey(
        'PackSize', null=True, blank=True, on_delete=models.CASCADE)
    preservatives = models.CharField(max_length=50, null=True, blank=True)
    medicine_type = models.CharField(max_length=50, choices=medicine_type)
    allow_tablet_break = models.CharField(max_length=10, choices=diff)
    active = models.CharField(max_length=10, choices=diff)
    genericSaltStrength = models.OneToOneField(
        'GenericStrength', on_delete=models.CASCADE,
        primary_key=True)
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=50, null=True, blank=True)
    secondaryUnit = models.IntegerField(null=True, blank=True)
    packSize = models.ForeignKey(
        'PackSize', on_delete=models.CASCADE, null=True, blank=True)
    minStock = models.IntegerField(null=True, blank=True)
    maxStock = models.IntegerField(null=True, blank=True)
    tax = models.CharField(max_length=10, choices=tax)

    def __str__(self):
        return self.brandName

# Surgical item foreign key model start


class SurgicalGroup(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Surgical(models.Model):
    surgicalName = models.OneToOneField('SurgicalGroup', on_delete=models.CASCADE,
                                        primary_key=True,)
    type_size = models.CharField(max_length=50, null=True, blank=True)
    remarks = models.TextField()

    def __str__(self):
        return self.surgicalName


# Surgical item foreign key model end
# Master
class SurgicalItem(models.Model):
    brandName = models.CharField(max_length=50, null=True, blank=True)
    standard = models.ForeignKey(
        'Standard', on_delete=models.CASCADE, null=True, blank=True)
    unit = models.ForeignKey(
        'Unit', on_delete=models.CASCADE, null=True, blank=True)
    primaryUnit = models.IntegerField(null=True, blank=True)
    packSize = models.ForeignKey(
        'PackSize', null=True, blank=True, on_delete=models.CASCADE)
    secondaryUnit = models.IntegerField(null=True, blank=True)
    packSize = models.ForeignKey(
        'PackSize', on_delete=models.CASCADE, null=True, blank=True)
    tax = models.CharField(max_length=20, choices=tax, null=True, blank=True)
    active = models.CharField(
        max_length=10, choices=diff, null=True, blank=True)
    surgicalName = models.OneToOneField('Surgical', on_delete=models.CASCADE,
                                        primary_key=True)
    manufacturer = models.ForeignKey(
        'Manufacturer', null=True, blank=True, on_delete=models.CASCADE)
    surgical_item_type = models.CharField(
        max_length=20, choices=medicine_type, null=True, blank=True)
    min_stock = models.IntegerField(null=True, blank=True)
    max_stock = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.brandName

# extraitem foreign key models start


class Size(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    isActive = models.CharField(max_length=10, choices=diff)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
# extraitem foreign key models end

# Master


class ExtraItem(models.Model):
    brandName = models.CharField(
        max_length=50, null=True, blank=True, default='N/A')
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)
    size = models.OneToOneField('Size', on_delete=models.CASCADE,
                                primary_key=True)
    maxStock = models.IntegerField(null=True, blank=True)
    extraItemType = models.CharField(
        max_length=20, choices=medicine_type, null=True, blank=True)
    groupName = models.ForeignKey(
        'Group', on_delete=models.CASCADE, null=True, blank=True)
    manufacturer = models.ForeignKey(
        'Manufacturer', null=True, blank=True, on_delete=models.CASCADE)
    minStock = models.IntegerField(null=True, blank=True)
    tax = models.CharField(max_length=20, choices=tax, null=True, blank=True)
    active = models.CharField(
        max_length=10, choices=diff, null=True, blank=True)

    def __str__(self):
        return self.brandName


# Master

class ShareSetting(models.Model):
    mode = models.ForeignKey(
        'BillingMode', on_delete=models.CASCADE, null=True, blank=True)
    outValue = models.IntegerField(null=True, blank=True)
    source = models.ManyToManyField('Consultant')
    doctor = models.ForeignKey('Consultant', on_delete=models.CASCADE,
                               null=True, blank=True, related_name='doctor_consultant')
    inType = models.CharField(
        max_length=20, choices=in_outType, null=True, blank=True)
    tax = models.IntegerField(null=True, blank=True)
    startDate = models.DateField(null=True, blank=True)
    outType = models.CharField(
        max_length=30, choices=in_outType, null=True, blank=True)
    service = models.ManyToManyField('ServiceGroup')

    def __str__(self):
        return self.doctor

# Master


# Foreign field for service package


class ServicePackageCategory(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name
# Foreign field for service package

# Master


class ServicePackage(models.Model):
    billingMode = models.ForeignKey(
        'BillingMode', on_delete=models.CASCADE, null=True, blank=True)
    packageType = models.CharField(
        max_length=20, choices=service_package_type, null=True, blank=True)
    groupName = models.CharField(max_length=100, null=True, blank=True)
    packageName = models.ForeignKey(
        'ServiceCost', on_delete=models.CASCADE, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    category = models.ManyToManyField('ServicePackageCategory')

    def __str__(self):
        return self.packageName

# Master


class Menu(models.Model):
    menuName = models.CharField(max_length=50, null=True, blank=True)
    hasSubMenu = models.BooleanField(null=True, blank=True)
    URL = models.CharField(max_length=50, null=True, blank=True)
    under = models.CharField(
        max_length=40, choices=under, null=True, blank=True)
    isOpen = models.BooleanField(null=True, blank=True)
    iconName = models.CharField(max_length=50, null=True, blank=True)
    isActive = models.BooleanField(null=True, blank=True)
    isActiveWeb = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.menuName

# Master


class DiscoutCategory(models.Model):
    discountCategory = models.CharField(max_length=50, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True, default='N/A')

    def __str__(self):
        return self.discountCategory

# Master


class BillingFraction(models.Model):
    billNo = models.IntegerField(null=True, blank=True)
    inType = models.CharField(
        max_length=50, choices=inoutType, null=True, blank=True)
    tax = models.IntegerField(null=True, blank=True)
    itemId = models.IntegerField(null=True, blank=True)
    inValue = models.IntegerField(null=True, blank=True)
    doctor = models.ForeignKey(
        'Consultant', on_delete=models.CASCADE, null=True, blank=True, related_name='doctor')
    outType = models.CharField(
        max_length=10, null=True, blank=True, choices=inoutType)
    source = models.ForeignKey(
        'Consultant', on_delete=models.CASCADE, null=True, blank=True)
    outValue = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.billNo

# Master


class SymptomMapping(models.Model):
    symptomEng = models.CharField(max_length=50, null=True, blank=True)
    symptomNep = models.CharField(max_length=50, null=True, blank=True)
    active = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.symptomEng

# Master


class Symptom(models.Model):
    symptom = models.ManyToManyField('SymptomMapping')
    department = models.ForeignKey(
        'Department', on_delete=models.CASCADE, null=True, blank=True)
    active = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.symptom

# Master


class CustomReport(models.Model):
    reportTitle = models.CharField(max_length=50, null=True, blank=True)
    script = models.TextField(null=True, blank=True)
    orderBy = models.CharField(max_length=50, null=True, blank=True)
    parameters = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.reportTitle

# Master


class CustomForm(models.Model):
    menu = models.ForeignKey(
        'Menu', on_delete=models.CASCADE, null=True, blank=True)
    fieldName = models.CharField(max_length=50, null=True, blank=True)
    # fieldType =
    required = models.CharField(max_length=10, choices=diff)
    orderNo = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.fieldName

# Master


class ClaimPrefix(models.Model):
    tpName = models.CharField(
        max_length=50, choices=tpName, null=True, blank=True)
    prefix = models.CharField(max_length=50, null=True, blank=True)
    suffix = models.CharField(max_length=50, null=True, blank=True)
    fiscalYear = models.ForeignKey(
        'FiscalYear', on_delete=models.CASCADE, null=True, blank=True)
    startDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)
    startIndex = models.IntegerField(null=True, blank=True)
    endIndex = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.tpName

# Master


class PatientSchemeDiscount(models.Model):
    patientType = models.CharField(
        max_length=50, choices=patientType, null=True, blank=True)
    serviceGroup = models.ForeignKey(
        'ServiceGroup', on_delete=models.CASCADE, null=True, blank=True)
    billingMode = models.ForeignKey(
        'BillingMode', on_delete=models.CASCADE, null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    opd = models.BooleanField(null=True, blank=True)
    ipd = models.BooleanField(null=True, blank=True)
    emergency = models.BooleanField(null=True, blank=True)
    discountFixedRakhne = models.BooleanField(null=True, blank=True)
    rateFixedRakhne = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.patientType

# Account ledger model start


class AccountLedgerGroup(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    nature = models.CharField(
        max_length=40, choices=accountGroupNature, null=True, blank=True)
    under = models.CharField(
        max_length=40, choices=accountGroupUnder, null=True, blank=True)
    narration = models.TextField(null=True, blank=True)
    affectGrossProfit = models.CharField(
        max_length=10, choices=diff, null=True, blank=True)

    def __str__(self):
        return self.name

# Account ledger model end


# Account
class AccountLedger(models.Model):
    code = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    group = models.ForeignKey('AccountLedgerGroup',
                              on_delete=models.CASCADE, null=True, blank=True)
    openingBalance = models.IntegerField(null=True, blank=True)
    debit_credit = models.CharField(
        max_length=10, choices=account_debit_credit, null=True, blank=True)
    narration = models.TextField(null=True, blank=True)
    ledger = models.CharField(
        max_length=20, choices=account_ledger_type, null=True, blank=True)

    def __str__(self):
        return self.name


# Account


class JournalVoucherSub(models.Model):
    voucherNo = models.IntegerField(null=True, blank=True)
    journalVoucherType = models.CharField(
        max_length=20, choices=journalVoucherType, null=True, blank=True)
    accountLedger = models.ForeignKey(
        'AccountLedger', on_delete=models.CASCADE, null=True, blank=True)
    subLedger = models.ForeignKey(
        'AccountLedger', on_delete=models.CASCADE, null=True, blank=True, related_name='subLedger')
    debit_credit = models.CharField(
        null=True, blank=True, max_length=10, choices=account_debit_credit)
    amount = models.IntegerField(null=True, blank=True)
    cheque_no = models.IntegerField(null=True, blank=True)
    cheque_date = models.DateField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.voucherNo)

# Account


class PaymentVoucher(models.Model):
    voucherNo = models.IntegerField(null=True, blank=True)
    paidTo = models.ForeignKey(
        'AccountLedger', on_delete=models.CASCADE, null=True, blank=True, related_name='paidTo_ac_ledger')
    bank_cash = models.ForeignKey(
        'AccountLedger', on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    chequeNo = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    chequeDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.voucherNo)

# Account


class RecieptVoucher(models.Model):
    voucherNo = models.IntegerField(null=True, blank=True)
    paidTo = models.ForeignKey(
        'AccountLedger', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    bank_cash = models.ForeignKey(
        'AccountLedger', on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    chequeNo = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    chequeDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.voucherNo)

# Account


class ContraVoucher(models.Model):
    voucherNo = models.IntegerField(null=True, blank=True)
    paidTo = models.ForeignKey(
        'AccountLedger', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    bank_cash = models.ForeignKey(
        'AccountLedger', on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    chequeNo = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    chequeDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.voucherNo)

# Account


class DebitCreditNote(models.Model):
    voucherNo = models.IntegerField(null=True, blank=True)
    accountLedger = models.ForeignKey(
        'AccountLedger', on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    debit_Credit = models.CharField(
        null=True, blank=True, max_length=10, choices=account_debit_credit)
    debit_or_credit = models.CharField(
        null=True, blank=True, max_length=10, choices=debit_credit)
    chequeNo = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    reference = models.CharField(
        max_length=20, choices=reference, null=True, blank=True)
    chequeDate = models.CharField(
        max_length=20, choices=chequeDate, null=True, blank=True)

    def __str__(self):
        return str(self.voucherNo)

# Account


# Account


class PDC(models.Model):
    pdc_type = models.CharField(
        max_length=20, choices=pdc, null=True, blank=True)
    voucherNo = models.IntegerField(null=True, blank=True)
    accountLedger = models.ForeignKey(
        'AccountLedger', on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    bank = models.ForeignKey(
        'AccountLedger', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    chequeNo = models.IntegerField(null=True, blank=True)
    chequeDate = models.DateField(null=True, blank=True)
    narration = models.TextField(null=True, blank=True)
    printAfterSave = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return str(self.voucherNo)

# Account


class PDCclearance(models.Model):
    voucherNo = models.IntegerField(null=True, blank=True)
    voucherDate = models.DateField(null=True, blank=True)
    voucherType = models.CharField(
        max_length=20, choices=pdcClearance, null=True, blank=True)
    # againstInvoiceNo =
    accountLedger = models.ForeignKey(
        'AccountLedger', on_delete=models.CASCADE, null=True, blank=True)
    chequeNo = models.IntegerField(null=True, blank=True)
    chequeDate = models.DateField(null=True, blank=True)
    bank = models.ForeignKey(
        'AccountLedger', on_delete=models.CASCADE, null=True, blank=True, related_name='bank_ac_ledger')
    amount = models.IntegerField(null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=pdcClearanceStatus, null=True, blank=True)
    narration = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.voucherNo)

# Account


class BudgetType(models.Model):
    typeName = models.CharField(max_length=50, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    active = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.typeName

# Account


class BudgetCategory(models.Model):
    categoryId = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    under = models.CharField(max_length=50, null=True,
                             blank=True, choices=budgetCategoryUnder)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.category


# Account


class BudgetTitle(models.Model):
    fiscalYear = models.ForeignKey(
        'FiscalYear', on_delete=models.CASCADE, null=True, blank=True,)
    title = models.CharField(
        max_length=20, choices=budgetTitle, null=True, blank=True,)
    cateory = models.ForeignKey(
        'BudgetCategory', on_delete=models.CASCADE, null=True, blank=True,)
    amount = models.IntegerField(null=True, blank=True,)
    remarks = models.TextField(null=True, blank=True,)

    def __str__(self):
        return self.title

# Account


class BudgetIssue(models.Model):
    date = models.DateField(null=True, blank=True)
    budgetTitle = models.ForeignKey(
        'BudgetTitle', on_delete=models.CASCADE, null=True, blank=True)
    budgetType = models.CharField(
        max_length=20, choices=budgetIssueType, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    # issuePeriod =
    remarks = models.TextField(null=True, blank=True)
    budgetCategory = models.ForeignKey(
        'BudgetCategory', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.budgetTitle

# Registration models start


class Country(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    status = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    status = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.name


class Municipality(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    district = models.ForeignKey(
        'District', on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.name
# Registration models end

# <------------------- Cashier models start ------------------------------>
# note : In cashier some models contain patientID and also fields of age name personal details, I think the model is meant to pre fill those data or not fill those data as patient Id should give all the information about a patient.
# Cashier


class Registration(models.Model):
    patientNo = models.IntegerField(null=True, blank=True)
    billingMode = models.ForeignKey(
        'BillingMode', on_delete=models.CASCADE, null=True, blank=True)
    nhsioNo = models.IntegerField(null=True, blank=True)
    newborn = models.BooleanField(null=True, blank=True)
    autoBill = models.BooleanField(null=True, blank=True)
    intRef = models.BooleanField(null=True, blank=True)
    bookingId = models.IntegerField(null=True, blank=True)
    department = models.ForeignKey(
        'Department', on_delete=models.CASCADE, null=True, blank=True)
    firstName = models.CharField(max_length=50, null=True, blank=True)
    lastName = models.CharField(max_length=50, null=True, blank=True)
    country = models.ForeignKey(
        'Country', on_delete=models.CASCADE, null=True, blank=True)
    wardNo = models.IntegerField(null=True, blank=True)
    referBy = models.ForeignKey(
        'Referby', on_delete=models.CASCADE, null=True, blank=True)
    relation = models.CharField(
        max_length=20, choices=relation, null=True, blank=True)
    consultant = models.ForeignKey(
        'Consultant', on_delete=models.CASCADE, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    district = models.ForeignKey(
        'District', on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.BigIntegerField(null=True, blank=True)
    isFollowUp = models.CharField(
        max_length=50, choices=diff, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    gender = models.CharField(
        max_length=10, choices=gender, null=True, blank=True)
    municipaltiy = models.ForeignKey(
        'Municipality', on_delete=models.CASCADE, null=True, blank=True)
    patientType = models.CharField(
        max_length=50, choices=patientType, null=True, blank=True)
    c_o = models.CharField(max_length=50, null=True, blank=True)
    passportNo = models.IntegerField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    referCorpo = models.ForeignKey(
        'ReferCorporation', on_delete=models.CASCADE, null=True, blank=True)
    panNo = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.patientNo)

# Cashier
# All fields are not covered due to technical issues.


class Cash_CreditBilling(models.Model):
    patientId = models.IntegerField(null=True, blank=True)
    performedBy = models.ManyToManyField('Consultant')
    patientType = models.CharField(
        max_length=50, choices=patientType, null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    loadDraft = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.patientId


# Cashier
# In my guess this model is complete
class Deposit(models.Model):
    mode = models.CharField(
        max_length=10, choices=deposit_mode, null=True, blank=True)
    rec_ledger = models.ForeignKey(
        'AccountLedger', on_delete=models.CASCADE, null=True, blank=True)  # Only bank
    remarks = models.TextField(null=True, blank=True)
    patientId = models.IntegerField(null=True, blank=True)
    ac_ledger = models.ForeignKey(
        'AccountLedger', on_delete=models.CASCADE, null=True, blank=True, related_name='ac_ledger')
    depositAmount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.mode

# Cashier


class BillReturn(models.Model):
    billNo = models.IntegerField(null=True, blank=True)
    patientId = models.IntegerField(null=True, blank=True)
    quanitity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.billNo

# Cashier


class Admission_Discharge(models.Model):
    pass

# Cashier


class Booking(models.Model):
    patientNo = models.IntegerField(null=True, blank=True)
    bookedID = models.IntegerField(null=True, blank=True)
    billingMode = models.ForeignKey(
        'BillingMode', on_delete=models.CASCADE, null=True, blank=True)
    consultant = models.ForeignKey(
        'Consultant', on_delete=models.CASCADE, null=True, blank=True)
    firstName = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    district = models.ForeignKey(
        'District', on_delete=models.CASCADE, null=True, blank=True)
    wardNo = models.IntegerField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    relation = models.CharField(
        max_length=20, choices=relation, null=True, blank=True)
    referBy = models.ForeignKey(
        'Referby', on_delete=models.CASCADE, null=True, blank=True)
    isFollowUp = models.CharField(
        max_length=10, choices=diff, null=True, blank=True)
    department = models.ForeignKey(
        'Department', on_delete=models.CASCADE, null=True, blank=True)
    consultDate = models.DateField(null=True, blank=True)
    consultTime = models.TimeField(null=True, blank=True)
    lastName = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(
        max_length=20, choices=gender, null=True, blank=True)
    municipality = models.ForeignKey(
        'Municipality', on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.BigIntegerField(null=True, blank=True)
    guardian = models.CharField(max_length=50, null=True, blank=True)
    referCorpo = models.ForeignKey(
        'ReferCorporation', on_delete=models.CASCADE, null=True, blank=True)
    patientType = models.CharField(
        max_length=50, choices=patientType, null=True, blank=True)
    panNo = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.patientNo)

# Cashier


class EditPatient(models.Model):
    pass

# Cashier


class AutoBillingSetting(models.Model):
    billingMode = models.ForeignKey(
        'BillingMode', on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(
        'Department', on_delete=models.CASCADE, null=True, blank=True)
    startDate = models.DateField(null=True, blank=True)
    startTime = models.TimeField(null=True, blank=True)
    isFollowUp = models.CharField(
        max_length=10, choices=diff, null=True, blank=True)
    serviceCost = models.ForeignKey(
        'ServiceCost', on_delete=models.CASCADE, null=True, blank=True, related_name='autoBillServiceCost')
    qty = models.IntegerField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)
    endTime = models.TimeField(null=True, blank=True)
    refOPDcost = models.ForeignKey(
        'ServiceCost', on_delete=models.CASCADE, null=True, blank=True, related_name='refOpdCost')

    def __str__(self):
        return self.serviceCost

# Cashier


class DefaultBillingLedger(models.Model):
    billingMode = models.ForeignKey(
        'BillingMode', on_delete=models.CASCADE, null=True, blank=True)
    patientType = models.CharField(
        max_length=50, choices=patientType, null=True, blank=True)
    patientStatus = models.CharField(
        max_length=50, choices=patientStatus, null=True, blank=True)
    isModeFixed = models.CharField(
        max_length=10, choices=diff, null=True, blank=True)
    billingType = models.CharField(
        max_length=10, choices=billing_def_ledger_Type, null=True, blank=True)
    accountLedger = models.ForeignKey(
        'AccountLedger', on_delete=models.CASCADE, null=True, blank=True)
    isLedgerFixed = models.CharField(
        max_length=10, choices=diff, null=True, blank=True)
    isActive = models.CharField(
        max_length=10, choices=diff, null=True, blank=True)

    def __str__(self):
        return self.accountLedger

# Cashier


class DueClerance(models.Model):
    pass

# Cashier


class DepositReturn(models.Model):
    pass

# Cashier


class PatientTransit(models.Model):
    pass


# Cashier
class MembershipRegisteration(models.Model):
    membershipType = models.CharField(
        max_length=50, choices=patientType, null=True, blank=True)
    firstName = models.CharField(max_length=50, null=True, blank=True)
    lastName = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=10, choices=gender, null=True, blank=True)
    district = models.ForeignKey(
        'District', on_delete=models.CASCADE, null=True, blank=True)
    municipality = models.ForeignKey(
        'Municipality', on_delete=models.CASCADE, null=True, blank=True)
    wardNo = models.IntegerField(null=True, blank=True)
    street = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.BigIntegerField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    pharmacyDiscount = models.IntegerField(null=True, blank=True)
    isActive = models.CharField(max_length=10, choices=diff)
    billingDiscount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.firstName

# Cashier


class PatientVisitorPass(models.Model):
    patientID = models.IntegerField(null=True, blank=True)
    numberOfPass = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.patientID)

# Cashier


class BillingDraft(models.Model):
    pass

# Cashier


class DisChargeBilling(models.Model):
    pass

# Cashier


class BankCollection(models.Model):
    pass

# New line of codes to merge with the above codes
# Patients


bloodType = [('A+', 'A+'), ('A', 'A'), ('AB', 'AB'), ('AB+', 'AB+'),
             ('B+', 'B+'), ('B', 'B'), ('O+', 'O+'), ('O', 'O')]

currentOperativePlan = [('Completed', 'Completed'),
                        ('Dropped', 'Dropped'), ('Planned', 'Planned')]


appointmentStatus = [('Attended', 'Attended'), ('Scheduled',
                                                'Scheduled'), ('Missed', 'Missed'), ('Cancelled', 'Cnacelled')]

billStatus = [('Paid', 'Paid'), ('Due', 'Due')]

patient_status = [('Registered', 'Registered'), ('Admitted', 'Admitted')]

paymentMethod = [('Cash', 'Cash'), ('Bank', 'Bank'), ('Online', 'Online')]

payment_for = [('Deposit', 'Deposit'), ('Payment', 'Payment')]

bill_status = [('Paid', 'Paid'), ('Unpaid', 'Unpaid')]
# Patient registeration


class TypePatient(models.Model):
    name = models.CharField(max_length=100)
    discount = models.BigIntegerField(null=True, blank=True)
    creditLimit = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Ward(models.Model):
    ward_no = models.IntegerField(null=True, blank=True)
    ward_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.ward_no)


class Bed(models.Model):
    bed_no = models.IntegerField(null=True, blank=True)
    ward = models.ForeignKey(
        'Ward', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.bed_no)


class Patient(models.Model):
    firstName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100, null=True, blank=True)
    lastName = models.CharField(max_length=100)
    sex = models.CharField(max_length=50, null=True, blank=True)
    dateOfBirth = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    placeOfBirth = models.CharField(max_length=100, null=True, blank=True)
    occupation = models.CharField(max_length=80, null=True, blank=True)
    patientType = models.ForeignKey(
        'TypePatient', on_delete=models.DO_NOTHING, null=True, blank=True)
    patientStatus = models.CharField(
        max_length=100, choices=patientStatus, null=True, blank=True)
    bloodType = models.CharField(max_length=10, choices=bloodType)
    referBy = models.ForeignKey(
        'Referby', on_delete=models.DO_NOTHING, null=True, blank=True)
    referredDate = models.DateField(null=True, blank=True)
    religion = models.CharField(max_length=100, null=True, blank=True)
    parent_guardian = models.CharField(max_length=200, null=True, blank=True)
    # photo =
    phone = models.BigIntegerField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=80, null=True, blank=True)
    # For contact
    name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.BigIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    relationships = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.firstName + ' ' + self.lastName

# In patient listing start


class PrimaryDiagnosis(models.Model):
    patient = models.IntegerField(null=True)
    diagnosis = models.CharField(max_length=300)
    date = models.DateField()
    secondaryDiagnosis = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.diagnosis
    # Note if the secondary diagnosis is true than in new  place it should be listed.


class PatientAllergies(models.Model):
    patient = models.IntegerField(null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CurrentOperativePlan(models.Model):
    patient = models.IntegerField(null=True)
    Description = models.TextField(null=True, blank=True)
    procedure = models.CharField(max_length=100, null=True, blank=True)
    surgeon = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, choices=currentOperativePlan)
    caseComplexity = models.IntegerField(null=True, blank=True)
    instructionsUponAdmission = models.TextField(null=True, blank=True)
    additionalNotes = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        p = Patient.objects.get(id=self.patient.id)
        return '%s' % (p)
# In patient listing start


class PatientNotes(models.Model):
    patient = models.IntegerField(null=True)
    note = models.TextField()
    # Visit model relation
    visit = models.ForeignKey('PatientVisitType', on_delete=models.DO_NOTHING)
    onBehalfOf = models.ForeignKey(
        'Consultant', on_delete=models.DO_NOTHING, null=True, blank=True)  # Doctor relation
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        p = Patient.objects.get(id=self.patient.id)
        return '%s' % (p)


class PatientVisitType(models.Model):
    typeName = models.CharField(max_length=200)
    status = models.CharField(max_length=100, choices=status)

    def __str__(self):
        return self.typeName


class PatientSurgery(models.Model):
    date = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    patient = models.ForeignKey(
        'Patient', on_delete=models.DO_NOTHING, null=True, blank=True)
    allDay = models.BooleanField(null=True, blank=True)
    surgeryWith = models.ForeignKey(
        'Consultant', on_delete=models.DO_NOTHING, null=True, blank=True)  # Relation with doctor
    department = models.ForeignKey(
        'Department', on_delete=models.DO_NOTHING, null=True, blank=True)
    room_no = models.ManyToManyField('Room')
    location = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField()

    def __str__(self):
        return str(self.date)


class PatientAppointment(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.DO_NOTHING)
    startdate = models.DateField()
    # If the appointmentType is admission below
    dischargeDate = models.DateField(null=True, blank=True)
    startTime = models.TimeField(
        null=True, blank=True)  # If the type is followUp
    # If the type is follow up
    endTime = models.TimeField(null=True, blank=True)
    allDay = models.BooleanField(null=True, blank=True)
    appointment_type = models.ForeignKey(
        'PatientVisitType', on_delete=models.DO_NOTHING)
    department = models.ForeignKey(
        'Department', on_delete=models.DO_NOTHING, null=True, blank=True)
    rooms = models.ManyToManyField('Room')
    # The below field should be a relation with doctor and when the model is created this should be listed on that doctors page.
    appointmentWith = models.ForeignKey(
        'Consultant', on_delete=models.DO_NOTHING, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=50, choices=appointmentStatus)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.date) + '-' + self.appointment_type


class PatientVisit(models.Model):
    date = models.DateField()
    dischargeDate = models.DateField()  # If the visit type is admission
    location = models.CharField(max_length=200)
    # Relation with visitchoices
    # Patient will be auto selected if done from list of patients.
    patient = models.ForeignKey(
        'Patient', on_delete=models.DO_NOTHING)
    visitType = models.ForeignKey(
        'PatientVisitType', on_delete=models.DO_NOTHING)
    appointments = models.ManyToManyField(
        'PatientAppointment')  # appointments under the patient
    # If the visit type is admission
    ward = models.ForeignKey(
        'Ward', on_delete=models.DO_NOTHING, null=True, blank=True)
    # If the visit type is admission
    bed_no = models.ForeignKey(
        'Bed', on_delete=models.DO_NOTHING, null=True, blank=True)
    department = models.ForeignKey(
        'Department', on_delete=models.DO_NOTHING, null=True, blank=True)
    roomsToAttend = models.ManyToManyField('Room')
    # Relation with doctor model
    examiner = models.ForeignKey(
        'Consultant', on_delete=models.DO_NOTHING, null=True, blank=True)
    reasonForVisit = models.TextField()

    def __str__(self):
        return str(self.date) + '-' + self.visitType


# Followup registaration

class PatientReporting(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.DO_NOTHING)
    doctor_consultant = models.ForeignKey(
        'Consultant', on_delete=models.DO_NOTHING)
    surgery = models.ForeignKey(
        'PatientSurgery', on_delete=models.CASCADE, null=True)
    appointment = models.ForeignKey(
        'PatientAppointment', on_delete=models.CASCADE, null=True)
    visit = models.ForeignKey(
        'PatientVisit', on_delete=models.CASCADE, null=True)

    def __str__(self):
        p = Patient.objects.get(id=self.patient.id)
        return '%s' % (p)


class ReportFieldTitle(models.Model):
    fieldTitle = models.CharField(max_length=100)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.fieldTitle


class ReportField(models.Model):
    reportFieldTitleId = models.IntegerField()
    fieldName = models.CharField(max_length=100)
    description = models.TextField()
    patientReportId = models.IntegerField()

    def __str__(self):
        return self.fieldName

# Emergency registeration


class Emergency(models.Model):
    sentinelEvent = models.BooleanField(null=True, blank=True)
    dateOfIncident = models.DateTimeField()
    incidentReportedTo = models.CharField(
        max_length=200, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    incidentCausedBy = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, default='Reported')
    patientImpacted = models.ForeignKey('Patient', on_delete=models.CASCADE)
    incidentDescription = models.TextField(null=True, blank=True)
    to_department = models.ForeignKey(
        'Department', on_delete=models.DO_NOTHING, null=True, blank=True)
    to_room = models.ForeignKey(
        'Room', on_delete=models.DO_NOTHING, null=True, blank=True)
    transferredFrom = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.patientImpacted


class Bill(models.Model):
    # billNo =
    date = models.DateField(auto_now_add=True)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    visit = models.ForeignKey('PatientVisit', on_delete=models.DO_NOTHING)
    totalDiscount = models.IntegerField(default=0, null=True, blank=True)
    nationalInsurance = models.IntegerField(default=0, null=True, blank=True)
    hmo_com = models.IntegerField(default=0, null=True, blank=True)
    totalPayAmount = models.IntegerField(default=0, null=True)
    totalCharge = models.BigIntegerField(null=True, default=0)
    totalPayment = models.IntegerField(null=True, default=0)
    grandTotal = models.BigIntegerField(null=True, default=0)
    status = models.CharField(null=True, max_length=50, choices=bill_status)

    def __str__(self):
        p = Patient.objects.get(id=self.patient_id)
        return '%s' % (p)

    def save(self, *args, **kwargs):
        try:
            TotalPayment.objects.get(patient=self.patient.id)
        except ObjectDoesNotExist:
            c = TotalPayment(patient=self.patient.id)
            c.save()
        patientTotalPayment = TotalPayment.objects.get(
            patient=self.patient.id)
        amount = patientTotalPayment.amount
        prevAmount = int(amount)
        remCharge = int(self.totalCharge) - int(self.totalPayAmount)
        if remCharge <= 0:
            super(Bill, self).save(*args, **kwargs)
        else:
            totalAmount = prevAmount - remCharge
            patientTotalPayment.amount = totalAmount
            patientTotalPayment.save()
            super(Bill, self).save(*args, **kwargs)


class TotalCharge(models.Model):
    billId = models.IntegerField()
    amount = models.BigIntegerField(null=True, default=0)

    def __str__(self):
        return str(self.billId)


class Charge(models.Model):
    date = models.DateField(auto_now_add=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    patientId = models.IntegerField(null=True)
    itemName = models.CharField(max_length=200, default='ex')
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    billId = models.IntegerField(null=True, blank=True)
    totalCharge = models.BigIntegerField()

    def __str__(self):
        p = Patient.objects.get(id=self.patientId)
        return '%s' % (p)

    def save(self, *args, **kwargs):
        try:
            TotalCharge.objects.get(billId=self.billId)
        except ObjectDoesNotExist:
            c = TotalCharge(billId=self.billId)
            c.save()
        patientTotalCharge = TotalCharge.objects.get(
            billId=self.billId)
        prevAmount = int(patientTotalCharge.amount)
        newAmount = int(self.totalCharge)
        totalAmount = prevAmount + newAmount
        print(totalAmount)
        patientTotalCharge.amount = totalAmount
        patientTotalCharge.save()
        super(Charge, self).save(*args, **kwargs)


class TotalPayment(models.Model):
    patient = models.IntegerField()
    amount = models.IntegerField(null=True, default=0)

    def __str__(self):
        p = Patient.objects.get(id=self.patient)
        return '%s' % (p)


class Payment(models.Model):
    date = models.DateField(auto_now_add=True)
    patient = models.IntegerField(null=True)
    amount = models.IntegerField()
    method = models.CharField(
        max_length=50, choices=paymentMethod, default='Cash')
    notes = models.TextField(null=True, blank=True)
    paymentFor = models.CharField(
        max_length=50, choices=payment_for, default='Payment')
    bill = models.IntegerField(null=True)

    def __str__(self):
        return self.datePaid

    def save(self, *args, **kwargs):
        try:
            TotalPayment.objects.get(patient=self.patient)
        except ObjectDoesNotExist:
            c = TotalPayment(patient=self.patient)
            c.save()
        patientTotalPayment = TotalPayment.objects.get(
            patient=self.patient)
        print(patientTotalPayment.amount)
        prevAmount = int(patientTotalPayment.amount)
        newAmount = int(self.amount)
        totalAmount = prevAmount + newAmount
        print(totalAmount)
        patientTotalPayment.amount = totalAmount
        patientTotalPayment.save()
        super(Payment, self).save(*args, **kwargs)


class Revenue(models.Model):
    fiscalYear = models.ForeignKey(
        'FiscalYear', on_delete=models.CASCADE, null=True, blank=True)
    payments = models.ForeignKey(
        'Payment', on_delete=models.DO_NOTHING, null=True, blank=True)
    # sum of totalCharge of everyBill.
    totalRevenue = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.totalRevnue)


# Lab
samplStatus = [('Collect', 'Collect'), ('Collected',
                                        'Collected'), ('Report', 'Report')]


class Sample(models.Model):
    patientId = models.IntegerField()
    sampleSource = models.ForeignKey('Department', on_delete=models.DO_NOTHING)
    receivedDate = models.DateField(auto_now_add=True)
    requestersName = models.CharField(max_length=200)
    labReportNote = models.TextField(null=True)
    status = models.CharField(max_length=50, choices=samplStatus, default="Collect")

    def __str__(self):
        return self.patientId


class SampleType(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=status)

    def __str__(self):
        return self.name


class SampleTest(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    sampleType = models.ForeignKey('SampleType', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SampleTypeTest(models.Model):
    sampleTest = models.ForeignKey("SampleTest", on_delete=models.CASCADE)
    field = models.CharField(max_length=200, null=True)
    sampleType = models.ForeignKey("SampleType", on_delete=models.CASCADE)
    sampleId = models.IntegerField()

    def __str__(self):
        p = SampleTest.objects.get(id=self.sampleTest)
        return '%s' % (p)
