import namecheck


def parser(data, current_node, file_append, output_links):

    lines = data.splitlines()
    first_line = 0

    for y in range(0, len(lines)):
        if "Local" in lines[y]:
            first_line = y
            break

    lengths = []
    final1 = []
    unique = []
    y = first_line + 1

    while y < len(lines):
        delimited_line = lines[y].split()
        final1 = delimited_line

        if len(final1) >= 5:
            if "." in final1[4]:
                final1[4] = final1[4][0:(final1[4].index("."))]

            final2 = final1[:1] + final1[-2:]
            final3 = current_node + "\t" + \
                final2[2].lower() + "\t" + final2[0] + "\t" + final2[1] + "\n"
        elif len(final1) < 5:
            y += 1
            continue

        if namecheck.namecheck(str(final2[2].lower())) is False:
            y += 1
            continue

        output_links.put(final3)

        if (final2[2].lower() != current_node.lower()) and (final2[2].lower() not in unique):
            unique.append(final2[2].lower())

        y += 1

    return unique
