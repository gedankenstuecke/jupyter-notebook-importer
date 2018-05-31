# jupyter-notebook-importer

Work in Progress. The goal is to push a notebook from our Notebook Gallery right
into a user's notebook folder.

## Development
To install on your own Jupyter Notebook setup to test:

```
git clone https://github.com/gedankenstuecke/jupyter-notebook-importer.git
cd jupyter-notebook-importer
pip install -e .
jupyter serverextension enable --py oh_notebook_importer
```

Now you can run `jupyter notebook` as usual and you're good to go.

## Demo
Right now this extension basically doesn't do anything at all. It follows the
`Jupyter docs` in setting up a new handler at `/hello`, so if you head your browser
to `localhost:8888/hello?foo=bar` it will show the hello world and also display
the `request.arguments` on the shell. 
