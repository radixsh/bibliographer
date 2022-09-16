import datetime
import os
import webbrowser

class Citation:
    def __init__(self, details):
        self.details = details
    def printMla(self):
        filename = 'mla.html'
        f = open(filename, 'w')
        html = '<html><head></head><body>'
        html += f'{self.details["Article author"]}. '
        html += f'"{self.details["Article title"]}." '
        html += f'<i>{self.details["Publisher"]}</i>, '
        html += f'{self.details["Date published"]}, '
        html += f'{self.details["URL"]}. '
        html += f'Accessed {self.details["Date accessed"]}. '
        html += '</body></html>'
        f.write(html)
        f.close()
        # https://stackoverflow.com/questions/40905703/how-to-open-an-html-file-in-the-browser-from-python
        webbrowser.open('file://' + os.path.realpath(filename), new=2)
    def printApa(self):
        filename = 'apa.html'
        f = open(filename, 'w')
        html = '<html><head></head><body>'
        html += f'{self.details["Article author"]}. '
        html += f'({self.details["Date published"]}). '
        html += f'<i>{self.details["Article title"]}.</i> '
        html += f'{self.details["Publisher"]}. '
        html += f'{self.details["URL"]}'
        html += '</body></html>'
        f.write(html)
        f.close()
        webbrowser.open('file://' + os.path.realpath(filename), new=2)

def validate_date(date, string):
    try:
        datetime.datetime.strptime(date, string)
        return date 
    except ValueError:
        print('Invalid date; you\'ll have to fix this by hand later.')
        return "DATE HERE"

def clean_url(url):
    if url == '':
        url = 'Invalid URL; you\'ll have to fix this by hand later.'
        return url
    url = url.replace('https://', '')
    url = url.replace('http://', '')
    if not url.startswith('www.'):
        url = f'www.{url}'
    # https://stackoverflow.com/questions/7053607/how-to-trim-characters-in-python
    url = url.rstrip('/')
    return url

def mla():
    details = {} # dictionary of strings, mapping categories to values

    author = input('Article author (Last, First M): ')
    details['Article author'] = author.title().strip()
    print(f'{details["Article author"]}\n')

    title = input('Article title: ')
    details['Article title'] = title.title().strip('". ')
    print(f'{details["Article title"]}\n')

    publisher = input('Publisher (e.g., The New York Times): ')
    details['Publisher'] = publisher.title().strip('". ')
    print(f'{details["Publisher"]}\n')

    date_published = input('Date published (e.g., 22 May 2007): ')
    mla_date_format = "%d %B %Y"
    details['Date published'] = validate_date(date_published, mla_date_format).strip()
    print(f'{details["Date published"]}\n')

    url = input('URL: ')
    details['URL'] = clean_url(url)
    print(f'{details["URL"]}\n')

    # https://www.w3schools.com/python/python_datetime.asp
    date_accessed = input('Date accessed (if empty, default is today): ')
    if not date_accessed:
        date_accessed = datetime.datetime.now().strftime(mla_date_format)
        details['Date accessed'] = date_accessed
    else:
        details['Date accessed'] = validate_date(date_accessed, mla_date_format) 
    print(f'{details["Date accessed"]}\n')

    mycitation = Citation(details)
    mycitation.printMla()

# https://owl.purdue.edu/owl/research_and_citation/apa_style/apa_formatting_and_style_guide/reference_list_electronic_sources.html
def apa():
    details = {} # dictionary of strings, mapping categories to values

    author = input('Article author (Last, F. M.): ')
    details['Article author'] = author.title().rstrip(' .');
    print(f'{details["Article author"]}\n')

    date_published = input('Date published (e.g., 2003, November 18): ')
    details['Date published'] = validate_date(date_published, "%Y, %B %d").strip()
    print(f'{details["Date published"]}\n')

    title = input('Article title: ')
    details['Article title'] = title.strip('". ')
    print(f'{details["Article title"]}\n')

    site_name = input('Site name (e.g., Medium): ')
    details['Publisher'] = site_name.title().strip('". ')
    print(f'{details["Publisher"]}\n')

    url = input('URL: ')
    details['URL'] = clean_url(url)
    print(f'{details["URL"]}\n')

    mycitation = Citation(details)
    mycitation.printApa();

if __name__ == "__main__":
    citation_type = input("Which citation type you want today? (mla, chicago, apa): ")
    if citation_type == "mla":
        mla()
    elif citation_type == "chicago":
        chicago()
    elif citation_type == "apa":
        apa()
    else:
        print("Unrecognized citation type :(")
