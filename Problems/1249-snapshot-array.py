// https://leetcode.com/problems/snapshot-array

class SnapshotArray:

    def __init__(self, length: int):
        self.array = [0]*length
        self.snap_id = 0
        self.snap_to_change = dict()

    def set(self, index: int, val: int) -> None:
        self.snap_to_change[(self.snap_id, index)] = val

    def snap(self) -> int:
        cur_snap = self.snap_id
        self.snap_id += 1
        return cur_snap
    
    def get(self, index: int, snap_id: int) -> int:
        cur_snap = snap_id
        while cur_snap >= 0:
            if (cur_snap, index) in self.snap_to_change:
                return self.snap_to_change[(cur_snap, index)]
            else:
                cur_snap -= 1
        return self.array[index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)