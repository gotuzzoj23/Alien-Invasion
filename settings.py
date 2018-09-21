import pygame


class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship's settings
        self.ship_speed_factor = 1.5  #100
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 5  #50
        self.bullet_width = 10  #500
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        # Alien settings
        self.alien_speed_factor = 5 #30
        self.fleet_drop_speed = 10 #15
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughput the game."""
        self.ship_speed_factor =  5 #50
        self.bullet_speed_factor =  3  #10
        self.alien_speed_factor = 2 #2
        # Fleet direction of 1 represents right ; -1 represents left.
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)


    def start_music(self):
        pygame.mixer.music.load("music/Mozart_Omni.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

