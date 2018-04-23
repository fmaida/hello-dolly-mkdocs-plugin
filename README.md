# Hello Dolly

"Hello Dolly" is a very basic [mkdocs plugin](http://www.mkdocs.org/user-guide/plugins/) 
that will try to teach you how to write a simple plugin for mkdocs, 
inspired by this [built-in plugin](https://wordpress.org/plugins/hello-dolly/) of WordPress.

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
Now, each time you'll write the tag `{{dolly}}` 
inside a page in your mkdocs document folder, 
this plugin will substitute that sentence with 
a random lyric taken from the main song of the 
musical "Hello Dolly".

For example, you could edit the `docs/index.md` 
file and insert the tag in any place, like this:

````markdown
# Welcome to MkDocs

For full documentation visit [mkdocs.org](http://mkdocs.org).

{{dolly}}

## Commands
````

The plugin will substitute your tag with:

<h1>Welcome to MkDocs</h1>

For full documentation visit [mkdocs.org](http://mkdocs.org).

« It's so nice to have you back where you belong »

<h2>Commands</h2>