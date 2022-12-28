class CodecastDetails:
    class CodecastDetailsNotFound:
        def __init__(self):
            self.isViewable = False
            self.isDownloadable = False
            self.title = "No Found Title"
            self.publicationDate = "No publication date"
            self.permalink = "None"
            self.duration = 0
            self.author = "No Author"

    def __init__(self):
        self.isViewable = False
        self.isDownloadable = False
        self.title = None
        self.publicationDate = None
        self.permalink = None
        self.duration = None
        self.author = None