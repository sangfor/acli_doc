"""
文档模板生成工具 - 基于命令字符串数组生成 Docusaurus 文档模板
"""

import os
import json
import copy
import re
from typing import List, Dict, Set
from pathlib import Path

class DocTemplateGenerator:
    """
    根据 命令结构 和 当前目录的文档树 生成 Docusaurus 模板文件
    """
    
    def __init__(self, output_dir: str, template_dir: str):
        self.output_dir = output_dir
        self.template_dir = template_dir
        self._template_cache = {}  # 模板内容缓存
        self._generated_files = []  # 记录新生成的文件（只包含文件内容）
        self._new_directories = set()  # 记录新生成的目录
        
        print(f"文档生成器初始化:")
        print(f"  输出目录: {output_dir}")
        print(f"  模板目录: {template_dir}")
    
    def _load_template(self, template_name: str):
        """
        加载模板文件内容
        """
        if template_name in self._template_cache:
            return self._template_cache[template_name]
        
        template_path = os.path.join(self.template_dir, template_name)
        print(f"  尝试加载模板: {template_path}")
        
        try:
            if template_name.endswith('.json'):
                with open(template_path, 'r', encoding='utf-8') as f:
                    content = json.load(f)
                    self._template_cache[template_name] = content
                    print(f"  ✓ 成功加载 JSON 模板: {template_name}")
                    return content
            else:
                with open(template_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self._template_cache[template_name] = content
                    print(f"  ✓ 成功加载 Markdown 模板: {template_name}")
                    return content
        except FileNotFoundError:
            print(f"  ✗ 模板文件不存在: {template_path}")
            return None
        except Exception as e:
            print(f"  ✗ 加载模板失败: {e}")
            return None
    
    def _replace_placeholders(self, content: str, **kwargs) -> str:
        """
        替换模板中的占位符
        模式：
        1. {占位符文字} - 根据文字匹配并替换
        2. {} - 空占位符，用默认值（如果有的话）替换
        """
        # 先处理有文字的占位符
        for key, value in kwargs.items():
            # 匹配 {key} 或 {包含key的文字}
            patterns = [
                f"{{{key}}}",  # 直接的 {key}
                f"{{.*{key}.*}}"  # 包含 key 的描述，如 {和文件名同名的命令，如：get.md 这里就是 get}
            ]
            for pattern in patterns:
                content = re.sub(pattern, str(value), content)
        
        # 处理空的 {} 占位符
        # 如果提供了 default_value 参数，替换所有 {}
        if 'default_value' in kwargs:
            content = re.sub(r"{}", str(kwargs['default_value']), content)
        
        return content
    
    def _file_exists(self, file_path: str) -> bool:
        """
        检查文件是否已存在
        """
        return os.path.exists(file_path)
    
    def _check_label_conflict(self, label: str) -> bool:
        """
        检查 label 是否与现有的 _category_.json 文件冲突
        通过搜索 "label".*"目录名" 来查找冲突
        """
        # 使用 Path. rglob 替代 os.walk，更简洁高效
        output_path = Path(self.output_dir)
        
        for category_file in output_path.rglob("_category_.json"):
            try:
                # 直接解析 JSON 而不是正则匹配文本
                with category_file.open('r', encoding='utf-8') as f:
                    data = json.load(f)
                    # 直接访问 label 字段
                    if data.get('label') == label:
                        return True
            except (json.JSONDecodeError, OSError, KeyError):
                # 统一异常处理，降低圈复杂度
                continue
        
        return False
    
    def _generate_category_json(self, dir_path: str, label: str):
        """
        生成普通的 _category_.json 文件（模板1）
        """
        category_file = os.path.join(dir_path, "_category_.json")
        
        # 加载模板
        template = self._load_template("_category_.json")
        
        if template is None:
            # 使用默认模板
            template = {
                "label": label,
                "position": 1,
                "link": {
                    "type": "generated-index",
                    "description": f"{label} 相关文档"
                }
            }
        else:
            # 复制模板并替换占位符
            template = copy.deepcopy(template)
            # 替换 "label" 字段
            template["label"] = label
            # TODO: 后续考虑替换对应字段
        
        # 写入文件
        with open(category_file, 'w', encoding='utf-8') as f:
            json.dump(template, f, indent=4, ensure_ascii=False)
        
        # 记录新生成的文件（只记录路径，不记录内容）
        rel_path = os.path.relpath(category_file, self.output_dir)
        self._generated_files.append(rel_path)
        
        print(f"  ✓ 生成 {rel_path}")
    
    def _generate_category_conflict(self, dir_path: str, label: str, full_path: str):
        """
        生成冲突版本的 _category_.json 和对应的 category.md
        """
        # 生成 _category_.json（模板2）
        category_file = os.path.join(dir_path, "_category_.json")
        
        template = self._load_template("_category_conflict.json")
        
        if template is None:
            # 使用默认模板
            template = {
                "label": label,
                "position": 1,
                "link": {
                    "type": "doc",
                    "id": f"{full_path}/category"
                }
            }
        else:
            # 复制模板并替换占位符
            template = copy.deepcopy(template)
            # 替换 "label" 字段
            template["label"] = label
            # 替换 "id" 字段
            template["link"]["id"] = f"{full_path}/category"

        # 写入 _category_.json
        with open(category_file, 'w', encoding='utf-8') as f:
            json.dump(template, f, indent=4, ensure_ascii=False)
        
        # 记录新生成的文件（只记录路径，不记录内容）
        rel_path = os.path.relpath(category_file, self.output_dir)
        self._generated_files.append(rel_path)
        
        print(f"  ✓ 生成冲突版本 {rel_path}")
        
        # 生成 category.md（模板3）
        self._generate_category_category(dir_path, label)
    
    def _generate_category_category(self, dir_path: str, label: str):
        """
        生成 category 的 category.md 文件（模板3）
        """
        category_file = os.path.join(dir_path, "category.md")
        
        # 加载模板
        content = self._load_template("category.md")
        
        if content is None:
            # 使用默认模板
            content = """---
sidebar_position:1
---

{对应的description}

import DocCardList from '@theme/DocCardList';

<DocCardList />
"""
        else:
            # TODO: 后续考虑替换对应字段
            pass
        
        # 写入文件
        with open(category_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # 记录新生成的文件（只记录路径，不记录内容）
        rel_path = os.path.relpath(category_file, self.output_dir)
        self._generated_files.append(rel_path)
        
        print(f"  ✓ 生成 {rel_path}")
    
    def _generate_command_md(self, namespace: List[str], command: str,
                            description: str = "", parameters: List[Dict] = None):
        """
        生成命令的 markdown 文件（模板4）
        如果文件已存在则跳过
        """
        dir_path = os.path.join(self.output_dir, *namespace)
        os.makedirs(dir_path, exist_ok=True)
        
        md_file = os.path.join(dir_path, f"{command}.md")
        
        # 检查文件是否已存在
        if self._file_exists(md_file):
            print(f"  ⊙ 跳过已存在文件: {os.path.relpath(md_file, self.output_dir)}")
            return
        
        # 构建完整命令字符串
        full_command = ' '.join(namespace) + ' ' + command
        
        # 生成描述
        desc_text = description or f"{' > '.join(namespace) if namespace else ''} > {command}"
        
        # 加载模板
        content = self._load_template("command.md")
        
        if content is None:
            # 使用默认模板
            content = f"""---
sidebar_position: 10
---
  
# {command}
操作概述: {desc_text}
  
命令参数:
```bash
```
  
使用示例:
```bash
{full_command}
```
  
结果示例:
```bash

```
"""
        else:
            # 替换标题 {和文件名同名的命令，如：get.md 这里就是 get}
            content = re.sub(r"# \{.*?\}", f"# {command}", content)
            # 替换 {} 占位符为描述
            content = content.replace("{}", desc_text)
        
        # 写入文件
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # 记录新生成的文件（只记录路径，不记录内容）
        rel_path = os.path.relpath(md_file, self.output_dir)
        self._generated_files.append(rel_path)
        
        print(f"  ✓ 生成 {rel_path}")
    
    def _get_existing_dirs(self) -> Set[str]:
        """
        获取输出目录中已存在的所有目录路径
        返回相对路径的集合（统一使用正斜杠）
        """
        existing_dirs = set()
        if not os.path.exists(self.output_dir):
            return existing_dirs
        
        for root, dirs, files in os.walk(self.output_dir):
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                rel_path = os.path.relpath(dir_path, self.output_dir)
                # 统一使用正斜杠，确保跨平台一致性
                existing_dirs.add(rel_path.replace('\\', '/'))
        
        return existing_dirs
    
    def _collect_new_dirs(self, commands: List[Dict]) -> Set[str]:
        """
        收集所有需要生成的新目录路径
        """
        existing_dirs = self._get_existing_dirs()
        new_dirs = set()
        
        for cmd in commands:
            namespace = cmd.get("namespace", [])
            if not namespace:
                continue
            
            # 构建路径层次
            current_path = []
            for folder in namespace:
                current_path.append(folder)
                full_path = '/'.join(current_path)
                
                # 只添加新的目录
                if full_path not in existing_dirs:
                    new_dirs.add(full_path)
                existing_dirs.add(full_path)
        
        return new_dirs
    
    def generate_from_commands(self, commands: List[Dict]):
        """
        从命令列表生成文档模板
        """
        print(f"\n开始处理 {len(commands)} 个命令...")
        
        # 步骤1: 收集所有新目录路径
        print("\n步骤 1: 收集新目录路径...")
        new_dirs = self._collect_new_dirs(commands)
        print(f"发现 {len(new_dirs)} 个新目录需要生成")
        self._new_directories = new_dirs  # 记录新生成的目录
        
        # 步骤2: 为每个新目录生成 _category_.json
        print("\n步骤 2: 生成目录分类文件...")
        for dir_path_str in sorted(new_dirs):
            dir_path = os.path.join(self.output_dir, dir_path_str)
            folder_name = os.path.basename(dir_path_str)
            
            # 确保目录存在
            os.makedirs(dir_path, exist_ok=True)
            
            # 检查 label 冲突
            has_conflict = self._check_label_conflict(folder_name)
            
            if has_conflict:
                print(f"  检测到 label 冲突: {folder_name}")
                # 生成冲突版本的 _category_.json 和 category.md
                self._generate_category_conflict(dir_path, folder_name, dir_path_str)
            else:
                # 生成普通的 _category_.json
                self._generate_category_json(dir_path, folder_name)
        
        # 步骤3: 生成命令文件，跳过已存在的
        print("\n步骤 3: 生成命令文档文件...")
        for _, cmd_data in enumerate(commands, 1):
            namespace = cmd_data.get("namespace", [])
            command = cmd_data.get("command", "")
            description = cmd_data.get("description", "")
            parameters = cmd_data.get("parameters", [])
            
            if not namespace or not command:
                continue
            
            # 生成命令的 markdown 文件
            self._generate_command_md(namespace, command, description, parameters)
    
    def generate_full_structure(self, commands: List[Dict]):
        """
        从命令列表生成模板
        """
        self.generate_from_commands(commands)
        
        print(f"\n文档生成完成！")
        
        return {
            "success": True,
        }
    
    def get_generation_summary(self) -> Dict:
        """
        获取生成摘要
        返回本次生成过程中创建的文件和目录列表
        """
        total_size = 0
        for file_path in self._generated_files:
            full_path = os.path.join(self.output_dir, file_path)
            if os.path.exists(full_path):
                total_size += os.path.getsize(full_path)
        
        return {
            "files": sorted(self._generated_files),
            "directories": sorted(self._new_directories),
            "total_files": len(self._generated_files),
            "total_size": total_size
        }


def parse_command_string(command_str: str) -> Dict:
    """
    解析命令字符串为结构化数据
    """
    parts = command_str.strip().split()
    
    # 移除 'acli' 前缀（如果存在）
    if parts and parts[0].lower() == 'acli':
        parts = parts[1:]
    
    if len(parts) < 2:
        return {
            "namespace": [],
            "command": "",
            "full_command": command_str,
            "original": command_str
        }
    
    # 最后一个部分是命令，其余是命名空间
    command = parts[-1]
    namespace = parts[:-1]
    
    # 生成完整命令字符串（移除 acli 前缀后）
    if command_str.lower().startswith('acli '):
        full_command = command_str[5:]
    else:
        full_command = " ".join(parts)
    
    # 添加描述占位符
    if namespace:
        description = f"{' > '.join(namespace)} > {command}"
    else:
        description = command
    
    return {
        "namespace": namespace,
        "command": command,
        "description": description,
        "full_command": full_command,
        "original": command_str,
        "parameters": []
    }


def parse_command_strings(command_strings: List[str]) -> List[Dict]:
    """
    批量解析命令字符串数组
    """
    commands = []
    for cmd_str in command_strings:
        parsed = parse_command_string(cmd_str)
        if parsed["command"]:
            commands.append(parsed)
    return commands


def doc_template_generate(
    commands_json: str,
    output_dir: str = "./docs",
    template_dir: str = "./src/statics",
) -> Dict:
    """
    根据命令字符串数组生成 Docusaurus 文档模板
    
    Args:
        commands_json: 命令字符串数组的 JSON 格式（必填）
            格式示例：'["acli network nic list", "acli system cpu info"]'
        output_dir: 输出目录，默认 "./docs"
        template_dir: 模板目录，默认 "./src/statics"
    
    Returns:
        包含生成摘要的字典
        - files: 生成的文件路径列表
        - directories: 生成的目录路径列表
        - total_files: 文件总数
        - total_size: 总大小（字节）
    """
    # 初始化结果
    result_lines = []
    result_lines.append("开始生成文档模板...")
    
    # 1. 解析命令字符串
    result_lines.append("\n步骤 1: 解析命令字符串...")
    
    # --- 优化开始 ---
    try:
        # 检查是否为空字符串
        if not commands_json or commands_json.strip() == "":
            return {"error": "收到的命令参数为空。请检查引号转义。在 Windows CMD 中，使用：python acli_doc_generate.py --commands \"[\\\"acli network nic list\\\"]\""}
        
        # 解析 JSON
        raw_data = json.loads(commands_json)
        
        # 校验类型：必须是列表
        if not isinstance(raw_data, list):
            return {"error": "JSON 格式错误：输入必须是一个数组，例如 '[\"cmd1\", \"cmd2\"]'"}
        
        # 校验内容：列表不能为空，且每个元素最好是字符串
        if not raw_data:
            return {"error": "命令列表不能为空"}
            
        # 清洗数据：强制转换为字符串并去除首尾空格
        command_strings: List[str] = [str(cmd).strip() for cmd in raw_data]
        
        result_lines.append(f"成功解析 {len(command_strings)} 条命令。")
        
    except json.JSONDecodeError as e:
        return {"error": f"JSON 格式不正确 - {str(e)}。请确保使用双引号。"}
    except Exception as e:
        return {"error": f"解析过程中发生未知错误 - {str(e)}"}
    
    if not isinstance(command_strings, list):
        return {"error": "commands_json 必须是数组格式"}
    
    result_lines.append(f"接收到 {len(command_strings)} 个命令字符串")
    
    # 2. 转换为结构化命令
    result_lines.append("\n步骤 2: 转换命令格式...")
    parsed_commands = parse_command_strings(command_strings)
    result_lines.append(f"成功解析 {len(parsed_commands)} 个命令")
    
    # 显示解析结果
    for i, cmd in enumerate(parsed_commands[:5], 1):
        namespace_str = " > ".join(cmd["namespace"]) if cmd["namespace"] else "根级别"
        result_lines.append(f"  [{i}] {namespace_str} > {cmd['command']}")
    if len(parsed_commands) > 5:
        result_lines.append(f"  ... 还有 {len(parsed_commands) - 5} 个命令")
    
    # 3. 创建模板生成器
    result_lines.append("\n步骤 3: 初始化文档生成器...")
    os.makedirs(output_dir, exist_ok=True)
    
    generator = DocTemplateGenerator(output_dir=output_dir, template_dir=template_dir)
    result_lines.append(f"输出目录: {output_dir}")
    result_lines.append(f"模板目录: {template_dir}")
    
    # 4. 生成文档
    result_lines.append("\n步骤 4: 生成文档结构...")
    try:
        generation_result = generator.generate_full_structure(commands=parsed_commands)
        
        if generation_result.get("success"):
            result_lines.append(f"✅ 成功生成文档")
        else:
            result_lines.append("❌ 生成过程出错")
            
    except Exception as e:
        result_lines.append(f"❌ 生成过程出错: {str(e)}")
        import traceback
        result_lines.append(f"错误详情:\n{traceback.format_exc()}")
    
    # 5. 获取生成摘要
    result_lines.append("\n步骤 5: 获取生成摘要...")
    summary = generator.get_generation_summary()
    result_lines.append(f"生成文件: {summary['total_files']} 个")
    result_lines.append(f"生成目录: {len(summary['directories'])} 个")
    result_lines.append(f"总大小: {summary['total_size']} 字节")
    
    # 总结
    result_lines.append("\n" + "=" * 50)
    result_lines.append("生成完成！")
    result_lines.append("=" * 50)
    
    print("\n".join(result_lines))
    print(f"\n生成的文件列表:")
    for file_path in summary['files']:
        print(f"  - {file_path}")
    
    return summary


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="文档模板生成工具 - 基于命令字符串数组生成 Docusaurus 文档模板",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
入参格式说明：
  commands_json: 命令字符串数组的 JSON 格式（必填）
  
  格式示例（字符串形式）：
    '["acli network nic list", "acli system cpu info"]'
  
  注意：如果在命令行中直接传递 JSON，需要正确处理引号转义

使用示例：
**注意，应在项目根目录下执行该python文件，而不是当前目录**
  python acli_doc_generate.py --commands \'["acli network nic list", "acli system cpu info"]\' --output ./docs --template ./static
        """
    )
    
    parser.add_argument(
        '--commands',
        type=str,
        help='命令字符串数组的 JSON 格式，例如：\'["acli network nic list", "acli system cpu info"]\''
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default='./docs',
        help='输出目录，默认 "./docs"'
    )
    
    parser.add_argument(
        '--template',
        type=str,
        default='./src/statics',
        help='模板目录，默认 "./src/statics"'
    )
    
    args = parser.parse_args()
    
    print(f"接收到的命令参数: {args.commands}")
    print(f"输出目录: {args.output}")
    print(f"模板目录: {args.template}")
    print()
    
    # 调用文档生成函数
    result = doc_template_generate(
        commands_json=args.commands,
        output_dir=args.output,
        template_dir=args.template
    )
    
    # 检查结果
    if isinstance(result, dict) and "error" in result:
        print(f"\n❌ 错误: {result['error']}")
        exit(1)
    else:
        print(f"\n✅ 文档生成成功！")