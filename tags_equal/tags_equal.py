def list_dic(tag1):
    rtn = {}
    for tag in tag1:
        test = tag.split('=')
        if len(test) > 1:
            rtn[test[0]] = test[1]
        else:
            rtn[test[0]] = ''

    return rtn

def old_parse_tag(html_tag):
    items = html_tag[1:-1].lower().split()
    name = items[0]
    attrs = sorted(items[1:])
    return name, attrs

def parse_tag(html_tag):
    items = html_tag[1:-1].lower().split()
    attributes = [
        attr.split('=')
        for attr in reversed(items[1:])
    ]
    return items[0], dict(attributes)

def tags_equal(tag1, tag2):
    name1, attrs1 = parse_tag(tag1)
    name2, attrs2 = parse_tag(tag2)

    return name1 == name2 and attrs1 == attrs2


if __name__ == '__main__':
    tmp = tags_equal("<img src=cats.jpg height=90 height=40>", "<IMG SRC=Cats.JPG height=90>")
    if tmp == True:
        print('true')
