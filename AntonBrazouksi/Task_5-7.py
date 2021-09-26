# 1. Mod_b imports after mod_c, which changes the value of
#   mod_c.x variable to 5 (same)
# 2. The added statement in mod_b changes mod_c.x
# variable value from 5 to [1,2,3]. 
# 3. from mod_c import * and from mod_b import * change 
# had no effect.
