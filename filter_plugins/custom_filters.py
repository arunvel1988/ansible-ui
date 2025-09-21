# This function will mask a password
def mask_password(value):
    """
    Take a string (password) and hide all characters except first and last
    Example: 'Secret123' -> 'S******3'
    """
    if not value:
        return ""
    if len(value) <= 2:
        return "*" * len(value)
    return value[0] + "*"*(len(value)-2) + value[-1]

# This class tells Ansible that we are creating a filter plugin
class FilterModule(object):
    def filters(self):
        # The key 'mask_password' is what we will use in the template
        return {
            'mask_password': mask_password
        }
