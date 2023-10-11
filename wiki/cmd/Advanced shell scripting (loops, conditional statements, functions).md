# Advanced Shell Scripting (Loops, Conditional Statements, Functions)

In this section, we will explore advanced shell scripting techniques such as loops, conditional statements, and functions. These powerful features allow us to write complex scripts to automate tasks and improve productivity on the command line.

## Loops

Loops in shell scripts provide a way to repeat a set of commands multiple times. There are two types of loops commonly used in shell scripting: `for` loops and `while` loops.

### For Loops

A `for` loop iterates over a specified list of items and executes a set of commands for each item in the list. Here is the basic syntax for a `for` loop:

```bash
for item in list
do
    # commands to be executed
done
```

Here's an example that prints the numbers from 1 to 5:

```bash
for i in {1..5}
do
    echo $i
done
```

### While Loops

A `while` loop executes a set of commands as long as a certain condition is true. The condition can be any command that returns a successful exit status (zero) for the loop to continue. Here is the basic syntax for a `while` loop:

```bash
while condition
do
    # commands to be executed
done
```

A common use case for a `while` loop is reading lines from a file. Here's an example that reads each line from a file:

```bash
while read line
do
    echo $line
done < input.txt
```

## Conditional Statements

Conditional statements allow us to make decisions in our scripts based on certain conditions. The most commonly used conditional statement in shell scripting is the `if` statement.

### If Statement

An `if` statement allows us to execute a block of commands if a certain condition is true. The basic syntax for an `if` statement is as follows:

```bash
if condition
then
    # commands to be executed if condition is true
fi
```

Here's an example that checks if a number is greater than 10:

```bash
if [ $number -gt 10 ]
then
    echo "Number is greater than 10"
fi
```

### If-Else Statement

An `if-else` statement extends the `if` statement by allowing us to execute a different set of commands if the condition is false. The basic syntax is as follows:

```bash
if condition
then
    # commands to be executed if condition is true
else
    # commands to be executed if condition is false
fi
```

Here's an example that checks if a number is even or odd:

```bash
if [ $((number % 2)) -eq 0 ]
then
    echo "Number is even"
else
    echo "Number is odd"
fi
```

## Functions

Functions in shell scripting allow us to define reusable blocks of code. They can be used to organize our scripts and make them more modular. Here is the basic syntax to define a function:

```bash
function_name() {
    # commands to be executed
}
```

Here's an example that defines a function to print a message:

```bash
print_message() {
    echo "Hello, world!"
}
```

To call a function, simply use its name followed by parentheses:

```bash
print_message
```

Functions can also accept arguments. Here's an example that multiplies two numbers:

```bash
multiply() {
    local result=$(( $1 * $2 ))
    echo $result
}

result=$(multiply 5 3)
echo $result
```

## Conclusion

In this section, we have explored advanced shell scripting concepts including loops, conditional statements, and functions. These features provide powerful automation capabilities on the command line and allow for more complex and modular scripts. Practice and experimentation will help you become proficient in leveraging these techniques to your advantage.