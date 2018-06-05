# jupyter-notebook-importer

This `jupyter serverextension` adds a new request handler to the notebook server itself to automate the import from notebooks from 3rd party websites. The new handler can be found at `/notebook-import` and takes two parameters:

- `notebook_location`, which can be any URL behind which there is a JSON encoded `.ipynb` file, and
- `notebook_name`, which describes the name the notebook have in the user's directory.

A valid URL would be `http://localhost:8888/notebook-import?notebook_location=http://127.0.0.1:5000/export-notebook/2/&notebook_name=mylittlenotebook.ipynb`. If `mylittlenotebook.ipynb` already exists in a user's directory the date/time of the import will be appended to make it unique.

## Install & Development
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
