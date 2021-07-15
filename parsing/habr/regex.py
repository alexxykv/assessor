class RegexUser:
    NAME = r'<a .*? class="user-info__fullname user-info__fullname_medium" .*?>(.*?)</a>'
    NICKNAME = r'<a .*? class="user-info__nickname user-info__nickname_doggy".*?>(.*?)</a>'
    HUB_NAMES = r'<a .*? class="profile-section__user-hub ">(.*?)</a>'
    HUB_ALIAS = r'<a href=".*?/hub/(.*?)/" class="profile-section__user-hub ">.*?</a>'
    STATS = r'<div class="stacked-counter__value .*?">(.*?)</div>'
    SPECIALIZATION = r'<div class="user-info__specialization">(.*?)</div>'
    RANKED = r'<a href=".*" class="defination-list__link">(\d*).*?</a>'
    CITY = r'<a .*?city.*? class="defination-list__link".*?>(.*?)</a>'
    REGION = r'<a .*?region.*? class="defination-list__link".*?>(.*?)</a>'
    COUNTRY = r'<a .*?country.*? class="defination-list__link".*?>(.*?)</a>'
    DOB = r'<span.*?>[Дата рождения]{13}</span>\s*<span class="defination-list__value">(.*?)</span>'
    ACTIVITY = r'<span.*?>[Активность]{10}</span>\s*<span class="defination-list__value">(.*?)</span>'
    REGISTERED = r'<span.*?>[Зарегистрирован]{15}</span>\s*<span class="defination-list__value">(.*?)</span>'
    WORK_NAME = r'<a href="/company/.*?/" class="defination-list__link".*?>(.*?)</a>'
    WORK_ALIAS = r'<a href="/company/(.*?)/" class="defination-list__link".*?>.*?</a>'
    COMPANY_NAME = r'<a href=".*?/company/.*?/" class="list-snippet__title-link">(.*?)</a>'
    COMPANY_ALIAS = r'<a href=".*?/company/(.*?)/" class="list-snippet__title-link">.*?</a>'
    CONTRIB_ALIAS = r'<a href=".*?/hub/(.*?)/" class="media-obj media-obj_link">'
    CONTRIB_NAME = r'<span class="rating-info__title".*?>(.*?)</span>'
    CONTRIB_VALUE = r'<span class="rating-info__stat">(.*?)</span>'
    POST_ID = r'<a href=".*?/[postblog]{1,4}/(.*?)/" class="post__title_link">.*?</a>'
    POST_TYPE = r'<a href=".*?/([postblog]{1,4})/.*?/" class="post__title_link">.*?</a>'
    POST_TITLE = r'<a .*?class="post__title_link">(.*?)</a>'
    POST_VOITINGS = r'<span class="post-stats__result-counter.*?".*?>(.*?)</span>'
    POST_VIEWS = r'<span class="post-stats__views-count">(.*?)</span>'
    POST_FAVS_COUNT = r'<span class="bookmark__counter js-favs_count".*?>(.*?)</span>'
    POST_COMS_COUNT = r'<span .*?id="post-stats-comments-count".*?>(.*?)</span>'
    COM_ID = r'<a href=".*?#comment_(.*?)" class="icon_comment-anchor".*?>.*?</a>'
    COM_POST_ID = r'<a href=".*?/[postblog]{1,4}/(.*?)/#comment_.*?" class="icon_comment-anchor".*?>.*?</a>'
    COM_TIME = r'<time class="comment__date-time comment__date-time_published">(.*?)</time>'
    COM_VOITINGS = r'<span class="voting-wjt__counter.*?>(.*?)</span>'


