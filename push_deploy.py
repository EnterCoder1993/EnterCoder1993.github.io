import os

def push_deploy(message):
    os.system('hexo clean && hexo generate && hexo deploy')
    os.system('git add .')
    cmd = 'git commit -m "' + message + '"'
    os.system(cmd)
    os.system('git push origin hexo')

def main():
    workpath = '/Users/entercoder/entercoder1993.github.io'
    os.chdir(workpath)
    message = input("commit message:")
    push_deploy(message)

if __name__ == '__main__':
    main()
