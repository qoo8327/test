import os
from datetime import datetime
log_dp = "/tmp/v5dnn/log/"
log_pipe="adder_cmd.log"
log_pipe = os.path.join(log_dp, log_pipe)
log_pipe = os.path.getmtime(log_pipe)

log_cmd="v5dnn_server_cmd.log"
log_cmd = os.path.join(log_dp, log_cmd)
log_cmd = os.path.getmtime(log_cmd)

print(log_pipe)
print(log_cmd)

print(abs(log_cmd-log_pipe))




'''d=datetime.strptime(last_line2, "%H:%M:%S")
d2=datetime.strptime(last_line1, "%H:%M:%S")
print("close_sever_log_time_print",(d-d2).total_seconds())
if (d-d2).total_seconds() > 300:
	print("test")
	#self._can_DaemonRun = False'''



