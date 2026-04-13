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

        # 使用片头留下的标题
        for i, (title, desc) in enumerate(traits):
            self.show_trait(title, desc, i)

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
        """片头动画 - 放射线效果"""
        # 大标题
        title = Text(
            "情绪稳定到让对手害怕的7个特征",
            font="Heiti SC",
            font_size=60,
            color="#FFD700",
            weight=BOLD
        )
        title.move_to(ORIGIN)

        # 标题先全部出来
        self.play(
            Write(title),
            run_time=1.2
        )
        self.wait(0.3)

        # 创建放射线（从文字中心向外射出）
        radiating_lines = self.create_radiating_lines()

        # 放射线出现并射出去
        self.play(
            *[Create(line) for line in radiating_lines],
            run_time=0.6
        )
        self.wait(0.2)

        # 放射线扩散消失，标题缩小移到顶部
        self.play(
            *[line.animate.scale(2.5).set_opacity(0) for line in radiating_lines],
            title.animate.scale(0.5).move_to(UP * 3.5),
            run_time=0.8
        )
        self.wait(0.2)

    def create_radiating_lines(self):
        """创建放射线/集中线效果 - 从文字边缘射出"""
        lines = VGroup()
        n_lines = 40  # 放射线数量

        # 金色调色板
        gold_colors = ["#FFD700", "#FFA500", "#FF8C00", "#D4AF37", "#F0E68C", "#FFE4B5"]

        for i in range(n_lines):
            angle = 2 * PI * i / n_lines

            # 线条从文字边缘开始，延伸到屏幕外
            inner_r = 2.8  # 内半径（文字边缘附近）
            outer_r = 10   # 外半径（超出屏幕）

            start_x = inner_r * np.cos(angle)
            start_y = inner_r * np.sin(angle)
            end_x = outer_r * np.cos(angle)
            end_y = outer_r * np.sin(angle)

            # 创建粗线，金色系
            color = gold_colors[i % len(gold_colors)]
            line = Line(
                start=[start_x, start_y, 0],
                end=[end_x, end_y, 0],
                color=color,
                stroke_width=3,
                stroke_opacity=0.8
            )
            lines.add(line)

        self.add(lines)
        return lines

    def show_trait(self, title_text, desc_text, index):
        """展示单个特征 - 依次出场"""
        # 标题（左边70%区域）- 金色，左对齐，加粗
        title = Text(
            title_text,
            font="Heiti SC",
            font_size=46,
            color="#FFD700",
            weight=BOLD
        )
        title.move_to(LEFT * 4.5 + UP * 1.5)
        title.align_to(LEFT * 6 + UP * 1.5, LEFT)

        # 描述 - 白色，左对齐，与标题对齐
        desc = Text(
            desc_text,
            font="Heiti SC",
            font_size=32,
            color=WHITE,
            line_spacing=1.8
        )
        desc.move_to(LEFT * 4.5 + DOWN * 0.3)
        desc.align_to(title, LEFT)

        # 右边动画区域
        animation_group = self.create_trait_animation(index)
        animation_group.move_to(RIGHT * 3.5)

        # 入场动画 - 依次出现
        # 1. 标题先出现
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.4)
        # 2. 描述接着出现
        self.play(FadeIn(desc, shift=UP * 0.2), run_time=0.4)

        # 3. 右边动画的子元素依次入场
        for element in animation_group:
            self.play(FadeIn(element, scale=0.8), run_time=0.25)

        # 播放特征动画 - 持续动感
        self.play(animation_group.create_animation(), run_time=2)
        self.wait(1.5)

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
        """平稳心跳动画 - 丝滑律动"""
        group = VGroup()

        # 心脏
        heart = VGroup()
        left_circle = Circle(radius=0.4, color=RED, fill_opacity=0.7)
        left_circle.shift(LEFT * 0.3)
        right_circle = Circle(radius=0.4, color=RED, fill_opacity=0.7)
        right_circle.shift(RIGHT * 0.3)
        bottom_triangle = Polygon(
            [-0.6, 0, 0], [0.6, 0, 0], [0, -0.8, 0],
            color=RED, fill_opacity=0.7
        )
        heart.add(left_circle, right_circle, bottom_triangle)
        group.add(heart)

        # 心电图 - 一条流畅的波形
        wave_line = VMobject()
        wave_line.set_points_as_corners([
            [-1.8, -1.2, 0], [-1.2, -1.2, 0], [-0.9, -0.7, 0],
            [-0.6, -1.2, 0], [-0.3, -1.2, 0], [0, -0.8, 0],
            [0.3, -1.2, 0], [0.6, -1.2, 0], [0.9, -0.7, 0],
            [1.2, -1.2, 0], [1.8, -1.2, 0]
        ])
        wave_line.set_color(GREEN)
        wave_line.set_stroke(width=3)
        group.add(wave_line)

        # 攻击箭头（被弹开）
        arrows = VGroup()
        for i in range(4):
            angle = -PI/4 + i * PI/6
            start = [2.2 * np.cos(angle), 2.2 * np.sin(angle), 0]
            end = [1.0 * np.cos(angle), 1.0 * np.sin(angle), 0]
            arrow = Arrow(start, end, color=RED_C, buff=0.05)
            arrows.add(arrow)
        group.add(arrows)

        def create_animation():
            return AnimationGroup(
                # 心脏丝滑跳动
                heart.animate.scale(1.25).set_color(RED_E),
                # 波形闪烁流动
                wave_line.animate.set_color(YELLOW).set_stroke(width=5),
                # 箭头被弹开
                arrows.animate.shift(LEFT * 0.6).rotate(PI/8).set_opacity(0.2),
                rate_func=there_and_back,
                run_time=1.8
            )

        group.create_animation = create_animation
        return group

    # ========== 特征2: 计划被打乱，从容调整 - 水流绕道 ==========
    def anim_flowing_water(self):
        """水流绕道动画 - 丝滑流动"""
        group = VGroup()

        # 障碍物
        obstacle = Rectangle(height=1.3, width=0.4, color=GRAY, fill_opacity=0.8)
        group.add(obstacle)

        # 上方流动曲线
        upper_curve = ParametricFunction(
            lambda t: [2.5 * (t - 0.5), 0.6 + 0.4 * np.sin(PI * t), 0],
            t_range=[0, 1],
            color=BLUE_C,
            stroke_width=3
        )
        group.add(upper_curve)

        # 下方流动曲线
        lower_curve = ParametricFunction(
            lambda t: [2.5 * (t - 0.5), -0.6 - 0.4 * np.sin(PI * t), 0],
            t_range=[0, 1],
            color=BLUE_C,
            stroke_width=3
        )
        group.add(lower_curve)

        # 流动粒子（沿曲线运动）
        particles = VGroup()
        for i in range(8):
            t = i / 7
            # 上方粒子
            x1 = 2.5 * (t - 0.5)
            y1 = 0.6 + 0.4 * np.sin(PI * t)
            p1 = Dot(point=[x1, y1, 0], radius=0.08, color=BLUE)
            particles.add(p1)

            # 下方粒子
            x2 = 2.5 * ((1-t) - 0.5)
            y2 = -0.6 - 0.4 * np.sin(PI * (1-t))
            p2 = Dot(point=[x2, y2, 0], radius=0.08, color=BLUE)
            particles.add(p2)
        group.add(particles)

        def create_animation():
            return AnimationGroup(
                # 曲线发光流动
                upper_curve.animate.set_color(BLUE).set_stroke(width=5),
                lower_curve.animate.set_color(BLUE).set_stroke(width=5),
                # 粒子沿曲线流动
                particles.animate.shift(RIGHT * 0.5).set_color("#00FFFF"),
                rate_func=there_and_back,
                run_time=1.8
            )

        group.create_animation = create_animation
        return group

    # ========== 特征3: 听到坏消息，先深呼吸 - 呼吸波浪 ==========
    def anim_breathing_wave(self):
        """呼吸波浪动画 - 丝滑扩散"""
        group = VGroup()

        # 人物轮廓
        person = Circle(radius=0.6, color=WHITE, stroke_width=2)
        group.add(person)

        # 呼吸环（4个环，依次扩散）
        rings = VGroup()
        for i in range(4):
            ring = Circle(
                radius=0.9 + i * 0.35,
                color=BLUE_C,
                stroke_width=2.5,
                stroke_opacity=0.6 - i * 0.1
            )
            rings.add(ring)
        group.add(rings)

        # 倒计时数字
        numbers = VGroup()
        for i, num in enumerate(["3", "2", "1"]):
            text = Text(num, font="Heiti SC", font_size=36, color=YELLOW)
            text.move_to(RIGHT * 1.5 + UP * (1 - i) * 0.7)
            numbers.add(text)
        group.add(numbers)

        # 深呼吸文字
        breath_text = Text("深呼吸", font="Heiti SC", font_size=28, color=BLUE_C)
        breath_text.move_to(DOWN * 1.3)
        group.add(breath_text)

        def create_animation():
            return AnimationGroup(
                # 人物呼吸起伏
                person.animate.scale(1.2),
                # 环依次扩散消失
                *[rings[i].animate.scale(1.6).set_opacity(0) for i in range(4)],
                # 数字依次亮起
                numbers[0].animate.set_opacity(1).scale(1.3),
                numbers[1].animate.set_opacity(1).scale(1.3),
                numbers[2].animate.set_opacity(1).scale(1.3),
                # 文字发光
                breath_text.animate.set_color(BLUE).scale(1.1),
                rate_func=there_and_back,
                run_time=1.8
            )

        group.create_animation = create_animation
        return group

    # ========== 特征4: 被当众质疑，微笑回应 - 淡定波纹 ==========
    def anim_calm_ripple(self):
        """淡定波纹动画 - 丝滑消融"""
        group = VGroup()

        # 中心微笑
        face = VGroup()
        face_circle = Circle(radius=0.7, color="#FFD700", fill_opacity=0.2, stroke_width=3)

        # 眼睛
        left_eye = Arc(radius=0.15, angle=PI, color="#FFD700", stroke_width=3)
        left_eye.rotate(PI)
        left_eye.shift(LEFT * 0.2 + UP * 0.15)
        right_eye = Arc(radius=0.15, angle=PI, color="#FFD700", stroke_width=3)
        right_eye.rotate(PI)
        right_eye.shift(RIGHT * 0.2 + UP * 0.15)

        # 微笑
        smile = Arc(radius=0.4, angle=PI, color="#FFD700", stroke_width=4)
        smile.rotate(-PI/2)
        smile.shift(DOWN * 0.1)

        face.add(face_circle, left_eye, right_eye, smile)
        group.add(face)

        # 波纹（4个环）
        ripples = VGroup()
        for i in range(4):
            ripple = Circle(
                radius=1.1 + i * 0.4,
                color=BLUE_C,
                stroke_width=2.5,
                stroke_opacity=0.6 - i * 0.12
            )
            ripples.add(ripple)
        group.add(ripples)

        # 质疑的问号
        questions = VGroup()
        for i in range(6):
            angle = i * PI / 3
            x = 2.3 * np.cos(angle)
            y = 2.3 * np.sin(angle)
            q = Text("?", font="Heiti SC", font_size=26, color=GRAY)
            q.move_to([x, y, 0])
            questions.add(q)
        group.add(questions)

        def create_animation():
            return AnimationGroup(
                # 微笑放大
                face.animate.scale(1.25),
                # 波纹依次扩散消融
                *[ripples[i].animate.scale(1.7).set_opacity(0) for i in range(4)],
                # 问号消融
                questions.animate.scale(0.5).set_opacity(0.1),
                rate_func=linear,
                run_time=1.8
            )

        group.create_animation = create_animation
        return group

    # ========== 特征5: 遭遇失败，立即复盘 - 旋转上升 ==========
    def anim_spiral_rise(self):
        """旋转上升动画 - 丝滑螺旋"""
        group = VGroup()

        # 螺旋路径
        spiral = ParametricFunction(
            lambda t: [
                0.25 * t * np.cos(2.5 * t),
                0.25 * t * np.sin(2.5 * t) - 0.7,
                0
            ],
            t_range=[0, 6],
            color=BLUE_C,
            stroke_width=3
        )
        group.add(spiral)

        # 上升箭头
        arrow = Arrow(
            start=DOWN * 1.0,
            end=UP * 1.8,
            color=GREEN,
            buff=0.1
        )
        group.add(arrow)

        # 上升节点
        nodes = VGroup()
        for i in range(5):
            angle = 2.5 * i * 0.9
            r = 0.25 * i * 0.9
            x = r * np.cos(angle)
            y = r * np.sin(angle) - 0.7
            node = Dot(point=[x, y, 0], radius=0.1, color=YELLOW)
            nodes.add(node)
        group.add(nodes)

        # "复盘"文字
        review = Text("复盘", font="Heiti SC", font_size=28, color=GREEN, weight=BOLD)
        review.move_to(RIGHT * 1.3)
        group.add(review)

        def create_animation():
            return AnimationGroup(
                # 螺旋变色上升
                spiral.animate.set_color(GREEN).shift(UP * 0.3),
                # 箭头脉动
                arrow.animate.scale(1.2).set_color(GREEN_C),
                # 节点依次亮起
                *[nodes[i].animate.scale(1.8).set_color(GREEN) for i in range(5)],
                # 复盘文字闪烁
                review.animate.scale(1.2).set_color(GREEN),
                rate_func=there_and_back,
                run_time=1.8
            )

        group.create_animation = create_animation
        return group

    # ========== 特征6: 被人误解，懒得解释 - 静音屏障 ==========
    def anim_silent_barrier(self):
        """静音屏障动画 - 丝滑阻挡"""
        group = VGroup()

        # 中心人物
        person = Circle(radius=0.5, color=WHITE, fill_opacity=0.1, stroke_width=2)
        face = Text("- _ -", font="Heiti SC", font_size=20, color=WHITE)
        face.scale(0.6)
        person_face = VGroup(person, face)
        group.add(person_face)

        # 静音屏障（3层）
        barriers = VGroup()
        for i in range(3):
            barrier = Circle(
                radius=1.0 + i * 0.4,
                color=BLUE_C,
                stroke_width=2.5,
                stroke_opacity=0.6 - i * 0.15
            )
            barriers.add(barrier)
        group.add(barriers)

        # 静音符号
        mute_icon = Text("🔇", font_size=36)
        mute_icon.move_to(RIGHT * 1.3 + UP * 0.4)
        group.add(mute_icon)

        # 外部噪音波浪
        noise_waves = VGroup()
        for i in range(6):
            angle = i * PI / 3
            r = 2.2
            x = r * np.cos(angle)
            y = r * np.sin(angle)
            # 声波弧线
            for j in range(2):
                arc_r = 0.2 + j * 0.1
                arc = Arc(radius=arc_r, angle=PI*0.8, color=RED_C, stroke_width=2)
                arc.move_to([x, y, 0])
                arc.rotate(angle + PI)
                noise_waves.add(arc)
        group.add(noise_waves)

        def create_animation():
            return AnimationGroup(
                # 屏障脉动
                *[barriers[i].animate.scale(1.2) for i in range(3)],
                # 人物淡定
                person_face.animate.scale(1.1),
                # 噪音消散
                noise_waves.animate.scale(0.4).set_opacity(0.1),
                # 静音符号闪烁
                mute_icon.animate.scale(1.3),
                rate_func=there_and_back,
                run_time=1.8
            )

        group.create_animation = create_animation
        return group

    # ========== 特征7: 突发事件，冷静处理 - 核心稳定 ==========
    def anim_stable_core(self):
        """核心稳定动画 - 丝滑镇定"""
        group = VGroup()

        # 稳定核心（3层）
        cores = VGroup()
        for i in range(3):
            core = Circle(
                radius=0.3 + i * 0.2,
                color=GREEN,
                fill_opacity=0.5 - i * 0.12,
                stroke_width=2.5
            )
            cores.add(core)
        group.add(cores)

        # 混乱粒子（旋转）
        chaos = VGroup()
        for i in range(12):
            angle = i * PI / 6
            r = 1.5 + np.random.random() * 0.4
            x = r * np.cos(angle)
            y = r * np.sin(angle)
            particle = Dot(point=[x, y, 0], radius=0.07, color=RED_C)
            chaos.add(particle)
        group.add(chaos)

        # 稳定射线
        rays = VGroup()
        for i in range(12):
            angle = i * PI / 6
            x = 2 * np.cos(angle)
            y = 2 * np.sin(angle)
            ray = Line([0, 0, 0], [x, y, 0], color=GREEN_C, stroke_width=2.5)
            rays.add(ray)
        group.add(rays)

        # "稳"字
        stable_text = Text("稳", font="Heiti SC", font_size=48, color=GREEN, weight=BOLD)
        group.add(stable_text)

        def create_animation():
            return AnimationGroup(
                # 核心依次扩散
                *[cores[i].animate.scale(1.5).set_color(GREEN_C) for i in range(3)],
                # 射线脉动
                rays.animate.scale(1.3).set_color(GREEN),
                # 混乱消散
                chaos.animate.scale(0.4).set_opacity(0.15),
                # 稳字显现
                stable_text.animate.scale(1.3),
                rate_func=there_and_back,
                run_time=1.8
            )

        group.create_animation = create_animation
        return group


    def show_outro(self):
        """片尾动画"""
        # 金句
        quote = Text(
            "情绪稳定，是最深不可测的力量",
            font="Heiti SC",
            font_size=42,
            color="#FFD700",
            weight=BOLD
        )

        # 副标题
        sub = Text(
            "你做到了几个？",
            font="Heiti SC",
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
