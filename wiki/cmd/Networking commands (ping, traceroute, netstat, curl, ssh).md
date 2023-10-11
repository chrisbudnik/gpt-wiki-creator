# Networking commands on Mac Command Line

In this guide, we will explore a set of networking commands available on the command line interface (CLI) of a Mac. These commands are useful for troubleshooting network connectivity issues, analyzing network performance, and interacting with remote servers.

## Ping

Ping is a basic networking command used to test the reachability of a host and the round-trip time for packets sent from your machine to the target host. To use the `ping` command:

```shell
ping <host>
```

- `<host>`: The domain name or IP address of the target host.

The `ping` command sends small packets to the target host and waits for an ICMP echo reply. It prints statistics about the round-trip time and packet loss. Press `Ctrl + C` to stop the ping command.

## Traceroute

Traceroute is a command used to trace the route that packets take from your machine to a destination host. It displays a list of all the intermediate routers (hops) along the path. To use the `traceroute` command:

```shell
traceroute <host>
```

- `<host>`: The domain name or IP address of the destination host.

The `traceroute` command sends packets with increasing TTL (Time-to-Live) values and records the IP addresses of the routers that forward the packets. This helps identify network latency issues and routing problems.

## Netstat

Netstat is a versatile command that displays network connection information, routing tables, and network interface statistics. It provides insights into active network connections, listening ports, and network usage statistics. To use the `netstat` command:

```shell
netstat [options]
```

Some common options of the `netstat` command include:

- `-a`: Displays all active connections and the listening state of ports.
- `-r`: Prints the routing table.
- `-s`: Shows network statistics.
- `-n`: Displays IP addresses and port numbers in numerical format.

Refer to the manual (`man netstat`) for more advanced usage options.

## Curl

Curl is a command-line tool for making HTTP requests to servers. It can send GET, POST, PUT, and DELETE requests and display the response from the server. To use the `curl` command:

```shell
curl [options] <url>
```

Some commonly used options of the `curl` command include:

- `-i`: Displays the response headers along with the response body.
- `-X` <method>: Specifies the HTTP method (GET, POST, PUT, DELETE).
- `-d` <data>: Sends data as the request body.
- `-H` <header>: Adds a custom header to the request.

Refer to the manual (`man curl`) for more advanced usage and options.

## SSH

SSH (Secure Shell) is a cryptographic network protocol used for secure remote access and data transfer. It provides a secure method for connecting to remote servers and executing command-line operations. To establish an SSH connection:

```shell
ssh <username>@<hostname>
```

- `<username>`: Your username on the remote server.
- `<hostname>`: The domain name or IP address of the remote server.

The first time you connect to a remote server, you may be prompted to verify its authenticity by checking its fingerprint. Once authenticated, you can execute commands on the remote server as if you were physically using it.

## Conclusion

These networking commands are valuable tools for troubleshooting network issues, analyzing network performance, and interacting with remote servers. By understanding their usage and options, you can leverage the command line interface to effectively manage network connectivity on your Mac.