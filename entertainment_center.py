import media
import fresh_tomatoes

# the terminal info
TERMINAL_NAME = "The Terminal"
TERMINAL_DESCRIPTION = "Is a 2004 American romantic comedy film"
TERMINAL_IMAGE = "http://www.movieartarena.com/imgs/terminalf.jpg"
TERMINAL_TRAILER = "https://www.youtube.com/watch?v=HGOaj_IetHY"

the_terminal = media.Movie(TERMINAL_NAME, TERMINAL_DESCRIPTION,
                           TERMINAL_IMAGE, TERMINAL_TRAILER)

# the croods info

CROOD_NAME = "The Croods"
CROOD_DESCRIPTION = "Is a 2013 American 3D animated adventure comedy film"
CROOD_IMAGE = "http://www.aceshowbiz.com/images/still/the-croods-pstr06.jpg"
CROOD_TRAILER = "https://www.youtube.com/watch?v=4fVCKy69zUY"

the_croods = media.Movie(CROOD_NAME, CROOD_DESCRIPTION,
                         CROOD_IMAGE, CROOD_TRAILER)

# the fault in our star info
FAULT_NAME = "The fault in our star"
FAULT_DESCRIPTION = "Is narrated by a sixteen-year-old cancer patient"
FAULT_IMAGE = "http://static.tumblr.com/4pxlsbd/xzJn3p0ei/"\
              + "tfios_soundtrack_cover.jpg"
FAULT_TRAILER = "https://www.youtube.com/watch?v=9ItBvH5J6ss"

fault_in_our_star = media.Movie(FAULT_NAME, FAULT_DESCRIPTION,
                                FAULT_IMAGE, FAULT_TRAILER)


MOVIES = [the_terminal, the_croods, fault_in_our_star]

fresh_tomatoes.open_movies_page(MOVIES)
