import bitly_api
from colors import Cl
from timer import W

BITLY_ACCESS_TOKEN = "#################################"
# LOGIN TO BITLY TO GET ACCESS TOKEN

x = bitly_api.Connection(access_token=BITLY_ACCESS_TOKEN)
u = input(Cl.cl("ENTER URL: ", Cl.G))
print(Cl.cl("SHORTENING URL!", Cl.W))
W.w()
print(Cl.cl("URL SHORTENED!", Cl.G))
r = x.shorten(u)
print(r)
