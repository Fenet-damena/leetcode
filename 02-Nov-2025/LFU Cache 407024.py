# Problem: LFU Cache - https://leetcode.com/problems/lfu-cache/

from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val = {}
        self.key_to_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)
        self.min_freq = 0

    def _update_freq(self, key):
        freq = self.key_to_freq[key]
        val = self.key_to_val[key]

        del self.freq_to_keys[freq][key]

        if not self.freq_to_keys[freq] and self.min_freq == freq:
            self.min_freq += 1

        self.key_to_freq[key] = freq + 1
        self.freq_to_keys[freq + 1][key] = val

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        self._update_freq(key)
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._update_freq(key)
            return

        if len(self.key_to_val) >= self.capacity:
            old_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val[old_key]
            del self.key_to_freq[old_key]

        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = value
        self.min_freq = 1
