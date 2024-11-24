import ipaddress
import asyncio
from aioping import ping
from datetime import datetime
from typing import Union

async def ping_host(ip: str) -> Union[float, None]:
    try:
        response_time = await ping(ip, timeout=1.0)
        return response_time
    except TimeoutError:
        return None
    except Exception as e:
        return None


async def scan(subnet: str, verbose: bool) -> list:
    network = ipaddress.ip_network(subnet, strict=False)
    tasks = []
    result = []

    for ip in network.hosts():
        tasks.append(ping_host(str(ip)))

    responses = await asyncio.gather(*tasks, return_exceptions=True)

    for ip, response in zip(network.hosts(), responses):
        timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        if response:
            result.append(f'[#] Available: {timestamp} - {ip} (response time {response:.4f}s)')
        else:
            if verbose:
                result.append(f'[#] Unavailable: {timestamp} - {ip}')

    return result
