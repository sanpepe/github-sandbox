import unittest
import datetime

from websand.tests.TestSetup import TestSetup
from websand.src.usecases.codecastSummaries.CodecastSummariesPresenter import CodecastSummariesPresenter
from websand.src.usecases.codecastSummaries.CodecastSummary import CodecastSummary
from websand.src.usecases.codecastSummaries.CodecastSummariesResponseModel import CodecastSummariesResponseModel


class CodecasstsSummariesPresenterUnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CodecasstsSummariesPresenterUnitTest, self).__init__(*args, **kwargs)

    def setUp(self):
        TestSetup.setupContext()
    
    def test_validateViewModel(self):
        respondModel = CodecastSummariesResponseModel()
        summary = CodecastSummary()
        summary.title = "Title"
        now_str = '10/3/2015'
        summary.publicationDate = datetime.datetime.strptime(now_str, '%m/%d/%Y')
        summary.permalink = "permalink"
        summary.isViewable = True
        summary.isDownloadable = False
        respondModel.addCodecastSummary(summary)

        presenter = CodecastSummariesPresenter()
        presenter.present(respondModel)
        viewModel = presenter.getViewModel()
        viewableSummary = viewModel.viewableCodecastSummaries[0]

        self.assertEqual(summary.title, viewableSummary.title)
        
