"""Auto-generated file, do not edit by hand. BO metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BO = PhoneMetadata(id='BO', country_code=591, international_prefix='00(1\d)?',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[23467]\d{7}', possible_number_pattern=u'\d{7,8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:2(?:2\d{2}|5(?:11|[258]\d|9[67])|6(?:12|2\d|9[34])|8(?:2[34]|39|62))|3(?:3\d{2}|4(?:6\d|8[24])|8(?:25|42|5[257]|86|9[25])|9(?:2\d|3[234]|4[248]|5[24]|6[2-6]|7\d))|4(?:4\d{2}|6(?:11|[24689]\d|72)))\d{4}', possible_number_pattern=u'\d{7,8}', example_number=u'22123456'),
    mobile=PhoneNumberDesc(national_number_pattern=u'[67]\d{7}', possible_number_pattern=u'\d{8}', example_number=u'71234567'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0(1\d)?',
    number_format=[NumberFormat(pattern='([234])(\d{7})', format=u'\\1 \\2', leading_digits_pattern=['[234]'], domestic_carrier_code_formatting_rule=u'0$CC \\1'),
        NumberFormat(pattern='([67]\d{7})', format=u'\\1', leading_digits_pattern=['[67]'], domestic_carrier_code_formatting_rule=u'0$CC \\1')])
