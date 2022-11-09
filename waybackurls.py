from random import randint
import requests
import sys
import json


'''
=============================================================
Inspired by @mhmdiaa's  waybackurls.py script. Thanks to his 
brilliant idea (Mohammed Diaa).

This is the improved version, these features were added:

- fetching only the latest urls from the target domain (of year 2022)
- save the fetched urls (output) in the .txt file 
- removed unnessary codes, make it super fast

Still on building...

Author: maen08  
=============================================================
'''


def generate_filename(hostname):
    digits = 3
    id = ''.join(["{}".format(randint(0, digits)) for num in range(0, digits)])
    filename_ = hostname + '-' + 'file' + '-' + id

    return filename_


def waybackurls(host, with_subs):
    # url = f'http://index.commoncrawl.org//CC-MAIN-2022-40-index?url={host}/*&output=json'
    
    if with_subs:
        url = f'http://web.archive.org/cdx/search/cdx?url=*.{host}/*&output=json&fl=original&collapse=urlkey' 
        source_url_01 = f'http://index.commoncrawl.org/CC-MAIN-2018-22-index?url={host}/*&output=json'
    else:
        url = f'http://web.archive.org/cdx/search/cdx?url={host}/*&output=json&fl=original&collapse=urlkey'
        
    r = requests.get(url)
    results = r.json()

    return results[1:]


if __name__ == '__main__':
    argc = len(sys.argv)
    if argc < 2:
        print('========================= USAGE ============================')
        print('\npython3 waybackurls.py <url> <include_subdomains:optional>')
        print('\n')
        sys.exit()

    host = sys.argv[1]
    with_subs = False
    if argc > 3:
        with_subs = True

    urls = waybackurls(host, with_subs)
    
    filename = f'{generate_filename(host)}.txt'
    url_list = []
    for url in urls:
        str_url = ''.join(url)
        url_list.append(str_url)
        continue
        
    with open(filename, 'a') as f:
        for url in url_list:
            f.write(url)
            f.write('\n')
            continue
    
    print(f"\n[+] Output saved in {filename}")
            
   
