def nba_stat_grabber(search_term, c_or_s):
    import requests, bs4, sys

    search_term_list = search_term.lower().split()
    last_name = search_term_list[1]
    first_name = search_term_list[0]

    url = "https://www.basketball-reference.com/players/%s/%s01.html" % (last_name[0], last_name[0:5] + first_name[0:2])
    r = requests.get(url)
    html = r.text
    soup = bs4.BeautifulSoup(html, "html.parser")

    title = soup.find("title")
    title_list = title.text.split(" ")

    if first_name.lower() == title_list[0].lower() and last_name.lower() == title_list[1].lower():
        print("Player Found!")
    else:
        url = "https://www.basketball-reference.com/players/%s/%s02.html" % (last_name[0], last_name[0:5] + first_name[0:2])
        r = requests.get(url)
        html = r.text
        soup = bs4.BeautifulSoup(html, "html.parser")
        if r.status_code != 200:
            print("Player Not Found.")
            sys.exit()
        print("Player Found!")

    if r.status_code != 200:
        print("Request failed, Error Code: %d" % (r.status_code))
        print(url)

    html = r.text
    soup = bs4.BeautifulSoup(html, "html.parser")
    stat_loc = soup.find("div", class_="p1")

    # Season Statistics
    SGames = stat_loc.find_all("p")[0].text.strip()
    SPpg = stat_loc.find_all("p")[2].text.strip()
    SRpg = stat_loc.find_all("p")[4].text.strip()
    SApg = stat_loc.find_all("p")[6].text.strip()

    # Career Statistics
    CGames = stat_loc.find_all("p")[1].text.strip()
    CPpg = stat_loc.find_all("p")[3].text.strip()
    CRpg = stat_loc.find_all("p")[5].text.strip()
    CApg = stat_loc.find_all("p")[7].text.strip()

    if c_or_s == "c":
        print("%s career stats - Games: %s, PPG: %s, RPG: %s, APG: %s" % (search_term, CGames, CPpg, CRpg, CApg))
    else:
        print("%s 2020-2021 season stats - Games: %s, PPG: %s, RPG: %s, APG: %s" % (search_term, SGames, SPpg, SRpg, SApg))
    print(url)
    return

nba_stat_grabber("Carmelo Anthony", "c")