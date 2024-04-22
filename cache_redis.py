from redis import StrictRedis
import requests
import time


cache = StrictRedis(
    host='localhost',
    port=6379,
    db=0,
    # decode_responses=True,
)


def get_file(url: str, filename: str) -> None:

    filedump = cache.get(url)

    if not filedump:
        print('Запрошенный файл отсутствует в кэше')
        r = requests.get(url)

        if r.status_code == 200:
            filedump = r.content

        cache.set(url, filedump)

    else:
        print('Запрошенный файл взят из кэша!')

    with open(filename, 'wb') as f:
        f.write(filedump)


if __name__ == '__main__':

    URL1 = 'http://rasfokus.ru/images/photos/medium/2eaa901080686f6045cfac0ca217daf2.jpg'
    URL2 = 'https://i.pinimg.com/originals/16/ac/c3/16acc399cc0703b14cd08cbb81ee47af.jpg'
    URL3 = 'https://suntango.ru/site_files/fileattach/1555d3aa11e0f7928a0110c435dddb1f60768632.jpg'

    url = URL2

    tm1 = time.time()
    get_file(url, url.split('/')[-1])
    tm2 = time.time()
    print(tm2 - tm1)
