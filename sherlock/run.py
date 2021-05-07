from sherlock.sherlock import sherlock
from sherlock.notify import QueryNotify, QueryStatus
from sherlock.sites import SitesInformation


def search(username):
    sites = SitesInformation('sherlock/resources/data.json')
    site_data = {}
    for site in sites:
        site_data[site.name] = site.information

    query_notify = QueryNotify()

    response = sherlock(username, site_data, query_notify)

    results = {}
    for website_name in response:
        dictionary = response[website_name]
        if dictionary['status'].status == QueryStatus.CLAIMED:
            results[website_name] = dictionary['url_user']
    
    return results
