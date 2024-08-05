> 接口地址为前端代理后请求的地址，后端编写时无需携带/api路由。
> 如无特殊备注，所有API接口均需token。Token位于Cookie，请求中自带。

### User
> - [X] 登录 `POST /api/user/login`

| 请求参数     | 参数值    | 备注  |
| -------- | ------ | --- |
| username | string |     |
| password | string |     |

| 返回参数 | 默认值     | 错误值      |
| ---- | ------- | -------- |
| code | 200     | 403      |
| msg  | success | 用户名或密码错误 |

> - [X] 注册 `POST /api/user/register`

| 请求参数     | 参数值    | 备注            |
| -------- | ------ | ------------- |
| email    | string | 用户邮箱          |
| username | string | 用户名称          |
| password | string | 密码仅限 数字+字母 组合 |

| 返回参数 | 默认值     | 错误值          |
| ---- | ------- | ------------ |
| code | 200     | 403          |
| msg  | success | 密码格式错误/账号已存在 |

> - [X] 账号激活 `POST /api/active/`

| 请求参数     | 参数值    | 备注            |
| -------- | ------ | ------------- |
| email    | string | 用户邮箱          |
| username | string | 用户名称          |
| active_code | string | 激活码 |

| 返回参数 | 默认值     | 错误值 |
| ---- | ------- | --- |
| code | 200     | 403 |
| msg  | success |     |

> - [X] 获取用户信息 `GET /api/user/`

| 返回参数       | 默认值 | 备注       |
| ---------- | --- | -------- |
| code       | 200 |          |
| username   |     | 用户名      |
| email      |     | 用户邮箱     |
| point      |     | 用户的积分    |
| point_last |     | 用户最后签到时间 |

### Instance
> - [X] 获取一键开服列表 `GET /api/instance/gameinfo`

不加参数时直接输出支持的游戏服务器类别列表

| 服务器类别        | id  | ico      |     |
| ------------ | --- | -------- | --- |
| Minecraft JE | 1   | 复制jhh的就行 |     |
| Minecraft BE | 2   | 复制jhh的就行 |     |
|              |     |          |     |

带有参数id时，向数据库获取对应id的类别的所有服务端，例子如下：

| 请求参数id | 返回参数                                                             |
| ------ | ---------------------------------------------------------------- |
| 2      | 参考[简幻欢的Api](https://api.simpfun.cn/api/games/kindlist?game_id=5) |

###### 至于版本整合包怎么来就要靠我们的MCSM接口小哥哥了（耳洞再小也是洞）

> - [X] 创建实例 `POST /api/instance/create`

| 请求参数  | 参数值    | 备注      |
| ----- | ------ | ------- |
| name | string | 实例名 |
| type | string | 实例类型 |

| 返回参数  | 默认值     | 错误值   | 备注    |
| ----- | ------- | ----- | ----- |
| code  | 200     |       |       |
| msg   | success |  | 返回消息  |
| user_uuid   | |  | 用户UUID  |
| instance_id   | |  | 实例uuid  |

> - [ ] 获取当前用户实例 `GET /api/user/instance`

| 请求参数  | 参数值    | 备注      |
| ----- | ------ | ------- |
| token | string | 用户token |
将对应用户的所有实例输出，基于McsmAPI进行查询

> - [ ] 获取实例信息 `GET /api/instance`

| 请求参数  | 参数值    | 备注      |
| ----- | ------ | ------- |
| id    | string | 实例id    |
| token | string | 用户token |
基于McsmAPI把对应id的实例查询一遍然后输出就行（一定检查实例是否属于当前用户）

> - [ ] 上传文件 `` 

空白zzzzzz
### 信息获取
> - [X] 获取公告 `GET /api/info/notices`

| 输出示例                                                                                |
| ----------------------------------------------------------------------------------- |
| {"id": 1,"title": "我是公告标题","content": "我是公告内容","type": "我是公告类型","time": "我是公告创建时间"} |
公告类型包括 `info` `warning` `error` `success`

> - [X] 获取广告 `GET /api/info/ads`

| 输出示例 |
| -------------------|
| {"id": 1,"name": "我是广告名称","img":"我是广告图片"}                                           |

### 积分系统
> - [X] 签到 `GET /api/point/sign`

通过读取point_log表来实现判断是否签到，每次签到为point_log增加一个数据，里面包含 签到用户名 签到获取积分 签到时间

当然user表中的point_last也需更新，用于前端锁定签到按钮

| 返回参数  | 默认值     | 错误值   | 备注    |
| ----- | ------- | ----- | ----- |
| code  | 200     |       |       |
| point |         |       | 获取的积分 |
| msg   | success | 今日已签到 | 返回消息  |

