# def monitor_virtual(self, result_data,ports_data,ping_stats,rtts,rtts_list):
#             if isinstance(result_data, dict):
#                 for station in self.sta_list:
#                     if station not in self.real_sta_list:
#                         current_device_data = ports_data[station]
#                         if station.split('.')[2] in result_data['name']:
#                             self.result_json[station] = {
#                                 'command': result_data['command'],
#                                 'sent': result_data['tx pkts'],
#                                 'recv': result_data['rx pkts'],
#                                 'dropped': result_data['dropped'],
#                                 'mac': current_device_data['mac'],
#                                 'ip': current_device_data['ip'],
#                                 'bssid': current_device_data['ap'],
#                                 'ssid': current_device_data['ssid'],
#                                 'channel': current_device_data['channel'],
#                                 'mode': current_device_data['mode'],
#                                 'name': station,
#                                 'os': 'Virtual',
#                                 'remarks': [],
#                                 'last_result': self.get_safe_last_result(ping_data.get('last results', ''))
#                             }
#                             ping_stats[station]['sent'].append(result_data['tx pkts'])
#                             ping_stats[station]['received'].append(result_data['rx pkts'])
#                             ping_stats[station]['dropped'].append(result_data['dropped'])
#                             self.result_json[station]['ping_stats'] = ping_stats[station]
#                             if len(result_data['last results']) != 0 and 'min/avg/max' in result_data['last results']:
#                                 temp_last_results = result_data['last results'].split('\n')[0: len(result_data['last results']) - 1]
#                                 drop_count = 0  # let dropped = 0 initially
#                                 dropped_packets = []
#                                 # sample result - 64 bytes from 192.168.1.61: icmp_seq=28 time=3.66 ms *** drop: 0 (0, 0.000)  rx: 28  fail: 0  bytes: 1792 min/avg/max: 2.160/3.422/5.190
#                                 for result in temp_last_results:
#                                     try:
#                                         # fetching the first part of the last result e.g., 64 bytes from 192.168.1.61: icmp_seq=28 time=3.66 ms into t_result and the remaining part into t_fail
#                                         t_result, t_fail = result.split('***')
#                                     except BaseException:
#                                         continue
#                                     t_result = t_result.split()
#                                     if 'icmp_seq=' not in result and 'time=' not in result:
#                                         continue
#                                     for t_data in t_result:
#                                         if 'icmp_seq=' in t_data:
#                                             seq_number = int(t_data.strip('icmp_seq='))
#                                         if 'time=' in t_data:
#                                             rtt = float(t_data.strip('time='))
#                                     rtts[station][seq_number] = rtt
#                                     rtts_list.append(rtt)

#                                     # finding dropped packets
#                                     t_fail = t_fail.split()  # [' drop:', '0', '(0, 0.000)', 'rx:', '28', 'fail:', '0', 'bytes:', '1792', 'min/avg/max:', '2.160/3.422/5.190']
#                                     t_drop_val = t_fail[1]  # t_drop_val = '0'
#                                     t_drop_val = int(t_drop_val)  # type cast string to int
#                                     if t_drop_val != drop_count:
#                                         current_drop_packets = t_drop_val - drop_count
#                                         drop_count = t_drop_val
#                                         for drop_packet in range(1, current_drop_packets + 1):
#                                             dropped_packets.append(seq_number - drop_packet)

#                             if rtts_list == []:
#                                 rtts_list = [0]
#                             min_rtt = str(min(rtts_list))
#                             avg_rtt = str(sum(rtts_list) / len(rtts_list))
#                             max_rtt = str(max(rtts_list))
#                             self.result_json[station]['min_rtt'] = min_rtt
#                             self.result_json[station]['avg_rtt'] = avg_rtt
#                             self.result_json[station]['max_rtt'] = max_rtt
#                             if list(rtts[station].keys()) != []:
#                                 required_sequence_numbers = list(range(1, max(rtts[station].keys())))
#                                 for seq in required_sequence_numbers:
#                                     if seq not in rtts[station].keys():
#                                         if seq in dropped_packets:
#                                             rtts[station][seq] = 0
#                                         else:
#                                             rtts[station][seq] = 0.11
#                             else:
#                                 self.result_json[station]['rtts'] = {}
#                             self.result_json[station]['rtts'] = rtts[station]
#                             self.result_json[station]['remarks'] = self.generate_remarks(self.result_json[station])
#                             # self.result_json[station]['dropped_packets'] = dropped_packets

