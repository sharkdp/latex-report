import sys
import re


regex = p = re.compile(u'\\\\(?:re)?newcommand\{\\\\([^\}]+)\}(\[[0-9]+\])?\{([^%]*)\}(?:\s*%.*|\s*)$')


def parse(filename):
    with open(filename) as f:
        for l in f:
            l = l.strip()

            res = regex.match(l)
            if res:
                command = res.group(1)
                gargs = res.group(2)
                replacement = res.group(3)

                nargs = 0
                if gargs:
                    rargs = re.match("\[([0-9]+)\]", res.group(2))
                    if rargs:
                        nargs = int(rargs.group(1))

                # escape backslashes
                replacement = replacement.replace('\\', '\\\\')

                # replace #1 by \1, #2 by \2, etc.
                replacement = re.sub(r'#([0-9])', '\\\\\\1', replacement)

                # create capturing groups for the arguments
                if nargs == 0:
                    # add positive lookahead to assure that this is not just part of a command
                    # we don't want \d to match on \delta
                    argRegex = '(?=[^a-zA-Z])'
                else:
                    # match {..} groups (nargs times) WITHOUT any inner {..} braces
                    argRegex = '\{([^{}%]*)\}' * nargs

                print(
                    's/\\\\{command}{argRegex}/{replacement}/g;'
                    .format(command=command, argRegex=argRegex, replacement=replacement)
                )

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: create-replacement-script.py commands.tex > replace.pl\n"
              "\n"
              "  This will create a perl script with the replacement commands.\n"
              "  Then, use the perl script on your tex file:\n"
              "  $ perl -pi replace.pl main.tex\n"
              "\n"
              "  NOTE:\n"
              "  - This will *modify* the tex file!\n"
              "  - Double-check the new output file by diffpdf or similar tools.\n"
              "  - It might be necessary to run the perl script multiple times.")
    else:
        filename = sys.argv[1]
        parse(filename)
