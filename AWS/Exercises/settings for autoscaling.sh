# created security with http and ssh rules
# created loadbalancer together with target group
# do not add any instance to the target group
# auto scaling group using launch template and target group 
# within auto scaling group, setup simple policy for both decrease and increase grop size
# health check type is set to ELB
# simple policy for increasing the instance number, 
    # select cpu usage >= 50%, 
    # setup an alarm and sns notification,
    # add 1 instance
    # wait 30s
# simple policy for decreasign the instance number, 
    # select cpu usage <= 20%, 
    # setup an alarm and sns notification,
    # remove 1 instance
    # wait 30s
# monitored the instance and health checks and interpret how the health checks are affectign auto scaling group
# changed heath check type to EC2, and monitor
# edited auto scaling group configuration and changed minimum number of instances
# stressed currently running instances with commands below 
sudo amazon-linux-extras install epel -y
sudo yum install -y stress
uptime
stress --cpu 2 --timeout 300 &
watch uptime
# checked email for sns notifications
# checked the cloud-watch for alarm state
# monitored affect of our stress command which caused asg to add extra instances
# changed launched template with new version
# terminated all instances within dashboard
# monitored auto scaling group which launched new instances with new template version