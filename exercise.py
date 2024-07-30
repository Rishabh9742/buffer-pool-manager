import buffer_pool_manager as bm

def main():


    ## IMPLEMENT THE FOLLOWING STEPS USING YOUR BUFFER POOL MANAGER


    #1. Create a BufferPool that can hold 16 frames
 class BufferPoolManager:
    def __init__(self, pool_size):
        self.pool_size = pool_size
        self.buffer_pool = [None] * pool_size
        self.free_frames = set(range(pool_size))

    def read_page(self, page_id):
        # Check if the page is already in the buffer pool
        for frame_id, page in enumerate(self.buffer_pool):
            if page and page['page_id'] == page_id:
                return frame_id, page  # Return frame_id and page if found

        # If the page is not in the buffer pool, find a free frame to load the page
        if len(self.free_frames) > 0:
            frame_id = self.free_frames.pop()
        else:
            # If no free frame is available, use a replacement policy (e.g., LRU) to find a frame to replace
            frame_id = self.lru_replacement_policy()

        # Load the page into the selected frame
        # In a real system, you would read the page from disk into self.buffer_pool[frame_id]
        self.buffer_pool[frame_id] = {'page_id': page_id, 'data': None}
        return frame_id, self.buffer_pool[frame_id]

    def write_page(self, frame_id, data):
        # Write data to the specified frame in the buffer pool
        if 0 <= frame_id < self.pool_size:
            self.buffer_pool[frame_id]['data'] = data

    def lru_replacement_policy(self):
        # Implement LRU replacement policy to find the frame to replace
        # In a real system, you would track the access timestamps for each frame
        # and find the frame with the oldest timestamp.

        # For simplicity, let's just replace the first frame in this example.
        
        # In a real system, you would use something like the following to find the frame with the oldest timestamp:
        oldest_frame = min(range(len(self.access_timestamps)), key=self.access_timestamps.__getitem__)
        return oldest_frame
    #2. Add 16 pages (page 0 to 15) to the BufferPool
def add_pages_to_pool(self):
        for page_id in range(self.pool_size):
            frame_id, page = self.read_page(page_id)
            print(f"Read page {page_id} into frame {frame_id}")
    #3. Print the Buffer's Pool PageTable
def print_page_table(self):
        print("Page Table:")
        print("Page ID | Frame ID")
        print("-" * 20)
        for frame_id, page in enumerate(self.buffer_pool):
            if page:
                print(f"{page['page_id']:^8} | {frame_id:^8}")
            else:
                print(f"{'Empty':^8} | {frame_id:^8}")
        print("-" * 20)    
    #4. Print the replacer free frames list
def print_free_frames(self):
        print(f"Free Frames: {list(self.free_frames)}")
    #5. Fetch page #14 from your bufferPool and prints the page_id
        frame_id, page = buffer_pool_manager.read_page(14)
        if page:
            print(f"Page ID in frame {frame_id}: {page['page_id']}")
        else:
                print("Page not found in the buffer pool.")    
    #6. Print page #14 pin counter
def print_free_frames(self):
        print(f"Free Frames: {list(self.free_frames)}")

def pin_page(self, frame_id):
        if 0 <= frame_id < self.pool_size:
            self.buffer_pool[frame_id]['pin_count'] += 1

def unpin_page(self, frame_id):
        if 0 <= frame_id < self.pool_size and self.buffer_pool[frame_id]['pin_count'] > 0:
            self.buffer_pool[frame_id]['pin_count'] -= 1
    #7. Fetch page #16 from your bufferPool and prints the page_id. Did it work? Why?
frame_id, page = buffer_pool_manager.read_page(15)

if page:
    print(f"Page ID in frame {frame_id}: {page['page_id']}")
else:
    print("Page not found in the buffer pool.")
    #this did not work because the page was not found in the buffer pool

    #8. Print the Buffer's Pool PageTable
def print_page_table(self):
        print("Page Table:")
        print("Page ID | Frame ID | Pin Count")
        print("-" * 30)
        for frame_id, entry in enumerate(self.buffer_pool):
            if entry['page']:
                print(f"{entry['page']['page_id']:^8} | {frame_id:^8} | {entry['pin_count']:^10}")
            else:
                print(f"{'Empty':^8} | {frame_id:^8} | {'N/A':^10}")
        print("-" * 30)
    #9. Unpin page #14. Page #14 is not dirty
def unpin_page(self, frame_id):
        if 0 <= frame_id < self.pool_size and self.buffer_pool[frame_id]['pin_count'] > 0:
            self.buffer_pool[frame_id]['pin_count'] -= 1

def mark_page_as_clean(self, frame_id):
        if 0 <= frame_id < self.pool_size:
            self.buffer_pool[frame_id]['dirty'] = False
    #10. Try again to fetch page #16. Did it work? Why?
frame_id, page = buffer_pool_manager.read_page(15)

if page:
    print(f"Page ID in frame {frame_id}: {page['page_id']}")
else:
    print("Page not found in the buffer pool.")
    #it did not work because the page 16 was not in the bufferpool

    #11. Print the replacer free frame
def print_free_frames(self):
        print(f"Free Frames: {list(self.free_frames)}")

    #12. Unpin page #14 again. Page 14 is not dirty
# Pin page #14 for demonstration purposes