#             else:
#                 for station in self.sta_list:
#                     if station not in self.real_sta_list:
#                         current_device_data = ports_data[station]
#                         for ping_device in result_data:
#                             ping_endp, ping_data = list(ping_device.keys())[
#                                 0], list(ping_device.values())[0]
#                             if station.split('.')[2] in ping_endp:
#                                 self.result_json[station] = {
#                                     'command': ping_data['command'],
#                                     'sent': ping_data['tx pkts'],
#                                     'recv': ping_data['rx pkts'],
#                                     'dropped': ping_data['dropped'],
#                                     'mac': current_device_data['mac'],
#                                     'ip': current_device_data['ip'],
#                                     'bssid': current_device_data['ap'],
#                                     'ssid': current_device_data['ssid'],
#                                     'channel': current_device_data['channel'],
#                                     'mode': current_device_data['mode'],
#                                     'name': station,
#                                     'os': 'Virtual',
#                                     'remarks': [],
#                                     'last_result': self.get_safe_last_result(ping_data.get('last results', ''))
#                                 }
#                                 ping_stats[station]['sent'].append(ping_data['tx pkts'])
#                                 ping_stats[station]['received'].append(ping_data['rx pkts'])
#                                 ping_stats[station]['dropped'].append(ping_data['dropped'])
#                                 self.result_json[station]['ping_stats'] = ping_stats[station]
#                                 if len(ping_data['last results']) != 0 and 'min/avg/max' in ping_data['last results']:
#                                     temp_last_results = ping_data['last results'].split('\n')[0: len(ping_data['last results']) - 1]
#                                     drop_count = 0  # let dropped = 0 initially
#                                     dropped_packets = []
#                                     # sample result - 64 bytes from 192.168.1.61: icmp_seq=28 time=3.66 ms *** drop: 0 (0, 0.000)  rx: 28  fail: 0  bytes: 1792 min/avg/max: 2.160/3.422/5.190
#                                     for result in temp_last_results:
#                                         try:
#                                             # fetching the first part of the last result e.g., 64 bytes from 192.168.1.61: icmp_seq=28 time=3.66 ms into t_result and the remaining part into t_fail
#                                             t_result, t_fail = result.split('***')
#                                         except BaseException:
#                                             continue  # first line of ping result
#                                         t_result = t_result.split()
#                                         if 'icmp_seq=' not in result and 'time=' not in result:
#                                             continue
#                                         for t_data in t_result:
#                                             if 'icmp_seq=' in t_data:
#                                                 seq_number = int(t_data.strip('icmp_seq='))
#                                             if 'time=' in t_data:
#                                                 rtt = float(t_data.strip('time='))
#                                         rtts[station][seq_number] = rtt
#                                         rtts_list.append(rtt)

#                                         # finding dropped packets
#                                         t_fail = t_fail.split()  # [' drop:', '0', '(0, 0.000)', 'rx:', '28', 'fail:', '0', 'bytes:', '1792', 'min/avg/max:', '2.160/3.422/5.190']
#                                         t_drop_val = t_fail[1]  # t_drop_val = '0'
#                                         t_drop_val = int(t_drop_val)  # type cast string to int
#                                         if t_drop_val != drop_count:
#                                             current_drop_packets = t_drop_val - drop_count
#                                             drop_count = t_drop_val
#                                             for drop_packet in range(1, current_drop_packets + 1):
#                                                 dropped_packets.append(seq_number - drop_packet)

#                                 if rtts_list == []:
#                                     rtts_list = [0]
#                                 min_rtt = str(min(rtts_list))
#                                 avg_rtt = str(sum(rtts_list) / len(rtts_list))
#                                 max_rtt = str(max(rtts_list))
#                                 self.result_json[station]['min_rtt'] = min_rtt
#                                 self.result_json[station]['avg_rtt'] = avg_rtt
#                                 self.result_json[station]['max_rtt'] = max_rtt
#                                 if list(rtts[station].keys()) != []:
#                                     required_sequence_numbers = list(range(1, max(rtts[station].keys())))
#                                     for seq in required_sequence_numbers:
#                                         if seq not in rtts[station].keys():
#                                             if seq in dropped_packets:
#                                                 rtts[station][seq] = 0
#                                             else:
#                                                 rtts[station][seq] = 0.11
#                                 else:
#                                     self.result_json[station]['rtts'] = {}
#                                 self.result_json[station]['rtts'] = rtts[station]
#                                 self.result_json[station]['remarks'] = self.generate_remarks(self.result_json[station])
#                                 # self.result_json[station]['dropped_packets'] = dropped_packets

