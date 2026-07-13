import math
import time
import threading
from collections import namedtuple

import curses


# Constants
speed_mult = 0.4567

venus_orbit_radius = 0.72
mars_orbit_radius = 1.524
jupiter_orbit_radius = 5.203

venus_orbit_period = 0.615
mars_orbit_period = 1.881
jupiter_orbit_period = 11.86


# Initialize curses
stdscr = curses.initscr()
curses.curs_set(False)
curses.start_color()
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

sh, sw = stdscr.getmaxyx()

Planet = namedtuple('Planet', 'name, orbit_radius, orbit_period, color_pair, y, x')

# Define the planets
venus = Planet('Venus', venus_orbit_radius, venus_orbit_period, curses.color_pair(1), 0, 0)
mars = Planet('Mars', mars_orbit_radius, mars_orbit_period, curses.color_pair(2), 0, 0)
jupiter = Planet('Jupiter', jupiter_orbit_radius, jupiter_orbit_period, curses.color_pair(3), 0, 0)

planets = [venus, mars, jupiter]

max_orbit_radius = max(planet.orbit_radius for planet in planets)

# function to draw a planet, contains calculation
def draw_planet(planet, current_time):

    planet_angle = speed_mult * current_time / planet.orbit_period % 1 * math.pi * 2

    y = math.sin(planet_angle) * planet.orbit_radius
    x = math.cos(planet_angle) * planet.orbit_radius

    # Limit the y and x values to fit within the screen dimensions
    y = int(sh / 2 + y * sh / (2 * max_orbit_radius))
    x = int(sw / 2 + x * sw / (2 * max_orbit_radius))

    # Ensure the coordinates are within the screen boundaries
    y = max(0, min(sh - 1, y))
    x = max(0, min(sw - 1, x))

    stdscr.attron(planet.color_pair)
    stdscr.addch(y, x, planet.name[0])
    stdscr.attroff(planet.color_pair)


if __name__ == '__main__':
    running = True


    def check_keypress():
        global running
        while running:
            key = stdscr.getch(time.time() * 1000)
            if key == ord('q'):
                running = False


    keypress_thread = threading.Thread(target=check_keypress)
    keypress_thread.start()

    while running:
        # Calculate the positions of the planets
        current_time = time.time()

        # Clear the screen
        stdscr.clear()

        # Draw the planets
        for planet in planets:
            draw_planet(planet, current_time)

        # Refresh the screen
        stdscr.refresh()

        # Add a short delay using curses.napms()
        curses.napms(25)

    # Set the running flag to False to allow the keypress checking thread to exit
    running = False
    keypress_thread.join()