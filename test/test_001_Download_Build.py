import pysftp
import paramiko
import glob
import os
import io
import unittest
import allure

class download(unittest.TestCase):


    def test_downloadn_build(self):

        from base64 import decodebytes
        # ...
        cnopts = pysftp.CnOpts(knownhosts='known_hosts')
        cnopts.hostkeys = None
        myHostname = "10.97.58.147"
        myUsername = "temp1"
        myPassword = "temp1"

        with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword, cnopts=cnopts) as sftp:
            print("Connection succesfully stablished ... ")

            sftp.cwd("/mnt/citadel/release/")
            # directory_structure = sftp.listdir_attr()
            # for attr in directory_structure:
            # print(attr.filename, attr)
            latest = 0
            latestfile = None

            for fileattr in sftp.listdir_attr():
                if fileattr.filename.startswith('MediaSuite-3') and fileattr.st_mtime > latest:
                    # latest = fileattr.st_mtime
                    latestfile = fileattr.filename

            if latestfile is not None:
                print('folder is', latestfile)
                localpath = 'D:\\Project\\Media suite\\releases'
                path = '/mnt/citadel/release/' + latestfile
                print('path is', path)
                # localFilePath = './latestfile'
                # file = open(latestfile)
                sftp.cwd('/mnt/citadel/release/' + latestfile)
                # path = '/mnt/citadel/release/'+latestfile
                for obj in sftp.listdir_attr():
                    print('open file:', obj)
                    # if 'pkg' in obj.filename:     #use this if need to download specific file
                    if obj.filename.startswith('MediaSuite-'):

                        requiredfile = obj.filename

                        print('Required file is', requiredfile)
                        sftp.get(path + '/' + requiredfile,
                                 'C:/release/latest' + '/' + requiredfile)
                    else:
                        print('File is not found')

                print('File has been downloaded')


    if __name__ == '__main__':
        unittest.main()

