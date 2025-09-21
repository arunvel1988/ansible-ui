#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import requests
import time
import csv
import json
import os

def run_module():
    # Define arguments
    module_args = dict(
        urls=dict(type='list', required=True, elements='str'),
        keyword=dict(type='str', required=False, default=None),
        output_file=dict(type='str', required=True),
        output_format=dict(type='str', choices=['csv', 'json'], default='csv'),
        timeout=dict(type='int', required=False, default=5)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    urls = module.params['urls']
    keyword = module.params['keyword']
    output_file = module.params['output_file']
    output_format = module.params['output_format']
    timeout = module.params['timeout']

    results = []

    for url in urls:
        entry = {
            'url': url,
            'status_code': None,
            'response_time': None,
            'keyword_found': False,
            'error': None
        }
        try:
            start = time.time()
            response = requests.get(url, timeout=timeout)
            end = time.time()

            entry['status_code'] = response.status_code
            entry['response_time'] = round(end - start, 3)

            if keyword and keyword in response.text:
                entry['keyword_found'] = True

        except Exception as e:
            entry['error'] = str(e)

        results.append(entry)

    # Save results to file
    try:
        if output_format == 'csv':
            with open(output_file, 'w', newline='') as csvfile:
                fieldnames = ['url', 'status_code', 'response_time', 'keyword_found', 'error']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(results)
        else:  # json
            with open(output_file, 'w') as jsonfile:
                json.dump(results, jsonfile, indent=4)

    except Exception as e:
        module.fail_json(msg=f"Failed to write output file: {str(e)}")

    module.exit_json(changed=True, results=results, output_file=output_file)

def main():
    run_module()

if __name__ == '__main__':
    main()
