import logging, sys, argparse


def str2bool(v):
    # copy from StackOverflow
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def get_entity(tag_seq, char_seq):
    COM=get_COM_entity(tag_seq,char_seq)
    return COM


def get_COM_entity(tag_seq, char_seq):
    length = len(char_seq)
    com=''
    COM = []
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-COM':
            if 'com' in locals().keys():
                COM.append(com)
                del com
            com = char
            if i+1 == length:
                COM.append(com)
        if tag == 'I-COM':
            com += char
            if i+1 == length:
                COM.append(com)
        if tag not in ['I-COM', 'B-COM']:
            if 'com' in locals().keys():
                COM.append(com)
                del com
            continue
    return COM

def get_logger(filename):
    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    handler = logging.FileHandler(filename)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
    logging.getLogger().addHandler(handler)
    return logger
