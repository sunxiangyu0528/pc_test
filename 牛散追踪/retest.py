import re

a = '{"CCL": 1.6185e-319, "JSJ": 3.776909537386438e131, "fLow": 98.13, "fHigh": 104, "fOpen": 98.95, "YClose": 100.01, "fClose": 99.06, "dVolume": 6102848, "fAmount": 618347912.89, "jclTime": 20220304150003000, "dwItemNum": 3810}'
b = re.match('"fClose": .*"dVolume', a, flags=0)
print(b)
