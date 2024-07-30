import disk_manager as dm
import lru_replacer as lru

# setup_logger.py
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BufferPoolManager:
    """
    A class to represent the BufferPoolManager
    The BufferPoolManager is responsible for fetching database pages from the DiskManager and 
    storing them in memory. 
    
    The BufferPoolManager must write the contents of a dirty Page back to disk before that object can be reused. It 
    writes dirty pages out to disk when it is either explicitly instructed to do so or when it needs to evict a page to make space for a new page.
    
    The BufferPoolManager is not allowed to free a Page that is pinned. 
    
    This BufferPoolManager implementation will use the LRUReplacer class. 
    

    Attributes
    ----------
    buffer_pool : array
        list with page objects
    page_table: array
        list of page_ids current in the buffer pool 
    buffer_total_no_of_frames: int
        total of frames that the buffer pool can hold
    disk_manager: DiskManager
        diskManager object
    replacer: LRUReplacer
        replacer object
   
    Methods
    -------
    getBufferPoll():
        returns all page objects in the buffer pool
    getPageTable():
        return the index of all pages objects currently in the buffer pool
    getDiskManager():
        return disk manager object
    getReplacer():
        return replace object
    fetchPage(page_id):
        returns a page stored in memory. If the page is not in memory, then the page must be read from the disk.
    newPage(page_id):
        reads a page from the disk using the disk manager
    deletePage(page_id):
        deletes a page from the buffer pool and from the disk
    unpinPage(page_id, is_dirty):
        uping a page so the replacer knows it is a free frame that can be evited if needed.
    flushPage(page_id):
        flushs a page with id = page_id from the buffer pool to disk regardless of its pin status.
    flushAllPages():
        flush all pages from the buffer pool to disk regardless of its pin status.
    
    """
    
    def __init__(self, no_of_frames):
        self.buffer_pool = []
        self.page_table = []
        self.disk_manager = dm.DiskManager()
        self.replacer = lru.LRUReplacer()
        self.buffer_total_no_of_frames = no_of_frames
        
    def getBufferPool(self):
        return self.buffer_pool

    def getPageTable(self):
        return self.page_table

    def getReplacer(self):
        return self.replacer

    def getDiskManager(self):
        return self.disk_manager
    
    def fetchPage(self, page_id):
        logger.info(f"Fetching page {page_id} from buffer pool")

    # Search the page table for the requested page_id
        frame_id, page = self.find_page_in_buffer(page_id)

        if page:
             # Page is already in the buffer pool, increment its pin counter and return it
             self.pin_page(frame_id)
             return frame_id, page
        else:
        # Page is not in the buffer pool, fetch it from disk
           frame_id, page = self.read_page(page_id)

        if frame_id is not None:
            # Page was loaded into a frame
            self.pin_page(frame_id)
            return frame_id, page
        else:
            # Buffer pool is full, find a replacement page using the replacer
            frame_id = self.replacer.get_next_victim()
            
            if frame_id is not None:
                # Evict the victim page if it is dirty, write it back to disk
                self.write_dirty_page(frame_id)

                # Delete the evicted page from the page table
                self.remove_page_from_page_table(frame_id)

                # Insert the fetched page into the page table
                self.insert_page_into_page_table(frame_id, page_id)

                # Update the page metadata
                self.buffer_pool[frame_id] = {'page_id': page_id, 'data': None, 'pin_count': 1, 'dirty': False}
                return frame_id, self.buffer_pool[frame_id]
            else:
                # All pages are pinned, print an error message
                logger.error("All pages are pinned, cannot fetch the requested page.")
                return None, None

def find_page_in_buffer(self, page_id):
    # Helper function to search the page table for the requested page_id
    for frame_id, page in enumerate(self.buffer_pool):
        if page and page['page_id'] == page_id:
            return frame_id, page
    return None, None

def write_dirty_page(self, frame_id):
    # Helper function to write a dirty page back to disk
    if 0 <= frame_id < self.pool_size and self.buffer_pool[frame_id]['dirty']:
        self.disk_manager.write_page(self.buffer_pool[frame_id]['page_id'], self.buffer_pool[frame_id]['data'])

def remove_page_from_page_table(self, frame_id):
    # Helper function to delete a page from the page table
    if 0 <= frame_id < self.pool_size:
        self.page_table.pop(self.buffer_pool[frame_id]['page_id'], None)

def insert_page_into_page_table(self, frame_id, page_id):
    # Helper function to insert a page into the page table
    if 0 <= frame_id < self.pool_size:
        self.page_table[page_id] = frame_id

                    
def loadPage(self, page_id):
        logger.info(f"Fetching a new page to the buffer pool. Page {page_id} is not in buffer pool; it has to be read from disk")
        if not self.disk_manager.is_valid_page(page_id):
            logger.error(f"Invalid page {page_id} in disk.")
            return None, None
        if page_id in self.page_table:
            frame_id = self.page_table[page_id]
            self.pin_page(frame_id)
        else:
            frame_id, page = self.fetchPage(page_id)
            if frame_id is not None:
                self.pin_page(frame_id)
            else:
                logger.error(f"Failed to load page {page_id} from disk.")
        return frame_id, self.buffer_pool[frame_id]

def deletePage(self, page_id):
        logger.info(f"Deleting page {page_id} from buffer pool")
        if page_id not in self.page_table:
            logger.warning(f"Page {page_id} not found in buffer pool.")
            return False
        frame_id = self.page_table[page_id]
        if self.buffer_pool[frame_id]['pin_count'] > 0:
            logger.error(f"Cannot delete page {page_id}, it is pinned.")
            return False
        self.unpin_page(frame_id)
        self.remove_page_from_page_table(frame_id)
        return True

def unpinPage(self, page_id, is_dirty):
        logger.info(f"Unpinning page {page_id} in the buffer pool")
        if page_id not in self.page_table:
            logger.warning(f"Page {page_id} not found in buffer pool.")
            return
        frame_id = self.page_table[page_id]
        if self.buffer_pool[frame_id]['pin_count'] > 0:
            self.buffer_pool[frame_id]['pin_count'] -= 1
            self.buffer_pool[frame_id]['dirty'] = is_dirty
            if self.buffer_pool[frame_id]['pin_count'] == 0:
                self.replacer.unpin(frame_id)
        else:
            logger.warning(f"Page {page_id} is not pinned.")

def flushPage(self, page_id):
        logger.info(f"Flushing page {page_id} out of the buffer pool")
        if page_id not in self.page_table:
            logger.warning(f"Page {page_id} not found in buffer pool.")
            return
        frame_id = self.page_table[page_id]
        if self.buffer_pool[frame_id]['pin_count'] > 0:
            logger.warning(f"Cannot flush page {page_id}, it is pinned.")
            return
        self.write_dirty_page(frame_id)

def flushAllPages(self):
        logger.info("Flushing all pages out of the buffer pool")
        for frame_id, page in enumerate(self.buffer_pool):
            if page and page['pin_count'] == 0:
                self.write_dirty_page(frame_id)