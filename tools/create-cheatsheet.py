import sys
import re


STD_ARGS = ["x", "y", "z"]
NEWCOMMAND_REGEX = '\\\\(?:re)?newcommand\{\\\\([^\}]+)\}(\[[0-9]+\])?[^%]*(%%!? ?.*)?$'


def render(filename):
    print("\\newcommand{\\lrDirectory}{..}")
    print("\\newcommand{\\lrTitle}{Custom \\TeX~commands}")
    print("\\newcommand{\\lrAuthor}{David Peter}")
    print("\\input{../include/header.tex}")
    print("\\toggletrue{lrHideToc}")
    print("\\toggletrue{lrHideTitle}")
    print("\\usepackage{longtable}")
    print("\\usepackage[left=2cm,right=2cm]{geometry}")
    print("\\definecolor{command}{HTML}{0F61BF}")

    print("\\begin{document}")
    print("\\renewcommand*{\\arraystretch}{1.4}")
    print("\\begin{longtable}[l]{p{6.5cm}p{2cm}l}")

    nrsection = 1
    with open(filename) as f:
        for l in f.readlines():
            l = l.strip()

            res = re.match('^%%% (.*)$', l)
            if res:
                section = res.group(1)
                if nrsection > 1:
                    print("\\multicolumn{3}{l}{} \\\\")
                print("\\multicolumn{3}{l}{{\\large \\textsf{$\\triangleright$ " +
                      section + "}}\\vspace{2mm}} \\\\")
                nrsection += 1
            else:
                res = re.match(NEWCOMMAND_REGEX, l)
                if res:
                    command = res.group(1)
                    gargs = res.group(2)
                    doc = res.group(3)

                    args = ""
                    dargs = ""
                    if gargs:
                        rargs = re.match("\[([0-9]+)\]", res.group(2))
                        if rargs:
                            nargs = int(rargs.group(1))
                            if nargs <= 3:
                                args = "\\verb+{..}+" * nargs
                            else:
                                args = "\\verb+(" + str(nargs) + " arguments)+"
                            dargs = "".join(list(map(lambda s: "{" + s + "}", STD_ARGS[:nargs])))

                    output = "$\\" + command + dargs + "$"
                    if doc is None:
                        doc = ""
                    else:
                        if doc.startswith('%%!'):
                            args = "\\verb+(" + str(nargs) + " arguments)+"
                            doc = doc[3:].strip()
                            output = None
                        else:
                            doc = doc[2:]

                    if output is None:
                        print(
                            "{{\\color{{command}}\\verb+\\{command}+}}{args} & "
                            "\\multicolumn{{2}}{{l}}{{"
                            "{doc}"
                            "}} \\\\"
                            .format(command=command, args=args, doc=doc)
                        )
                    else:
                        print(
                            "{{\\color{{command}}\\verb+\\{command}+}}{args} & "
                            "{output} & "
                            "{doc} "
                            " \\\\"
                            .format(command=command, args=args, doc=doc, output=output)
                        )

    print("\\end{longtable}")
    print("\\end{document}")


if __name__ == "__main__":
    filename = sys.argv[1]
    render(filename)
