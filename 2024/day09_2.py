from io import TextIOWrapper
from typing import List

"""
--- Part Two ---

Upon completion, two things immediately become clear. First, the disk definitely has a lot more contiguous free space, just like the amphipod hoped. Second, the computer is running much more slowly! Maybe introducing all of that file system fragmentation was a bad idea?

The eager amphipod already has a new plan: rather than move individual blocks, he'd like to try compacting the files on his disk by moving whole files instead.

This time, attempt to move whole files to the leftmost span of free space blocks that could fit the file. Attempt to move each file exactly once in order of decreasing file ID number starting with the file with the highest file ID number. If there is no span of free space to the left of a file that is large enough to fit the file, the file does not move.

The first example from above now proceeds differently:

00...111...2...333.44.5555.6666.777.888899
0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
00992111777.44.333....5555.6666.....8888..
The process of updating the filesystem checksum is the same; now, this example's checksum would be 2858.

Start over, now compacting the amphipod's hard drive using this new method instead. What is the resulting filesystem checksum?


"""


class SpaceBlock:
    def __init__(self, start_index, size):
        self.start_index = start_index
        self.size = size
        self.end_index = start_index + size


class FileBlock:
    def __init__(self, id, start_index, size):
        self.id = id
        self.start_index = start_index
        self.size = size
        self.end_index = start_index + size


def solve(input: TextIOWrapper):
    line = input.readline()
    disk_map = []
    file_blocks: List[FileBlock] = []
    space_blocks: List[SpaceBlock] = []
    for i, _ in enumerate(line):
        if i % 2 == 0:
            block_size = int(line[i])
            block_id = i // 2
            file_blocks.append(FileBlock(block_id, len(disk_map), block_size))
            disk_map.extend([block_id for _ in range(block_size)])
        else:
            space_size = int(line[i])
            if space_size == 0:
                continue
            space_blocks.append(SpaceBlock(len(disk_map), space_size))
            disk_map.extend(["." for _ in range(space_size)])

    # disk_map_str = ""
    # for i in range(len(disk_map)):
    #     disk_map_str += str(disk_map[i])
    # print(disk_map_str)
    while len(file_blocks) > 0:
        right_most_file_block = file_blocks.pop()

        for j, space_block in enumerate(space_blocks):
            available_space_block = space_block

            if right_most_file_block.start_index < available_space_block.start_index:
                break

            if right_most_file_block.size <= available_space_block.size:
                for i in range(right_most_file_block.size):
                    disk_map[available_space_block.start_index + i] = (
                        right_most_file_block.id
                    )
                    disk_map[right_most_file_block.start_index + i] = "."

                available_space_block.size -= right_most_file_block.size
                available_space_block.start_index += right_most_file_block.size

                if available_space_block.size == 0:
                    space_blocks.pop(j)

                # disk_map_str = ""
                # for i in range(len(disk_map)):
                #     disk_map_str += str(disk_map[i])
                # print(disk_map_str)
                break

    fs_checksum = 0
    for i in range(len(disk_map)):
        if disk_map[i] == ".":
            continue
        fs_checksum += i * disk_map[i]
        pass

    # print(disk_map)
    # print(last_index)
    # 8564936405055 is too high
    print(fs_checksum)
