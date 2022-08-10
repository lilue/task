from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
import time
from school.models import Teacher, Student


# 1.实例化调度器
scheduler = BackgroundScheduler(timezone='Asia/Shanghai')

# 2.调度器使用DjangoJobStore()
scheduler.add_jobstore(DjangoJobStore(), "default")

try:
    # 3.设置定时任务，选择方式为interval，时间间隔为10s
    # 另一种方式为每天固定时间执行任务，对应代码为：
    # @register_job(scheduler, 'cron', hour='9', minute='30', second='10',id='task_time')

    @register_job(scheduler, 'cron', hour='11', minute='30', second='10', id='task_time')
    def task_time():
        print("现在是11点30分10秒")


    @register_job(scheduler, 'cron', minute='1', id='task_time1')
    def task_time1():
        print("每分钟执行一次")

    @register_job(scheduler, "interval", minutes=1, seconds=10, replace_existing=True)
    def my_job():
        teacher = Teacher.objects.all()
        for item in teacher:
            print(item.name)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    # 4.注册定时任务
    # register_events(scheduler)          # 新版本已经不需要这一步了

    @register_job(scheduler, "interval", seconds=30, replace_existing=True)
    def my_job2():
        print('运行第二个方法')

    # 5.开启定时任务
    scheduler.start()

except Exception as e:
    print(str(e))
    # 有错误就停止定时器
    scheduler.shutdown()
