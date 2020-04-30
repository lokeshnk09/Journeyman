import os
import sys


def make_at(path, dir_name):

    try:
        os.chdir(path)
        os.mkdir(dir_name)

    except (OSError, FileExistsError) as e:
        print("OS Error: {}".format(str(e)), file=sys.stderr)

    finally:
        return os.getcwd()


if __name__ == '__main__':
    make_at("/home/nirvaan/PycharmProjects/Journeyman/Exceptions/", 'test_folder')
    print('Current working directory! {}'.format(os.getcwd()))




