#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        name=dict(type='str', required=True)   # input parameter
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Get the value passed from Ansible
    name = module.params['name']

    # Output result
    result = dict(
        changed=False,
        message=f"Hello {name}, this is a custom module!"
    )

    module.exit_json(**result)   # Exit with JSON output

def main():
    run_module()

if __name__ == '__main__':
    main()
