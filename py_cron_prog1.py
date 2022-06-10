from datetime import datetime
now = datetime.now()
f = open("", "a")
f.write("Adding Line from program python_cron_program_1 @ {}\n".format(now))
f.close()
