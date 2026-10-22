class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        unique = set()
        for email in emails:
            plusSplit = email.split("+")
            local, domain = plusSplit[0], plusSplit[-1]
            domain = "@" +domain.split("@")[-1]
            # print(local)
            # print(domain)

            dotSplit = local.split(".")
            tmp = "".join(dotSplit) + domain
            unique.add(tmp)

        print(unique)
        return len(unique)
