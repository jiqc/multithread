import threading
import queue

def tests():
    def worker():
        while True:
            item = q.get()
            if item is None:
                break
            print (item)
            q.task_done()

    num_worker_threads = 5;
    q = queue.Queue()
    threads = []
    for i in range(num_worker_threads):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    for item in range(11,16):
        q.put(item)

    # block until all tasks are done
    q.join()
    print ('all done')
    # stop workers
    for i in range(num_worker_threads):
        q.put(None)
    for t in threads:
        t.join()

if __name__ == '__main__':
    tests()
