# https://leetcode.com/problems/accounts-merge/
#%%
#DFS solution 8% 34%
from collections import defaultdict
class Solution:

    def dfs(self,account_idx,accounts):
        if account_idx in self.visited:
            return []
        self.visited.append(account_idx)
        all_mails = []
        for mail in accounts[account_idx][1:]:
            all_mails.append(mail)
            accounts_for_this_mail = self.mail_accounts[mail]
            for account_i in accounts_for_this_mail:
                all_mails.extend(self.dfs(account_i,accounts))
        return all_mails

    def accountsMerge(self, accounts):
        self.visited = []
        #Map which accounts have each mail (building the graph)
        self.mail_accounts = defaultdict(list)
        for i,names_mails in enumerate(accounts):
            for mail in names_mails[1:]:
                self.mail_accounts[mail].append(i)
        # print(self.mail_accounts)
        out = []
        for i,names_mails in enumerate(accounts):
            if i not in self.visited:
                all_mails  = self.dfs(i,accounts)
                all_mails = sorted(list(set(all_mails)))
                out.append([names_mails[0],*all_mails])
            # print(i,names_mails,out)
        return out

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]]
#Output: [
# ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
# ["Mary","mary@mail.com"],
# ["John","johnnybravo@mail.com"]]
Solution().accountsMerge(accounts)

#%%



# accounts = [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],
#             ["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],
#             ["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],
#             ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],
#             ["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]
#output: [
# ["Alex","Alex0@m.co","Alex4@m.co","Alex5@m.co"],
# ["Ethan","Ethan0@m.co","Ethan3@m.co"],
# ["Gabe","Gabe0@m.co","Gabe2@m.co","Gabe3@m.co","Gabe4@m.co"],
# ["Kevin","Kevin2@m.co","Kevin4@m.co"]]
# Solution().accountsMerge(accounts)



# accounts = [["David","David0@m.co","David1@m.co"],
#             ["David","David3@m.co","David4@m.co"],
#             ["David","David4@m.co","David5@m.co"],
#             ["David","David2@m.co","David3@m.co"],
#             ["David","David1@m.co","David2@m.co"]]
#Expected [
# ["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]

