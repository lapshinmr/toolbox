import os
import hashlib
import argparse


class DupFinder:
    def __init__(self, dir_path, part_size=1024):
        """
        :param part_size: size in bytes by that you read file
        """
        self.dir_path = dir_path
        self.part_size = part_size

    def part_reader(self, file_obj):
        """
        Generator that reads a file in parts of bytes
        :param file_obj: any opening file
        :return: file as generator
        """
        while True:
            part = file_obj.read(self.part_size)
            if not part:
                return
            yield part

    def get_hash(self, file_path):
        """
        Get hash of file
        :param file_path:
        :param part_size:
        :return: hash
        """
        with open(file_path, 'rb') as file_obj:
            file_hash = hashlib.md5()
            for part in self.part_reader(file_obj):
                file_hash.update(part)
        return file_hash.hexdigest()

    def find_all_hashs(self):
        """
        Method for search hashes for oll files in folder and subfolders.
        :return: {hash: [file_path1]}
        """
        dups = {}
        for dir_name, sub_dirs, file_list in os.walk(self.dir_path):
            for filename in file_list:
                file_path = os.path.join(dir_name, filename)
                file_hash = self.get_hash(file_path)
                if file_hash in dups:
                    dups[file_hash].append(file_path)
                else:
                    dups[file_hash] = [file_path]
        return dups

    def find_dups(self):
        """
        Eject duplicates from all found hashes.
        :return: {hash: [file_path1, file_path2, ...]} but only with duplicates.
        """
        dup_files = {}
        for hash, paths in self.find_all_hashs().items():
            if len(paths) > 1:
                dup_files[hash] = paths
        return dup_files


if __name__ == '__main__':
    finder = DupFinder('to_compare')
    dups = finder.find_dups()
    for hash, paths in dups.items():
        for path in paths:
            if 'to_compare/new' in path:
                print('delete %s' % path)
                os.remove(path)
                break
