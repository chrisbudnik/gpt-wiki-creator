# Introduction to Scripting

In this guide, we will explore the basics of scripting in the command line interface for Mac. Scripting allows us to automate and execute a series of commands, making our workflow more efficient. We will be focusing on writing and executing shell scripts, which are programs that run in the command line.

## What is a Script?

A script is a set of commands or instructions that can be executed by a computer. In the context of the command line interface, a script is a text file containing a sequence of commands that would otherwise need to be executed manually.

## Creating a Shell Script

To create a shell script, follow these steps:

1. Open a text editor such as TextEdit or Visual Studio Code.
2. Create a new file.
3. Save the file with a `.sh` extension, which indicates that it is a shell script.

## Writing Shell Scripts

Shell scripts can include various types of commands, such as:

### 1. Command Execution

To execute a command in a shell script, simply type the command followed by any required arguments or options. For example:

```shell
echo "Hello, World!"
```

### 2. Variables

Variables allow us to store and manipulate data in shell scripts. To declare a variable, use the following syntax:

```shell
variable_name="value"
```

For example:

```shell
name="John"
echo "Welcome, $name!"
```

### 3. User Input

To prompt the user for input in a shell script, use the `read` command. For example:

```shell
echo "What is your name?"
read name
echo "Hello, $name!"
```

### 4. Control Flow

Control flow statements help make decisions and repeat commands based on conditions. Some common control flow statements in shell scripts are:

- `if` statements: Execute a block of code based on a condition.
- `for` loops: Execute a block of code repeatedly for a specified number of times.
- `while` loops: Execute a block of code repeatedly as long as a condition is true.

### 5. Functions

Functions allow you to organize your code into reusable blocks. To define a function, use the following syntax:

```shell
function_name() {
    # Code to be executed
}
```

For example:

```shell
greet() {
    echo "Hello, $1!"
}

greet "John"
```

## Running Shell Scripts

To run a shell script, open the Terminal application and navigate to the directory where the script is saved. Use the `cd` command to change directories.

Once you are in the correct directory, run the script by typing `./script_name.sh`, where `script_name.sh` is the name of your script.

## Conclusion

Scripting is a powerful tool that allows us to automate tasks and improve our efficiency on the command line. By understanding the basics of writing and executing shell scripts, you can take your command line skills to the next level.

Happy scripting!