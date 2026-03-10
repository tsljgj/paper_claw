# 贡献指南

感谢您对 Article Claw 项目的关注！我们欢迎各种形式的贡献。

## 🚀 如何贡献

### 报告问题

如果您发现了 bug 或有功能建议，请通过 [GitHub Issues](https://github.com/yourusername/article_claw/issues) 提交。

- 使用对应的 issue 模板
- 提供清晰的复现步骤
- 附上相关日志或截图

### 提交代码

1. Fork 本仓库
2. 创建您的功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

## 📝 开发指南

### 环境设置

```bash
# 克隆仓库
git clone https://github.com/yourusername/article_claw.git
cd article_claw

# 创建环境
conda create -n article_claw python=3.11 -y
conda activate article_claw
pip install -r requirements.txt
```

### 本地测试

```bash
# 重置状态
python scripts/reset_state.py

# 运行测试
python scripts/main.py --day 2026-03-10

# 检查结果
ls content/posts/
ls data/processed/
```

### 代码规范

- 保持代码简洁明了
- 添加适当的注释
- 遵循 PEP 8 风格
- 不要硬编码敏感信息
- 保留英文原文，避免猜测

## 🎯 贡献方向

我们特别欢迎以下方面的贡献：

- 🏷️ **分类优化** - 改进论文分类准确性
- 📝 **总结质量** - 提升中文摘要质量
- 🎨 **模板美化** - 改进输出格式和样式
- ⚡ **性能优化** - 提升运行效率
- 📚 **文档完善** - 补充使用说明和示例

## 📋 PR 检查清单

- [ ] 代码能够正常运行
- [ ] 添加了必要的注释
- [ ] 更新了相关文档
- [ ] 遵循项目代码规范
- [ ] 如果是模板变更，提供了前后对比

## 💬 联系我们

如有疑问，欢迎通过 GitHub Discussions 或 Issues 与我们交流。

---

再次感谢您对 Article Claw 的贡献！
