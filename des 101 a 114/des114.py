import urllib
import urllib.request

url = "https://www.youtube.com"
print('- ' * 25)
try:
    acesso = urllib.request.urlopen(url)
except:
    print(f'\033[1;31m  O Site está indisponível: \033[m {url}')
else:
    print(f'\033[1;32m  O Site esta disponível: \033[m {url}')
print('- ' * 25)
