from notebook.utils import url_path_join
from notebook.base.handlers import IPythonHandler
from tornado import web
from .helper import import_notebook


def _jupyter_server_extension_paths():
    return [{
        "module": "oh_notebook_importer"
    }]


class HelloWorldHandler(IPythonHandler):
    @web.authenticated
    def get(self):
        notebook_location = self.get_argument('notebook_location')
        notebook_name = self.get_argument('notebook_name')
        target = self.get_argument('target', default=None)
        notebook_name = import_notebook(notebook_location, notebook_name)
        # self.finish('Imported notebook {}'.format(
        #    notebook_name))
        if target == 'voila':
            url = "{base}voila/voila/render/{nbname}".format(
                base=self.base_url,
                nbname=notebook_name
            )
        else:
            url = "{base}notebooks/{nbname}".format(
                        base=self.base_url,
                        nbname=notebook_name
            )
        print(url)
        self.redirect(url)
        # self.redirect(self.base_url)


def load_jupyter_server_extension(nb_server_app):
    """
    Called when the extension is loaded.

    Args:
        nb_server_app (NotebookWebApplication):
            handle to the Notebook webserver instance.
    """
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    route_pattern = url_path_join(web_app.settings['base_url'],
                                  '/notebook-import')
    web_app.add_handlers(host_pattern, [(route_pattern, HelloWorldHandler)])