class RegexPost:
    AUTHOR = r'<span class="user-info__nickname user-info__nickname_small">(.*)</span>'
    VOITINGS = r'<span class="voting-wjt__counter  voting-wjt__counter_positive  js-score".*>(.*)</span>'
    FAVS_COUNT = r'<span class="bookmark__counter js-favs_count" title=".*">(\d*)</span>'
    VIEWS = r'<span class="post-stats__views-count">(.*)</span>'
    COMMENTS_COUNT = r'<span class="comments-section__head-counter" id="comments_count">\s*(.*)\s*</span>'
    TAGS = r'<a href=".*" rel="tag" class="inline-list__item-link post__tag  ">(.*)</a>'
    HUBS = r'<a href="(.*)" class="inline-list__item-link hub-link " title=".*">(.*)</a>'
    COMMENTS = r'<a href="(.*)" class="icon_comment-anchor" title=".*">.*</a>'
    TIME = r'<span class="post__time" data-time_published=".*">(.*)</span>'


class RegexComment:
    ID = r'<a href=".*#comment_(.*)" class="icon_comment-anchor" title=".*">.*</a>'
    POST_ID = r'<a href=".*/[postblog]{4}/(.*)/#comment_.*" class="icon_comment-anchor" title=".*">.*</a>'
    TIME = r'<time class="comment__date-time comment__date-time_published">(.*)</time>'
    VOITINGS = r'<span class="voting-wjt__counter .*" title=".*">(.*)</span>'
    AUTHOR = r'<span class="user-info__nickname user-info__nickname_small user-info__nickname_comment">(.*)</span>'


class RegexHub:
    NAME = r'<h1 class="page-header__info-title">(.*)</h1>'
    RATING = r'<div class="page-header__stats-value">(.*)</div>'
    AUTHORS = r'<a href=".*/users/(.*)/" class="list-snippet__fullname">(.*)</a>&'
    CONTRIB_AUTHORS = r'<div class="stats__counter stats__counter_table-grid stats__counter_invest">(.*)</div>'
    COMPANIES = r'<a href=".*/company/(.*)/" class="list-snippet__title-link">\s*(.*)\s*</a>'
    POSTS = r'<a href=".*/([postblog]{4})/(.*)/" class="post__title_link">(.*)</a>'


class RegexCompany:
    NAME = r'<a href="/company/ruvds/" class="page-header__info-title">(.*)</a>'
    RATING = r'<div class="page-header__stats-value">(.*)</div>'
    FOUNDED = r'<span class="defination-list__value">(.*)</span>'
    SITE = r'class="defination-list__link" title="(.*)"'
    COUNT_EMPLOYES = r'<span class="defination-list__value">(.*)</span>'
    REGISTERED = r'<span class="defination-list__value">(.*)</span>'
    REPRESENTATIVE = r'<a title="ruvds" href=".*/users/.*">(.*)</a>'
    EMPLOYES_NICKNAME = r'<a href=".*" class="list-snippet__nickname">(.*)</a>'
    EMPLOYES_KARMA = r'<div class="stats__counter stats__counter_table-grid stats__counter_karma" title=".*">(.*)</div>'
    EMPLOYES_RATING = r'<div class="stats__counter stats__counter_table-grid stats__counter_rating" title=".*">(.*)</div>'
    SUBSCRIBER_NICKNAME = EMPLOYES_NICKNAME
    SUBSCRIBER_KARMA = EMPLOYES_KARMA
    SUBSCRIBER_RATING = EMPLOYES_RATING
    POSTS = r'<a href=".*/([postblog]{4})/(.*)/" class="post__title_link">(.*)</a>'
    
class RegexSearch:
    POSTS = r'<a href=".*/([postblog]{4})/(.*)/" class="post__title_link">(.*)</a>'
    HUBS = r'<a href="https://habr.com/ru/[hubcompany]{3,7}/(.*)/" class="list-snippet__title-link">'
    HUB_SUBS = r'<div class="stats__counter stats__counter_table-grid stats__counter_subscribers" title=".*">(.*)</div>'
    HUB_RATING = r'<div class="stats__counter stats__counter_table-grid stats__counter_rating" title=".*">(.*)</div>'
    USER_NAME = r'<a href=".*" class="list-snippet__fullname">(.*)</a>&'
    USER_NICKNAME = r'<a href=".*" class="list-snippet__nickname">(.*)</a>'
