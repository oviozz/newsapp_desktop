


class SwitchScreen:
    def switch_screen(self, screen, tab_widget):
        if screen == 'home':
            return tab_widget.setCurrentIndex(0)

        elif screen == 'search':
            return tab_widget.setCurrentIndex(1)

        elif screen == 'category':
            return tab_widget.setCurrentIndex(2)

        elif screen == 'media':
            return tab_widget.setCurrentIndex(3)

        elif screen == 'weather':
            return tab_widget.setCurrentIndex(4)








