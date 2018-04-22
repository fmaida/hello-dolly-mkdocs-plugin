# Hello Dolly

"Hello Dolly" is a very basic [mkdocs plugin](http://www.mkdocs.org/user-guide/plugins/) 
that tries to teach how to write a plugin, 
inspired by the well-known plugin available in WordPress

## Usage

1. Execute `python setup.py develop` to install 
   the plugin on your local machine

2. In your mkdocs project, edit the `mkdocs.yml` file 
   and add these few lines:

   ```yaml
   plugins:
       - hello-dolly
   ```

That's it.
Now, each time you'll write the sentence "{{dolly}}" (without the quotes) 
this plugin will substitute that sentence with a random lyric taken from "Hello Dolly".