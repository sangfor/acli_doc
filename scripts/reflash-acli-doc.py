import os
import json
import re

# ================= 配置常量 =================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CMD_CONFIG_ROOT = os.path.join(BASE_DIR, 'acli', 'etc', 'cmds')
DOC_OUTPUT_ROOT = os.path.join(BASE_DIR, 'docs')
DEFAULT_FRONTMATTER = "---\nsidebar_position: 1\n---\n"

DEFAULT_USAGE_TEMPLATE = """```bash
TODO: 添加使用示例
```"""

DEFAULT_RESULT_TEMPLATE = """```bash
TODO: 添加结果示例
```"""


def ensure_category_json(directory):
    """确保目录下存在 _category_.json"""
    if not os.path.exists(directory):
        return
    cat_file = os.path.join(directory, '_category_.json')
    if not os.path.exists(cat_file):
        try:
            with open(cat_file, 'w', encoding='utf-8') as f:
                f.write('{}')
        except Exception as e:
            print(f"Error creating _category_.json in {directory}: {e}")


def parse_json_file(file_path):
    """读取并解析JSON文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"[Error] Failed to load JSON {file_path}: {e}")
        return None


def get_arg_info(item):
    """
    [通用提取] 获取描述和类型
    item: 可以是顶层 input item，也可以是内部 schema item
    """
    # 1. 尝试直接获取描述
    desc = item.get('description')

    # 2. 如果顶层没有描述，尝试从 data 中获取 (针对顶层 item)
    if not desc:
        data_node = item.get('data')
        if isinstance(data_node, dict):
            desc = data_node.get('description')

    # 3. 获取类型
    arg_type = item.get('type', 'string')

    return arg_type, desc or ""


def format_arguments(inputs):
    """
    格式化命令参数，支持 Array 和 Object 的展开显示
    """
    if not inputs:
        return "无参数"

    all_lines = []  # 存储所有行（包括父级和展开的子级）

    for item in inputs:
        # --- 1. 处理父级参数 ---
        abbrv = item.get('abbrv', '')
        name = item.get('name', '')

        # 获取父级基本信息
        arg_type, raw_desc = get_arg_info(item)

        # 构建父级左侧：-v|--vm-ids=array
        prefix = f"{abbrv}|" if abbrv else ""
        parent_left = f"{prefix}{name}={arg_type}"

        # 构建父级描述
        is_required = item.get('required') is True
        desc_prefix = "必要参数，" if is_required else ""
        parent_desc = desc_prefix + raw_desc

        all_lines.append({
            "left": parent_left,
            "desc": parent_desc
        })

        # --- 2. 处理复杂类型展开 ---
        data_schema = item.get('data', {})
        if not isinstance(data_schema, dict):
            continue

        # == 场景 A: Array (数组) ==
        # 目标格式: --vm-ids.N=string  描述...
        if arg_type == 'array':
            items_schema = data_schema.get('items')
            if items_schema and isinstance(items_schema, dict):
                # 提取子项信息
                sub_type = items_schema.get('type', 'string')
                sub_desc = items_schema.get('description', '')

                # 构造子项名称
                sub_name = f"{name}.N"
                sub_left = f"{sub_name}={sub_type}"

                all_lines.append({
                    "left": sub_left,
                    "desc": sub_desc
                })

        # == 场景 B: Object (对象) ==
        # 目标格式: --data.key=type  描述...
        elif arg_type == 'object':
            properties = data_schema.get('properties')
            if properties and isinstance(properties, dict):
                # 遍历所有属性
                for prop_key, prop_val in properties.items():
                    if not isinstance(prop_val, dict):
                        continue

                    # 提取属性信息
                    sub_type = prop_val.get('type', 'string')
                    sub_desc = prop_val.get('description', '')

                    # 构造属性名称：父名.属性名
                    sub_name = f"{name}.{prop_key}"
                    sub_left = f"{sub_name}={sub_type}"

                    all_lines.append({
                        "left": sub_left,
                        "desc": sub_desc
                    })

    # --- 3. 统一计算对齐并生成文本 ---
    if not all_lines:
        return ""

    # 计算最长左侧文本长度
    max_len = max(len(x['left']) for x in all_lines)
    pad_width = max_len + 4  # 留白

    formatted_lines = []
    formatted_lines.append("```bash")
    for x in all_lines:
        # 左对齐填充
        formatted_row = f"{x['left'].ljust(pad_width)}{x['desc']}"
        formatted_lines.append(formatted_row)
    formatted_lines.append("```")

    return "\n".join(formatted_lines)


def extract_existing_content(md_path):
    """
    从现有Markdown中提取内容
    [Strict Mode] 严格匹配 '### 使用示例' 和 '### 结果示例'
    """
    content = {
        "usage": DEFAULT_USAGE_TEMPLATE,
        "result": DEFAULT_RESULT_TEMPLATE
    }
    if not os.path.exists(md_path):
        return content

    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            raw_text = f.read()

        # [Important] 正则表达式必须匹配 generate_markdown 中的标题格式
        # 严格查找 "### 使用示例" 之后的内容
        usage_match = re.search(
            r'### 使用示例\s*\n(.*?)(?=\n### 结果示例|$)',
            raw_text, re.DOTALL)

        if usage_match:
            content["usage"] = usage_match.group(1).strip()

        # 严格查找 "### 结果示例" 之后的内容
        result_match = re.search(
            r'### 结果示例\s*\n(.*)$',
            raw_text, re.DOTALL)

        if result_match:
            content["result"] = result_match.group(1).strip()

    except Exception as e:
        print(f"[Warning] Failed to read existing MD {md_path}: {e}")
    return content


def get_description_from_json(json_data):
    """智能获取命令描述"""
    priority_keys = ['execute', 'execute_api', 'execute_cmd', 'execute_script']
    for key in priority_keys:
        info = json_data.get(key)
        if isinstance(info, dict) and 'execute_description' in info:
            return info['execute_description']
    for key, value in json_data.items():
        if key.startswith('execute') and isinstance(value, dict):
            if 'execute_description' in value:
                return value['execute_description']
    return "暂无描述"


def generate_markdown(json_data, dest_path, cmd_name):
    """生成Markdown内容并写入"""
    description = get_description_from_json(json_data)
    inputs = json_data.get('input', [])

    # 生成参数块
    args_block = format_arguments(inputs)

    # 提取旧内容（保留手动修改过的示例）
    old_content = extract_existing_content(dest_path)
    usage_content = old_content['usage']
    result_content = old_content['result']

    # 组装新的 Markdown
    md_content = f"""{DEFAULT_FRONTMATTER}
