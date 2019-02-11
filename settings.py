import random
class Settings():
    """储存所有设置"""
    def __init__(self):
        """初始化设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.bg_image = 'images/39072081_p0.jpg'

        # 上升的火焰
        self.fire_width = 3
        self.fire_height = 10
        # self.fire_speed = 3
        self.fire_color = [(255, 255, 255), (255, 0, 0), (64, 224, 205),
                           (252, 230, 202), (237, 145, 33), (255, 255, 0)]

        # 爆炸的速度，时间，大小
        self.size = 50
        self.expend_v = [5, 7, 9, 10, 11, 12, 13, 14, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20,
                         21, 21, 21, 22, 22, 22, 23, 23, 23, 23, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25]
        self.expend_size_width = 2
        self.expend_size_height = 2
        self.tho = 360

        # 重力加速度
        self.GRIVITY = 1
