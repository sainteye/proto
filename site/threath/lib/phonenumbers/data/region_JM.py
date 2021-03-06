"""Auto-generated file, do not edit by hand. JM metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_JM = PhoneMetadata(id='JM', country_code=1, international_prefix='011',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[589]\d{9}', possible_number_pattern=u'\d{7}(?:\d{3})?'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'876(?:(?:5[0-26]|6\d)\d{5}|(?:7(?:0[2-689]|[1-6]\d|8[056]|9[45])|9(?:0[1-8]|1[02378]|[2-8]\d|9[2-468]))\d{4})', possible_number_pattern=u'\d{7}(?:\d{3})?', example_number=u'8765123456'),
    mobile=PhoneNumberDesc(national_number_pattern=u'876(?:(?:2[178]|[348]\d|5[78])\d|7(?:0[07]|7\d|8[1-47-9]|9[0-36-9])|9(?:[01]9|9[0579]))\d{4}', possible_number_pattern=u'\d{10}', example_number=u'8762101234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'8(?:00|55|66|77|88)[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'8002123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'900[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'9002123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'5(?:00|33|44)[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'5002345678'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'1',
    national_prefix_for_parsing=u'1',
    leading_digits='876')
