import sys
import codecs 

STR = '▁'
TWO_STR = '▁▁'


def detokenization(line):
    if TWO_STR in line:
        line = line.strip().replace(' ', '').replace(TWO_STR, ' ').replace(STR, '').strip()
    else:
        line = line.strip().replace(' ', '').replace(STR, ' ').strip()

    return line


if __name__ == "__main__":
    # UTF8Reader = codecs.getreader(encoding='UTF-8')
    # sys.stdin = UTF8Reader(sys.stdin)

    for line in sys.stdin:
        if line.strip() != "":
            buf = []
            for token in line.strip().split('\t'):
                buf += [detokenization(token)]

            sys.stdout.write('\t'.join(buf) + '\n')
        else:
            sys.stdout.write('\n')

    # with open('review.sorted.uniq.refined.tok.bpe.tsv', 'r', encoding='utf-8') as f:

    #     for line in f:
    #         if line.strip() != "":
    #             buf = []
    #             for token in line.strip().split('\t'):
    #                 buf += [detokenization(token)]

    #             sys.stdout.write('\t'.join(buf) + '\n')
    #         else:
    #             sys.stdout.write('\n')
