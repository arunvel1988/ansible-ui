#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import requests
import time

def run_module():
    # Define arguments
    module_args = dict(
        url=dict(type='str', required=True),
        keyword=dict(type='str', required=False, default=None),
        timeout=dict(type='int', required=False, default=5)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    url = module.params['url']
    keyword = module.params['keyword']
    timeout = module.params['timeout']

    result = dict(
        changed=False,
        url=url,
        status_code=None,
        response_time=None,
        keyword_found=False,
        msg=""
    )

    try:
        start = time.time()
        response = requests.get(url, timeout=timeout)
        end = time.time()

        result['status_code'] = response.status_code
        result['response_time'] = round(end - start, 3)

        if keyword:
            if keyword in response.text:
                result['keyword_found'] = True
                result['msg'] = f"Keyword '{keyword}' found on {url}"
            else:
                result['msg'] = f"Keyword '{keyword}' not found on {url}"
        else:
            result['msg'] = f"Website {url} returned status {response.status_code}"

        module.exit_json(**result)

    except Exception as e:
        module.fail_json(msg=f"Failed to reach {url}: {str(e)}")

def main():
    run_module()

if __name__ == '__main__':
    main()
