import codecs
import re
def delete_html_tags(html_file, result_file='draft.html'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html_content = file.read()
    clean_text = re.sub(r'<[^>]+>', '', html_content)
    with codecs.open(result_file, 'w', 'utf-8') as output_file:
        output_file.write(clean_text)
delete_html_tags('draft.html', 'cleaned.txt')

print("Текст очищен и записан в 'cleaned.txt'.")
