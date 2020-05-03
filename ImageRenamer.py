import os, sys, platform, time

rootPath = ''

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if len(sys.argv[1]) > 0:
            if os.path.exists(sys.argv[1]):
                rootPath = sys.argv[1]
                print('Searching in folder: ' + rootPath)
            else:
                print('The folder\n' + rootPath + '\n doesn\'t exist.')

    if len(rootPath) == 0:
        rootPath = os.path.abspath(os.getcwd())
        print('Searching in folder: ' + rootPath)

    for root, dirs, files in os.walk(rootPath):
        for f in files:
            (fileName, fileExt) = os.path.splitext(f)

            if fileExt.lower() in ['.jpg', '.jpeg', '.png']:
                srcPath = os.path.join(root, f)

                if platform.system() == 'Darwin': 
                    creationTime = os.stat(srcPath).st_birthtime

                if platform.system() == 'Windows': 
                    creationTime = os.stat(srcPath).st_ctime

                tgtPath = os.path.join(root, time.strftime('%Y%m%d_%H%M%S', time.gmtime(creationTime)) + fileExt)
                print('Renaming: ' + f + ' -> ' + os.path.basename(tgtPath))
                os.rename(srcPath, tgtPath)