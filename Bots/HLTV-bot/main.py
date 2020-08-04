import requests
from bs4 import BeautifulSoup


def get_parsed_page(url):  # Получает сайт для парсинга
    headers = {
        "referer": "https://www.hltv.org/stats",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    return BeautifulSoup(requests.get(url, headers=headers).text, "lxml")


def top5teams():  # Парсит с сайта топ 5 команд
    home = get_parsed_page("http://hltv.org/")
    teams = []
    for team in home.find_all("div", {"class": ["col-box rank"], }):
        teamname = team.text[3:]
        teams.append(teamname)
    return teams


def top30teams():  # Парсит с сайта топ 30 команд
    page = get_parsed_page("http://www.hltv.org/ranking/teams/")
    teams = page.find("div", {"class": "ranking"})
    teamlist = []
    #rank = []
    for team in teams.find_all("div", {"class": "ranked-team standard-box"}):
        newteam = team.find(
            'div', {"class": "ranking-header"}).select('.name')[0].text.strip()
        teamlist.append(newteam)
    return teamlist


def get_matches():  # Парсит с сайта ближайшие матчи
    matches = get_parsed_page("http://www.hltv.org/matches/")
    matches_list = []
    upcomingmatches = matches.find("div", {"class": "upcoming-matches"})
    ("div", {"class": "match-day"})
    matchdays = upcomingmatches.find_all(
        "div", {"class": "match-day"}, limit=1)

    for match in matchdays:
        matchDetails = match.find_all("table", {"class": "table"})

        for getMatch in matchDetails:
            matchObj = {}

            #matchObj['date'] = match.find("span", {"class": "standard-headline"}).text.encode('utf8')

            if (getMatch.find_all("td", {"class": "team-cell"})):
                matchObj['1'] = getMatch.find_all("td", {"class": "team-cell"})[0].text.encode(
                    'utf8').lstrip().rstrip()
                matchObj['2'] = getMatch.find_all("td", {"class": "team-cell"})[1].text.encode(
                    'utf8').lstrip().rstrip()
            else:
                matchObj['team1'] = None
                matchObj['team2'] = None
            matchObj['time'] = getMatch.find(
                "td", {"class": "time"}).text.encode('utf8').lstrip().rstrip()
            matches_list.append(matchObj)

    return matches_list


if __name__ == "__main__":
    import pprint

    pp = pprint.PrettyPrinter()

    pp.pprint('top5')
    pp.pprint(top5teams())

    pp.pprint('top30')
    pp.pprint(top30teams())

    pp.pprint(get_matches())
