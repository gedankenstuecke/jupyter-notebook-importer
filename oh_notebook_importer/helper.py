import requests
import os
import arrow


def import_notebook(notebook_url, notebook_name):
    notebook_content = requests.get(notebook_url).content
    if os.path.isfile(notebook_name):
        notebook_name = notebook_name.replace('.ipynb',
                                              '-{}.ipynb'.format(
                                                arrow.now().format(
                                                'YYYY-MM-DD-HH:mm:ss'
                                                )))
    with open(notebook_name,'wb') as f:
        f.write(notebook_content)
    return notebook_name
