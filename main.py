import os.path
from datetime import timedelta
from time import time
from tkinter import Tk, Button
from Background import Background
from Bird import Bird
from Tubes import Tubes

class App(Tk, Settings):
    __background_animation_speed = 720
    __bestScore = 0
    __bird_descend_speed = 35
    __buttons = []
    __playing = False
    __score = 0
    __time = "%H:%M:%S"

    def __init__(self):
        Tk.__init__(self)
        self.setOptions()
        if all([self.window_width, self.window_height]):
            self.__width = self.window_width
            self.__height = self.window_height
        else:
            self.__width = self.winfo_screenwidth()
            self.__height = self.winfo_screenheight()
        self.title(self.window_name)
        self.geometry("{}x{}".format(self.__width, self.__height))
        self.resizable(*self.window_rz)
        self.attributes("-fullscreen", self.window_fullscreen)
        self["bg"] = "black"
        for file in self.images_fp:
            if not os.path.exists(file):
                raise FileNotFoundError(
                    "The following file was not found:\n{}".format(file))
        self.__startButton_image = Background.getPhotoImage(
            image_path=self.startButton_fp,
            width=(self.__width // 100) * self.button_width,
            height=(self.__height // 100) * self.button_height,
            closeAfter=True
        )[0]
        self.__exitButton_image = Background.getPhotoImage(
            image_path=self.exitButton_fp,
            width=(self.__width // 100) * self.button_width,
            height=(self.__height // 100) * self.button_height,
            closeAfter=True
        )[0]
        self.__title_image = Background.getPhotoImage(
            image_path=self.title_fp,
            width=(self.__width // 100) * self.title_width,
            height=(self.__height // 100) * self.title_height,
            closeAfter=True
        )[0]
        self.__scoreboard_image = Background.getPhotoImage(
            image_path=self.scoreboard_fp,
            width=(self.__width // 100) * self.scoreboard_width,
            height=(self.__height // 100) * self.scoreboard_height,
            closeAfter=True
        )[0]
        self.__background_animation_speed //= self.__width / 100
        self.__background_animation_speed = int(
            self.__background_animation_speed)
        self.__bird_descend_speed //= self.__height / 100
        self.__bird_descend_speed = int(self.__bird_descend_speed)

    def changeFullscreenOption(self, event=None):

        self.window_fullscreen = not self.window_fullscreen
        self.attributes("-fullscreen", self.window_fullscreen)

    def close(self, event=None):

        self.saveScore()
        try:
            self.__background.stop()
            self.__bird.kill()
            self.__tubes.stop()
        finally:
            quit()


if __name__ == "__main__":
    try:
        app = App()
        app.init()
        app.mainloop()
    except FileNotFoundError as error:
        print(error)

