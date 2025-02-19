__version__ = '0.1.1'


def parse_version_info(version_str):
    _version_info = []
    for x in version_str.split('.'):
        if x.isdigit():
            _version_info.append(int(x))
        elif x.find('rc') != -1:
            patch_version = x.split('rc')
            _version_info.append(int(patch_version[0]))
            _version_info.append(f'rc{patch_version[1]}')
    return tuple(_version_info)


version_info = parse_version_info(__version__)
