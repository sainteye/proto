app.service('errors', [ function(){
    var errors = {};
    errors.ERROR_GENERAL_NO_ERROR                  = 00000
    errors.ERROR_GENERAL_UNKNOWN_ERROR             = 10000
    errors.ERROR_GENERAL_BAD_SIGNATURE             = 10001
    errors.ERROR_GENERAL_NOT_FOUND                 = 10002
    errors.ERROR_GENERAL_USER_NOT_FOUND            = 10003
    errors.ERROR_GENERAL_BAD_TYPE                  = 10004
    errors.ERROR_GENERAL_TARGET_NOT_FOUND          = 10005
    errors.ERROR_GENERAL_BAD_ID_FORMAT             = 10006
    errors.ERROR_GENERAL_INVALID_OPERATION         = 10007
    errors.ERROR_GENERAL_BAD_PARA_FORMAT           = 10008
    errors.ERROR_AUTH_NOT_AUTHENTICATED            = 10100
    errors.ERROR_AUTH_BAD_CREDENTIALS              = 10101
    errors.ERROR_AUTH_NOT_AUTHORIZED               = 10102
    errors.ERROR_AUTH_PASSWORD_CONFIRM_NOT_MATCH   = 10103
    errors.ERROR_AUTH_NO_PASSWORD                  = 10104
    errors.ERROR_AUTH_PASSWORD_INVALID             = 10105
    errors.ERROR_AUTH_USER_ALREADY_LOGIN           = 10106
    errors.ERROR_AUTH_USER_ALREADY_ACTIVATED       = 10107
    errors.ERROR_AUTH_USER_CANNT_CHANGE_USERNAME   = 10108
    errors.ERROR_AUTH_USER_EMAIL_NOT_EXIST         = 10109
    errors.ERROR_AUTH_USER_NO_GROUP                = 10110
    errors.ERROR_AUTH_PASSWORD_CONFIRM_INVALID     = 10111
    errors.ERROR_AUTH_USERNAME_NOT_EXIST           = 10112
    errors.ERROR_USER_PASSWORD_NOT_MATCH           = 10200
    errors.ERROR_USER_FREIND_REQUEST_NOT_FOUND     = 10201
    errors.ERROR_USER_INVALID_FEEDBACK             = 10202
    errors.ERROR_REGISTRATION_INVALID_USERNAME     = 10300
    errors.ERROR_REGISTRATION_USERNAME_UNAVAILABLE = 10301
    errors.ERROR_REGISTRATION_EMAIL_USED           = 10302
    errors.ERROR_REGISTRATION_INVALID_EMAIL        = 10303
    errors.ERROR_REGISTRATION_NOT_ACTIVATE         = 10304
    errors.ERROR_REGISTRATION_INVALID_FULLNAME     = 10305
    errors.ERROR_REGISTRATION_NOT_REGIST_YET       = 10306
    errors.ERROR_REGISTRATION_PHONE_CODE_NOT_MATCH = 10307
    errors.ERROR_REGISTRATION_INVALID_ID           = 10308
    errors.ERROR_FACEBOOK_INVALID_TOKEN            = 10400
    errors.ERROR_FACEBOOK_BAD_CREDENTIALS          = 10401
    errors.ERROR_FACEBOOK_BAD_REQUEST              = 10402
    errors.ERROR_FACEBOOK_NO_PROFILE               = 10403
    errors.ERROR_FACEBOOK_INVALID_FACEBOOKID       = 10404
    errors.ERROR_PHOTOS_TOO_LARGE                  = 10500
    errors.ERROR_PHOTOS_BAD_FORMAT                 = 10501
    errors.ERROR_PHOTOS_NO_IMAGE                   = 10502
    errors.ERROR_PHOTOS_BROKEN_LINK                = 10503
    errors.ERROR_PHOTOS_BASE64_DECODE_FAILED       = 10504
    errors.ERROR_VIDEO_NO_VIDEO                    = 10600
    errors.ERROR_WEIBO_INVALID_TOKEN               = 10700
    errors.ERROR_FOLDER_REPLICA_NAME               = 10800
    errors.ERROR_FILE_REPLICA_NAME                 = 10801
    errors.ERROR_FILE_INVALID_FORMAT               = 10802
    errors.ERROR_FOLDER_CANNOT_BE_SHARED           = 10803
    errors.ERROR_FOLDER_NOT_FOUND                  = 10804
    errors.ERROR_FOLDER_CANNOT_BE_MOVED            = 10805
    errors.ERROR_FOLDER_EXCEED_QUOTA               = 10806
    errors.ERROR_FILE_NOT_FOUND                    = 10807
    errors.ERROR_FOLDER_INVALID_NAME               = 10808
    errors.ERROR_FILE_INVALID_NAME                 = 10809
    errors.ERROR_FOLDER_DESTINATION_NOT_ALLOWED    = 10810
    errors.ERROR_DROPBOX_PROFILE_NOT_FOUND         = 10900
    errors.ERROR_DROPBOX_NOT_AUTH                  = 10901
    errors.ERROR_DROPBOX_FILE_NOT_FOUND            = 10902
    errors.ERROR_DROPBOX_NO_UPDATE                 = 10903
    errors.ERROR_GROUP_NOT_BEEN_INVITED            = 11000
    errors.ERROR_GROUP_NOT_MEMBER                  = 11001
    errors.ERROR_GROUP_NOT_TEMPORARY               = 11002
    errors.ERROR_SHARE_NOT_FOUND                   = 11100
    errors.ERROR_SHARE_REPEAT_TWITTER_MSG          = 11101
    errors.ERROR_INVALID_SLUG                      = 11200
    errors.ERROR_INSTAGRAM_NO_PROFILE              = 11300
    errors.ERROR_MESSAGE_NOT_FOUND                 = 11400
    errors.ERROR_CARD_NOT_IN_BOOK                  = 11500
    errors.ERROR_EVENT_USER_NOT_INVITED            = 11600
    errors.ERROR_BLOG_EMPTY_TITLE                  = 10700
    errors.ERROR_BLOG_EMPTY_CONTENT                = 10701
    errors.ERROR_IOS_TOKEN_INVALID                 = 11701
    errors.ERROR_ANDROID_REGISTER_ID_INVALID       = 11702
    errors.ERROR_CHATROOM_NOT_EDITABLE             = 11800
    errors.ERROR_CHATROOM_NAME_TOO_LONG            = 11801
    errors.ERROR_LINK_INVALID_URL                  = 11901
    errors.ERROR_STICKER_DOES_NOT_EXIST            = 12000

    return errors;
}]);