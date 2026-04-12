from manim import *
import numpy as np

# 设置中文字体
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 8
config.frame_width = 14.22


class InnerStrength10Traits(Scene):
    def construct(self):
        # 设置纯黑背景
        self.camera.background_color = BLACK

        # ========== 片头 ==========
        self.show_intro()

        # ========== 十大特征 ==========
        traits = [
            ("1. 不在乎他人评价", "有自己的价值判断体系，\n不被外界声音左右"),
            ("2. 遇事不抱怨", "把精力放在解决问题上，\n而非发泄情绪"),
            ("3. 能享受独处", "不依赖外界刺激，\n内心自洽丰盈"),
            ("4. 不害怕被拒绝", "把拒绝当反馈，\n而非对自我的否定"),
            ("5. 情绪稳定", "不因一时得失大喜大悲，\n内核稳定"),
            ("6. 敢于说\"不\"", "有清晰的边界感，\n不讨好不委屈自己"),
            ("7. 接纳不完美", "允许自己犯错，\n不苛求事事完美"),
            ("8. 不与他人比较", "专注自己的节奏，\n不被外界带偏"),
            ("9. 延迟满足", "能为长远目标，\n克制眼前欲望"),
            ("10. 持续自我迭代", "把挫折当成长养分，\n越挫越勇"),
        ]

        # 片头标题保留作为header
        header_title = Text(
            "内心强大到可怕的十大特征",
            font="Songti SC",
            font_size=22,
            color=YELLOW
        )
        header_title.move_to(UP * 3.5)

        for title, desc in traits:
            self.show_trait(title, desc, header_title)

        # ========== 片尾 ==========
        self.show_outro()

    def show_intro(self):
        """片头动画"""
        # 主标题 - 黄色显眼
        title = Text(
            "内心强大到可怕的十大特征",
            font="Songti SC",
            font_size=48,
            color=YELLOW
        )
        title.move_to(UP * 2)

        # 副标题
        subtitle = Text(
            "你中了几个？",
            font="Songti SC",
            font_size=32,
            color=GRAY_C
        )
        subtitle.move_to(UP * 0.5)

        # 盾牌图标动画（右边30%区域）
        shield = self.create_shield()
        shield.move_to(RIGHT * 4 + UP * 0.5)
        shield.scale(0.8)

        # 播放动画
        self.play(
            Write(title),
            run_time=1.5
        )
        self.play(
            FadeIn(subtitle, shift=UP * 0.3),
            Create(shield),
            run_time=1.5
        )
        self.wait(2)

        # 片头标题保留，缩小到22大小，移到上居中
        self.play(
            FadeOut(subtitle),
            FadeOut(shield),
            title.animate.scale(22/48).move_to(UP * 3.5),
            run_time=0.8
        )
        self.wait(0.5)

    def create_shield(self):
        """创建盾牌图标"""
        # 盾牌外轮廓
        shield_shape = Polygon(
            [-1, 1.5, 0],
            [1, 1.5, 0],
            [1, 0, 0],
            [0, -1.5, 0],
            [-1, 0, 0],
            color=BLUE_C,
            fill_opacity=0.3,
            stroke_width=3
        )

        # 内部对勾
        checkmark = VMobject()
        checkmark.set_points_as_corners([
            [-0.4, 0, 0],
            [-0.1, -0.3, 0],
            [0.5, 0.6, 0]
        ])
        checkmark.set_color(GREEN_C)
        checkmark.set_stroke(width=4)

        return VGroup(shield_shape, checkmark)

    def show_trait(self, title_text, desc_text, header_title=None):
        """展示单个特征"""
        # 标题（左边70%区域）- 黄色
        title = Text(
            title_text,
            font="Songti SC",
            font_size=36,
            color=YELLOW
        )
        title.move_to(LEFT * 3.5 + UP * 1.5)

        # 描述 - 白色
        desc = Text(
            desc_text,
            font="Songti SC",
            font_size=24,
            color=WHITE,
            line_spacing=1.5
        )
        desc.move_to(LEFT * 3.5 + DOWN * 0.5)

        # 右边动画区域 - 根据特征创建不同动画
        animation_mob = self.create_trait_animation(title_text)
        animation_mob.move_to(RIGHT * 4)

        # 播放动画
        self.play(
            Write(title),
            run_time=0.8
        )
        self.play(
            FadeIn(desc, shift=UP * 0.2),
            run_time=0.6
        )
        self.play(
            animation_mob.create_animation(),
            run_time=1.5
        )
        self.wait(1.5)

        # 退出
        anims = [FadeOut(title), FadeOut(desc), FadeOut(animation_mob)]
        if header_title is not None:
            anims.append(FadeOut(header_title))
        self.play(*anims, run_time=0.4)

    def create_trait_animation(self, title_text):
        """为每个特征创建对应的动画对象"""
        if "不在乎他人评价" in title_text:
            return self.anim_independent_judgment()
        elif "遇事不抱怨" in title_text:
            return self.anim_no_complaint()
        elif "享受独处" in title_text:
            return self.anim_solitude()
        elif "不害怕被拒绝" in title_text:
            return self.anim_no_fear_rejection()
        elif "情绪稳定" in title_text:
            return self.anim_emotional_stability()
        elif "敢于说\"不\"" in title_text:
            return self.anim_say_no()
        elif "接纳不完美" in title_text:
            return self.anim_accept_imperfection()
        elif "不与他人比较" in title_text:
            return self.anim_no_comparison()
        elif "延迟满足" in title_text:
            return self.anim_delayed_gratification()
        elif "持续自我迭代" in title_text:
            return self.anim_continuous_growth()
        else:
            return self.anim_default()

    # ========== 各个特征的动画 ==========

    def anim_independent_judgment(self):
        """1. 不在乎他人评价 - 独立判断"""
        # 中心人物
        person = Circle(radius=0.5, color=BLUE_C, fill_opacity=0.5)
        person.shift(UP * 0.5)

        # 周围的意见箭头
        arrows = VGroup()
        for angle in np.linspace(0, 2 * PI, 8, endpoint=False):
            start = np.array([np.cos(angle), np.sin(angle), 0]) * 2
            end = np.array([np.cos(angle), np.sin(angle), 0]) * 1.2
            arrow = Arrow(start, end, color=GRAY_D, buff=0)
            arrows.add(arrow)

        # 防护罩
        shield = Circle(radius=1.3, color=GREEN_C, stroke_width=2)

        mob = VGroup(arrows, shield, person)

        def create_anim():
            return AnimationGroup(
                FadeIn(arrows),
                Create(shield),
                FadeIn(person),
                lag_ratio=0.3
            )

        mob.create_animation = create_anim
        return mob

    def anim_no_complaint(self):
        """2. 遇事不抱怨 - 专注解决"""
        # 问题方块
        problem = Square(side_length=1, color=RED_C, fill_opacity=0.3)
        problem.shift(UP * 1)

        # 思考气泡
        thought = Ellipse(width=1.5, height=0.8, color=YELLOW_C)
        thought.shift(DOWN * 0.5)

        # 解决方案灯泡
        bulb = Circle(radius=0.3, color=YELLOW, fill_opacity=0.8)
        bulb.shift(DOWN * 0.5)

        # 工具图标
        tools = VGroup(
            Rectangle(height=0.4, width=0.1, color=GRAY_C).shift(LEFT * 0.5 + DOWN * 1.2),
            Rectangle(height=0.1, width=0.4, color=GRAY_C).shift(RIGHT * 0.5 + DOWN * 1.2)
        )

        mob = VGroup(problem, thought, bulb, tools)

        def create_anim():
            return AnimationGroup(
                FadeIn(problem),
                FadeIn(thought),
                FadeIn(bulb.scale(1.5)),
                FadeIn(tools),
                lag_ratio=0.2
            )

        mob.create_animation = create_anim
        return mob

    def anim_solitude(self):
        """3. 能享受独处 - 内心丰盈"""
        # 人物剪影
        head = Circle(radius=0.3, color=BLUE_C, fill_opacity=0.5)
        head.shift(UP * 0.8)
        body = Rectangle(height=0.8, width=0.6, color=BLUE_C, fill_opacity=0.5)
        person = VGroup(head, body)

        # 内心的光芒
        rays = VGroup()
        for angle in np.linspace(0, 2 * PI, 12, endpoint=False):
            start = np.array([np.cos(angle), np.sin(angle), 0]) * 0.8
            end = np.array([np.cos(angle), np.sin(angle), 0]) * 1.5
            ray = Line(start, end, color=YELLOW_C, stroke_width=2)
            rays.add(ray)

        # 内心的圆
        inner_circle = Circle(radius=0.6, color=YELLOW, fill_opacity=0.2)

        mob = VGroup(person, inner_circle, rays)

        def create_anim():
            return AnimationGroup(
                FadeIn(person),
                FadeIn(inner_circle),
                Create(rays),
                lag_ratio=0.2
            )

        mob.create_animation = create_anim
        return mob

    def anim_no_fear_rejection(self):
        """4. 不害怕被拒绝 - 把拒绝当反馈"""
        # 拒绝的X
        x_mark = VGroup(
            Line(UL * 0.5, DR * 0.5, color=RED_C, stroke_width=4),
            Line(UR * 0.5, DL * 0.5, color=RED_C, stroke_width=4)
        )
        x_mark.shift(LEFT * 1 + UP * 0.5)

        # 转换箭头
        arrow = Arrow(LEFT * 0.3, RIGHT * 0.8, color=YELLOW_C, buff=0)

        # 反馈/成长的向上箭头
        growth = Arrow(DOWN * 0.5, UP * 1, color=GREEN_C, buff=0)
        growth.shift(RIGHT * 1.5)

        # 阶梯
        steps = VGroup()
        for i in range(3):
            step = Rectangle(height=0.15, width=0.6 + i * 0.3, color=GRAY_C)
            step.shift(RIGHT * 1.5 + DOWN * (0.3 - i * 0.2))
            steps.add(step)

        mob = VGroup(x_mark, arrow, growth, steps)

        def create_anim():
            return AnimationGroup(
                FadeIn(x_mark),
                Create(arrow),
                Create(growth),
                FadeIn(steps),
                lag_ratio=0.2
            )

        mob.create_animation = create_anim
        return mob

    def anim_emotional_stability(self):
        """5. 情绪稳定 - 内核稳定"""
        # 波动的外界
        wave1 = FunctionGraph(
            lambda x: 0.5 * np.sin(3 * x),
            x_range=[-2, 2],
            color=RED_C
        ).shift(UP * 1.5)

        wave2 = FunctionGraph(
            lambda x: 0.3 * np.cos(4 * x),
            x_range=[-2, 2],
            color=ORANGE
        ).shift(UP * 1)

        # 稳定的内核
        core = Circle(radius=0.5, color=BLUE_C, fill_opacity=0.5)

        # 稳定线
        stable_line = Line(LEFT * 2, RIGHT * 2, color=GREEN_C, stroke_width=3)

        mob = VGroup(wave1, wave2, core, stable_line)

        def create_anim():
            return AnimationGroup(
                Create(wave1),
                Create(wave2),
                FadeIn(core),
                Create(stable_line),
                lag_ratio=0.2
            )

        mob.create_animation = create_anim
        return mob

    def anim_say_no(self):
        """6. 敢于说\"不\" - 边界感"""
        # 边界线
        boundary = Rectangle(height=3, width=2.5, color=BLUE_C, stroke_width=3)

        # 中心人物
        person = Dot(color=YELLOW).scale(2)

        # 外界的请求（箭头）
        arrows = VGroup()
        for pos in [LEFT * 2, RIGHT * 2, UP * 1.8, DOWN * 1.8]:
            arrow = Arrow(pos, pos * 0.5, color=GRAY_C, buff=0)
            arrows.add(arrow)

        # 拒绝的屏障
        barrier = DashedVMobject(
            Rectangle(height=2.5, width=2, color=GREEN_C),
            num_dashes=20
        )

        # NO文字
        no_text = Text("NO", font_size=36, color=RED_C)

        mob = VGroup(boundary, person, arrows, barrier, no_text)

        def create_anim():
            return AnimationGroup(
                Create(boundary),
                FadeIn(person),
                FadeIn(arrows),
                Create(barrier),
                Write(no_text),
                lag_ratio=0.15
            )

        mob.create_animation = create_anim
        return mob

    def anim_accept_imperfection(self):
        """7. 接纳不完美 - 允许犯错"""
        # 不完美的圆（有点缺口）
        imperfect = Arc(radius=1, angle=5 * PI / 3, color=ORANGE, stroke_width=4)
        imperfect.rotate(PI / 6)

        # 缺口处的小缺口标记
        gap = Arc(radius=0.8, angle=PI / 6, color=RED_C, stroke_width=3)
        gap.rotate(-PI / 3)

        # 接纳的拥抱形状
        left_arm = Arc(radius=0.8, angle=PI, color=GREEN_C, stroke_width=3)
        left_arc = ArcBetweenPoints(LEFT * 0.8 + DOWN * 0.3, LEFT * 0.3 + UP * 0.5, radius=0.8, color=GREEN_C)
        right_arc = ArcBetweenPoints(RIGHT * 0.3 + UP * 0.5, RIGHT * 0.8 + DOWN * 0.3, radius=0.8, color=GREEN_C)

        embrace = VGroup(left_arc, right_arc)

        # 对勾
        check = VMobject()
        check.set_points_as_corners([[0, 0.3, 0], [-0.2, 0, 0], [0.4, 0.6, 0]])
        check.set_color(GREEN)
        check.set_stroke(width=4)

        mob = VGroup(imperfect, gap, embrace, check)

        def create_anim():
            return AnimationGroup(
                Create(imperfect),
                FadeIn(gap),
                Create(embrace),
                Write(check),
                lag_ratio=0.2
            )

        mob.create_animation = create_anim
        return mob

    def anim_no_comparison(self):
        """8. 不与他人比较 - 专注自己"""
        # 自己的跑道
        own_path = Arrow(DOWN * 1.5, UP * 1.5, color=GREEN_C, buff=0)
        own_path.shift(LEFT * 0.8)

        # 他人的跑道
        other_path = Arrow(DOWN * 1.5, UP * 1.2, color=GRAY_D, buff=0)
        other_path.shift(RIGHT * 0.8)

        # 自己的进度
        own_dot = Dot(color=GREEN).scale(1.5)
        own_dot.move_to(LEFT * 0.8 + UP * 0.5)

        # 他人的进度
        other_dot = Dot(color=GRAY_C).scale(1.2)
        other_dot.move_to(RIGHT * 0.8 + UP * 0.8)

        # 分隔线（表示不比较）
        divider = DashedLine(DOWN * 1.5, UP * 1.5, color=BLUE_C, dash_length=0.1)

        mob = VGroup(own_path, other_path, own_dot, other_dot, divider)

        def create_anim():
            return AnimationGroup(
                Create(own_path),
                Create(other_path),
                FadeIn(own_dot),
                FadeIn(other_dot),
                Create(divider),
                lag_ratio=0.15
            )

        mob.create_animation = create_anim
        return mob

    def anim_delayed_gratification(self):
        """9. 延迟满足 - 克制眼前"""
        # 眼前的诱惑（小糖果）
        small_reward = Circle(radius=0.3, color=ORANGE, fill_opacity=0.6)
        small_reward.shift(LEFT * 1.5 + DOWN * 0.5)

        # 长远目标（大奖杯）
        trophy_base = Rectangle(height=0.3, width=0.4, color=YELLOW, fill_opacity=0.6)
        trophy_cup = Polygon(
            [-0.3, 0, 0], [0.3, 0, 0],
            [0.2, 0.5, 0], [-0.2, 0.5, 0],
            color=YELLOW, fill_opacity=0.6
        )
        trophy = VGroup(trophy_cup, trophy_base)
        trophy.shift(RIGHT * 1.5 + UP * 0.5)

        # 时间轴
        timeline = Arrow(LEFT * 2, RIGHT * 2, color=GRAY_C, buff=0)

        # 克制的手（抽象表示）
        hand = Line(UP * 0.8, DOWN * 0.3, color=BLUE_C, stroke_width=4)
        hand.shift(LEFT * 1)

        # 等待的时钟
        clock = Circle(radius=0.4, color=GREEN_C, stroke_width=2)
        clock_hand = Line(ORIGIN, UP * 0.25, color=GREEN_C, stroke_width=2)
        clock_group = VGroup(clock, clock_hand)

        mob = VGroup(timeline, small_reward, trophy, hand, clock_group)

        def create_anim():
            return AnimationGroup(
                Create(timeline),
                FadeIn(small_reward),
                FadeIn(trophy),
                Create(hand),
                FadeIn(clock_group),
                lag_ratio=0.15
            )

        mob.create_animation = create_anim
        return mob

    def anim_continuous_growth(self):
        """10. 持续自我迭代 - 越挫越勇"""
        # 螺旋上升
        spiral = ParametricFunction(
            lambda t: np.array([
                0.3 * t * np.cos(t * 2),
                0.3 * t * np.sin(t * 2) + 0.5,
                0
            ]),
            t_range=[0.5, 4],
            color=GREEN_C,
            stroke_width=3
        )

        # 挫折点（低谷）
        setbacks = VGroup()
        for pos in [LEFT * 0.8 + DOWN * 0.5, RIGHT * 0.5 + DOWN * 0.2]:
            x = VGroup(
                Line(UL * 0.15, DR * 0.15, color=RED_C, stroke_width=2),
                Line(UR * 0.15, DL * 0.15, color=RED_C, stroke_width=2)
            )
            x.move_to(pos)
            setbacks.add(x)

        # 成长的箭头
        growth_arrow = Arrow(DOWN * 1, UP * 1.5, color=YELLOW_C, buff=0)

        # 顶端的星星
        star = Star(n=5, outer_radius=0.3, inner_radius=0.15,
                    color=YELLOW, fill_opacity=0.8)
        star.shift(UP * 1.5)

        mob = VGroup(spiral, setbacks, growth_arrow, star)

        def create_anim():
            return AnimationGroup(
                Create(spiral),
                FadeIn(setbacks),
                Create(growth_arrow),
                FadeIn(star.scale(1.5)),
                lag_ratio=0.2
            )

        mob.create_animation = create_anim
        return mob

    def anim_default(self):
        """默认动画"""
        circle = Circle(radius=1, color=BLUE_C)

        def create_anim():
            return Create(circle)

        circle.create_animation = create_anim
        return circle

    def show_outro(self):
        """片尾总结"""
        # 片头标题保留到片尾
        header_title = Text(
            "内心强大到可怕的十大特征",
            font="Songti SC",
            font_size=22,
            color=YELLOW
        )
        header_title.move_to(UP * 3.5)
        self.add(header_title)

        # 总结语 - 黄色
        summary = Text(
            "内心强大，不是天生，而是选择",
            font="Songti SC",
            font_size=36,
            color=YELLOW
        )

        # 互动引导 - 白色
        cta = Text(
            "你中了几个？评论区聊聊",
            font="Songti SC",
            font_size=28,
            color=WHITE
        )
        cta.move_to(DOWN * 1.5)

        # 最终图标
        icon = self.create_shield()
        icon.scale(0.6)
        icon.move_to(UP * 1.5)

        self.play(
            FadeIn(icon),
            run_time=0.8
        )
        self.play(
            Write(summary),
            run_time=1
        )
        self.play(
            FadeIn(cta, shift=UP * 0.3),
            run_time=0.8
        )
        self.wait(2)

        # 结束
        self.play(
            FadeOut(header_title),
            FadeOut(icon),
            FadeOut(summary),
            FadeOut(cta),
            run_time=0.5
        )
