# 电影查询系统

## 获取数据

https://movie.douban.com/

电影名称 豆瓣评分 排名 制片国家/地区 类型 导演 主演 语言 上映时间 视频链接 名著改编（剧情简介判断）剧情简介... （可扩展）

数据清洗和处理

数据结构：

```python
{
  	'rank': 1,
	'score': 9.7，
  	'country': '美国',
	'language':'英语',
	'director': ['弗兰克·德拉邦特'],
	'major character': ['蒂姆·罗宾斯 Tim Robbins', 'xxx'],
	'title': ['肖申克的救赎', 'The Shawshank Redemption', '月黑高飞(港)', '刺激1995(台)'],
	'type': ['犯罪', '剧情'],
	'date': '1994-09-10',
	'introduction':'20世纪40年代末，小有成就的青年银行家安迪（蒂姆·罗宾斯 Tim Robbins 饰）因涉嫌杀害妻子及她的情人而锒铛入狱。在这座名为鲨堡的监狱内，希望似乎虚无缥缈，终身监禁的惩罚无疑注定了安迪接下来灰暗绝望的人生。未过多久，安迪尝试接近囚犯中颇有声望的瑞德（摩根·弗 里曼 Morgan Freeman 饰），请求对方帮自己搞来小锤子。以此为契机，二人逐渐熟稔，安迪也仿佛在鱼龙混杂、罪恶横生、黑白混淆的牢狱中找到属于自己的求生之道。他利用自身的专业知识，帮助监狱管理层逃税、洗黑钱，同时凭借与瑞德的交往在犯人中间也渐渐受到礼遇。表面看来，他已如瑞德那样对那堵高墙从憎恨转变为处之泰然，但是对自由的渴望仍促使他朝着心中的希望和目标前进。而关于其罪行的真相，似乎更使这一切朝前推进了一步……本片根据著名作家斯蒂芬·金（Stephen Edwin King）的原著改编。' # 需要去掉\n
	'link':{'爱奇艺':'https://www.iqiyi.com/v_19rra0h3wg.html?vfm=m_331_dbdy&fv=4904d94982104144a1548dd9040df241','腾讯视频':'https://v.qq.com/x/cover/1o29ui77e85grdr.html?ptag=douban.movie'}
}
```

## 功能分析

- 可选一种分类，在候选影片选择查询；或者直接根据名称查询

- 统计点击率，可排序；

- 可以根据上映时间、豆瓣评分等排序
- 模糊查询
- 添加影评，展示在下方

## 程序设计

目标：尽量多的应用数据结构与算法，其他放在第二位；先有再好

web 应用（react）+ flask 后端服务器

接收查询内容输入/分类选择

```cpp
// 展示网页数据
init:
	return 所有数据;  // 服务器 -> web

// 提供分类
if (用户选中一个分类) { // web -> 服务器
	count ++;
	return 该分类下的所有数据;	// 服务器 -> web  => *根据指标查找*
} else if (用户选中排序原则) { // web -> 服务器
	return 排序后所有数据; // 服务器 -> web	=> *排序*（count; date; score）
}

// 根据输入显示特定项
if (接收到输入) {	 // web -> 服务器
	return 可能的结果;	// 服务器 -> web	=> *字符串匹配查找*
}
```