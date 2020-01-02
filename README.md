Author: Mohammed Almodaeah
Date 1/1/2020
version: v 1.0 pre-alpha

Description:
This library provides basic interaction with ESXI through SSH. It allows powering on and shutting down VMs as well as shutting down ESXI itself. It also allows executing any command on ESXI

Tested on free version of ESXI 6.7

Note: The code will not work if one of your VMs has a description that contains multiple lines of text or if its name has spaces. Please delete all VMs descriptions and remove any whitespace characters from vm names before you start using this library. The reason is that ESXI returns VMs information in a tabular form where columns and rows are separated by whitespace and new line characters and I'm using the laziest way to parse the table :). Maybe you can enhance it. I'm not in a mood for writing regular expressions right now :). See the __get_all_vms() function.

See test.py to learn how to use the library
