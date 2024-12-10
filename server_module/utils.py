def separate_address(address: str):
    [host, port] = address.rsplit(':', 1)
    
    return host, int(port)


def unite_address(address: tuple[str, int]):
    (host, port) = address
    
    return f'{host}:{port}'
