def env_prefix(hostname, env):
    """Add environment prefix to hostnames"""
    return f"{env}-{hostname}"

class FilterModule(object):
    def filters(self):
        return {
            'env_prefix': env_prefix
        }
