'''
Created on Sep 19, 2011

@author: Geoff
'''
import os
import shutil


def removeDir(path):
    print 'Removing {0}'.format(path)
    shutil.rmtree(path)

def recurseDir(rootPath, item, action, depth=0, maxDepth = 0):
    dirs = [ d.lower() for d in os.listdir(rootPath) ]
    
    if item.lower() in dirs:
        path = os.path.join(rootPath, item)
        action(path)
        
    else:
        depth += 1
        if maxDepth:
            [ recurseDir(os.path.join(rootPath, d), item, action, depth, maxDepth) for d in dirs if depth <= maxDepth and not os.path.isfile(os.path.join(rootPath, d))]
        else:
            [ recurseDir(os.path.join(rootPath, d), item, action, depth, maxDepth) for d in dirs if not os.path.isfile(os.path.join(rootPath, d)) ]

if __name__ == '__main__':
    import sys
    import fnmatch
    import walklevel
    
    maxDepth = 1
    if len(sys.argv) == 2:
        maxDepth = int(sys.argv[1])
    
    for root, dirNames, filenames in walklevel.walklevel(".\\", level = 2):
        for dir in fnmatch.filter(dirNames, "bin"):
            removeDir(os.path.join(root, dir))
        for dir in fnmatch.filter(dirNames, "obj"):
            removeDir(os.path.join(root, dir))