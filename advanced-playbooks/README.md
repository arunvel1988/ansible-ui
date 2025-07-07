# Apache Webserver Playbook

This Ansible playbook installs and configures Apache on all webservers defined in the inventory.

## Structure

- `playbook.yml`: Main playbook entry point
- `inventory/`: Inventory file (INI format)
- `group_vars/`: Group-level variables (for `webservers`)
- `roles/apache/`: Role for installing and configuring Apache
    - `tasks/`: Contains the main task list
    - `handlers/`: Contains service restart handler
    - `files/`: Static content like `index.html`
    - `templates/`: Jinja2 templates for configuration
    - `defaults/`: Default variables for the role

## Usage

```bash
ansible-playbook -i ./../inventory.ini playbook.yml
