#made by fluffy
#for free use
#24/1/2023

import requests

gif_api = 01234567890 #api key

def gif(srch):
    
    gif_l = requests.get(f"https://tenor.googleapis.com/v2/search?q={srch}&key={gif_api}&limit=1&random=true&media_filter=gif")
    gif_s_temp = gif_l.json()
    gif_s = gif_s_temp['results'][0]["url"]
    
    print(f"tennor api returned {gif_s} as gif url")
    return (gif_s)