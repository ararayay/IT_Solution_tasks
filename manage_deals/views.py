from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
from integration_utils.bitrix24.functions.call_list_method import call_list_method
from django.conf import settings


@main_auth(on_start=True, set_cookie=True)
def home(request: HttpRequest) -> HttpResponse:
    app_settings = settings.APP_SETTINGS
    return render(request, 'home.html', locals())

@main_auth(on_cookies=True)
def last_deals(request: HttpRequest) -> HttpResponse:
    result = call_list_method(bx_token=request.bitrix_user_token,
                                  method='crm.deal.list',
                                  fields={'CLOSED': 'N',
                                          'DATE_CREATE': 'DESC'})
    last_deals = result[:10]
    return render(request, 'last_deals.html', {'last_deals': last_deals})