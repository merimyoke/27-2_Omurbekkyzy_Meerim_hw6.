import re

while True:
    with open('MOCK_DATA.txt', 'r', encoding='UTF-8') as file:
        content = file.read()
        print("PRESS 1 FOR NAMES \nPRESS 2 FOR EMAILS\nPRESS 3 FOR FILES\nPRESS 4 FOR COLORS\nPRESS 5 TO EXIT")
        client = int(input('write a number from 1 to 5: '))
        fio_list = re.findall(r'^[a-zA-Z\-]+[\s a-zA-Z\'\-]\w+[\-\'A-Za-z ]', content)
        email_list = re.findall(r'[\w\.-]+@[\w\.-]+', content)
        file_list = re.findall(
            r'[\w\.-]*\.[\w\.-]*(?:ppt|png|xls|avi|jpeg|txt|mpeg|mp3|doc|mov|tiff|gif|pdf)', content)
        color_list = re.findall(r'\#[0-9a-f]{6}', content)

    def opening_new_files(list_name, name='list1'):
        with open(name, 'w', encoding='UTF=8') as file_name:
            file_name.write(str(list_name))
            print(list_name)
    if client == 1:
        opening_new_files(fio_list, name='names_list.txt')
    elif client == 2:
        opening_new_files(email_list, name='emails_list.txt')
    elif client == 3:
        opening_new_files(file_list, name='files_list.txt')
    elif client == 4:
        opening_new_files(color_list, name='color_list.txt')
    elif client == 5:
        print('the end')
        break