# def monitor_real(self,result_data,Devices,ping_stats,rtts,rtts_list):
#     if isinstance(result_data, dict):
#                 for station in self.real_sta_list:
#                     current_device_data = Devices.devices_data[station]
#                     # logging.info(current_device_data)
#                     if station in result_data['name']:
#                         # logging.info(result_data['last results'].split('\n'))
#                         if len(result_data['last results']) != 0:
#                             result = result_data['last results'].split('\n')
#                             if len(result) > 1:
#                                 last_result = result[-2]
#                             else:
#                                 last_result = result[-1]
#                         else:
#                             last_result = ""

#                         hw_version = current_device_data['hw version']
#                         if "Win" in hw_version:
#                             os = "Windows"
#                         elif "Linux" in hw_version:
#                             os = "Linux"
#                         elif "Apple" in hw_version:
#                             os = "Mac"
#                         else:
#                             os = "Android"

#                         self.result_json[station] = {
#                             'command': result_data['command'],
#                             'sent': result_data['tx pkts'],
#                             'recv': result_data['rx pkts'],
#                             'dropped': result_data['dropped'],
#                             'mac': current_device_data['mac'],
#                             'ip': current_device_data['ip'],
#                             'bssid': current_device_data['ap'],
#                             'ssid': current_device_data['ssid'],
#                             'channel': current_device_data['channel'],
#                             'mode': current_device_data['mode'],
#                             'name': [current_device_data['user'] if current_device_data['user'] != '' else current_device_data['hostname']][0],
#                             'os': os,
#                             'remarks': [],
#                             'last_result': [last_result][0]
#                         }
#                         ping_stats[station]['sent'].append(result_data['tx pkts'])
#                         ping_stats[station]['received'].append(result_data['rx pkts'])
#                         ping_stats[station]['dropped'].append(result_data['dropped'])
#                         self.result_json[station]['ping_stats'] = ping_stats[station]
#                         if len(result_data['last results']) != 0:
#                             temp_last_results = result_data['last results'].split('\n')[0: len(result_data['last results']) - 1]
#                             drop_count = 0  # let dropped = 0 initially
#                             dropped_packets = []
#                             # sample result - 64 bytes from 192.168.1.61: icmp_seq=28 time=3.66 ms *** drop: 0 (0, 0.000)  rx: 28  fail: 0  bytes: 1792 min/avg/max: 2.160/3.422/5.190
#                             for result in temp_last_results:
#                                 try:
#                                     # fetching the first part of the last result e.g., 64 bytes from 192.168.1.61: icmp_seq=28 time=3.66 ms into t_result and the remaining part into t_fail
#                                     t_result, t_fail = result.split('***')
#                                 except BaseException:
#                                     continue
#                                 t_result = t_result.split()
#                                 if 'icmp_seq=' not in result and 'time=' not in result:
#                                     continue
#                                 for t_data in t_result:
#                                     if 'icmp_seq=' in t_data:
#                                         seq_number = int(t_data.strip('icmp_seq='))
#                                     if 'time=' in t_data:
#                                         rtt = float(t_data.strip('time='))
#                                 rtts[station][seq_number] = rtt
#                                 rtts_list.append(rtt)

#                                 # finding dropped packets
#                                 t_fail = t_fail.split()  # [' drop:', '0', '(0, 0.000)', 'rx:', '28', 'fail:', '0', 'bytes:', '1792', 'min/avg/max:', '2.160/3.422/5.190']
#                                 t_drop_val = t_fail[1]  # t_drop_val = '0'
#                                 t_drop_val = int(t_drop_val)  # type cast string to int
#                                 if t_drop_val != drop_count:
#                                     current_drop_packets = t_drop_val - drop_count
#                                     drop_count = t_drop_val
#                                     for drop_packet in range(1, current_drop_packets + 1):
#                                         dropped_packets.append(seq_number - drop_packet)

