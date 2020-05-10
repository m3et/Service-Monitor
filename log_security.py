import hashlib


def hashFile(filename):
    harsher = hashlib.md5()
    with open(filename, 'rb') as read_obj:
        content = read_obj.read()
        harsher.update(content)
    read_obj.close()

    return harsher.hexdigest()


def checkSum(filename, hashStr):
    return hashFile(filename) == hashStr


if __name__ == "__main__":
    print(hashFile('Logs/serviceList.txt'))
