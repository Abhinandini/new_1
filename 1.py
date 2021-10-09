from git import Repo

#INITIALIZE A NEW REPOSITORY
new_repo = Repo.init('new')
'''print ("New repository was created")'''
#OPEN AN EXISTING LOCAL REPO
my_repo = Repo('new')
'''print ("Opened")'''
#CLONE A REMOTE REPOSITORY
clone = Repo.clone_from('https://github.com/Abhinandini/new_1', '/Users/abhi/Desktop/GitRepository_1')
# or clone via ssh (will use default keys)
#git.Repo.clone_from('git@github.cim:DevDungeon/Cookbook', 'Cookbook-ssh')
file_list = ["abcd.py"
]
repo = Repo('GitRepository_1')
if repo.is_dirty(untracked_files=True):
    print('Changes detected.')
#diff = repo.git.diff('HEAD~1')
'''diff = repo.git.diff(repo.head.commit.tree)
print(diff)'''
repo.index.add(file_list)
#repo.index.add(update=True)
repo.index.commit("Adding new file")
origin = repo.remote(name='origin')
origin.push()

#USEFUL LINKS
#https://www.devdungeon.com/content/working-git-repositories-python#toc-11
#http://www.legendu.net/misc/blog/hands-on-GitPython/
#https://stackoverflow.com/questions/38594717/how-do-i-push-new-files-to-github