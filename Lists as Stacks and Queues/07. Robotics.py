robots = {r.split('-')[0]: [int(r.split('-')[1]), 0] for r in input().split(',')}
factory_name = datatime.strptime(input(), '%H:%M:%S')
