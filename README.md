<!-- # FastAPI Robust Project

## Quick Start

### Build

fastapi-app/
├── app/                                   # 应用主目录
│   ├── api/                               # API 路由模块
│   │   ├── v1/                            # API 版本 1（支持未来多版本扩展）
│   │   │   ├── endpoints/                 # 各个功能模块的路由入口
│   │   │   │   ├── users.py               # 用户相关接口
│   │   │   │   ├── auth.py                # 登录、注册、JWT 管理接口（可选）
│   │   │   ├── __init__.py
│   │   ├── __init__.py
│   │
│   ├── core/                              # 核心功能配置
│   │   ├── config.py                      # 配置文件（环境变量、数据库连接等）
│   │   ├── security.py                    # 安全相关（密码加密、JWT 等）
│   │   ├── logger.py                      # 日志配置（可选）
│   │
│   ├── models/                            # 数据库 ORM 模型
│   │   ├── user.py                        # 用户表模型定义
│   │   ├── __init__.py
│   │
│   ├── schemas/                           # Pydantic 数据模型（请求/响应）
│   │   ├── user.py                        # 用户请求体/响应体定义
│   │   ├── token.py                       # Token 返回格式（用于 JWT）
│   │   ├── __init__.py
│   │
│   ├── services/                          # 业务服务层（复杂逻辑放这里）
│   │   ├── user_service.py                # 用户相关业务逻辑
│   │   ├── auth_service.py                # 登录 / 鉴权业务逻辑
│   │   ├── __init__.py
│   │
│   ├── db/                                # 数据库相关
│   │   ├── session.py                     # 数据库 SessionLocal 配置
│   │   ├── base.py                        # BaseModel 导入，集中管理 ORM 模型
│   │   ├── init_db.py                     # 项目启动时初始化数据库（可选）
│   │   ├── __init__.py
│   │
│   ├── main.py                            # FastAPI 启动入口
│   ├── __init__.py
│
├── alembic/                               # 数据库迁移（可选）
│   ├── versions/                          # 迁移版本文件夹
│   ├── env.py                             # Alembic 运行环境
│   ├── script.py.mako                     # 模板文件
│
├── alembic.ini                            # Alembic 配置
│
├── requirements.txt                       # Python 依赖列表
│
├── Dockerfile                             # Docker 构建镜像文件
│
├── docker-compose.yml                     # docker-compose 启动配置
│
└── README.md                              # 项目说明文档 -->
