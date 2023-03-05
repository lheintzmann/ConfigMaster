
import os

home_dir = os.path.expanduser('~')

config_dirs = ['/etc', '/etc/opt', '/etc/default',
               os.path.join(home_dir), os.path.join(home_dir, '.config')]

configExtensions = ['.conf', '.cfg', '.ini', '.json', '.yaml', '.yml']

config_files = []

filters = ['log', 'History', 'cache', 'temp', 'tmp', 'registry', 'journal',
           'backup', 'old', 'lang', 'font', 'locale', 'bug', 'UserFeedback',
           'crash', 'modules', 'workspaceStorage', 'manifest', 'metadata',
           'Extensions', 'globalStorage', 'lib', 'lib64', 'bin', 'doc', 'pkg', 'packages']

filters = [filter.lower() for filter in filters]


def getConfigFiles():
    for config_dir in config_dirs:
        for root, dirs, files in os.walk(config_dir):
            for file in files:
                try:
                    if file.endswith(tuple(configExtensions)):
                        if not any(filter in file.lower() for filter in filters) and not any(filter in root.lower() for filter in filters):
                            config_files.append(os.path.join(root, file))
                except:
                    pass

    return config_files
