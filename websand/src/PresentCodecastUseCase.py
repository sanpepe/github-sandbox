# Model or data objects contain application independent business rules
#   - Used for high level policy so it can be used independently of the application    
# Use case objects application dependent business rules

from websand.src.Context import Context

class PresentCodecastUseCase:
    
    def presentCodecasts(self, loggedInUser):
        presentable_codecast_list = []
        return presentable_codecast_list
    
    def isLicensedToViewCodecast(self, user, codecast):
        licenses = Context.gateway.findLicensesForUserAndCodecast(user=user, codecast=codecast)
        return not (len(licenses) == 0)