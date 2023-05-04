from random import randint
# from F_NodeBasedQueue import Queue
from F_StackBasedQueue import Queue
from time import sleep

class Track():
    def __init__(self, title=None) -> None:
        self.title = title
        self.length = randint(5,6)
# Metodo 1 - Queue Node
# class MediaPlayerQueue(Queue):
#     def __init__(self) -> None:
#         super(MediaPlayerQueue, self).__init__()

#     def add_track(self, track):
#         self.enqueue(track)
    
#     def play(self):
#         print(f"Count: {self.count}")

#         while self.count>0 and self.head is not None:
#             current_track = self.dequeue()
#             print(f"Now Playing {current_track.title}")

#             sleep(current_track.length)

# Metodo 2 - Queue Stack
class MediaPlayerQueue(Queue):
    def __init__(self):
        super(MediaPlayerQueue,self).__init__()
    
    def add_track(self, data):
        self.enqueue(data)
    
    def play(self):
        while len(self.outbound_stack)>0 or len(self.inbound_stack)>0:
            current = self.dequeue()
            print(f"Now playing {current.title}")
            sleep(current.length)


track = ["Starway to heaven", "Alone", "Breath me", "Marisola", "Llovia"]
music = MediaPlayerQueue()

for i in track:
    music.add_track(Track(i))

music.play()