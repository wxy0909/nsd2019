# nsd_1908_devweb_day02

## CSS

- 由多个样式规则组成
- 每个样式规则有两个部分:选择器和样式声明

### css特征

- 继承性：父传子
- 层叠性：样式来自于多个样式表
- 优先级：应用的多个样式，如果有冲突，优先级高的生效

## 选择器

- 通用选择器，匹配所有元素：\*
- 元素选择器：html标签本身天然就是选择器，在名称前面没有任何修饰就是元素选择器
- 类选择器：使用class声明的选择器，可以理解为将多个元素放到同一组中
  - class为c3的元素：p.c3
  - p元素中的c4：p .c4

- id选择器：元素唯一的标识符
- 群组选择器：同时为多个元素设置样式，用逗号将选择器分隔，如h4, #id1, .c3
- 伪类选择器：经常为超链接设置访问前、访问后、鼠标悬停时的样式
  - a:link设置访问前的样式
  - a:hover设置鼠标悬停时的样式
  - a:visited设置访问后的样式

## 尺寸

- 最常用的是像素px，计算机屏幕上的一个点
- em：1em等于当前的字体尺寸,2em等于当前字体尺寸的两倍,继承父级元素的字体大小
- rem：与em类似,但是相对于根元素设置字体尺寸的倍数

## 颜色单位

- 使用RGB颜色，每种颜色都使用8位2进制数表示，表示成10进数为0~255，表示成16进制数为00~FF。颜色的数值越小，表示该颜色越暗，反之越亮
  - Red
  - Green
  - Blue






