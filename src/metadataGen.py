#!/usr/bin/env python3

import sys
import json
import getopt
import random

# Generate all the metadata on performance for the taskmanager to be used as configs with WASP,
# -n INT: number of task managers
# -c INT: number of configurations


def main(argv):
    numTaskManagers = 1
    numConfigs = 1

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'n:c:', ['n=', 'c='])
    except getopt.GetoptError:
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-n':
            numTaskManagers = int(arg)
        if opt == '-c':
            numConfigs = int(arg)

    configs = []
    for i in range(0, numConfigs):
        data = {}
        # Simulate some random bandwidth and latency
        for i in range(0, numTaskManagers):
            data[str(i)] = {}
            latencies = {}
            bws = {}
            for j in range(0, numTaskManagers):
                if (i != j):
                    latencies[str(j)] = random.uniform(1, 3)
                    bws[str(j)] = random.uniform(500, 3000)
                else:
                    latencies[str(j)] = 0
                    bws[str(j)] = 0

            data[str(i)]['latencies'] = latencies
            data[str(i)]['bandwidth'] = bws
            data[str(i)]['ipRate'] = random.uniform(0, 1000)
            data[str(i)]['opRate'] = random.uniform(0, 500)
            data[str(i)]['numSlots'] = random.randint(1, 10)

        configs.append(data)

        with open("config.json", "w") as configFile:
            json.dump(configs, configFile)


if __name__ == "__main__":
    main(sys.argv[1:])