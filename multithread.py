from threading import Thread
import queue
import time

class TaskQueue(queue.Queue):
    def __init__(self, num_workers=1):
        queue.Queue.__init__(self)
        self.num_workers = num_workers
        self.start_workers()
    def add_task(self, task, *args, **kwargs):
        args = args or ()
        kwargs = kwargs or {}
        self.put((task, args, kwargs))
    def start_workers(self):
        for i in range(self.num_workers):
            t = Thread(target=self.worker)
            t.daemon = True
            t.start()
    def worker(self):
        while True:
            #tupl = self.get()
            item, args, kwargs = self.get()
            item(*args, **kwargs)
            self.task_done()

def tests():
    def hi(*args, **kwargs):
        time.sleep(5)
        print (args)
        
    q = TaskQueue(num_workers=5)
    for item in range(5):
        q.add_task(hi,item)
    q.join() # block until all tasks are done
    print ('All done!')
    
if __name__ == '__main__':
    tests()
