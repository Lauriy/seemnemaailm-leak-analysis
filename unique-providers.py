with open('seemnemaailm-leak.txt') as f:
    with open('unique-providers.txt', 'w') as out:
        dict = {}
        for line in f.readlines():
            email = line.split(',')[2]
            parts = email.split('@')
            if len(parts) == 2:
                dict.setdefault(parts[1].strip())
        dict = sorted(dict)
        for each in dict:
            out.write(each + '\n')
