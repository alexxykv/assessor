class User:
    KURL = 'https://www.self.kaggle.com'

    def __init__(self, kaggle):
        self.kaggle = kaggle
        self.get_info = self.get_info()
        self.get_competitions = self.get_competitions()
        self.get_notebooks = self.get_notebooks()
        self.get_datasets = self.get_datasets()
        self.get_discussions = self.get_discussions()


    def get_info(self):
        info = dict(
            name=self.kaggle['displayName'],
            city=self.kaggle['city'],
            gitHubUserName= self.kaggle['gitHubUserName'],
            twitterUserName= self.kaggle['twitterUserName'],
            linkedInUrl=self.kaggle['linkedInUrl'],
            organization=self.kaggle['organization'],
            performanceTier=self.kaggle['performanceTier'],
            competitionsTier=self.kaggle['performanceTierCategory'],
            followers=self.kaggle['followers']['count'])
        return info

    def get_competitions(self):
        lenOfDict = len(self.kaggle['competitionsSummary']['highlights'])
        competitions = dict(
            compSummary=self.kaggle['competitionsSummary']['tier'],
            compTotalResults=self.kaggle['competitionsSummary']['totalResults'],
            compRankCurrent=self.kaggle['competitionsSummary']['rankCurrent'],
            compRankHighest=self.kaggle['competitionsSummary']['rankHighest'],
            compTotalGoldMedals=self.kaggle['competitionsSummary']['totalGoldMedals'],
            compTotalSilverMedals=self.kaggle['competitionsSummary']['totalSilverMedals'],
            compTotalBronzeMedals=self.kaggle['competitionsSummary']['totalBronzeMedals'],
            compHighlight1Title='' if lenOfDict == 0 else
            self.kaggle['competitionsSummary']['highlights'][0]['title'],
            compHighlightMedal='' if lenOfDict == 0 else
            self.kaggle['competitionsSummary']['highlights'][0]['medal'],
            compHighlight1Url='' if lenOfDict == 0 else
            User.KURL + self.kaggle['competitionsSummary']['highlights'][0]['url'],
            compHighlight2Title='' if lenOfDict < 2 else
            self.kaggle['competitionsSummary']['highlights'][1]['title'],
            compHighlight2Medal='' if lenOfDict < 2 else
            self.kaggle['competitionsSummary']['highlights'][1]['medal'],
            compHighlight2Url='' if lenOfDict < 2 else
            User.KURL + self.kaggle['competitionsSummary']['highlights'][1]['url'],
            compHighlight3Title='' if lenOfDict < 3 else
            self.kaggle['competitionsSummary']['highlights'][2]['title'],
            compHighlight3Medal='' if lenOfDict < 3 else
            self.kaggle['competitionsSummary']['highlights'][2]['medal'],
            compHighlight3Url='' if lenOfDict < 3 else
            User.KURL + self.kaggle['competitionsSummary']['highlights'][2]['url'])
        return competitions

    def get_datasets(self):
        lenOfDict = len(self.kaggle['datasetsSummary']['highlights'])
        datasets = dict(
            datasetsSummary=self.kaggle['datasetsSummary']['tier'],
            datasetsTotalResults=self.kaggle['datasetsSummary']['totalResults'],
            datasetsRankCurrent=self.kaggle['datasetsSummary']['rankCurrent'],
            datasetsRankHighest=self.kaggle['datasetsSummary']['rankHighest'],
            datasetsTotalGoldMedals=self.kaggle['datasetsSummary']['totalGoldMedals'],
            datasetsTotalSilverMedals=self.kaggle['datasetsSummary']['totalSilverMedals'],
            datasetsTotalBronzeMedals=self.kaggle['datasetsSummary']['totalBronzeMedals'],
            datasetsHighlight1Title='' if lenOfDict == 0 else
            self.kaggle['datasetsSummary']['highlights'][0]['title'],
            datasetsHighlightMedal='' if lenOfDict == 0 else
            self.kaggle['datasetsSummary']['highlights'][0]['medal'],
            datasetsHighlight1Url='' if lenOfDict == 0 else
            User.KURL + self.kaggle['datasetsSummary']['highlights'][0]['url'],
            datasetsHighlight2Title='' if lenOfDict <2 else
            self.kaggle['datasetsSummary']['highlights'][1]['title'],
            datasetsHighlight2Medal='' if lenOfDict <2 else
            self.kaggle['datasetsSummary']['highlights'][1]['medal'],
            datasetsHighlight2Url='' if lenOfDict <2 else
            User.KURL + self.kaggle['datasetsSummary']['highlights'][1]['url'],
            datasetsHighlight3Title='' if lenOfDict <3 else
            self.kaggle['datasetsSummary']['highlights'][2]['title'],
            datasetsHighlight3Medal='' if lenOfDict < 3 else
            self.kaggle['datasetsSummary']['highlights'][2]['medal'],
            datasetsHighlight3Url='' if lenOfDict < 3 else
            User.KURL + self.kaggle['datasetsSummary']['highlights'][2]['url'])
        return datasets

    def get_notebooks(self):
        lenOfDict = len(self.kaggle['scriptsSummary']['highlights'])
        notebooks = dict(
            scriptsSummary=self.kaggle['scriptsSummary']['tier'],
            scriptsTotalResults=self.kaggle['scriptsSummary']['totalResults'],
            scriptsRankCurrent=self.kaggle['scriptsSummary']['rankCurrent'],
            scriptsRankHighest=self.kaggle['scriptsSummary']['rankHighest'],
            scriptsTotalGoldMedals=self.kaggle['scriptsSummary']['totalGoldMedals'],
            scriptsTotalSilverMedals=self.kaggle['scriptsSummary']['totalSilverMedals'],
            scriptsTotalBronzeMedals=self.kaggle['scriptsSummary']['totalBronzeMedals'],
            scriptsHighlight1Title='' if lenOfDict == 0 else
            self.kaggle['scriptsSummary']['highlights'][0]['title'],
            scriptsHighlightMedal='' if lenOfDict == 0 else
            self.kaggle['scriptsSummary']['highlights'][0]['medal'],
            scriptsHighlight1Url='' if lenOfDict == 0 else
            User.KURL + self.kaggle['scriptsSummary']['highlights'][0]['url'],
            scriptsHighlight2Title='' if lenOfDict <2 else
            self.kaggle['scriptsSummary']['highlights'][1]['title'],
            scriptsHighlight2Medal='' if lenOfDict <2 else
            self.kaggle['scriptsSummary']['highlights'][1]['medal'],
            scriptsHighlight2Url='' if lenOfDict <2 else
            User.KURL + self.kaggle['scriptsSummary']['highlights'][1]['url'],
            scriptsHighlight3Title='' if lenOfDict < 3 else
            self.kaggle['scriptsSummary']['highlights'][2]['title'],
            scriptsHighlight3Medal='' if lenOfDict < 3 else
            self.kaggle['scriptsSummary']['highlights'][2]['medal'],
            scriptsHighlight3Url='' if lenOfDict < 3 else
            User.KURL + self.kaggle['scriptsSummary']['highlights'][2]['url'])
        return notebooks

    def get_discussions(self):
        lenOfDict = len(self.kaggle['discussionsSummary']['highlights'])
        discussion = dict(
            discussionsSummary=self.kaggle['discussionsSummary']['tier'],
            discussionsTotalResults=self.kaggle['discussionsSummary']['totalResults'],
            discussionsRankCurrent=self.kaggle['discussionsSummary']['rankCurrent'],
            discussionsRankHighest=self.kaggle['discussionsSummary']['rankHighest'],
            discussionsTotalGoldMedals=self.kaggle['discussionsSummary']['totalGoldMedals'],
            discussionsTotalSilverMedals=self.kaggle['discussionsSummary']['totalSilverMedals'],
            discussionsTotalBronzeMedals=self.kaggle['discussionsSummary']['totalBronzeMedals'],
            discussionsHighlight1Title='' if lenOfDict == 0 else
            self.kaggle['discussionsSummary']['highlights'][0]['title'],
            discussionsHighlightMedal='' if lenOfDict == 0 else
            self.kaggle['discussionsSummary']['highlights'][0]['medal'],
            discussionsHighlight1Url='' if lenOfDict == 0 else
            User.KURL + self.kaggle['discussionsSummary']['highlights'][0]['url'],
            discussionsHighlight2Title='' if lenOfDict <2 else
            self.kaggle['discussionsSummary']['highlights'][1]['title'],
            discussionsHighlight2Medal='' if lenOfDict <2 else
            self.kaggle['discussionsSummary']['highlights'][1]['medal'],
            discussionsHighlight2Url='' if lenOfDict <2 else
            User.KURL + self.kaggle['discussionsSummary']['highlights'][1]['url'],
            discussionsHighlight3Title='' if lenOfDict < 3 else
            self.kaggle['discussionsSummary']['highlights'][2]['title'],
            discussionsHighlight3Medal='' if lenOfDict < 3 else
            self.kaggle['discussionsSummary']['highlights'][2]['medal'],
            discussionsHighlight3Url='' if lenOfDict < 3 else
            User.KURL + self.kaggle['discussionsSummary']['highlights'][2]['url'])
        return discussion