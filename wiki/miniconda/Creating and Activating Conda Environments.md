# Creating and Activating Conda Environments

In this guide, we will explore how to create and activate Conda environments on MacOS using miniconda. Conda environments allow you to create isolated and self-contained environments where you can install different versions of packages and libraries without affecting your system's global environment. This is especially useful when working on multiple projects that require different dependencies.

## Installing Miniconda

Before we begin creating Conda environments, let's first install miniconda on your MacOS. Miniconda is a lightweight version of Anaconda, which is a popular Python distribution.

1. Visit the [Miniconda download page](https://docs.conda.io/en/latest/miniconda.html) on your web browser.
2. Download the installer for macOS by clicking on the link and selecting the appropriate version for your operating system.
3. Once the installer is downloaded, double-click on it to open the installation wizard.
4. Follow the instructions provided by the wizard to complete the installation. Make sure to select "Just Me" when prompted to specify the installation type.

## Creating a Conda Environment

To create a new Conda environment, follow these steps:

1. Open a terminal on your Mac by launching the Terminal application. You can find it in the Applications/Utilities folder or by searching for "Terminal" using the Spotlight search.
2. In the terminal, type the following command to create a new environment named "myenv" with Python version 3.8:

   ```
   conda create --name myenv python=3.8
   ```

   Replace "myenv" with a name of your choice for your environment. You can also specify a different Python version if needed.

3. Press Enter to execute the command. Conda will fetch the necessary packages and create the environment for you.

## Activating a Conda Environment

Once you have created a Conda environment, you need to activate it to start using it. Follow these steps to activate the environment:

1. In the terminal, type the following command to activate the "myenv" environment:

   ```
   conda activate myenv
   ```

   Replace "myenv" with the name of your environment.

2. Press Enter to execute the command. You will notice that the prompt in the terminal changes to indicate that you are now inside the "myenv" environment.

## Deactivating a Conda Environment

Once you are done working in a Conda environment, you can deactivate it to return to the base environment. To deactivate the environment, follow these steps:

1. In the terminal, type the following command:

   ```
   conda deactivate
   ```

2. Press Enter to execute the command. The prompt in the terminal will revert to the base environment.

## Listing Conda Environments

You can view a list of all available Conda environments on your machine using the following command:

```
conda env list
```

This will display a table showing the names of the environments, their locations, and their respective Python versions.

## Conclusion

Creating and activating Conda environments allows you to manage different versions of packages and libraries for different projects. This helps ensure that your projects are isolated and do not interfere with each other. By following the steps outlined in this guide, you can easily create and activate Conda environments on your Mac using miniconda.