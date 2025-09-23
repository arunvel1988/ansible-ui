#!/usr/bin/env python3
from ansible.plugins.inventory import BaseInventoryPlugin
from ansible.errors import AnsibleError

class InventoryModule(BaseInventoryPlugin):

    NAME = "my_simple_plugin"

    def verify_file(self, path):
        # Only load files named my_dynamic_plugin.yml
        return path.endswith(('my_dynamic_plugin.yml',))

    def parse(self, inventory, loader, path, cache=True):
        super().parse(inventory, loader, path)
        
        # Add a host
        inventory.add_host('web1', group='webservers')
        inventory.add_host('db1', group='dbservers')
        
        # Add group variables
        inventory.set_variable('webservers', 'http_port', 80)
        inventory.set_variable('dbservers', 'db_port', 3306)
        
        # Add host variables
        inventory.set_variable('web1', 'ansible_host', '192.168.1.10')
        inventory.set_variable('db1', 'ansible_host', '192.168.1.20')