#                         if rtts_list == []:
#                             rtts_list = [0]
#                         min_rtt = str(min(rtts_list))
#                         avg_rtt = str(sum(rtts_list) / len(rtts_list))
#                         max_rtt = str(max(rtts_list))
#                         self.result_json[station]['min_rtt'] = min_rtt
#                         self.result_json[station]['avg_rtt'] = avg_rtt
#                         self.result_json[station]['max_rtt'] = max_rtt
#                         if self.result_json[station]['os'] == 'Android' and isinstance(rtts, dict) and rtts != {}:
#                             if list(rtts[station].keys()) == []:
#                                 self.result_json[station]['sent'] = str(0)
#                                 self.result_json[station]['recv'] = str(0)
#                                 self.result_json[station]['dropped'] = str(0)
#                             else:
#                                 self.result_json[station]['sent'] = str(max(list(rtts[station].keys())))
#                                 self.result_json[station]['recv'] = str(len(rtts[station].keys()))
#                                 self.result_json[station]['dropped'] = str(int(self.result_json[station]['sent']) - int(self.result_json[station]['recv']))
#                         if len(rtts[station].keys()) != 0:
#                             required_sequence_numbers = list(range(1, max(rtts[station].keys())))
#                             for seq in required_sequence_numbers:
#                                 if seq not in rtts[station].keys():
#                                     if seq in dropped_packets:
#                                         rtts[station][seq] = 0
#                                     else:
#                                         rtts[station][seq] = 0.11
#                         self.result_json[station]['rtts'] = rtts[station]
#                         self.result_json[station]['remarks'] = self.generate_remarks(self.result_json[station])

#     else:
#         for station in self.real_sta_list:
#                         current_device_data = Devices.devices_data[station]
#                         # print('<<<<<<<<<<<<<<<<<<<', current_device_data)
#                         for ping_device in result_data:
#                             ping_endp, ping_data = list(ping_device.keys())[
#                                 0], list(ping_device.values())[0]
#                             eid = str(ping_data['eid'])
#                             self.sta_list = list(self.sta_list)
#                             # Removing devices with UNKNOWN CX
#                             if 'UNKNOWN' in ping_endp:
#                                 device_id = eid.split('.')[0] + '.' + eid.split('.')[1]
#                                 if device_id == station.split('.')[0] + '.' + station.split('.')[1]:
#                                     self.sta_list.remove(station)
#                                     self.real_sta_list.remove(station)
#                                 logger.info(result_data)
#                                 logger.info("Excluding {} from report as there is no valid generic endpoint creation during the test(UNKNOWN CX)".format(device_id))
#                                 continue
#                             if station in ping_endp:
#                                 if len(ping_data['last results']) != 0:
#                                     result = ping_data['last results'].split('\n')
#                                     if len(result) > 1:
#                                         last_result = result[-2]
#                                     else:
#                                         last_result = result[-1]
#                                 else:
#                                     last_result = ""

#                                 hw_version = current_device_data['hw version']
#                                 if "Win" in hw_version:
#                                     os = "Windows"
#                                 elif "Linux" in hw_version:
#                                     os = "Linux"
#                                 elif "Apple" in hw_version:
#                                     os = "Mac"
#                                 else:
#                                     os = "Android"

