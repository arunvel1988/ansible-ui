- name: Step 9 - Add Cron Job
  hosts: all
  become: true
  tasks:
    - name: Clear logs at midnight
      cron:
        name: "clear logs"
        minute: "0"
        hour: "0"
        job: "rm -f /tmp/*.log"
