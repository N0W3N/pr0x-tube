import csv
import os

"""csv_m is a dummy module (for now) to manipulate our created csv-files, filles and replaces it with our settings/information.
In the first step the csv file will be opened with the csv reader to retrieve all needed information - such as title, content, categories and so on - and stores it in seperate variables.
After that it replaces whitespaces and other unnecessary information in the file, when it finally creates an iframe object with the help of the uploader module.
If the dummy module got all the new information and all the new content, it creates an additionally csv file - as copy of the original file - filled/replaced with small changes.
"""

#TODO: give the variables better names

file_number = 1
while os.path.exists('test%s.csv' % file_number):
    file_number += 1
    with open('test%s.csv' % file_number, "r", newline='') as r:
        print("Opening index: ", file_number)
        reader = csv.reader(r, delimiter=' ', )
        rows = list(reader)
        title = str(''.join(rows[0]))
        content = str(''.join(rows[1]))
        category = str(''.join(rows[2]))
        cat = category.replace('.', '').replace('  ', ', ')
        con = content.replace('\n', '').replace('Watch:GOUNLIMITEDMIXDROPVIDEOBINVIDLOX', '')
        test = str(''.join(rows[3]))
        import uploader
        newfile = f"""<iframe src="https://gounlimited.to/embed-{uploader.gounlimited()}.html" scrolling="no" frameborder="0" width="100%" height="100%"
               allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"></iframe>

               <iframe width="560" height="315" src="//mixdrop.co/e/{uploader.mixdrop()}" frameborder="0" allowfullscreen></iframe>"""
        print(newfile)
        with open('test_%s.csv' % file_number, 'a+', newline='') as c:
            url_writer = csv.writer(c, delimiter=' ')
            url_writer.writerow([title])
            url_writer.writerow([con])
            url_writer.writerow([cat])
            url_writer.writerow([newfile])



