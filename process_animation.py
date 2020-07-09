import time
import threading

# abstract
class Animation:
    is_stop = False

    def run(self,  timeout=None, delay=0.1):
        self.thread = threading.Thread(target=self.anim, args=(delay,))
        self.thread.start()
        if timeout != None:
            self.stop(timeout)

    def stop(self, timeout: float=0):
        def inner_fn():
            self.is_stop = True
        time.sleep(timeout)
        threading.Thread(target=inner_fn).start()
        print('\r' + ' ' * self.MAX_FRAME_LEN, end='\r')

class Spinner(Animation):
    MAX_FRAME_LEN = 1

    def anim(self, delay):
        i=0
        while not self.is_stop:
            if i==0:
                s='\\'
                i+=1
            elif i==1:
                s='|'
                i+=1
            elif i==2:
                s='/'
                i+=1
            elif i==3:
                s='-'
                i=0
            print(s, end='\r')
            time.sleep(delay)

class Dotter(Animation):
    def __init__(self, word: str=''):
        self.word = word
        self.MAX_FRAME_LEN = len(word) + 3
        super().__init__()

    def anim(self, delay):
        i=0
        while not self.is_stop:
            if i==0:
                s='   '
                i+=1
            elif i==1:
                s='.  '
                i+=1
            elif i==2:
                s='.. '
                i+=1
            elif i==3:
                s='...'
                i=0
            print(self.word + s, end='\r')
            time.sleep(delay)

if __name__ == "__main__":
    Spinner().run(10)