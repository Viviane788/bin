#!/usr/bin/env python3
#
# Requires xcwd

import sys
import subprocess
import i3ipc
import os

i3 = i3ipc.Connection()


def on(i3, e):
    if e.container.window_class == 'kitty':
        e.container.command('floating enable')

        e.container.command("resize set 748 px 460 px, move window to position 347 px 230 px")
        sys.exit(0)


workspace_empty = i3.get_tree().find_focused().type == 'workspace'

# Not sure why, but when adding $(xcwd) to the list, it does not work properly
# thats why I am using os.popen() instead.
#subprocess.Popen(['kitty', '--title', 'kitty', '-d','"$(xcwd)"'], close_fds=True)

os.popen("kitty --title kitty -d $(xcwd)")

if not workspace_empty:
    sys.exit(0)

i3.on('window::new', on)
try:
    i3.main()
finally:
    i3.main_quit()
