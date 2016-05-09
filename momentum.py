from datetime import datetime,timedelta
import numpy as np
def initialize(context):  
    set_universe(universe.DollarVolumeUniverse(  
        floor_percentile=98, ceiling_percentile=100))  
    # set_do_not_order_list(security_lists.leveraged_etf_list)  
    schedule_function(daily_handle_data,  
                      date_rules.every_day(),  
                      time_rules.market_open(minutes=5))

def handle_data(context, data):  
    #return the handeld data
    return

def daily_handle_data(context, data):  
    # Fetch history, evaluate percent change, slice out the values' row  
    best_performer = history(256, '1d', 'price').pct_change(251).iloc[-1].idxmax()
    # This is running every day, 5 minutes after US market open  
    order_target_percent(best_performer, 0)  
