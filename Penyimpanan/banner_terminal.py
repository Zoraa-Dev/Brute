#!/usr/bin/env python3
# -*- coding:utf-8

from Penyimpanan.Database.data import * 

class Terminal:
    def __init__(self) -> None:
        pass
        
    def clear_terminalize(self):
        try: os.system('clear' if 'linux' in sys.platform.lower() else 'cls')
        except (Exception) as e: os.system('clear')
        
    def banner_instagram(self):
        self.clear_terminalize()
        Console().print('''\r[white]
╭━━━╮╱╱╱╱╱╱╱╱╱╭╮╭━━┳━━━╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱┃┃╰┫┣┫╭━╮┃
┃╰━━┳┳╮╭┳━━┳━━┫┃╱┃┃┃┃╱╰╯
╰━━╮┣┫╰╯┃╭╮┃┃━┫┃╱┃┃┃┃╭━╮
┃╰━╯┃┃┃┃┃╰╯┃┃━┫╰┳┫┣┫╰┻━┃
╰━━━┻┻┻┻┫╭━┻━━┻━┻━━┻━━━╯
╱╱╱╱╱╱╱╱┃┃  Author: [green]Zoraa Dev [white]
╱╱╱╱╱╱╱╱╰╯ V [green]20.1[white]''')
        return(True)
            
            
