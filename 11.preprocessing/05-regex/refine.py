# python refine.py refine.regex.txt 1 < review.sorted.uniq.tsv > review.sorted.uniq.refined.tsv

# \t[,.\-=|;]+$로 추가 정제

import sys
import re

def read_regex(fn):
    regexs = []

    f = open(fn, 'r', encoding='utf-8')

    for line in f:
        if not line.startswith("#"):
            tokens = line.split('\t')

            if len(tokens) == 1:
                tokens += [' ']

            tokens[0] = tokens[0][:-1] if tokens[0].endswith('\n') else tokens[0]
            tokens[1] = tokens[1][:-1] if tokens[1].endswith('\n') else tokens[1]

            regexs += [(tokens[0], tokens[1])]

    f.close()

    return regexs

if __name__ == "__main__":
    fn = sys.argv[1]  # refine.regex.txt
    target_index = int(sys.argv[2]) # 1

    regexs = read_regex(fn)

    for line in sys.stdin: # review.sorted.uniq.tsv
        if line.strip() != "":
            columns = line.strip().split('\t')
            if len(columns) != 2:
                continue

            for r in regexs:
                columns[target_index] = re.sub(r'%s' % r[0], r[1], columns[target_index].strip())

            sys.stdout.write('\t'.join(columns) + "\n")
        else:
            sys.stdout.write('\n')
