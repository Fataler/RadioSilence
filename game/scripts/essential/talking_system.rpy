init -1 python:
    import functools as ft
    from renpy.curry import curry
    
    talk_key = 'talk_'
    speaking = None

    def while_speaking(character_name, speak_d, done_d, st, at):
        if speaking == character_name:
            return speak_d, .1
        else:
            return done_d, None

    curried_while_speaking = curry(while_speaking)

    def WhileSpeaking(character_name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(character_name, speaking_d, done_d))

    def speaker_callback(character_name, event, **kwargs):        
        global speaking
        
        if event == "show" or event == "begin":
            speaking = character_name
        elif event == 'slow_done':
            speaking = None
        elif event == "end":
            speaking = None

    speaker = curry(speaker_callback)

    def get_character_pose(character_name, current_attrs): #legacy
        for attr in current_attrs:
            if not attr.startswith(talk_key):
                talk_attr = f'{talk_key}{attr}'
                if renpy.has_image((character_name, talk_attr)):
                    return attr
            elif attr.startswith(talk_key):
                base_attr = attr[len(talk_key):]
                if renpy.has_image((character_name, base_attr)):
                    return base_attr
        
        return None

    def talking_callback(event, character_name, interact=True, **kwargs): #legacy
        """Callback для персонажей с talk_pose структурой (alice, izumi)"""
        if not interact:
            return
            
        if preferences.text_cps > 0:
            if event == 'begin':
                if renpy.showing(character_name):
                    current_attrs = renpy.get_attributes(character_name)
                    current_pose = get_character_pose(character_name, current_attrs)
                    
                    if current_pose:
                        talk_attr = f'{talk_key}{current_pose}'
                        renpy.show(f'{character_name} {talk_attr}')
                    
            elif event == 'slow_done' or event == 'end':
                if renpy.showing(character_name):
                    current_attrs = renpy.get_attributes(character_name)
                    current_pose = get_character_pose(character_name, current_attrs)
                    
                    if current_pose:
                        renpy.show(f'{character_name} {current_pose}')
                        
                renpy.restart_interaction()

    def layered_talking_callback(event, character_name, interact=True, **kwargs):
        if not interact:
            return
            
        if preferences.text_cps > 0:
            if event == 'begin' or event == 'show':
                if renpy.showing(character_name):
                    renpy.show(f'{character_name} talk')
                    
            elif event == 'slow_done' or event == 'end':
                if renpy.showing(character_name):
                    renpy.show(f'{character_name} -talk')
                        
                renpy.restart_interaction()