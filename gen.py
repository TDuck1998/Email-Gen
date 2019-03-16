addr_list_lr = []
addr_list_sb = []
adding_names_lr = False
adding_names_sb = False

lr_sb = raw_input('LR or SB : ').lower()
if lr_sb == 'lr':
    adding_names_lr = True
elif lr_sb == 'sb':
    adding_names_sb = True
else:
    print('ERROR')

while adding_names_lr == True:
    first_name = raw_input('FIRST NAME : ').lower()
    last_name = raw_input('LAST NAME : ').lower()
    email_lr = first_name + '.' + last_name + '@laterooms.com'
    addr_list_lr.append(email_lr)
    if first_name == 'exit' or last_name == 'exit':
        write_file_lr = True
        if write_file_lr == True:
            lrf = open('addr_list_lr', 'w')
            for line in addr_list_lr:
                lrf.write(line)
                lrf.write('\n')
            adding_names_lr = False

while adding_names_sb == True:
    first_name = raw_input('FIRST NAME : ').lower()
    last_name = raw_input('LAST NAME : ').lower()
    email_sb = first_name + '.' + last_name + '@laterooms.com'
    addr_list_sb.append(email_sb)
    if first_name == 'exit' or last_name == 'exit':
        write_file_sb = True
        if write_file_sb == True:
            sbf = open('addr_list_sb', 'w')
            for line in addr_list_sb:
                sbf.write(line)
                sbf.write('\n')
            adding_names_sb = False
