# System Administration Tasks

In this section, we will explore various system administration tasks on a macOS command line interface. These tasks include user management, disk management, and service control.

## User Management

1. **Creating a User:** To create a new user, use the `sudo dscl . -create /Users/USERNAME` command, where `USERNAME` is the desired username. Then, set the user's password with `sudo passwd USERNAME`.

2. **Deleting a User:** To delete a user, use the following commands:
   - `sudo dscl . -delete /Users/USERNAME`: Deletes the user's record.
   - `sudo rm -rf /Users/USERNAME`: Deletes the user's home directory.
   - `sudo dscl . -delete /Groups/USERNAME`: Removes the user from any groups.

3. **Modifying User Attributes:** Use `sudo dscl . -create /Users/USERNAME ATTRIBUTE VALUE` to modify user attributes. For example:
   - `sudo dscl . -create /Users/john RealName "John Doe"`: Changes the user's real name to "John Doe".
   - `sudo dscl . -create /Users/jane UniqueID 501`: Changes the user's unique ID to 501.

4. **Granting Admin Privileges:** To grant admin privileges to a user, use `sudo dseditgroup -o edit -a USERNAME -t user admin`.

## Disk Management

1. **Viewing Disk Usage:** To check disk usage, use the `df` command. For detailed usage, add the `-h` flag: `df -h`.

2. **Creating Partitions:** The `diskutil` command is used for disk management tasks. To create a partition, use `sudo diskutil partitionDisk /dev/diskX GPT JHFS+ "My Partition" 50% ExFAT "Another Partition" 50%`. Replace `diskX` with the appropriate disk identifier.

3. **Mounting and Unmounting Volumes:** To mount a volume, use `sudo diskutil mount /dev/diskXsY`. To unmount, use `sudo diskutil unmount /dev/diskXsY`. Replace `diskXsY` with the appropriate volume identifier.

## Service Control

1. **Starting and Stopping Services:** Use the `sudo launchctl start SERVICE` command to start a service and `sudo launchctl stop SERVICE` to stop it. For example:
   - `sudo launchctl start com.mysql.mysql`: Starts the MySQL service.
   - `sudo launchctl stop com.mysql.mysql`: Stops the MySQL service.

2. **Enabling and Disabling Services:** To enable a service, use `sudo launchctl enable SERVICE`. To disable a service, use `sudo launchctl disable SERVICE`. For example:
   - `sudo launchctl enable sshd`: Enables the SSH service.
   - `sudo launchctl disable sshd`: Disables the SSH service.

---

With these commands and techniques, you can effectively perform various system administration tasks on macOS command line interface. Remember to exercise caution and double-check commands before executing them.