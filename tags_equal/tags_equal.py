
def tags_equal(tag1, tag2):
    tag1 = tag1[1:-1].lower().split()
    tag2 = tag2[1:-1].lower().split()

    for tag in tag1:
        if tag in tag2:
            pass
        else:
            return False
    return True


if __name__ == '__main__':
    tmp = tags_equal("<img src=cats.jpg height=90 height=40>", "<IMG SRC=Cats.JPG height=90>")
    if tmp == True:
        print('true')
