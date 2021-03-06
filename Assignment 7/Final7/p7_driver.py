import subprocess
import json
import collections
import random
import sys
import shlex
import p7_helper


G = subprocess.Popen(shlex.split("gringo level-core.lp level-style.lp level-sim.lp level-shortcuts.lp -c width=7"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
R = subprocess.Popen(shlex.split("reify"), stdin = G.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
C = subprocess.Popen(shlex.split("clingo - meta.lp metaD.lp metaO.lp metaS.lp --parallel-mode=4 --outf=2"), stdin = R.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

out, err = C.communicate()
if err:
    print err


design = p7_helper.parse_json_result(out)
print p7_helper.side_by_side(p7_helper.render_ascii_dungeon(design), *[p7_helper.render_ascii_touch(design,i) for i in range(1,4)])
