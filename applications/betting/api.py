from fastapi import Depends

from applications.betting.schema import Betting
from applications.betting.service import BettingService
from .router import router

#获取用户的竞猜信息
@router.post('/bettings')
def add_bettings_api(body:Betting):
    return BettingService.add_bettings_server(body)

#用户的竞猜记录
@router.get('/betting_record')
def get_betting_record_api():
    return BettingService.get_betting_record_server()

#第三方获取竞猜结果
@router.get('/betting_result')
def get_betting_result_api():
    return BettingService.get_betting_result_server()

@router.get('/nanometer_odds')
def get_nanometer_odds_api():
    return BettingService.get_nanometer_odds_server()


@router.get('/time_betting')
def get_time_betting_api():
    return BettingService.get_time_betting_server()

#用户钱包
@router.get('user_wallet')
def get_user_wallet_api():
    return BettingService.get_user_wallet_server()


#入榜
@router.get('/entry_day')
def get_entry_day_api():
    return BettingService.get_entry_day_server()

@router.get('/entry_week')
def get_entry_week_api():
    return BettingService.get_entry_week_server()

@router.get('/entry_month')
def get_entry_momnth_api():
    return BettingService.get_entry_month_server()

#排行
@router.get('/ranking_day')
def get_ranking_day_api():
    return BettingService.get_ranking_day_server()

@router.get('/ranking_week')
def get_ranking_week_api():
    return BettingService.get_ranking_week_server()

@router.get('/ranking_month')
def get_ranking_month_api():
    return BettingService.get_ranking_month_server()