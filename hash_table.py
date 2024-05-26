# input: string, output: int 
def calculate_hash(key):
    assert type(key) == str
    hash = 0
    for i in key:
        hash += ord(i)
    return hash

# key: string, value: anytype, next: Item
class Item:
    def __init__(self, key, value, next):
        assert type(key) == str
        self.key = key
        self.value = value
        self.next = next

# bucket_size: int, buckets: [Item], item_count: int
class HashTable:
    def __init__(self):
        self.bucket_size = 97
        self.buckets = [None] * self.bucket_size
        self.item_count = 0

    # key: string, value: anytype
    def put(self, key, value):
        assert type(key) == str
        self.check_size() # Note: Don't remove this code.
        bucket_index = calculate_hash(key) % self.bucket_size
        item = self.buckets[bucket_index]
        while item:
            if item.key == key:
                item.value = value
                return False
            item = item.next
        new_item = Item(key, value, self.buckets[bucket_index])
        self.buckets[bucket_index] = new_item
        self.item_count += 1
        return True

    # input: (key: string), output: (Item, boolean)
    def get(self, key):
        assert type(key) == str
        self.check_size() # Note: Don't remove this code.
        bucket_index = calculate_hash(key) % self.bucket_size
        item = self.buckets[bucket_index]
        while item:
            if item.key == key:
                return (item.value, True)
            item = item.next
        return (None, False)

    # input: (key: string), output: boolean
    def delete(self, key):
        assert type(key) == str
        #------------------------#
        # Write your code here!  #
        #------------------------#
        pass

    # output: int
    def size(self):
        return self.item_count

    # void
    # Check that the hash table has a "reasonable" bucket size.
    def check_size(self):
        assert (self.bucket_size < 100 or
                self.item_count >= self.bucket_size * 0.3)
