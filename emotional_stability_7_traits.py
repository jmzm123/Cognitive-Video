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
        """平稳心跳动画 - 多层律动效果"""
        group = VGroup()

        # 中心核心 - 多层心脏
        heart_group = VGroup()
        for i in range(3):
            heart = VGroup()
            scale = 1 - i * 0.2
            alpha = 0.6 - i * 0.15
            left_circle = Circle(radius=0.4 * scale, color=RED, fill_opacity=alpha)
            left_circle.shift(LEFT * 0.3 * scale)
            right_circle = Circle(radius=0.4 * scale, color=RED, fill_opacity=alpha)
            right_circle.shift(RIGHT * 0.3 * scale)
            bottom_triangle = Polygon(
                [-0.6 * scale, 0, 0], [0.6 * scale, 0, 0], [0, -0.8 * scale, 0],
                color=RED, fill_opacity=alpha
            )
            heart.add(left_circle, right_circle, bottom_triangle)
            heart_group.add(heart)
        group.add(heart_group)

        # 心电图 - 多层波形
        ecg_group = VGroup()
        for j in range(3):
            wave_points = []
            base_y = -1.2 - j * 0.3
            for i in range(40):
                x = -2 + i * 0.1
                if 15 <= i <= 17:
                    y = base_y + 0.5 * np.sin((i-15) * PI / 2)
                elif 25 <= i <= 27:
                    y = base_y + 0.5 * np.sin((i-25) * PI / 2)
                else:
                    y = base_y
                wave_points.append([x, y, 0])

            wave_line = VMobject()
            wave_line.set_points_as_corners(wave_points)
            wave_line.set_color([GREEN_C, GREEN, YELLOW][j])
            wave_line.set_stroke(width=2 + j)
            ecg_group.add(wave_line)
        group.add(ecg_group)

        # 攻击波浪（多层被弹开）
        attack_waves = VGroup()
        for wave in range(4):
            wave_arrows = VGroup()
            for i in range(6):
                angle = -PI/3 + i * PI/9 + wave * 0.2
                start_r = 2.5 + wave * 0.3
                end_r = 1.2
                start = [start_r * np.cos(angle), start_r * np.sin(angle), 0]
                end = [end_r * np.cos(angle), end_r * np.sin(angle), 0]
                arrow = Arrow(start, end, color=RED_C, buff=0.05, stroke_width=2)
                arrow.set_opacity(0.7 - wave * 0.15)
                wave_arrows.add(arrow)
            attack_waves.add(wave_arrows)
        group.add(attack_waves)

        def create_animation():
            return AnimationGroup(
                # 多层心脏依次跳动
                heart_group[0].animate.scale(1.2).set_color(RED_E),
                heart_group[1].animate.scale(1.15).set_color(RED_C),
                heart_group[2].animate.scale(1.1).set_color(RED),
                # 波形层层闪烁流动
                *[ecg_group[i].animate.set_color([GREEN, YELLOW, GREEN_C][i]).shift(RIGHT * 0.2)
                  for i in range(3)],
                # 攻击波被层层弹开
                *[wave.animate.shift(LEFT * 0.8).rotate(PI/6).set_opacity(0.2)
                  for wave in attack_waves],
                rate_func=there_and_back,
                run_time=2
            )

        group.create_animation = create_animation
        return group

    # ========== 特征2: 计划被打乱，从容调整 - 水流绕道 ==========
    def anim_flowing_water(self):
        """水流绕道动画 - 多层粒子流动效果"""
        group = VGroup()

        # 多层障碍物（岩石）
        obstacles = VGroup()
        for i in range(3):
            obstacle = Rectangle(
                height=1.2 + i*0.2,
                width=0.3 + i*0.1,
                color=[GRAY, GRAY_B, GRAY_C][i],
                fill_opacity=0.8 - i*0.2
            )
            obstacles.add(obstacle)
        group.add(obstacles)

        # 多层流动粒子
        all_particles = VGroup()
        colors = [BLUE_E, BLUE_D, BLUE_C, BLUE_B, BLUE_A]

        for layer in range(5):
            layer_particles = VGroup()
            for i in range(10):
                # 上方弧线流动
                t = i / 9
                angle = PI * t
                x = -2.5 + t * 5
                y = 0.8 + layer * 0.15 + 0.3 * np.sin(angle)
                dot1 = Dot(point=[x, y, 0], radius=0.05 + layer*0.01, color=colors[layer])

                # 下方弧线流动
                y2 = -0.8 - layer * 0.15 - 0.3 * np.sin(angle)
                dot2 = Dot(point=[x, y2, 0], radius=0.05 + layer*0.01, color=colors[layer])

                layer_particles.add(dot1, dot2)
            all_particles.add(layer_particles)
        group.add(all_particles)

        # 流动轨迹线（多层弧线）
        path_lines = VGroup()
        for i in range(4):
            offset = i * 0.2
            upper_path = ArcBetweenPoints(
                [-2.5, 1 + offset, 0],
                [2.5, 1 + offset, 0],
                angle=-PI/4 - i*0.1,
                color=BLUE_C,
                stroke_width=2 - i*0.3
            )
            lower_path = ArcBetweenPoints(
                [-2.5, -1 - offset, 0],
                [2.5, -1 - offset, 0],
                angle=PI/4 + i*0.1,
                color=BLUE_C,
                stroke_width=2 - i*0.3
            )
            path_lines.add(upper_path, lower_path)
        group.add(path_lines)

        # 流动光效
        glow_dots = VGroup()
        for i in range(6):
            glow = Dot(point=[-2 + i*0.8, 1.2, 0], radius=0.1, color=YELLOW)
            glow.set_opacity(0.6)
            glow_dots.add(glow)
            glow2 = Dot(point=[-2 + i*0.8, -1.2, 0], radius=0.1, color=YELLOW)
            glow2.set_opacity(0.6)
            glow_dots.add(glow2)
        group.add(glow_dots)

        def create_animation():
            return AnimationGroup(
                # 多层粒子依次流动
                *[layer.animate.shift(RIGHT * 2).rotate(PI/8) for layer in all_particles],
                # 轨迹线逐层发光
                *[path.animate.set_color([BLUE, BLUE_B, WHITE][i%3]).set_stroke(width=4-i)
                  for i, path in enumerate(path_lines)],
                # 光点流动
                glow_dots.animate.shift(RIGHT * 1.5).set_opacity(0.3),
                rate_func=linear,
                run_time=2
            )

        group.create_animation = create_animation
        return group

    # ========== 特征3: 听到坏消息，先深呼吸 - 呼吸波浪 ==========
    def anim_breathing_wave(self):
        """呼吸波浪动画 - 多层扩散+粒子效果"""
        group = VGroup()

        # 人物轮廓（多层）
        person_group = VGroup()
        for i in range(3):
            person = Circle(
                radius=0.5 + i * 0.1,
                color=WHITE,
                stroke_width=2 - i * 0.5,
                stroke_opacity=0.8 - i * 0.2
            )
            person_group.add(person)
        group.add(person_group)

        # 多层呼吸环（错位扩散）
        all_rings = VGroup()
        for layer in range(3):
            rings = VGroup()
            for i in range(5):
                ring = Circle(
                    radius=0.8 + i * 0.3 + layer * 0.1,
                    color=[BLUE_C, BLUE_D, BLUE_E][layer],
                    stroke_width=3 - layer * 0.5,
                    stroke_opacity=0.6 - i * 0.1
                )
                rings.add(ring)
            all_rings.add(rings)
        group.add(all_rings)

        # 倒计时数字（带光晕效果）
        numbers = VGroup()
        for i, num in enumerate(["3", "2", "1"]):
            num_group = VGroup()
            # 光晕
            for j in range(3):
                glow = Text(num, font="Heiti SC", font_size=40 + j*5, color=YELLOW)
                glow.move_to(RIGHT * 1.8 + UP * (1 - i) * 0.8)
                glow.set_opacity(0.3 - j * 0.1)
                num_group.add(glow)
            # 主数字
            main = Text(num, font="Heiti SC", font_size=40, color=YELLOW, weight=BOLD)
            main.move_to(RIGHT * 1.8 + UP * (1 - i) * 0.8)
            num_group.add(main)
            numbers.add(num_group)
        group.add(numbers)

        # 呼吸粒子
        breath_particles = VGroup()
        for i in range(20):
            angle = i * PI / 10
            for r in [1.2, 1.8, 2.4]:
                x = r * np.cos(angle)
                y = r * np.sin(angle)
                particle = Dot(point=[x, y, 0], radius=0.04, color=BLUE_B)
                breath_particles.add(particle)
        group.add(breath_particles)

        # 深呼吸文字（带装饰）
        breath_group = VGroup()
        breath_text = Text("深呼吸", font="Heiti SC", font_size=28, color=BLUE_C, weight=BOLD)
        breath_text.move_to(DOWN * 1.5)
        breath_group.add(breath_text)
        # 装饰线
        for offset in [-0.8, 0.8]:
            line = Line(
                [offset, -1.5, 0],
                [offset + (0.3 if offset > 0 else -0.3), -1.5, 0],
                color=BLUE_C
            )
            breath_group.add(line)
        group.add(breath_group)

        def create_animation():
            return AnimationGroup(
                # 多层人物呼吸效果
                *[p.animate.scale(1.1 + i*0.05) for i, p in enumerate(person_group)],
                # 多层环依次扩散
                *[ring.animate.scale(1.5).set_opacity(0)
                  for rings in all_rings for ring in rings],
                # 数字光晕闪烁
                *[num_group.animate.set_opacity(1).scale(1.2)
                  for num_group in numbers],
                # 呼吸粒子散开
                breath_particles.animate.scale(1.5).shift(RIGHT * 0.3).set_opacity(0.3),
                # 文字发光
                breath_group.animate.scale(1.1).set_color(BLUE),
                rate_func=there_and_back,
                run_time=2
            )

        group.create_animation = create_animation
        return group

    # ========== 特征4: 被当众质疑，微笑回应 - 淡定波纹 ==========
    def anim_calm_ripple(self):
        """淡定波纹动画 - 微笑消融质疑"""
        group = VGroup()

        # 中心微笑（多层光晕）
        face_group = VGroup()
        for i in range(4):
            face_circle = Circle(
                radius=0.8 + i * 0.15,
                color="#FFD700",
                fill_opacity=0.15 - i * 0.03,
                stroke_width=3 - i * 0.5
            )
            face_group.add(face_circle)

        # 眼睛（眯起带笑意）
        left_eye = Arc(radius=0.15, angle=PI, color="#FFD700", stroke_width=3)
        left_eye.rotate(PI)
        left_eye.shift(LEFT * 0.2 + UP * 0.15)
        right_eye = Arc(radius=0.15, angle=PI, color="#FFD700", stroke_width=3)
        right_eye.rotate(PI)
        right_eye.shift(RIGHT * 0.2 + UP * 0.15)

        # 微笑（多层）
        smile_group = VGroup()
        for i in range(3):
            smile = Arc(radius=0.4 + i * 0.05, angle=PI, color="#FFD700", stroke_width=4 - i)
            smile.rotate(-PI/2)
            smile.shift(DOWN * 0.1 - i * 0.02)
            smile_group.add(smile)

        face_group.add(left_eye, right_eye, smile_group)
        group.add(face_group)

        # 多层波纹扩散（不同速度）
        all_ripples = VGroup()
        for layer in range(3):
            ripples = VGroup()
            for i in range(4):
                ripple = Circle(
                    radius=1.2 + i * 0.4 + layer * 0.15,
                    color=[BLUE_C, BLUE_D, BLUE_E][layer],
                    stroke_width=3 - layer * 0.5,
                    stroke_opacity=0.7 - i * 0.15
                )
                ripples.add(ripple)
            all_ripples.add(ripples)
        group.add(all_ripples)

        # 质疑的问号（多层环绕）
        all_questions = VGroup()
        for layer in range(2):
            questions = VGroup()
            for i in range(8):
                angle = i * PI / 4 + layer * 0.3
                x = (2.2 + layer * 0.5) * np.cos(angle)
                y = (2.2 + layer * 0.5) * np.sin(angle)
                q = Text("?", font="Heiti SC", font_size=24 + layer * 4, color=[GRAY, GRAY_B][layer])
                q.move_to([x, y, 0])
                q.set_opacity(0.7 - layer * 0.2)
                questions.add(q)
            all_questions.add(questions)
        group.add(all_questions)

        # 淡定光环
        calm_ring = Annulus(inner_radius=0.9, outer_radius=1.1, color="#FFD700", fill_opacity=0.1)
        group.add(calm_ring)

        def create_animation():
            return AnimationGroup(
                # 微笑光晕层层扩散
                *[f.animate.scale(1.15 + i*0.05) for i, f in enumerate(face_group[:4])],
                # 眼睛弯起
                left_eye.animate.shift(UP * 0.05),
                right_eye.animate.shift(UP * 0.05),
                # 微笑更灿烂
                smile_group.animate.scale(1.2),
                # 多层波纹依次扩散消融
                *[ripple.animate.scale(1.7).set_opacity(0)
                  for ripples in all_ripples for ripple in ripples],
                # 问号层层被消融
                *[q.animate.scale(0.4).set_opacity(0)
                  for questions in all_questions for q in questions],
                # 淡定光环扩散
                calm_ring.animate.scale(2).set_opacity(0),
                rate_func=linear,
                run_time=2
            )

        group.create_animation = create_animation
        return group

    # ========== 特征5: 遭遇失败，立即复盘 - 旋转上升 ==========
    def anim_spiral_rise(self):
        """旋转上升动画 - 多层螺旋攀升效果"""
        group = VGroup()

        # 多层螺旋路径
        spirals = VGroup()
        colors = [BLUE_E, BLUE_D, BLUE_C]
        for layer in range(3):
            spiral = ParametricFunction(
                lambda t, l=layer: [
                    (0.2 + l*0.03) * t * np.cos((2.5 + l*0.2) * t),
                    (0.2 + l*0.03) * t * np.sin((2.5 + l*0.2) * t) - 0.8 + l*0.1,
                    0
                ],
                t_range=[0, 6],
                color=colors[layer],
                stroke_width=4 - layer
            )
            spirals.add(spiral)
        group.add(spirals)

        # 多层上升箭头
        arrows = VGroup()
        for i in range(3):
            arrow = Arrow(
                start=DOWN * (1 + i*0.3),
                end=UP * (1.5 + i*0.2),
                color=[GREEN_E, GREEN_D, GREEN_C][i],
                buff=0.1,
                stroke_width=3 - i*0.5
            )
            arrows.add(arrow)
        group.add(arrows)

        # 上升节点（多层螺旋分布）
        all_nodes = VGroup()
        for layer in range(3):
            nodes = VGroup()
            for i in range(6):
                angle = (2.5 + layer*0.2) * i * 0.8
                r = (0.2 + layer*0.03) * i * 0.8
                x = r * np.cos(angle)
                y = r * np.sin(angle) - 0.8 + layer*0.1
                node = Dot(
                    point=[x, y, 0],
                    radius=0.08 + layer*0.02,
                    color=[YELLOW_E, YELLOW_D, YELLOW_C][layer]
                )
                nodes.add(node)
            all_nodes.add(nodes)
        group.add(all_nodes)

        # "复盘"文字（带光晕）
        review_group = VGroup()
        for i in range(3):
            glow = Text("复盘", font="Heiti SC", font_size=26+i*4, color=GREEN)
            glow.move_to(RIGHT * 1.5)
            glow.set_opacity(0.3 - i*0.1)
            review_group.add(glow)
        review_main = Text("复盘", font="Heiti SC", font_size=26, color=GREEN, weight=BOLD)
        review_main.move_to(RIGHT * 1.5)
        review_group.add(review_main)
        group.add(review_group)

        # 成功星星
        stars = VGroup()
        for i in range(8):
            angle = i * PI / 4
            x = 2 * np.cos(angle)
            y = 2 * np.sin(angle)
            star = Text("✦", font_size=20, color=YELLOW)
            star.move_to([x, y, 0])
            stars.add(star)
        group.add(stars)

        def create_animation():
            return AnimationGroup(
                # 多层螺旋依次变色上升
                *[spirals[i].animate.set_color([GREEN_E, GREEN_D, GREEN_C][i]).shift(UP * 0.2*(i+1))
                  for i in range(3)],
                # 多层箭头依次脉动
                *[arrows[i].animate.scale(1.15).set_color(GREEN_C) for i in range(3)],
                # 节点依次闪烁升起
                *[node.animate.scale(2).set_color(GREEN).shift(UP * 0.3)
                  for nodes in all_nodes for node in nodes],
                # 复盘文字发光
                review_group.animate.scale(1.2),
                # 星星闪烁
                stars.animate.scale(1.3).set_color(GOLD),
                rate_func=there_and_back,
                run_time=2
            )

        group.create_animation = create_animation
        return group

    # ========== 特征6: 被人误解，懒得解释 - 静音屏障 ==========
    def anim_silent_barrier(self):
        """静音屏障动画 - 多层声波阻挡效果"""
        group = VGroup()

        # 中心人物（多层淡定表情）
        person_group = VGroup()
        for i in range(3):
            person = Circle(radius=0.45 + i*0.1, color=WHITE, fill_opacity=0.08 - i*0.02, stroke_width=2-i*0.3)
            person_group.add(person)
        # 表情
        face_group = VGroup()
        for offset in [0, -0.02, 0.02]:
            face = Text("- _ -", font="Heiti SC", font_size=20, color=WHITE)
            face.scale(0.6)
            face.shift(UP * offset)
            face_group.add(face)
        person_group.add(face_group)
        group.add(person_group)

        # 多层静音屏障（不同颜色）
        barriers = VGroup()
        barrier_colors = [BLUE_E, BLUE_D, BLUE_C, BLUE_B]
        for i in range(4):
            barrier = Circle(
                radius=0.9 + i * 0.35,
                color=barrier_colors[i],
                stroke_width=3 - i * 0.4,
                stroke_opacity=0.6 - i * 0.1
            )
            barriers.add(barrier)
        group.add(barriers)

        # 静音符号（带光晕）
        mute_group = VGroup()
        for i in range(3):
            mute = Text("🔇", font_size=32 + i*4)
            mute.move_to(RIGHT * 1.5 + UP * 0.5)
            mute.set_opacity(0.4 - i * 0.1)
            mute_group.add(mute)
        mute_group.add(Text("🔇", font_size=32).move_to(RIGHT * 1.5 + UP * 0.5))
        group.add(mute_group)

        # 多层外部噪音波浪（从不同方向涌来）
        all_noise = VGroup()
        for layer in range(3):
            noise_layer = VGroup()
            for i in range(8):
                angle = i * PI / 4 + layer * 0.2
                r = 2 + layer * 0.4
                # 声波弧线
                for j in range(3):
                    arc_r = 0.15 + j * 0.08
                    x = (r + j * 0.3) * np.cos(angle)
                    y = (r + j * 0.3) * np.sin(angle)
                    arc = Arc(radius=arc_r, angle=PI*0.7, color=[RED_E, RED_D, RED_C][layer], stroke_width=2-j*0.3)
                    arc.move_to([x, y, 0])
                    arc.rotate(angle + PI)
                    arc.set_opacity(0.6 - j*0.15)
                    noise_layer.add(arc)
            all_noise.add(noise_layer)
        group.add(all_noise)

        # 阻挡火花效果
        sparks = VGroup()
        for i in range(12):
            angle = i * PI / 6
            x = 1.2 * np.cos(angle)
            y = 1.2 * np.sin(angle)
            spark = Dot(point=[x, y, 0], radius=0.05, color=YELLOW)
            spark.set_opacity(0)
            sparks.add(spark)
        group.add(sparks)

        def create_animation():
            return AnimationGroup(
                # 多层屏障依次脉动
                *[barriers[i].animate.scale(1.2 + i*0.05).set_color([BLUE_D, BLUE_C, BLUE_B, WHITE][i])
                  for i in range(4)],
                # 人物淡定微动
                person_group.animate.scale(1.08),
                # 多层噪音被依次阻挡
                *[noise.animate.scale(0.5).shift(LEFT*0.3).set_opacity(0.1) for noise in all_noise],
                # 静音符号闪烁放大
                mute_group.animate.scale(1.5),
                # 阻挡火花闪现
                sparks.animate.set_opacity(1).scale(1.5),
                rate_func=there_and_back,
                run_time=2
            )

        group.create_animation = create_animation
        return group

    # ========== 特征7: 突发事件，冷静处理 - 核心稳定 ==========
    def anim_stable_core(self):
        """核心稳定动画 - 多层核心+混乱镇压效果"""
        group = VGroup()

        # 稳定核心（多层同心）
        core_group = VGroup()
        core_colors = [GREEN_E, GREEN_D, GREEN_C, GREEN_B, GREEN_A]
        for i in range(5):
            core = Circle(
                radius=0.25 + i * 0.15,
                color=core_colors[i],
                fill_opacity=0.5 - i * 0.08,
                stroke_width=3 - i * 0.4
            )
            core_group.add(core)
        group.add(core_group)

        # 混乱粒子（多层环绕+随机）
        all_chaos = VGroup()
        for layer in range(3):
            chaos = VGroup()
            for i in range(12):
                angle = i * PI / 6 + layer * 0.4
                r = 1.3 + layer * 0.5 + np.random.random() * 0.3
                x = r * np.cos(angle)
                y = r * np.sin(angle)
                # 不同形状表示混乱
                if i % 3 == 0:
                    shape = Square(side_length=0.12, color=[RED_E, RED_D, RED_C][layer])
                elif i % 3 == 1:
                    shape = Triangle(radius=0.08, color=[RED_E, RED_D, RED_C][layer])
                else:
                    shape = Dot(point=[x, y, 0], radius=0.07, color=[RED_E, RED_D, RED_C][layer])
                if isinstance(shape, (Square, Triangle)):
                    shape.move_to([x, y, 0])
                chaos.add(shape)
            all_chaos.add(chaos)
        group.add(all_chaos)

        # 稳定射线（多层脉动）
        all_rays = VGroup()
        for layer in range(3):
            rays = VGroup()
            for i in range(12):
                angle = i * PI / 6 + layer * 0.1
                x = (1.8 + layer * 0.3) * np.cos(angle)
                y = (1.8 + layer * 0.3) * np.sin(angle)
                ray = Line([0, 0, 0], [x, y, 0], color=[GREEN_C, GREEN_B, WHITE][layer], stroke_width=3 - layer * 0.5)
                rays.add(ray)
            all_rays.add(rays)
        group.add(all_rays)

        # "稳"字（带光晕）
        stable_group = VGroup()
        for i in range(4):
            glow = Text("稳", font="Heiti SC", font_size=48 + i*6, color=GREEN)
            glow.set_opacity(0.3 - i * 0.08)
            stable_group.add(glow)
        stable_main = Text("稳", font="Heiti SC", font_size=48, color=GREEN, weight=BOLD)
        stable_group.add(stable_main)
        group.add(stable_group)

        # 镇定波纹
        calm_waves = VGroup()
        for i in range(4):
            wave = Circle(radius=1 + i*0.3, color=GREEN, stroke_width=2, stroke_opacity=0.4)
            calm_waves.add(wave)
        group.add(calm_waves)

        def create_animation():
            return AnimationGroup(
                # 核心层层扩散增强
                *[core_group[i].animate.scale(1.5 + i*0.1).set_color([GREEN_D, GREEN_C, GREEN_B, WHITE, WHITE][i])
                  for i in range(5)],
                # 多层射线依次强脉动
                *[rays.animate.scale(1.4).set_color(GREEN)
                  for rays in all_rays],
                # 混乱层层被镇压消失
                *[chaos.animate.scale(0.3).rotate(PI).set_opacity(0.1) for chaos in all_chaos],
                # 稳字发光显现
                stable_group.animate.scale(1.4),
                # 镇定波纹扩散
                *[wave.animate.scale(2).set_opacity(0) for wave in calm_waves],
                rate_func=there_and_back,
                run_time=2
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
