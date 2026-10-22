class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.emailToName = defaultdict(str) # email: name
        self.parents = defaultdict(str) # kid: parent

        # 1. union find
        #
        def find(email):
            if email not in self.parents:
                return email
            if self.parents[email] != email:
                self.parents[email] = find(self.parents[email])
            
            return self.parents[email]

        def union(email1, email2):
            root1 = find(email1)
            root2 = find(email2)

            if root1 != root2:
                self.parents[root1] = root2
                return False
            return True

        for i in range(len(accounts)):
            emailList = accounts[i][1:]
            for email in emailList:
                self.parents[email] = email

        # fill in emailToName and connect these emails together
        for i in range(len(accounts)):
            name = accounts[i][0]
            firstEmail = accounts[i][1]
            emailList = accounts[i][1:]
            for email in emailList:
                self.emailToName[email] = name 
                # print("firstEmail", firstEmail)
                # print("email", email)
                union(firstEmail, email)
        
        # print("self.emailToName", self.emailToName)
        print("self.parents", self.parents)

        consolidatedEmails = defaultdict(list) # parentEmail: [kidEmails]
        for email in self.parents.keys():
            root = find(email)
            consolidatedEmails[root].append(email)

        print("consolidatedEmails", consolidatedEmails)
        # fill in res 
        res = []
        for _, emails in consolidatedEmails.items():
            # print("test")
            name = self.emailToName[emails[0]]
            res.append([name]+ sorted(emails))

        return res
