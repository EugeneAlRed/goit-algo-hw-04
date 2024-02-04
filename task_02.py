def get_cats_info(path):
    """return a list of dictionaries with information about one cat

    Args:
        path (str): path to the text file

    Returns:
        list(dict): information about one cat
    """
    try:
        with open(path, 'r') as fh:
            list_cat_info = []
            dict_cat = {'id': '', 'name': '', 'age': ''}
            for line in fh:
                line = line.split(',')
                line[-1] = line[-1].strip()
                dict_cat = {'id': line[0], 'name': line[1], 'age': line[2]}
                line = dict_cat
                list_cat_info.append(line)
            return list_cat_info
    except FileNotFoundError:
        print(f'No such file or directory: {path}')


cats_info = get_cats_info("file.txt")
print(cats_info)
