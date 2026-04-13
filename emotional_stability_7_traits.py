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
            font="Heiti SC",
            font_size=30,
            color="#FFD700"
        )
        header_title.move_to(UP * 3.5)
        self.add(header_title)

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
            color="#FFD700"
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
        """展示单个特征"""
        # 标题（左边70%区域）- 蓝色，左对齐
        title = Text(
            title_text,
            font="Heiti SC",
            font_size=46,
            color="#4F9EFF"
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

        # 播放特征动画 - 循环动感
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
        """平稳心跳动画 - 持续律动"""
        group = VGroup()

        # 心脏形状
        heart = VGroup()
        left_circle = Circle(radius=0.4, color=RED, fill_opacity=0.6)
        left_circle.shift(LEFT * 0.3)
        right_circle = Circle(radius=0.4, color=RED, fill_opacity=0.6)
        right_circle.shift(RIGHT * 0.3)
        bottom_triangle = Polygon(
            [-0.6, 0, 0], [0.6, 0, 0], [0, -0.8, 0],
            color=RED, fill_opacity=0.6
        )
        heart.add(left_circle, right_circle, bottom_triangle)
        group.add(heart)

        # 动态心跳线 - 持续波动
        wave_points = []
        for i in range(30):
            x = -1.5 + i * 0.1
            if 10 <= i <= 12:
                y = -1.2 + 0.4 * np.sin((i-10) * PI / 2)
            elif 18 <= i <= 20:
                y = -1.2 + 0.4 * np.sin((i-18) * PI / 2)
            else:
                y = -1.2
            wave_points.append([x, y, 0])

        wave_line = VMobject()
        wave_line.set_points_as_corners(wave_points)
        wave_line.set_color(GREEN_C)
        wave_line.set_stroke(width=3)
        group.add(wave_line)

        # 攻击箭头（被弹开）
        arrows = VGroup()
        for i in range(5):
            arrow = Arrow(
                start=[2, 0.5 - i*0.3, 0],
                end=[0.8, 0.5 - i*0.3, 0],
                color=RED_C,
                buff=0.1
            )
            arrows.add(arrow)
        group.add(arrows)

        def create_animation():
            return AnimationGroup(
                # 心脏持续跳动
                heart.animate.scale(1.15).set_color(RED_C),
                # 波形闪烁
                wave_line.animate.set_color(GREEN).set_stroke(width=5),
                # 箭头被弹开
                *[arrow.animate.shift(LEFT*0.5 + UP*(0.2 if i%2==0 else -0.2)).set_opacity(0.3)
                  for i, arrow in enumerate(arrows)],
                rate_func=there_and_back,
                run_time=0.8
            )

        group.create_animation = create_animation
        return group

    # ========== 特征2: 计划被打乱，从容调整 - 水流绕道 ==========
    def anim_flowing_water(self):
        """水流绕道动画 - 持续流动"""
        group = VGroup()

        # 障碍物
        obstacle = Rectangle(height=1.5, width=0.4, color=GRAY, fill_opacity=0.8)
        group.add(obstacle)

        # 创建流动的水流粒子（多组循环）
        all_particles = VGroup()
        for wave in range(3):  # 3组波浪
            wave_particles = VGroup()
            for i in range(8):
                # 上方绕道
                dot1 = Dot(point=[-2.5 + wave*0.5, 0.6 + i*0.15, 0], radius=0.06, color=BLUE_C)
                # 下方绕道
                dot2 = Dot(point=[-2.5 + wave*0.5, -0.6 - i*0.15, 0], radius=0.06, color=BLUE_C)
                wave_particles.add(dot1, dot2)
            all_particles.add(wave_particles)
        group.add(all_particles)

        # 流动轨迹线
        path_lines = VGroup()
        upper_path = ArcBetweenPoints([-2.2, 1.2, 0], [2.2, 1.2, 0], angle=-PI/6, color=BLUE_C, stroke_width=2)
        lower_path = ArcBetweenPoints([-2.2, -1.2, 0], [2.2, -1.2, 0], angle=PI/6, color=BLUE_C, stroke_width=2)
        path_lines.add(upper_path, lower_path)
        group.add(path_lines)

        def create_animation():
            return AnimationGroup(
                # 粒子向右流动
                *[wave.animate.shift(RIGHT * 1.5) for wave in all_particles],
                # 轨迹发光
                upper_path.animate.set_color(BLUE).set_stroke(width=4),
                lower_path.animate.set_color(BLUE).set_stroke(width=4),
                rate_func=linear,
                run_time=1.2
            )

        group.create_animation = create_animation
        return group

    # ========== 特征3: 听到坏消息，先深呼吸 - 呼吸波浪 ==========
    def anim_breathing_wave(self):
        """呼吸波浪动画 - 持续呼吸"""
        group = VGroup()

        # 人物轮廓
        person = Circle(radius=0.6, color=WHITE, stroke_width=2)
        group.add(person)

        # 多层呼吸环（持续扩散）
        rings = VGroup()
        for i in range(4):
            ring = Circle(
                radius=0.9 + i * 0.35,
                color=BLUE_C,
                stroke_width=2,
                stroke_opacity=0.7 - i * 0.15
            )
            rings.add(ring)
        group.add(rings)

        # 倒计时数字（轮流闪烁）
        numbers = VGroup()
        for i, num in enumerate(["3", "2", "1"]):
            text = Text(num, font="Heiti SC", font_size=40, color=YELLOW)
            text.move_to(RIGHT * 1.8 + UP * (1 - i) * 0.8)
            text.set_opacity(0.4)
            numbers.add(text)
        group.add(numbers)

        # 吸入呼出指示
        breath_text = Text("深呼吸", font="Heiti SC", font_size=28, color=BLUE_C)
        breath_text.move_to(DOWN * 1.5)
        group.add(breath_text)

        def create_animation():
            return AnimationGroup(
                # 环向外扩散
                *[ring.animate.scale(1.4).set_opacity(0.1) for ring in rings],
                # 人物起伏
                person.animate.scale(1.15),
                # 数字依次亮起
                numbers[0].animate.set_opacity(1).scale(1.3),
                breath_text.animate.set_color(BLUE),
                rate_func=there_and_back,
                run_time=1.5
            )

        group.create_animation = create_animation
        return group

    # ========== 特征4: 被当众质疑，微笑回应 - 淡定波纹 ==========
    def anim_calm_ripple(self):
        """淡定波纹动画 - 微笑消融质疑"""
        group = VGroup()

        # 中心微笑（更明显的表情）
        face = VGroup()
        face_circle = Circle(radius=0.7, color="#FFD700", fill_opacity=0.2, stroke_width=3)

        # 眼睛（眯起）
        left_eye = Line([-0.3, 0.25, 0], [-0.1, 0.25, 0], color="#FFD700", stroke_width=3)
        right_eye = Line([0.1, 0.25, 0], [0.3, 0.25, 0], color="#FFD700", stroke_width=3)

        # 微笑（更大）
        smile = Arc(radius=0.35, angle=PI, color="#FFD700", stroke_width=4)
        smile.rotate(-PI/2)
        smile.shift(DOWN * 0.15)

        face.add(face_circle, left_eye, right_eye, smile)
        group.add(face)

        # 多层波纹扩散
        ripples = VGroup()
        for i in range(5):
            ripple = Circle(
                radius=1 + i * 0.35,
                color=BLUE_C,
                stroke_width=2.5,
                stroke_opacity=0.6 - i * 0.1
            )
            ripples.add(ripple)
        group.add(ripples)

        # 质疑的问号（环绕）
        questions = VGroup()
        for i in range(8):
            angle = i * PI / 4
            x = 2.5 * np.cos(angle)
            y = 2.5 * np.sin(angle)
            q = Text("?", font="Heiti SC", font_size=28, color=GRAY)
            q.move_to([x, y, 0])
            q.set_opacity(0.6)
            questions.add(q)
        group.add(questions)

        def create_animation():
            return AnimationGroup(
                # 微笑更灿烂
                face.animate.scale(1.2),
                # 波纹扩散消融
                *[ripple.animate.scale(1.6).set_opacity(0) for ripple in ripples],
                # 问号被消融
                questions.animate.scale(0.5).set_opacity(0.1),
                rate_func=linear,
                run_time=1.5
            )

        group.create_animation = create_animation
        return group

    # ========== 特征5: 遭遇失败，立即复盘 - 旋转上升 ==========
    def anim_spiral_rise(self):
        """旋转上升动画 - 持续攀升"""
        group = VGroup()

        # 螺旋路径（更完整）
        spiral = ParametricFunction(
            lambda t: [
                0.25 * t * np.cos(2.5 * t),
                0.25 * t * np.sin(2.5 * t) - 0.8,
                0
            ],
            t_range=[0, 5],
            color=BLUE_C,
            stroke_width=3
        )
        group.add(spiral)

        # 上升箭头
        arrow = Arrow(
            start=DOWN * 1.2,
            end=UP * 1.8,
            color=GREEN,
            buff=0.1
        )
        group.add(arrow)

        # 动态上升节点
        nodes = VGroup()
        for i in range(5):
            angle = 2.5 * i
            r = 0.25 * i
            x = r * np.cos(angle)
            y = r * np.sin(angle) - 0.8
            node = Dot(point=[x, y, 0], radius=0.1, color=YELLOW)
            nodes.add(node)
        group.add(nodes)

        # "复盘"文字
        review = Text("复盘", font="Heiti SC", font_size=24, color=GREEN_C)
        review.move_to(RIGHT * 1.5)
        group.add(review)

        def create_animation():
            return AnimationGroup(
                # 螺旋变色向上
                spiral.animate.set_color(GREEN).shift(UP * 0.3),
                # 箭头脉动
                arrow.animate.scale(1.2).set_color(GREEN_C),
                # 节点依次亮起
                *[node.animate.scale(1.8).set_color(GREEN) for node in nodes],
                # 复盘文字闪烁
                review.animate.scale(1.3).set_color(GREEN),
                rate_func=there_and_back,
                run_time=1.5
            )

        group.create_animation = create_animation
        return group

    # ========== 特征6: 被人误解，懒得解释 - 静音屏障 ==========
    def anim_silent_barrier(self):
        """静音屏障动画 - 声波被阻挡"""
        group = VGroup()

        # 中心人物（淡定）
        person = Circle(radius=0.5, color=WHITE, fill_opacity=0.1, stroke_width=2)
        face = Text("- _ -", font="Heiti SC", font_size=20, color=WHITE)
        face.scale(0.6)
        person_face = VGroup(person, face)
        group.add(person_face)

        # 多层静音屏障
        barriers = VGroup()
        for i in range(3):
            barrier = Circle(
                radius=1 + i * 0.4,
                color=BLUE_C,
                stroke_width=2,
                stroke_opacity=0.5 - i * 0.1
            )
            barriers.add(barrier)
        group.add(barriers)

        # 静音符号
        mute_icon = Text("🔇", font_size=36)
        mute_icon.move_to(RIGHT * 1.5 + UP * 0.5)
        group.add(mute_icon)

        # 外部噪音波浪（持续涌来）
        noise_waves = VGroup()
        for i in range(4):
            for j in range(6):
                angle = j * PI / 3
                r = 2.2 + i * 0.3
                x = r * np.cos(angle)
                y = r * np.sin(angle)
                arc = Arc(
                    radius=0.2,
                    angle=PI,
                    color=RED_C,
                    stroke_width=2,
                    stroke_opacity=0.5
                )
                arc.move_to([x, y, 0])
                arc.rotate(angle + PI)
                noise_waves.add(arc)
        group.add(noise_waves)

        def create_animation():
            return AnimationGroup(
                # 屏障脉动
                *[barrier.animate.scale(1.15) for barrier in barriers],
                # 人物淡定不动
                person_face.animate.scale(1.05),
                # 噪音波被阻挡消散
                noise_waves.animate.scale(0.3).set_opacity(0.1),
                # 静音符号闪烁
                mute_icon.animate.scale(1.4),
                rate_func=there_and_back,
                run_time=1.5
            )

        group.create_animation = create_animation
        return group

    # ========== 特征7: 突发事件，冷静处理 - 核心稳定 ==========
    def anim_stable_core(self):
        """核心稳定动画 - 核心稳固，混乱消散"""
        group = VGroup()

        # 稳定核心（多层）
        cores = VGroup()
        for i in range(3):
            core = Circle(
                radius=0.3 + i * 0.15,
                color=GREEN,
                fill_opacity=0.6 - i * 0.15,
                stroke_width=2
            )
            cores.add(core)
        group.add(cores)

        # 混乱粒子（疯狂旋转）
        chaos_particles = VGroup()
        for i in range(16):
            angle = i * PI / 8
            r = 1.5 + np.random.random() * 0.5
            x = r * np.cos(angle)
            y = r * np.sin(angle)
            particle = Dot(point=[x, y, 0], radius=0.06, color=RED_C)
            chaos_particles.add(particle)
        group.add(chaos_particles)

        # 稳定射线（脉动）
        rays = VGroup()
        for i in range(12):
            angle = i * PI / 6
            x = 2 * np.cos(angle)
            y = 2 * np.sin(angle)
            ray = Line([0, 0, 0], [x, y, 0], color=GREEN_C, stroke_width=2.5)
            rays.add(ray)
        group.add(rays)

        # "稳"字
        stable_text = Text("稳", font="Heiti SC", font_size=48, color=GREEN)
        group.add(stable_text)

        def create_animation():
            return AnimationGroup(
                # 核心层层扩散
                *[core.animate.scale(1.4) for core in cores],
                # 射线强脉动
                rays.animate.scale(1.3).set_color(GREEN),
                # 混乱被镇压
                chaos_particles.animate.scale(0.4).set_opacity(0.2),
                # 稳字显现
                stable_text.animate.scale(1.3),
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
            font="Heiti SC",
            font_size=42,
            color="#FFD700"
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