# {cmd_name}

### 操作概述

{description}

### 命令参数

{args_block}

### 使用示例

{usage_content}

### 结果示例

{result_content}
"""

    try:
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"[Success] Reflashed: {dest_path}")
    except Exception as e:
        print(f"[Error] Writing file {dest_path}: {e}")


def process_file(json_path):
    filename = os.path.basename(json_path)
    name_parts = filename.replace('.json', '').split('.')
    if not name_parts:
        return
    cmd_name = name_parts[-1]
    dir_parts = name_parts[:-1]
    target_dir = os.path.join(DOC_OUTPUT_ROOT, *dir_parts)
    target_file = os.path.join(target_dir, f"{cmd_name}.md")

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    current_check_dir = DOC_OUTPUT_ROOT
    for part in dir_parts:
        current_check_dir = os.path.join(current_check_dir, part)
        if not os.path.exists(current_check_dir):
            os.makedirs(current_check_dir)
        ensure_category_json(current_check_dir)

    json_data = parse_json_file(json_path)
    if not json_data:
        return
    generate_markdown(json_data, target_file, cmd_name)


def main():
    print(f"Scanning configs in: {CMD_CONFIG_ROOT}")
    if not os.path.exists(CMD_CONFIG_ROOT):
        print(f"Error: Config directory not found: {CMD_CONFIG_ROOT}")
        return
    count = 0
    for root, dirs, files in os.walk(CMD_CONFIG_ROOT):
        for file in files:
            if file.endswith('.json') and file != '_category_.json':
                full_path = os.path.join(root, file)
                process_file(full_path)
                count += 1
    print(f"Processing complete. Total files processed: {count}")


if __name__ == "__main__":
    main()
