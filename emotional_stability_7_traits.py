from manim import *
import numpy as np


class EmotionalStability7Traits(Scene):
    """情绪稳定到让对手害怕的7个特征"""

    def construct(self):
        # 配置
        self.camera.background_color = BLACK
        config.pixel_height = 1080
        config.pixel_width = 1920
        config.frame_height = 8
        config.frame_width = 14.22

        # 创建背景网格
        grid = self.create_grid()
        self.add(grid)

        # ========== 片头 ==========
        self.show_intro()

        # ========== 7个特征 ==========
        traits = [
            ("1. 面对挑衅，面不改色", "心跳如常，让对方的攻击\n像打在棉花上"),
            ("2. 计划被打乱，从容调整", "不抱怨不抓狂，\n像水流一样绕道而行"),
            ("3. 听到坏消息，先深呼吸", "给自己3秒缓冲，\n不让情绪替你做决定"),
            ("4. 被当众质疑，微笑回应", "内心笃定的人，\n不需要用音量证明自己"),
            ("5. 遭遇失败，立即复盘", "不沉溺情绪，\n专注下一个行动"),
            ("6. 被人误解，懒得解释", "懂的人自然懂，\n时间是最好的答案"),
            ("7. 突发事件，冷静处理", "越是紧急，越要慢半拍，\n稳定就是掌控"),
        ]

        # 顶部标题
        header_title = Text(
            "情绪稳定到让对手害怕的7个特征",
            font="PingFang SC",
            font_size=30,
            color="#FFC000"
        )
        header_title.move_to(UP * 3.5)
        self.add(header_title)

        for i, (title, desc) in enumerate(traits):
            self.show_trait(title, desc, header_title, i)

        # ========== 片尾 ==========
        self.show_outro()

    def create_grid(self):
        """创建白色细线网格背景"""
        grid = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": "#333333",
                "stroke_width": 0.5,
            },
            axis_config={
                "stroke_color": "#333333",
                "stroke_width": 0.5,
            }
        )
        return grid

    def show_intro(self):
        """片头动画"""
        # 大标题
        title = Text(
            "情绪稳定到让对手害怕的7个特征",
            font="PingFang SC",
            font_size=60,
            color="#FFC000"
        )
        title.move_to(UP * 1.5)

        # 副标题
        subtitle = Text(
            "让对手摸不透你",
            font="PingFang SC",
            font_size=36,
            color=GRAY_C
        )
        subtitle.move_to(DOWN * 0.5)

        # 圆环粒子
        particles = self.create_particle_ring()
        particles.move_to(DOWN * 2)

        # 播放动画
        self.play(
            Write(title),
            run_time=1.5
        )
        self.play(
            FadeIn(subtitle, shift=UP * 0.3),
            Create(particles),
            run_time=1
        )
        self.wait(0.5)

        # 粒子炸开
        self.play(
            particles.animate.scale(2).set_opacity(0),
            run_time=0.8
        )
        self.wait(0.3)

        # 标题缩小移到顶部
        self.play(
            FadeOut(subtitle),
            title.animate.scale(0.5).move_to(UP * 3.5),
            run_time=0.8
        )
        self.wait(0.3)

    def create_particle_ring(self):
        """创建圆环粒子"""
        particles = VGroup()
        n_particles = 20
        radius = 1.5

        for i in range(n_particles):
            angle = 2 * PI * i / n_particles
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)

            particle = Dot(
                point=[x, y, 0],
                radius=0.08,
                color="#FFC000"
            )
            particles.add(particle)

        # 添加连接圆环
        ring = Circle(radius=radius, color="#FFC000", stroke_width=2)
        particles.add(ring)

        return particles

    def show_trait(self, title_text, desc_text, header_title, index):
        """展示单个特征"""
        # 标题（左边70%区域）- 蓝色
        title = Text(
            title_text,
            font="PingFang SC",
            font_size=46,
            color="#4F9EFF"
        )
        title.move_to(LEFT * 3.5 + UP * 1.5)

        # 描述 - 白色
        desc = Text(
            desc_text,
            font="PingFang SC",
            font_size=32,
            color=WHITE,
            line_spacing=1.5
        )
        desc.move_to(LEFT * 3.5 + DOWN * 0.5)

        # 右边动画区域
        animation_group = self.create_trait_animation(index)
        animation_group.move_to(RIGHT * 4)

        # 入场动画 - 从左右两侧滑入
        title.shift(LEFT * 2)
        desc.shift(LEFT * 2)
        animation_group.shift(RIGHT * 2)

        self.play(
            title.animate.shift(RIGHT * 2),
            desc.animate.shift(RIGHT * 2),
            animation_group.animate.shift(LEFT * 2),
            run_time=0.6
        )

        # 播放特征动画
        self.play(animation_group.create_animation(), run_time=1.5)
        self.wait(2)

        # 退场
        self.play(
            FadeOut(title),
            FadeOut(desc),
            FadeOut(animation_group),
            run_time=0.4
        )

    def create_trait_animation(self, index):
        """为每个特征创建对应的动画对象"""
        animations = [
            self.anim_calm_heartbeat(),      # 1. 面不改色
            self.anim_flowing_water(),       # 2. 从容调整
            self.anim_breathing_wave(),      # 3. 深呼吸
            self.anim_calm_ripple(),         # 4. 微笑回应
            self.anim_spiral_rise(),         # 5. 立即复盘
            self.anim_silent_barrier(),      # 6. 懒得解释
            self.anim_stable_core(),         # 7. 冷静处理
        ]
        return animations[index]

    # ========== 特征1: 面对挑衅，面不改色 - 心跳动画 ==========
    def anim_calm_heartbeat(self):
        """平稳心跳动画"""
        heart = VGroup()

        # 心脏形状
        left_circle = Circle(radius=0.4, color=RED, fill_opacity=0.6)
        left_circle.shift(LEFT * 0.3)
        right_circle = Circle(radius=0.4, color=RED, fill_opacity=0.6)
        right_circle.shift(RIGHT * 0.3)

        bottom_triangle = Polygon(
            [-0.6, 0, 0],
            [0.6, 0, 0],
            [0, -0.8, 0],
            color=RED,
            fill_opacity=0.6
        )

        heart.add(left_circle, right_circle, bottom_triangle)

        # 心跳线
        heartbeat_line = VMobject()
        heartbeat_line.set_points_as_corners([
            [-1.5, -1.2, 0],
            [-0.8, -1.2, 0],
            [-0.4, -0.8, 0],
            [0, -1.2, 0],
            [0.4, -1.2, 0],
            [0.8, -0.8, 0],
            [1.5, -1.2, 0],
        ])
        heartbeat_line.set_color(GREEN_C)
        heartbeat_line.set_stroke(width=3)

        group = VGroup(heart, heartbeat_line)

        def create_animation():
            return AnimationGroup(
                heart.animate.scale(1.1).set_color(RED_C),
                heartbeat_line.animate.set_color(GREEN),
                rate_func=there_and_back,
                run_time=0.6
            )

        group.create_animation = create_animation
        return group

    # ========== 特征2: 计划被打乱，从容调整 - 水流绕道 ==========
    def anim_flowing_water(self):
        """水流绕道动画"""
        # 障碍物
        obstacle = Rectangle(height=1.5, width=0.5, color=GRAY, fill_opacity=0.8)

        # 水流粒子
        particles = VGroup()
        for i in range(12):
            y_pos = -1 + i * 0.18
            left_dot = Dot(point=[-2, y_pos, 0], radius=0.06, color=BLUE_C)
            right_dot = Dot(point=[2, y_pos, 0], radius=0.06, color=BLUE_C)
            particles.add(left_dot, right_dot)

        # 弯曲路径
        path_left = ArcBetweenPoints(
            [-2, 0.5, 0],
            [2, -0.5, 0],
            angle=PI/3,
            color=BLUE_C,
            stroke_width=2
        )
        path_right = ArcBetweenPoints(
            [-2, -0.5, 0],
            [2, 0.5, 0],
            angle=-PI/3,
            color=BLUE_C,
            stroke_width=2
        )

        group = VGroup(obstacle, particles, path_left, path_right)

        def create_animation():
            return AnimationGroup(
                *[dot.animate.shift(RIGHT * 0.3) for dot in particles],
                path_left.animate.set_color(BLUE),
                path_right.animate.set_color(BLUE),
                rate_func=linear,
                run_time=1.5
            )

        group.create_animation = create_animation
        return group

    # ========== 特征3: 听到坏消息，先深呼吸 - 呼吸波浪 ==========
    def anim_breathing_wave(self):
        """呼吸波浪动画"""
        # 人物轮廓（简化的圆）
        person = Circle(radius=0.8, color=WHITE, stroke_width=2)

        # 呼吸环
        rings = VGroup()
        for i in range(3):
            ring = Circle(
                radius=1 + i * 0.4,
                color=BLUE_C,
                stroke_width=2,
                stroke_opacity=0.5 - i * 0.15
            )
            rings.add(ring)

        # 数字3,2,1
        numbers = VGroup()
        for i, num in enumerate(["3", "2", "1"]):
            text = Text(num, font="PingFang SC", font_size=48, color=YELLOW)
            text.move_to(UP * 1.5 + RIGHT * (i - 1) * 1.5)
            numbers.add(text)

        group = VGroup(person, rings, numbers)

        def create_animation():
            return AnimationGroup(
                *[ring.animate.scale(1.3).set_opacity(0) for ring in rings],
                person.animate.scale(1.1),
                *[num.animate.scale(1.2).set_color(GREEN) for num in numbers],
                rate_func=there_and_back,
                run_time=1.5
            )

        group.create_animation = create_animation
        return group

    # ========== 特征4: 被当众质疑，微笑回应 - 淡定波纹 ==========
    def anim_calm_ripple(self):
        """淡定波纹动画"""
        # 中心微笑
        face = VGroup()
        face_circle = Circle(radius=0.6, color=YELLOW, stroke_width=2)

        # 简化的微笑
        left_eye = Dot(point=[-0.2, 0.2, 0], radius=0.05, color=YELLOW)
        right_eye = Dot(point=[0.2, 0.2, 0], radius=0.05, color=YELLOW)
        smile = Arc(radius=0.25, angle=PI, color=YELLOW, stroke_width=2)
        smile.rotate(-PI/2)
        smile.shift(DOWN * 0.1)

        face.add(face_circle, left_eye, right_eye, smile)

        # 波纹
        ripples = VGroup()
        for i in range(4):
            ripple = Circle(
                radius=0.8 + i * 0.4,
                color=BLUE_C,
                stroke_width=2,
                stroke_opacity=0.6 - i * 0.15
            )
            ripples.add(ripple)

        # 质疑的问号
        questions = VGroup()
        for i in range(6):
            angle = i * PI / 3
            x = 2.2 * np.cos(angle)
            y = 2.2 * np.sin(angle)
            q = Text("?", font="PingFang SC", font_size=24, color=GRAY)
            q.move_to([x, y, 0])
            questions.add(q)

        group = VGroup(face, ripples, questions)

        def create_animation():
            return AnimationGroup(
                face.animate.scale(1.1),
                *[ripple.animate.scale(1.5).set_opacity(0) for ripple in ripples],
                questions.animate.set_opacity(0.3),
                rate_func=linear,
                run_time=1.5
            )

        group.create_animation = create_animation
        return group

    # ========== 特征5: 遭遇失败，立即复盘 - 旋转上升 ==========
    def anim_spiral_rise(self):
        """旋转上升动画"""
        # 螺旋路径
        spiral = ParametricFunction(
            lambda t: [
                0.3 * t * np.cos(3 * t),
                0.3 * t * np.sin(3 * t) - 1,
                0
            ],
            t_range=[0, 4],
            color=BLUE_C,
            stroke_width=3
        )

        # 上升箭头
        arrow = Arrow(
            start=DOWN * 1.5,
            end=UP * 1.5,
            color=GREEN,
            buff=0
        )

        # 复盘节点
        nodes = VGroup()
        for i in range(4):
            node = Dot(
                point=[0.3 * i * np.cos(3 * i), 0.3 * i * np.sin(3 * i) - 1, 0],
                radius=0.08,
                color=YELLOW
            )
            nodes.add(node)

        group = VGroup(spiral, arrow, nodes)

        def create_animation():
            return AnimationGroup(
                spiral.animate.set_color(GREEN),
                arrow.animate.scale(1.1),
                nodes.animate.scale(1.5).set_color(GREEN_C),
                rate_func=there_and_back,
                run_time=1.5
            )

        group.create_animation = create_animation
        return group

    # ========== 特征6: 被人误解，懒得解释 - 静音屏障 ==========
    def anim_silent_barrier(self):
        """静音屏障动画"""
        # 中心人物
        person = Circle(radius=0.6, color=WHITE, stroke_width=2)

        # 静音屏障
        barrier = Circle(radius=1.3, color=BLUE_C, stroke_width=3)

        # 静音符号
        mute_icon = VGroup()
        speaker = Polygon(
            [-0.3, -0.3, 0],
            [-0.3, 0.3, 0],
            [0.2, 0.5, 0],
            [0.2, -0.5, 0],
            color=GRAY
        )
        line = Line([0.3, 0.4, 0], [0.6, -0.4, 0], color=GRAY, stroke_width=3)
        mute_icon.add(speaker, line)

        # 外部噪音波浪
        waves = VGroup()
        for i in range(3):
            wave = Arc(
                radius=1.8 + i * 0.3,
                angle=PI/2,
                color=RED_C,
                stroke_width=2,
                stroke_opacity=0.4
            )
            waves.add(wave)

        group = VGroup(person, barrier, mute_icon, waves)

        def create_animation():
            return AnimationGroup(
                barrier.animate.scale(1.1).set_color(BLUE),
                person.animate.scale(1.05),
                waves.animate.set_opacity(0.1),
                mute_icon.animate.scale(1.2),
                rate_func=there_and_back,
                run_time=1.5
            )

        group.create_animation = create_animation
        return group

    # ========== 特征7: 突发事件，冷静处理 - 核心稳定 ==========
    def anim_stable_core(self):
        """核心稳定动画"""
        # 稳定核心
        core = Circle(radius=0.4, color=GREEN, fill_opacity=0.8)

        # 周围混乱
        chaos = VGroup()
        for i in range(8):
            angle = i * PI / 4
            for j in range(3):
                r = 1.2 + j * 0.4
                x = r * np.cos(angle + j * 0.3)
                y = r * np.sin(angle + j * 0.3)
                dot = Dot(point=[x, y, 0], radius=0.04, color=RED_C)
                chaos.add(dot)

        # 稳定射线
        rays = VGroup()
        for i in range(8):
            angle = i * PI / 4
            x = 1.8 * np.cos(angle)
            y = 1.8 * np.sin(angle)
            ray = Line([0, 0, 0], [x, y, 0], color=GREEN_C, stroke_width=2)
            rays.add(ray)

        group = VGroup(core, chaos, rays)

        def create_animation():
            return AnimationGroup(
                core.animate.scale(1.3).set_color(GREEN_C),
                rays.animate.scale(1.2).set_opacity(0.8),
                chaos.animate.set_opacity(0.2),
                rate_func=there_and_back,
                run_time=1.5
            )

        group.create_animation = create_animation
        return group


    def show_outro(self):
        """片尾动画"""
        # 金句
        quote = Text(
            "情绪稳定，是最深不可测的力量",
            font="PingFang SC",
            font_size=42,
            color="#FFC000"
        )

        # 副标题
        sub = Text(
            "你做到了几个？",
            font="PingFang SC",
            font_size=32,
            color=GRAY_C
        )
        sub.move_to(DOWN * 1.2)

        self.play(
            Write(quote),
            run_time=1.2
        )
        self.play(
            FadeIn(sub, shift=UP * 0.3),
            run_time=0.8
        )
        self.wait(2)