buffer_pool_manager = BufferPoolManager(16)

# Unpin page #14 and mark it as not dirty
buffer_pool_manager.unpin_page(14)

# Print the Buffer Pool's Page Table after unpinning page #14
buffer_pool_manager.print_page_table()

    #13.Print the replacer free frame
def print_free_frames(self):

# Pin page #14 for demonstration purposes
buffer_pool_manager = BufferPoolManager(14)
# Unpin page #14 and mark it as not dirty
buffer_pool_manager.unpin_page(14)
buffer_pool_manager.mark_page_as_clean(14)

# Print the list of free frames from the buffer pool's replacer perspective
buffer_pool_manager.print_free_frames()

    #14. Try again to fetch page #16.Did it work? Why?
buffer_pool_manager = BufferPoolManager(16)
buffer_pool_manager.add_pages_to_pool()

# Attempting to fetch page #16 (out of bounds)
frame_id, page = buffer_pool_manager.read_page(16)

if page:
    print(f"Page ID in frame {frame_id}: {page['page_id']}")
else:
    print("Page not found in the buffer pool.")
    #15. Print the Buffer's Pool PageTable
def print_page_table(self):
        print("Page Table:")
        print("Page ID | Frame ID | Pin Count | Dirty")
        print("-" * 40)
        for frame_id, entry in enumerate(self.buffer_pool):
            if entry['page']:
                print(f"{entry['page']['page_id']:^8} | {frame_id:^8} | {entry['pin_count']:^10} | {entry['dirty']:^5}")
            else:
                print(f"{'Empty':^8} | {frame_id:^8} | {'N/A':^10} | {'N/A':^5}")
        print("-" * 40)
buffer_pool_manager.print_page_table()
    #16. Unpin page #9 and #12. They are both dirty
buffer_pool_manager = BufferPoolManager(16)
buffer_pool_manager.add_pages_to_pool()

# Pin pages #9 and #12 for demonstration purposes
buffer_pool_manager.pin_page(9)
buffer_pool_manager.pin_page(12)

# Mark pages #9 and #12 as dirty and then unpin them
frame_id_9, _ = buffer_pool_manager.read_page(9)
frame_id_12, _ = buffer_pool_manager.read_page(12)

buffer_pool_manager.mark_page_as_dirty(frame_id_9)
buffer_pool_manager.mark_page_as_dirty(frame_id_12)

buffer_pool_manager.unpin_page(frame_id_9)
buffer_pool_manager.unpin_page(frame_id_12)

# Print the Buffer Pool's Page Table after unpinning and marking pages #9 and #12 as dirty
buffer_pool_manager.print_page_table()

    #17. Fetch page #14 from your bufferPool and prints the page_id. What happened with the page that was replaced to make room for page #14?
buffer_pool_manager = BufferPoolManager(16)
buffer_pool_manager.add_pages_to_pool()

# Fetch page #14 from the buffer pool
frame_id, page = buffer_pool_manager.read_page(14)

if page:
    print(f"Page ID in frame {frame_id}: {page['page_id']}")
else:
    print("Page not found in the buffer pool.")
    
# Print the Buffer Pool's Page Table after reading page #14
buffer_pool_manager.print_page_table()

    #18. Delete page #5. Did it work? Why?
buffer_pool_manager = BufferPoolManager(16)
buffer_pool_manager.add_pages_to_pool()

# Delete page #5 by replacing it with page #20
frame_id, _ = buffer_pool_manager.read_page(20)

# Print the Buffer Pool's Page Table after replacing page #5 with page #20
buffer_pool_manager.print_page_table()

    #19. Unpin page #5. The page is not dirty
buffer_pool_manager = BufferPoolManager(16)
buffer_pool_manager.add_pages_to_pool()

# Pin page #5 for demonstration purposes
buffer_pool_manager.pin_page(5)

# Unpin page #5 and mark it as not dirty
frame_id_5, _ = buffer_pool_manager.read_page(5)
buffer_pool_manager.unpin_page(frame_id_5)
buffer_pool_manager.mark_page_as_clean(frame_id_5)

# Print the Buffer Pool's Page Table after unpinning and marking page #5 as not dirty
buffer_pool_manager.print_page_table()

    #20. Try to delete page #5 again. Did it work?
buffer_pool_manager = BufferPoolManager(16)
buffer_pool_manager.add_pages_to_pool()

# Attempt to delete page #5 by replacing it with page #25
frame_id, _ = buffer_pool_manager.read_page(25)

# Print the Buffer Pool's Page Table after replacing page #5 with page #25
buffer_pool_manager.print_page_table()
    #21. Print page table
buffer_pool_manager = BufferPoolManager(16)
buffer_pool_manager.add_pages_to_pool()

# Attempt to delete page #5 by replacing it with page #25
frame_id, _ = buffer_pool_manager.read_page(25)

# Print the Buffer Pool's Page Table after replacing page #5 with page #25
buffer_pool_manager.print_page_table()    
    #22. Fetch page #5x
buffer_pool_manager = BufferPoolManager(16)
buffer_pool_manager.add_pages_to_pool()

# Attempt to fetch page #5
frame_id, page = buffer_pool_manager.read_page(5)

if page:
    print(f"Page ID in frame {frame_id}: {page['page_id']}")
else:
    print("Page not found in the buffer pool.")
            
    

main()