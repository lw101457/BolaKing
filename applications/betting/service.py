import datetime

from applications.betting.schema import Betting
from common.clients import clients
from model import t_betting_record


class BettingService:
    @staticmethod
    def add_bettings_server(body:Betting):
        with clients.mysql_db.connect() as conn:
            betting_time = datetime.datetime.now()
            user_id = conn.execute(
                t_betting_record.insert().values(betting_money= body.betting_money,)

            )




    @staticmethod
    def get_betting_record_server():
        pass

    @staticmethod
    def get_betting_result_server():
        pass

    @staticmethod
    def get_nanometer_odds_server():
        pass

    @staticmethod
    def get_time_betting_server():

        pass
    @staticmethod
    def get_user_wallet_server():
        pass

    @staticmethod
    def get_entry_day_server():
        pass

    @staticmethod
    def get_entry_week_server():
        pass

    @staticmethod
    def get_entry_month_server():
        pass

    @staticmethod
    def get_ranking_day_server():
        pass

    @staticmethod
    def get_ranking_week_server():

        pass
    @staticmethod
    def get_ranking_month_server():
        pass