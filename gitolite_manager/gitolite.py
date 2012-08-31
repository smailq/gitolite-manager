import os, glob, tempfile, shutil


class Gitolite(object):
  
  def __init__(self, path='./gitolite-admin'):
    self._repo_path = path
    self._user_repo_config = path + "/conf/user_repos.conf"
    self._key_path = path + "/keydir/"


  def addRepo(self, username, reponame):
    """
    Adds a new repo to gitolite.
    returns true iff successfully added repo to config
    """

    repo_data = self.__load_repo()

    repo = username + '/' + reponame
    if repo in repo_data:
      return False

    repo_data[repo] = [( 'RW+', username )]

    self.__save_repo(repo_data)

    return True


  def rmRepo(self, username, reponame):
    """
    Removes a repo
    returns true iff successfully removed repo from config.
    """

    repo_data = self.__load_repo()

    repo = username + '/' + reponame
    
    if repo not in repo_data:
      return False

    del repo_data[repo]

    self.__save_repo(repo_data)

    return True

  def getRepos(self):
    return self.__load_repo()


  def addSSHKey(self, username, keyname, sshkey):

    key_file_name = self.__get_ssh_key_path(username, keyname)

    try:
      with open(key_file_name) as f:
        return False
    except IOError as e:
      pass

    new_key_file = open(key_file_name, 'w')
    new_key_file.write(sshkey)
    new_key_file.close()

    return True

  def rmSSHKey(self, username, keyname):

    key_file_name = self.__get_ssh_key_path(username, keyname)

    try:
      os.remove(key_file_name)
    except:
      return False

    return True

  def getSSHKeys(self):

    keys = glob.glob(self._key_path + '*@*.pub')

    key_data = {}

    for keyfile in keys:
      filename = os.path.basename(keyfile)[:-4]
      filename_split = filename.split('@',1)

      if len(filename_split) != 2:
        raise SyntaxError('Invalid key file name')

      username = filename_split[0].strip()
      keyname = filename_split[1].strip()

      if username not in key_data:
        key_data[username] = []

      key_data[username].append(keyname)

    return key_data

  def __get_ssh_key_path(self, username, keyname):
    return self._key_path + username + "@" + keyname + ".pub"

  def __load_repo(self):
    """
    Read gitolite config file
    """

    repo_data = {}

    #repo [username]/[reponame]
    # RW+ = [username]

    repo_file_content = open(self._user_repo_config, 'r')

    line = repo_file_content.readline().strip()
    repo = ''

    while line != '':

      if line.startswith('repo'):
        line_split = line.split(None, 1)
        if len(line_split) != 2:
          raise SyntaxError('Invalid repository def.')
        repo = line_split[1].strip()
      elif line.startswith(' '):
        if repo == '':
          raise SyntaxError('Missing repo def.')

        line_split = line.split('=', 1)
        if len(line_split) != 2:
          raise SyntaxError('Invalid rule')

        perm = line_split[0].strip()
        user = line_split[1].strip()

        if repo not in repo_data:
          repo_data[repo] = []

        repo_data[repo].append( ( perm, user) )
      else:
        raise SyntaxError('Invalid line')

      line = repo_file_content.readline()

    repo_file_content.close()
  
    return repo_data

  def __save_repo(self, repo_data):
    """
    Write gitolite config file
    """


    tmp_file = tempfile.NamedTemporaryFile('w')

    for reponame, permlist in repo_data.items():
      tmp_file.write('repo ' + reponame + '\n')
      for perm, user in permlist:
        tmp_file.write(" " + perm + " = " + user + '\n')

    tmp_file.flush()
    shutil.copyfile(tmp_file.name, self._user_repo_config)
    tmp_file.close()


