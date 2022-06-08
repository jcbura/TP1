from datetime import datetime
now = datetime.now()
f = open("/Users/jason/PERSONAL_COMP/python_cron_test/cron_results.txt", "a")
f.write("Adding Line from program python_cron_program_1 @ {}\n".format(now))
f.close()
