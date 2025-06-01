class Links:
    MAIN_LINK = 'https://stellarburgers.nomoreparties.site/'
    RECOVERY_PAGE_LINK = MAIN_LINK + 'forgot-password'
    LOGIN_PAGE_LINK = MAIN_LINK + 'login'
    ACCOUNT_PAGE_LINK = MAIN_LINK + 'account'
    ORDER_HISTORY_LINK = MAIN_LINK + 'account/order-history'
    ORDER_FEED_LINK = MAIN_LINK + 'feed'


class Endpoints:
    REGISTER_ENDPOINT = 'api/auth/register'
    USER_ENDPOINT = '/api/auth/user'
    ORDER_ENDPOINT = '/api/orders'
    INGREDIENTS_ENDPOINT = '/api/ingredients'
