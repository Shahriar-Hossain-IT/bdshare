from ._version import __version__
__author__ = 'Raisul Islam'

"""
for trading data
"""
from bdshare.stock.trading import (get_current_trade_data, get_dsex_data, get_current_trading_code,
                                    get_hist_data, get_basic_hist_data,
                                    get_close_price_data, get_last_trade_price_data, get_cse_current_trade_data)


"""
for trading news
"""
from bdshare.stock.news import (get_agm_news, get_all_news)


"""
for market data
"""
from bdshare.stock.market import (get_market_inf, get_latest_pe, get_market_inf_more_data, get_market_depth_data)
