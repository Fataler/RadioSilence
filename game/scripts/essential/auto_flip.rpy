init -1 python:
    from renpy.curry import curry
    
    def check_flip_direction_with_tag(tag, default_direction, trans, st, at):
        try:
            attributes = renpy.get_attributes(tag)
            
            if attributes:
                if 'left' in attributes:
                    trans.xzoom = 1.0 if default_direction == 'left' else -1.0
                elif 'right' in attributes:
                    trans.xzoom = 1.0 if default_direction == 'right' else -1.0
                else:
                    trans.xzoom = 1.0
            else:
                trans.xzoom = 1.0
        except Exception as e:
            renpy.log(f"Error in auto_flip for {tag}: {e}")
            trans.xzoom = 1.0
        return None

    curried_flip = curry(check_flip_direction_with_tag)

init -1:
    transform auto_flip(tag, default_direction="right"):
        on show:
            function curried_flip(tag, default_direction)
        on replace:
            function curried_flip(tag, default_direction)
        on hide:
            function curried_flip(tag, default_direction)