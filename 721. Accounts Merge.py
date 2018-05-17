"""
Draw an edge between two emails if they occur in the same account.
 The problem comes down to finding connected components of this graph.
"""
#1. DFS T: O(Sum [a_i log(a_i)  a_i = len(Accounts[i]) Build Graph and search for each component )
# class Solution(object):
#     def accountsMerge(self, accounts):
#         """
#         :type accounts: List[List[str]]
#         :rtype: List[List[str]]
#         """
#
#         import collections
#         email_account_graph = collections.defaultdict(list)
#         visited = [False] * len(accounts)
#         res =[]
#
#         # 1.create a graph <email,list(accounts)>
#         #Multiple accounts can have same name so mail is key,
#         #Two accounts definitely belong to the same person if there is some email that is common to both accounts.
#         for i,account in enumerate(accounts):
#             for mailid in account[1:]:
#                 email_account_graph[mailid].append(i)
#
#         #2. DFS
#         def DFS(account_id,emails):
#             if visited[account_id]:
#                 return
#             visited[account_id] = True
#
#             for mail in accounts[account_id][1:]:
#                 emails.add(mail)
#                 for id in email_account_graph[mail]: #call ids coresoponding to same mail
#                     DFS(id,emails)
#
#
#         for i,account in enumerate(accounts):
#             emails = set()
#             DFS(i,emails)
#             if emails:
#                 res.append([account[0]] + sorted(emails))
#         return res

#2.union find, Page Rank path compression
# class Solution(object):
#     def accountsMerge(self, accounts):
#
#         def find(a):
#             if ds[a] < 0: #-1 so it is the root
#                 return a
#             ds[a] = find(ds[a])
#             return ds[a]
#
#         def union(a, b):
#             a, b = find(a), find(b)
#             if a != b:#not in the same disjoint set,union them by rank
#                 if ds[a] < ds[b]:
#                     ds[a] += ds[b]
#                     ds[b] = a
#                 else:
#                     ds[b] += ds[a]
#                     ds[a] = b
#
#         c, ds, email_to_id, id_to_name = 0, [], {}, {}
#         for account in accounts:
#             for email in account[1:]:
#                 if email not in email_to_id:
#                     email_to_id[email] = c
#                     id_to_name[c] = account[0]
#                     ds.append(-1) #add as root
#                     c += 1
#                 union(email_to_id[account[1]], email_to_id[email])
#
#         res = {}
#         for email, id in email_to_id.items():
#             master = find(id)
#             res[master] = res.get(master, []) + [email]
#         return [[id_to_name[id]] + sorted(emails) for id, emails in res.items()]


#Union Find without PageRank
class DSU:#Disjoint Set Union
    def __init__(self):
        self.p = range(10001) #array for storing parent
    def find(self, x):
        if self.p[x] != x:#by default p[x] == x
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

class Solution(object):
    def accountsMerge(self, accounts):
        dsu = DSU()
        em_to_name = {}
        em_to_id = {}
        i = 0
        #draw edges between emails if they occur in the same account.
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = i
                    i += 1
                dsu.union(em_to_id[acc[1]], em_to_id[email])

        import collections
        ans = collections.defaultdict(list)
        for email in em_to_name:
            ans[dsu.find(em_to_id[email])].append(email)

        return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]

s = Solution()
print s.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])
