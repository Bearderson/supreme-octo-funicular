def data_snatcher(the_file, startstring, endstring):
    for line in the_file:
        if '<Name>' in line:
            get_start = re.search(r'(<Name>)', line)
            get_start = get_start.end()
            get_end = re.search(r'(</Name>)', line)
            get_end = get_end.start()
            print(line[get_start:get_end])