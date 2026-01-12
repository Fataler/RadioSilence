import renpy

"""renpy
python early:
"""

def ease_curve(t):
    return t * t * (3.0 - 2.0 * t)

ease_dissolve = Dissolve(1.0, time_warp=_warper.easein_cubic)

def Sdissolve(t):
    return Dissolve(t, time_warp=_warper.easein_cubic)

renpy.store.ds = ease_dissolve
renpy.store.Sdissolve = Sdissolve

def parse_custom_statement(lex):
    return lex.rest()

def execute_ds(name):
    renpy.with_statement(ease_dissolve)

def execute_showd(name):
    name_parts = name.split()
    if name_parts:
        renpy.show(tuple(name_parts))
        renpy.with_statement(ease_dissolve)

def predict_showd(name):
    name_parts = name.split()
    if name_parts:
        return renpy.predict_show(tuple(name_parts))
    return []

def execute_hidef(name):
    renpy.hide(name.strip())
    renpy.with_statement(ease_dissolve)

def predict_hidef(name):
    return renpy.predict_hide(name.strip())

renpy.register_statement("ds", 
                        parse=parse_custom_statement, 
                        execute=execute_ds)

renpy.register_statement("showd", 
                        parse=parse_custom_statement, 
                        execute=execute_showd, 
                        predict=predict_showd)

renpy.register_statement("hidef", 
                        parse=parse_custom_statement, 
                        execute=execute_hidef, 
                        predict=predict_hidef)
