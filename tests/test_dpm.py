#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import acsys.dpm

FORMAT = '%(asctime)-15s [%(levelname)s] %(message)s'
logging.basicConfig(format=FORMAT)

log = logging.getLogger('acsys')
log.setLevel(logging.DEBUG)

async def my_client(con):
    log.info('entered main')

    # Setup context

    async with acsys.dpm.DPMContext(port=6808) as dpm:

        # Add acquisition requests

        await dpm.add_entry(0, 'M:OUTTMP@p,1S')

        # Process incoming data

        async for evt_res in dpm.replies():
            print(evt_res)
            if evt_res.is_reading_for(0):
                print(f'cycle: {evt_res.cycle}, status: {evt_res.status}')
                for (stamp, value) in evt_res.data:
                    print(f'received: {stamp}, {value}')
            else:
                raise RuntimeError(f'expected ItemData, got {evt_res}')

acsys.run_client(my_client)
