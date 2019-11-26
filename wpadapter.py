import csv
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost


"""def create_csv():
- Dummy function

    file_number = 0
    with open('test%s.csv' % file_number, 'w+') as tester:
        writer = csv.writer(tester)
        writer.writerow(['test1234'])
        writer.writerow(['test124567'])"""


def reader():

    """ reads the csv file and returns title, content and categories to the main function """

    file_number = 0
    with open('test%s.csv' % file_number, 'r+', newline='') as parser:
        content = csv.reader(parser, delimiter=' ')
        for row in content:
            title = row
            content1 = row
            categories = row
            print(row)
        return title, content1, categories


def main(title, content1, categories):

    """Create a new Wordpress-Post based on the information given from reader()"""

    #create_csv()

    reader()

    wp = Client(('http://mysite.wordpress.com/xmlrpc.php', 'username', 'password'))
    post = WordPressPost()
    post.title = title
    post.content = content1
    post.post_status = 'publish'
    post.terms_names = {
        # 'post_tag': ['test', 'firstpost'],
        'category': categories
    }
    wp.call(NewPost(post))

    print(NewPost(post))
