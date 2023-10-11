# Redirection and Pipes

**Redirection** is a powerful feature of the command line interface (CLI) that allows you to control where the input and output of a command or program goes. By redirecting the input or output, you can manipulate and combine data, making your command line tasks more efficient and flexible.

**Pipes**, on the other hand, allow you to connect two or more commands together, using the output of one command as the input of another. This enables you to build complex and performant command line workflows.

In this guide, we will explore the concepts of redirection and pipes, and how they can be used to enhance your command line experience on a Mac.

## Redirection

### Output Redirection

When you run a command on the CLI, the output is typically displayed on the terminal screen. However, you can redirect this output to a file instead using the `>` operator.

For example, to redirect the output of the `ls` command to a file called `filelist.txt`, you can use the following command:

```
ls > filelist.txt
```

This will create a file `filelist.txt` in the current directory, containing the list of files and directories.

If the file already exists, the command will overwrite its contents. If you want to append the output to an existing file instead, use the `>>` operator:

```
ls >> filelist.txt
```

### Input Redirection

Similarly, you can redirect the input of a command from a file instead of typing it in manually. This can be useful when you have a large amount of data to process.

To redirect the input of a command from a file, you can use the `<` operator. For example, to sort the contents of a file called `data.txt`, you can use the following command:

```
sort < data.txt
```

This will sort the contents of `data.txt` and display the result on the terminal screen.

## Pipes

Pipes allow you to connect multiple commands together, by using the output of one command as the input of another. This enables you to perform complex operations and manipulate data efficiently.

To use a pipe, you can use the `|` operator. For example, to list all the files in a directory and search for a specific file in the result, you can use the following command:

```
ls | grep myfile
```

This command will list all the files in the current directory and pass the result to the `grep` command, which will search for the string `myfile` in the list.

You can chain multiple commands together using pipes. For example, to list all the files in a directory, sort them, and display the result, you can use the following command:

```
ls | sort | less
```

This command will list all the files in the current directory, sort them alphabetically, and display the result in a pager called `less`.

## Conclusion

Redirection and pipes are powerful features of the command line interface that allow you to control the input and output of commands, and connect multiple commands together. By leveraging these features, you can build complex workflows and automate repetitive tasks on your Mac. Experiment with different commands and explore the possibilities to make the most out of your command line experience.