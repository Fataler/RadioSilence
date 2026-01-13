python early:

    def parse_custom_statement(lex):
        return lex.rest()

    def execute_ds(name):
        trans = getattr(renpy.store, 'ds', renpy.display.transition.Dissolve(1.0))
        renpy.exports.with_statement(trans)

    def execute_showd(name):
        trans = getattr(renpy.store, 'ds', renpy.display.transition.Dissolve(1.0))
        name_parts = name.split()
        if name_parts:
            renpy.exports.show(tuple(name_parts))
            renpy.exports.with_statement(trans)

    def predict_showd(name):
        name_parts = name.split()
        if name_parts:
            return renpy.exports.predict_show(tuple(name_parts))
        return []

    def execute_hidef(name):
        trans = getattr(renpy.store, 'ds', renpy.display.transition.Dissolve(1.0))
        renpy.exports.hide(name.strip())
        renpy.exports.with_statement(trans)

    def predict_hidef(name):
        return renpy.exports.predict_hide(name.strip())

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

init -100 python:
    def _get_cubic_warper():
        try:
            return renpy.atl.warpers.get('easein_cubic', lambda t: t**3)
        except:
            return lambda t: t**3

    ds = Dissolve(1.0, time_warp=_get_cubic_warper())
    
    def Sdissolve(t):
        return Dissolve(t, time_warp=_get_cubic_warper())
