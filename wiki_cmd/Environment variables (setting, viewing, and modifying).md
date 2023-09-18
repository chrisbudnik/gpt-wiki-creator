# Environment Variables on Mac

In this guide, we will explore what environment variables are and how to set, view, and modify them on a Mac using the command line interface (CLI).

## What are Environment Variables?

Environment variables are dynamic values that can affect the behavior of processes and programs running on your computer. They provide a way to store and retrieve configuration settings or data that can be used by various applications and tools.

## Viewing Environment Variables

To view the current environment variables on your Mac, open a terminal and type the following command:

```bash
printenv
```

This will display a list of all the environment variables and their corresponding values.

## Setting Environment Variables

To set a new environment variable, you can use the `export` command followed by the variable name and its value. For example, to set a variable named `MY_VARIABLE` with the value `hello`, run the following command:

```bash
export MY_VARIABLE=hello
```

You can also set multiple variables at once by separating them with spaces:

```bash
export VAR1=value1 VAR2=value2 VAR3=value3
```

## Modifying Environment Variables

To modify the value of an existing environment variable, use the `export` command followed by the variable name and its new value. For example, to change the value of `MY_VARIABLE` to `world`, run the following command:

```bash
export MY_VARIABLE=world
```

If the variable does not exist, it will be created with the provided value.

## Persistent Environment Variables

By default, environment variables set using the `export` command are only available for the current shell session. If you want to make them persistent, you can add them to one of the shell initialization files, such as `.bash_profile` or `.zshrc`. These files are executed when a new shell session is started.

To add a new variable to your `bash` shell, open your `.bash_profile` file using a text editor and add the following line:

```bash
export MY_VARIABLE=value
```

Save the file and run the following command to apply the changes:

```bash
source ~/.bash_profile
```

For `zsh` shell, use `.zshrc` instead of `.bash_profile`:

```bash
export MY_VARIABLE=value
```

Save the file and run the following command to apply the changes:

```bash
source ~/.zshrc
```

## Removing Environment Variables

To remove an environment variable, use the `unset` command followed by the variable name. For example, to remove the `MY_VARIABLE` variable, run the following command:

```bash
unset MY_VARIABLE
```

## Conclusion

Environment variables are a powerful way to configure and customize your Mac's command line environment. By understanding how to set, view, modify, and remove them, you can enhance your productivity and tailor your system to your needs.

Remember to restart your terminal or reload the shell configuration files to apply any changes made to environment variables.