#                                 self.result_json[station] = {
#                                     'command': ping_data['command'],
#                                     'sent': ping_data['tx pkts'],
#                                     'recv': ping_data['rx pkts'],
#                                     'dropped': ping_data['dropped'],
#                                     'mac': current_device_data['mac'],
#                                     'ip': current_device_data['ip'],
#                                     'bssid': current_device_data['ap'],
#                                     'ssid': current_device_data['ssid'],
#                                     'channel': current_device_data['channel'],
#                                     'mode': current_device_data['mode'],
#                                     'name': [current_device_data['user'] if current_device_data['user'] != '' else current_device_data['hostname']][0],
#                                     'os': os,
#                                     'remarks': [],
#                                     'last_result': [last_result][0]
#                                 }
#                                 ping_stats[station]['sent'].append(ping_data['tx pkts'])
#                                 ping_stats[station]['received'].append(ping_data['rx pkts'])
#                                 ping_stats[station]['dropped'].append(ping_data['dropped'])
#                                 self.result_json[station]['ping_stats'] = ping_stats[station]
#                                 if len(ping_data['last results']) != 0:
#                                     temp_last_results = ping_data['last results'].split('\n')[0: len(ping_data['last results']) - 1]
#                                     drop_count = 0  # let dropped = 0 initially
#                                     dropped_packets = []
#                                     for result in temp_last_results:
#                                         # sample result - 64 bytes from 192.168.1.61: icmp_seq=28 time=3.66 ms *** drop: 0 (0, 0.000)  rx: 28  fail: 0  bytes: 1792 min/avg/max: 2.160/3.422/5.190
#                                         if 'time=' in result:
#                                             try:
#                                                 # fetching the first part of the last result e.g., 64 bytes from 192.168.1.61: icmp_seq=28 time=3.66 ms into t_result and the remaining part into t_fail
#                                                 t_result, t_fail = result.split('***')
#                                             except BaseException:
#                                                 continue
#                                             t_result = t_result.split()
#                                             if 'icmp_seq=' not in result and 'time=' not in result:
#                                                 continue
#                                             for t_data in t_result:
#                                                 if 'icmp_seq=' in t_data:
#                                                     seq_number = int(t_data.strip('icmp_seq='))
#                                                 if 'time=' in t_data:
#                                                     rtt = float(t_data.strip('time='))
#                                             rtts[station][seq_number] = rtt
#                                             rtts_list.append(rtt)

#                                             # finding dropped packets
#                                             t_fail = t_fail.split()  # [' drop:', '0', '(0, 0.000)', 'rx:', '28', 'fail:', '0', 'bytes:', '1792', 'min/avg/max:', '2.160/3.422/5.190']
#                                             t_drop_val = t_fail[1]  # t_drop_val = '0'
#                                             t_drop_val = int(t_drop_val)  # type cast string to int
#                                             if t_drop_val != drop_count:
#                                                 current_drop_packets = t_drop_val - drop_count
#                                                 drop_count = t_drop_val
#                                                 for drop_packet in range(1, current_drop_packets + 1):
#                                                     dropped_packets.append(seq_number - drop_packet)

#                                 if rtts_list == []:
#                                     rtts_list = [0]
#                                 min_rtt = str(min(rtts_list))
#                                 avg_rtt = str(sum(rtts_list) / len(rtts_list))
#                                 max_rtt = str(max(rtts_list))
#                                 self.result_json[station]['min_rtt'] = min_rtt
#                                 self.result_json[station]['avg_rtt'] = avg_rtt
#                                 self.result_json[station]['max_rtt'] = max_rtt
#                                 if self.result_json[station]['os'] == 'Android' and isinstance(rtts, dict) and rtts != {}:
#                                     if list(rtts[station].keys()) == []:
#                                         self.result_json[station]['sent'] = str(0)
#                                         self.result_json[station]['recv'] = str(0)
#                                         self.result_json[station]['dropped'] = str(0)
#                                     else:
#                                         self.result_json[station]['sent'] = str(max(list(rtts[station].keys())))
#                                         self.result_json[station]['recv'] = str(len(rtts[station].keys()))
#                                         self.result_json[station]['dropped'] = str(int(self.result_json[station]['sent']) - int(self.result_json[station]['recv']))
#                                 if len(rtts[station].keys()) != 0:
#                                     required_sequence_numbers = list(range(1, max(rtts[station].keys())))
#                                     for seq in required_sequence_numbers:
#                                         if seq not in rtts[station].keys():
#                                             if seq in dropped_packets:
#                                                 rtts[station][seq] = 0
#                                             else:
#                                                 rtts[station][seq] = 0.11
#                                         # print(station, rtts[station])
#                                 self.result_json[station]['rtts'] = rtts[station]
#                                 self.result_json[station]['remarks'] = self.generate_remarks(self.result_json[station])
#                                 # self.result_json[station]['dropped_packets'] = dropped_packets
                
# def monitor_virtual(self, result_data, ports_data, ping_stats, rtts, rtts_list, lock):

#     if isinstance(result_data, dict):

#         for station in self.sta_list:
#             if station not in self.real_sta_list:

#                 current_device_data = ports_data[station]

