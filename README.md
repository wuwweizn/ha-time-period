
# 时间段 Time Period - Home Assistant 自定义集成

本集成会创建一个传感器 `sensor.time_period`，自动根据当前时间判断当前处于哪个时间段。

## ⏰ 时间段划分

- 清晨：05:00-08:00  
- 上午：08:00-12:00  
- 中午：12:00-14:00  
- 下午：14:00-17:00  
- 傍晚：17:00-19:00  
- 晚上：19:00-22:00  
- 午夜：22:00-00:00  
- 深夜：00:00-05:00

## 🛠️ 安装方法

### 方法一：HACS 自定义源安装（推荐）
1. 添加 HACS 自定义仓库：https://github.com/wuwweizn/ha-time-period
2. 搜索 `Time Period` 安装
3. 重启 Home Assistant

### 方法二：手动安装
1. 将 `custom_components/time_period/` 文件夹复制到你的 `config/custom_components/` 目录中。
2. 重启 Home Assistant
3. 在“设置 → 设备与服务 → 添加集成”搜索 “时间段” 并安装



## 贡献 无为智能
如果遇到ha更新升级导致报错，请及时反馈。
欢迎提交 issue 或 PR！

---

