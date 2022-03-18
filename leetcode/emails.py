class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = set()
        for email in emails:
            seperator = email.find('@')
            local = email[0:seperator]
            local = self.clean_local(local)
            unique_email = local + email[seperator:len(email)]
            unique_emails.add(unique_email)
        print(unique_email)
        return len(unique_emails)
    
    def clean_local(self, local):
        """
        :type local: str
        :rtype: str
        """
        cut = local.find('+')
        if cut != -1:
            local = local[0:cut]
        local = local.replace('.','')
        print(local)
        return local


emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
emails1 = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
s = Solution()
print(s.numUniqueEmails(emails1))