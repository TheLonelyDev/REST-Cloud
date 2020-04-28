import logging
import argparse

def main(args):
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    config = configuration()
    import libcloud.security
    libcloud.security.VERIFY_SSL_CERT = False
    api = LibcloudApi(config)
    api.build_controllers()
    api.start()


if '__main__' == __name__:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-d', '--debug', action='store_true')
    args = parser.parse_args()
    main(args)
