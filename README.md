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
To remove the development version do these steps in this order:

```
jupyter serverextension disable --py oh_notebook_importer
pip uninstall oh_notebook_importer
```

Now everything should be restored to the earlier settings!

## Demo
This extension now properly accepts notebooks from an external URL to be imported into a user's notebook directory. Following the
`Jupyter docs` it sets up a new handler at `/gallery-import`. This handler takes two URL encoded parameters:
- `notebook_location`, which can be any URL behind which there is a JSON encoded `.ipynb` file, and
- `notebook_name`, which describes the name the notebook have in the user's directory.

A valid URL would be `http://localhost:8888/gallery-import?notebook_location=http://127.0.0.1:5000/export-notebook/2/&notebook_name=mylittlenotebook.ipynb`. If `mylittlenotebook.ipynb` already exists in a user's directory the date/time of the import will be appended to make it unique. 
