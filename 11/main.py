import time
import threading
import dearpygui.dearpygui as de_py_gu

running = False
progress_in_percent = 0
DELAY = 0.05


def run_task():
    global running
    global progress_in_percent
    print("Running...")

    for i in range(1, 101):
        if not running:
            return
        progress_in_percent = i
        de_py_gu.set_value(progress_bar, 1 / 100 * i)
        de_py_gu.configure_item(progress_bar, overlay=f"{i}%")
        time.sleep(DELAY)

    print("Loading finished")
    running = False
    de_py_gu.set_item_label(button_start, "Finished!")
    de_py_gu.disable_item(button_start)

    width, height, channels, data = de_py_gu.load_image("loaded.png")

    with de_py_gu.texture_registry():
        de_py_gu.add_static_texture(width=width, height=height, default_value=data, tag="tag_loaded")

    with de_py_gu.window(label="Loaded splash screen", width=width, height=height):
        de_py_gu.add_image("tag_loaded")


def start_stop_callback():
    global running
    if not running:
        print("Loading started")
        running = True
        thread = threading.Thread(target=run_task, args=(), daemon=True)
        thread.start()
        de_py_gu.set_item_label(button_start, "Loading...")


if __name__ == "__main__":
    de_py_gu.create_context()

    with de_py_gu.font_registry():
        font_default = de_py_gu.add_font("Hack-Bold.ttf", 48)

    with de_py_gu.window() as primary_window:
        progress_bar = de_py_gu.add_progress_bar(default_value=0, width=-1, overlay="0%")
        with de_py_gu.group(horizontal=True):
            button_start = de_py_gu.add_button(label="Start loading", width=400, callback=start_stop_callback)
            de_py_gu.bind_item_font(button_start, font_default)

    de_py_gu.set_primary_window(primary_window, True)
    de_py_gu.create_viewport(width=800, height=400, title="Loading progress slider imitation", resizable=False)
    de_py_gu.setup_dearpygui()
    de_py_gu.show_viewport()
    de_py_gu.start_dearpygui()
    de_py_gu.destroy_context()
