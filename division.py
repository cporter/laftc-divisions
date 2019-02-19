SCORES = 'http://ftcstats.org/california.html'
TEAMS_FILE = 'regionals_teams.txt'

def oprs():
    from bs4 import BeautifulSoup
    import requests
    soup = BeautifulSoup(requests.get(SCORES).text, 'html.parser')

    table = soup.find_all('table')[1]
    for row in table.find_all('tr'):
        cols = [x.get_text() for x in row.find_all('td')]
        if 18 > len(cols):
            continue
        team, name, opr, tourney = cols[1], cols[2], cols[4], cols[19]
        if 'ilt' in tourney.lower():
            yield team, name, float(opr)

def main():
    import os
    opr, name = {}, {}
    for team, n, o in oprs():
        opr[team] = o
        name[team] = n
    teams = [line.strip() for line in open(TEAMS_FILE)]
    for team in teams:
      if team not in opr:
        opr[team] = 0
        name[team] = 'Not Ready'
    for i, team in enumerate(sorted(teams, key = opr.get, reverse = True)):
        if 0 == i % 2:
            division = 'Galielo'
        else:
            division = 'Odyssey'
        if os.getenv('AUDIT'):
            print('%s\t%s\t%s\t%.2f' % (division, team, name[team], opr[team]))
        else:
            print('%s\t%s\t%s' % (division, team, name[team]))
        

if '__main__' == __name__:
    main()
