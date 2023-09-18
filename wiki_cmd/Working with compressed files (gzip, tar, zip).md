# Working with Compressed Files

In this guide, you will learn how to work with compressed files on macOS command line interface (CLI). We will explore three commonly used compression formats: gzip, tar, and zip. Compressed files are often used to reduce file sizes and make data transfer and storage more efficient.

## Gzip

The gzip command is used to compress and decompress files using the gzip compression format. Here are some useful commands:

### Compressing a File

To compress a file, use the following command:

```
gzip <file>
```

For example, to compress a file named "example.txt", run the command:

```
gzip example.txt
```

This will create a compressed file named "example.txt.gz". The original file will be replaced with the compressed version.

### Decompressing a File

To decompress a gzip file, use the following command:

```
gzip -d <file>.gz
```

For example, to decompress a file named "example.txt.gz", run the command:

```
gzip -d example.txt.gz
```

This will create a new file named "example.txt" in the current directory.

## Tar

The tar command is used to manipulate tar archives, which can contain multiple files and directories. Here are some useful commands:

### Creating a Tar Archive

To create a tar archive, use the following command:

```
tar -cf <archive>.tar <file1> <file2> ...
```

For example, to create a tar archive named "archive.tar" containing two files "file1.txt" and "file2.txt", run the command:

```
tar -cf archive.tar file1.txt file2.txt
```

This will create a tar archive named "archive.tar" in the current directory.

### Extracting Files from a Tar Archive

To extract files from a tar archive, use the following command:

```
tar -xf <archive>.tar
```

For example, to extract files from the "archive.tar" archive, run the command:

```
tar -xf archive.tar
```

This will extract all files from the archive into the current directory.

### Adding Files to an Existing Tar Archive

To add files to an existing tar archive, use the following command:

```
tar -rf <archive>.tar <file1> <file2> ...
```

For example, to add two files "file3.txt" and "file4.txt" to the "archive.tar" archive, run the command:

```
tar -rf archive.tar file3.txt file4.txt
```

This will add the specified files to the existing archive.

## Zip

The zip command is used to create, modify, and extract zip archives. Here are some useful commands:

### Creating a Zip Archive

To create a zip archive, use the following command:

```
zip <archive>.zip <file1> <file2> ...
```

For example, to create a zip archive named "archive.zip" containing two files "file1.txt" and "file2.txt", run the command:

```
zip archive.zip file1.txt file2.txt
```

This will create a zip archive named "archive.zip" in the current directory.

### Extracting Files from a Zip Archive

To extract files from a zip archive, use the following command:

```
unzip <archive>.zip
```

For example, to extract files from the "archive.zip" archive, run the command:

```
unzip archive.zip
```

This will extract all files from the archive into the current directory.

### Adding Files to an Existing Zip Archive

To add files to an existing zip archive, use the following command:

```
zip -r <archive>.zip <file1> <file2> ...
```

For example, to add two files "file3.txt" and "file4.txt" to the "archive.zip" archive, run the command:

```
zip -r archive.zip file3.txt file4.txt
```

This will add the specified files to the existing archive.

---

With the knowledge of gzip, tar, and zip commands, you can compress and decompress files, create and extract tar archives, and create and modify zip archives on macOS command line interface. These skills will improve your productivity and efficiency when working with compressed files.