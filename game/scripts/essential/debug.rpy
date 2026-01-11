default _show_bounds = False

init -1 python:
    import os, datetime

    def log_debug(msg):
        path = os.path.join(config.basedir, "debug_log.txt")
        ts   = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(path, "a", encoding="utf-8") as f:
            f.write(f"[{ts}] {msg}\n")
        if renpy.config.developer:
            print(f"[{ts}] {msg}")

    from functools import partial as curry

    if renpy.config.developer:
        try:
            overlay_attr = getattr(config, "overlay_screens", None)
            overlays = list(overlay_attr) if overlay_attr is not None and hasattr(overlay_attr, '__iter__') else []

            to_add = ["dev_hotkeys", "dev_hud", "debug_bounds_info", "debug_bounds_overlay"]
            for name in to_add:
                if name not in overlays:
                    overlays.append(name)
            config.overlay_screens = overlays

            if hasattr(config, "always_shown_screens"):
                always_attr = getattr(config, "always_shown_screens", None)
                always = list(always_attr) if always_attr is not None and hasattr(always_attr, '__iter__') else []

                for name in ["dev_hotkeys", "dev_hud"]:
                    if name not in always:
                        always.append(name)
                config.always_shown_screens = always
        except Exception as e:
            log_debug(f"[Debug] Error setting up screens: {e}")
            try:
                config.overlay_screens += ["dev_hotkeys", "dev_hud", "debug_bounds_info", "debug_bounds_overlay"]
                if hasattr(config, "always_shown_screens"):
                    config.always_shown_screens += ["dev_hotkeys", "dev_hud"]
            except Exception as fallback_e:
                log_debug(f"[Debug] Fallback failed: {fallback_e}")

    class DebugBorder(renpy.Displayable):
        """Draws a rectangular border using Solid without filling the center."""
        def __init__(self, color="#ff0000cc", thickness=2, **kwargs):
            renpy.Displayable.__init__(self, **kwargs)
            self.color = color
            self.thickness = int(thickness)
            self.solid = Solid(self.color)

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)
            t = self.thickness
            if width <= 0 or height <= 0 or t <= 0:
                return r
            # top
            r.blit(renpy.render(self.solid, width, t, st, at), (0, 0))
            # bottom
            r.blit(renpy.render(self.solid, width, t, st, at), (0, max(0, height - t)))
            # left
            r.blit(renpy.render(self.solid, t, height, st, at), (0, 0))
            # right
            r.blit(renpy.render(self.solid, t, height, st, at), (max(0, width - t), 0))
            return r

    _bounds_saved_foregrounds = {}
    _bounds_saved_outlines = {}

    def _get_all_styles():
        """Get all currently defined style names dynamically."""
        from renpy.store import style
        style_names = []

        known_styles = [
            # Base styles
            "default", "text", "fixed", "hbox", "vbox", "grid", "side", "window",
            "frame", "image", "animation",

            # Dialogue styles
            "say_label", "say_dialogue", "say_thought", "say_window",
            "say_who_window", "say_two_window_vbox", "say_vbox",

            # Menu styles
            "menu", "menu_caption", "menu_choice", "menu_choice_button",
            "menu_choice_chosen", "menu_choice_chosen_button", "menu_window",

            # Input styles
            "input", "input_text", "input_prompt", "input_window",

            # Button styles
            "button", "button_text", "small_button", "small_button_text",
            "radio_button", "radio_button_text", "check_button", "check_button_text",
            "large_button", "large_button_text",

            # Other UI elements
            "label", "label_text", "bar", "vbar", "slider", "vslider",
            "scrollbar", "vscrollbar", "viewport", "vpgrid",

            # Image styles
            "image_button", "image_button_image", "imagemap", "hotspot",
            "imagemap_button", "hotbar",

            # Layout styles
            "centered_window", "centered_text", "centered_vtext",
            "motion", "transform", "tile",

            # Link styles
            "hyperlink", "hyperlink_text", "ruby_text",

            # Game menu styles
            "mm_root", "gm_root",

            # Additional styles that might exist
            "confirm_frame", "skip_frame", "notify_frame",
            "file_slot", "page_button", "quick_button",

            # Project-specific styles from screens
            "say_textframe", "namebox", "pref_text_label", "pref_bar",
            "reset_button", "tooltip", "navigation_button", "choice_button",
            "choice_button_text", "slot_button", "quick_button_text",
            "main_menu_button", "game_menu_button"
        ]

        # Test each known style
        for style_name in known_styles:
            try:
                s = getattr(style, style_name)
                # Check if it has foreground property (indicating it's a real style)
                if hasattr(s, 'foreground'):
                    style_names.append(style_name)
            except Exception as e:
                log_debug(f"[DebugBounds] style {style_name} not available: {e}")

        if not style_names:
            log_debug("[DebugBounds] no styles found")

        log_debug(f"[DebugBounds] total styles found: {len(style_names)}")
        return style_names

    def _apply_debug_bounds():
        """Apply or revert global style foreground/outline overlays based on _show_bounds."""
        from renpy.store import style
        global _bounds_saved_foregrounds, _bounds_saved_outlines

        try:
            showing = renpy.store._show_bounds
        except Exception:
            showing = False

        if showing:
            all_styles = _get_all_styles()
            log_debug(f"[DebugBounds] found {len(all_styles)} styles")

            for sname in all_styles:
                try:
                    s = getattr(style, sname)
                    if sname not in _bounds_saved_foregrounds:
                        _bounds_saved_foregrounds[sname] = s.foreground
                    s.foreground = DebugBorder("#ff0000ff", 4)
                except Exception as e:
                    log_debug(f"[DebugBounds] skip {sname}: {e}")
                    continue
        else:
            # Revert foregrounds
            for sname, fg in list(_bounds_saved_foregrounds.items()):
                try:
                    getattr(style, sname).foreground = fg
                except Exception as e:
                    log_debug(f"[DebugBounds] revert error {sname}: {e}")
                    pass
            _bounds_saved_foregrounds.clear()

        renpy.style.rebuild()
        renpy.restart_interaction()

    def _toggle_debug_bounds():
        """Toggle bounds overlay and apply style changes."""
        renpy.store._show_bounds = not getattr(renpy.store, "_show_bounds", False)
        try:
            log_debug(f"[DebugBounds] toggled -> {renpy.store._show_bounds}")
            if renpy.store._show_bounds:
                renpy.notify("Debug bounds enabled - look for red borders around UI elements")
            else:
                renpy.notify("Debug bounds disabled")
        except Exception as e:
            log_debug(f"[DebugBounds] error: {e}")
            pass
        _apply_debug_bounds()

