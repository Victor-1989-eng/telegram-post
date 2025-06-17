# файл: imghdr.py (в корне проекта)
def what(file, h=None):
    if h is None:
        if isinstance(file, str):
            with open(file, 'rb') as f:
                h = f.read(32)
        else:
            h = file.read(32)
            file.seek(0)
    if h[:3] == b'\xff\xd8\xff':
        return 'jpeg'
    if h[:8] == b'\x89PNG\r\n\x1a\n':
        return 'png'
    return None