#                 if station.split('.')[2] in result_data['name']:

#                     # -----------------------------
#                     # PARSING SECTION (NO LOCK)
#                     # -----------------------------
#                     ping_data = result_data
#                     dropped_packets = []
#                     drop_count = 0

#                     if len(ping_data['last results']) != 0 and 'min/avg/max' in ping_data['last results']:

#                         temp_last_results = ping_data['last results'].split('\n')[
#                             0: len(ping_data['last results']) - 1
#                         ]

#                         for result in temp_last_results:
#                             try:
#                                 t_result, t_fail = result.split('***')
#                             except BaseException:
#                                 continue

#                             t_result = t_result.split()

#                             if 'icmp_seq=' not in result and 'time=' not in result:
#                                 continue

#                             for t_data in t_result:
#                                 if 'icmp_seq=' in t_data:
#                                     seq_number = int(t_data.strip('icmp_seq='))
#                                 if 'time=' in t_data:
#                                     rtt = float(t_data.strip('time='))

#                             # WRITE to shared rtts inside lock
#                             with lock:
#                                 rtts[station][seq_number] = rtt
#                                 rtts_list.append(rtt)

#                             t_fail = t_fail.split()
#                             t_drop_val = int(t_fail[1])

#                             if t_drop_val != drop_count:
#                                 current_drop_packets = t_drop_val - drop_count
#                                 drop_count = t_drop_val
#                                 for drop_packet in range(1, current_drop_packets + 1):
#                                     dropped_packets.append(seq_number - drop_packet)

#                     if rtts_list == []:
#                         rtts_list = [0]

#                     min_rtt = str(min(rtts_list))
#                     avg_rtt = str(sum(rtts_list) / len(rtts_list))
#                     max_rtt = str(max(rtts_list))

#                     # -----------------------------
#                     # SHARED WRITES (LOCKED)
#                     # -----------------------------
#                     with lock:

#                         self.result_json[station] = {
#                             'command': ping_data['command'],
#                             'sent': ping_data['tx pkts'],
#                             'recv': ping_data['rx pkts'],
#                             'dropped': ping_data['dropped'],
#                             'mac': current_device_data['mac'],
#                             'ip': current_device_data['ip'],
#                             'bssid': current_device_data['ap'],
#                             'ssid': current_device_data['ssid'],
#                             'channel': current_device_data['channel'],
#                             'mode': current_device_data['mode'],
#                             'name': station,
#                             'os': 'Virtual',
#                             'remarks': [],
#                             'last_result': self.get_safe_last_result(
#                                 ping_data.get('last results', '')
#                             )
#                         }

#                         ping_stats[station]['sent'].append(ping_data['tx pkts'])
#                         ping_stats[station]['received'].append(ping_data['rx pkts'])
#                         ping_stats[station]['dropped'].append(ping_data['dropped'])

#                         self.result_json[station]['ping_stats'] = ping_stats[station]
#                         self.result_json[station]['min_rtt'] = min_rtt
#                         self.result_json[station]['avg_rtt'] = avg_rtt
#                         self.result_json[station]['max_rtt'] = max_rtt

#                         if list(rtts[station].keys()) != []:
#                             required_sequence_numbers = list(
#                                 range(1, max(rtts[station].keys()))
#                             )
#                             for seq in required_sequence_numbers:
#                                 if seq not in rtts[station].keys():
#                                     if seq in dropped_packets:
#                                         rtts[station][seq] = 0
#                                     else:
#                                         rtts[station][seq] = 0.11
#                         else:
#                             self.result_json[station]['rtts'] = {}

#                         self.result_json[station]['rtts'] = rtts[station]
#                         self.result_json[station]['remarks'] = \
#                             self.generate_remarks(self.result_json[station])

# client_type = "Real"
# print(type(client_type))

# client_type = client_type.split(',')
# print(type(client_type))

# list1 = ["Manoj"]

# list2 = ["Thunder", "mango"]

# list3 = list1 + list2
# print(list3)




# --------------------------------------
# 1. Add virtual  clients and real clients individualy in test inut box
# 2. in final table add column ofclient type to check whether it is real/monitor_virtual
# 3. in graph add client names in y-axis
# 4. clent names is missing in final able for real devices


bands = ""
band_list = bands.split(',')

print(band_list)
