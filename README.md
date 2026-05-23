# Claude Camp Week 3 练习项目

这个仓库包含 3 个 Python 小项目，分别练习了 CSV 处理、JSON 配置文件读写，以及带单元测试的字符串工具函数。

## 项目 1：CSV 学员数据分析器

目录：`project-1-csv-analyzer`

内容说明：
- 读取学员 CSV 文件
- 统计总人数
- 统计各国家人数
- 统计对赌完成率
- 将结果保存为 `report.json`

相关文件：
- `csv_analyzer.py`
- `students.csv`
- `report.json`

运行方式：

```powershell
cd project-1-csv-analyzer
python csv_analyzer.py
```

运行后会读取 `students.csv`，并更新 `report.json`。

测试方法：
- 这个项目当前没有单独测试文件。
- 可通过运行脚本后检查 `report.json` 内容是否正确来验证结果。

## 项目 2：JSON 配置文件读写器

目录：`project-2-config-editor`

内容说明：
- 读取 `config.json`
- 在命令行中显示当前配置
- 让用户选择并修改设置项
- 支持输入校验
- 支持重置默认配置
- 支持保存退出、放弃修改、继续编辑
- 当配置文件缺失或损坏时自动恢复默认配置

相关文件：
- `openclaw_config_editor.py`
- `config.json`

运行方式：

```powershell
cd project-2-config-editor
python openclaw_config_editor.py
```

测试方法：
- 这个项目当前没有单独测试文件。
- 可手动验证以下场景：
  - 正常修改设置
  - 输入非法选项后重新提示
  - 字体大小输入超出 `8-32` 时重新提示
  - 选择保存退出或放弃修改

## 项目 3：带单元测试的字符串工具库

目录：`project-3-string-toolbox`

内容说明：
- `reverse_words(s)`：反转单词顺序
- `count_vowels(s)`：统计元音字母数量
- `is_palindrome(s)`：判断是否为回文

相关文件：
- `string_utils.py`
- `test_string_utils.py`

运行方式：

```powershell
cd project-3-string-toolbox
python
```

进入 Python 后可手动调用函数，例如：

```python
from string_utils import reverse_words, count_vowels, is_palindrome

print(reverse_words("hello world"))
print(count_vowels("OpenAI"))
print(is_palindrome("level"))
```

测试方法：

```powershell
cd project-3-string-toolbox
python -m pytest
```

如果只运行单个测试文件，也可以使用：

```powershell
python -m pytest test_string_utils.py
```

## 环境说明

建议使用：
- Python 3
- `pandas`：用于项目 1
- `pytest`：用于项目 3

如需安装依赖，可使用：

```powershell
pip install pandas pytest
```
