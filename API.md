
> 接口地址为前端代理后请求的地址，后端编写时无需携带/api路由。如无特殊备注，所有API接口均需APIKey！！！

### Auth
> - [ ] 登录 `POST /api/auth/login`

| 请求参数     | 参数值    | 备注  |
| -------- | ------ | --- |
| username | string |     |
| password | string |     |

| 返回参数 | 默认值     | 错误值      |
| ---- | ------- | -------- |
| code | 200     |          |
| msg  | success | 用户名或密码错误 |

> - [ ] 注册 `POST /api/auth/reg`


| 请求参数     | 参数值    | 备注          |
| -------- | ------ | ----------- |
| username | number | 用户名称仅限QQ号   |
| password | string | 仅限 数字+字母 组合 |
| email    | string |             |

| 返回参数 | 默认值     | 错误值1   | 错误值2  |
| ---- | ------- | ------ | ----- |
| code | 200     |        |       |
| msg  | success | 密码格式错误 | 账号已存在 |

### User
