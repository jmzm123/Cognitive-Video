---
name: poster-generator
description: 为特定的标题生成“黑金极简风格”的 3D 认知视频封面提示词。适用于制作认知类、职场类、个人成长类的社交媒体配图。
argument-hint: [视频标题]
---

当你接收到标题（由 $ARGUMENTS 传入）时，请按照以下逻辑生成绘图提示词：

## 第一步：核心符号推导
基于标题的含义，选择一个具有“认知深度”或“科技感”的 3D 核心符号（如：大脑、眼睛、迷宫、指南针、上升阶梯、沙漏等）。

## 第二步：视觉规范要求
1. **背景**：必须是纯深黑 (Deep Black)，带有极细微的金属拉丝或碳纤维质感。
2. **配色**：严格黑金 (Black & Gold) 方案。金色需具备“浮雕 (Embossed)”、“发光 (Glowing)”和“拉丝金属 (Brushed Metal)”的质感。
3. **构图**：9:16 纵横比。标题位于正上方，核心符号位于画面中心，并带有光晕 (Halo) 效果。
4. **排除项**：严禁出现任何 UI 元素、点赞图标、心形图标或多余的数字。

## 第三步：输出提示词 (Prompt Output)

请直接输出如下格式的内容：

**建议符号：** [符号名称]
**Midjourney/DALL-E 提示词：**
> A high-end minimalist vertical poster on a deep black background. The central element is a prominent glowing, 3D metallic golden [核心符号], contained within a thin gold hexagon frame. Radiant golden light rays emit from the center. At the top center, large bold glowing golden Chinese characters "$ARGUMENTS" are displayed. Premium textures, high contrast, 8k resolution, cinematic lighting, no UI elements. --ar 9:16