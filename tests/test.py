from bdshare import get_hist_data

df = get_hist_data('2020-03-01','2020-03-01','ACI') # get specific instrument data
print(df.to_string())