# Hello Dolly

"Hello Dolly" is a very basic 
[mkdocs plugin](http://www.mkdocs.org/user-guide/plugins/) that searches in 
all your mkdocs documents the tag `{{dolly}}` and substitutes it with a 
random lyrics taken from "Hello Dolly!", the main song of the musical 
of the same name.

It was inspired by the once [built-in plugin](https://wordpress.org/plugins/hello-dolly/) 
of WordPress, and it's main purpose is to help understanding how to write a simple plugin 
for *mkdocs*.
 


## Quick start

If you want to try this plugin as-it-is, follow these steps:

1. Download this repo and (eventually) unzip it in a folder

2. Inside the project folder, execute the command 
   `python setup.py develop` to install 
   the plugin on your local machine. 

3. Go to your mkdocs project folder, edit the `mkdocs.yml` file 
   and add these few lines at the end:

   ```yaml
   plugins:
       - hello-dolly
   ```

That's it.
Now, each time you'll write the tag `{{dolly}}` 
inside any page in your mkdocs document folder, 
this plugin will substitute that tag with 
a random lyric taken from the main song of the 
musical "Hello Dolly".

### An example

For example, you could edit the `docs/index.md` 
file and insert the tag in any place, like this:

````markdown
# Welcome to MkDocs

For full documentation visit [mkdocs.org](http://mkdocs.org).

{{dolly}}

## Commands
````