# Working with Text Files

In this guide, we will explore the command line interface (CLI) tools available on macOS for working with text files. We will cover various operations such as viewing, editing, searching, and manipulating text files using command line commands.

## Viewing Text Files

To view the contents of a text file on the command line, you can use the `cat` command. Here's an example:

```bash
cat filename.txt
```

The `cat` command displays the entire content of the file `filename.txt` in the terminal.

## Editing Text Files

To edit a text file using the command line, we can use a variety of text editors. Here are two popular options:

### nano

Nano is a simple text editor that comes pre-installed on macOS. To open a file for editing with nano, use the following command:

```bash
nano filename.txt
```

Once opened, you can make changes to the file. Press `Ctrl + X` to exit nano, and you will be prompted to save the changes.

### vim

Vim is a powerful text editor that provides advanced editing features. To open a file for editing with vim, use the following command:

```bash
vim filename.txt
```

Vim has different modes for navigation and editing. Press `i` to enter insert mode and make changes. To save the changes and exit, press `Esc` to exit insert mode, then type `:wq` and hit Enter.

## Searching Text Files

To search for specific text within a file, you can use the `grep` command. Here's an example:

```bash
grep "search term" filename.txt
```

The `grep` command searches for lines containing the specified "search term" in the file `filename.txt` and displays them in the terminal.

## Manipulating Text Files

The command line provides several powerful commands for manipulating text files. Here are a few examples:

### Sort

The `sort` command can be used to sort the lines of a text file alphabetically. Here's an example:

```bash
sort filename.txt
```

The `sort` command will display the sorted lines in the terminal.

### Cut

The `cut` command can be used to extract specific columns or fields from a text file. Here's an example:

```bash
cut -d, -f2 filename.txt
```

The `cut` command above extracts the second field (column) from a comma-separated file and displays it in the terminal.

### Sed

The `sed` command is a powerful text stream editor that can perform various text transformations. Here's an example:

```bash
sed 's/old_text/new_text/g' filename.txt
```

The `sed` command replaces all occurrences of 'old_text' with 'new_text' in the file `filename.txt` and displays the result in the terminal.

## Conclusion

In this guide, we have explored various command line tools for working with text files on macOS. You now have the knowledge to view, edit, search, and manipulate text files using the command line interface effectively.

Remember, practice is key to becoming proficient with these tools. Experiment with different commands and options to become more comfortable with working with text files on the command line.