screen dev_hud():
    if _show_hud:
        frame align (1.0, 1.0) padding (6, 4) background "#0008":
            $ mouse_x, mouse_y = renpy.get_mouse_pos()
            $ rel_x = round(mouse_x / config.screen_width, 3)
            $ rel_y = round(mouse_y / config.screen_height, 3)
            text str(mouse_x) + " × " + str(mouse_y) + " (" + str(rel_x) + ", " + str(rel_y) + ")" style "debug_text"
        timer 0.33 action renpy.restart_interaction repeat True

screen debug_bounds_overlay():
    """Draw borders around actual displayables on screen."""
    zorder 1000
    if getattr(renpy.store, "_show_bounds", False):
        python:
            displayables = []
            try:
                # Method 2: Try scene lists if method 1 didn't work
                if not displayables:
                    try:
                        from renpy.display.core import scene_lists
                        for layer_name in scene_lists.layers:
                            layer = scene_lists.layers[layer_name]
                            for d in layer:
                                try:
                                    placement = renpy.get_placement(d)
                                    if placement and len(placement) >= 4:
                                        x, y, width, height = placement[:4]
                                        if (width > 0 and height > 0 and width < config.screen_width and height < config.screen_height):
                                            displayables.append((x, y, width, height, str(type(d).__name__)))
                                            log_debug(f"[DebugBounds] ADDED from scene_lists: {type(d).__name__} at ({x}, {y}, {width}, {height})")
                                except:
                                    pass
                    except Exception as e:
                        log_debug(f"[DebugBounds] Scene lists error: {e}")

                log_debug(f"[DebugBounds] Total displayables to render: {len(displayables)}")

            except Exception as e:
                log_debug(f"[DebugBounds] Error in overlay: {e}")

        for x, y, width, height, type_name in displayables:
            python:
                if "text" in type_name.lower():
                    color = "#00ff0080"
                elif "button" in type_name.lower():
                    color = "#ff000080"
                else:
                    color = "#ff00ff80"
            add Solid(color, xsize=width, ysize=height):
                xpos x
                ypos y

screen debug_bounds_info():
    if getattr(renpy.store, "_show_bounds", False):
        frame align (0.0, 1.0) padding (6, 4) background "#0008":
            text "Bounds: ON (Shift+B/F8)" style "debug_text"

screen dev_hotkeys():
    key "shift_K_h" action ToggleVariable("_show_hud")
    key "shift_K_j" action Function(_open_jump)
    key "shift_K_l" action Function(ShowMenu("image_tools"))
    key "shift_K_b" action Function(_toggle_debug_bounds)
    key "K_F8" action Function(_toggle_debug_bounds)

style debug_jump_textbutton is gui_button_text
style debug_jump_textbutton_text is gui_button_text:
    size 20
    xalign 0.0

style debug_text:
    color "#ffffff"
