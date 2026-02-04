import os

# ================= 使用说明 =================
# python scripts/clean-deprecated-doc.py

# ================= 配置常量 =================
# 脚本所在目录的上两级目录作为项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 输入配置文件根路径
CMD_CONFIG_ROOT = os.path.join(BASE_DIR, 'acli', 'etc', 'cmds')
# 输出文档根路径
DOC_OUTPUT_ROOT = os.path.join(BASE_DIR, 'docs')

# 定义系统文件/元数据文件，这些文件在判断目录是否为空时，被视为“空内容”
SYSTEM_FILES = {'_category_.json', 'category.md'}


def get_valid_md_paths():
    """
    遍历 JSON 配置文件，生成所有合法的 Markdown 相对路径集合
    """
    valid_paths = set()

    if not os.path.exists(CMD_CONFIG_ROOT):
        print(f"[Error] Config directory not found: {CMD_CONFIG_ROOT}")
        return valid_paths

    for root, dirs, files in os.walk(CMD_CONFIG_ROOT):
        for file in files:
            if file.endswith('.json') and file != '_category_.json':
                name_parts = file.replace('.json', '').split('.')

                if name_parts:
                    cmd_name = name_parts[-1]
                    dir_parts = name_parts[:-1]
                    rel_path = "/".join(dir_parts + [f"{cmd_name}.md"])
                    valid_paths.add(rel_path)

    return valid_paths


def clean_orphan_files(valid_paths):
    """
    第一步：扫描 docs 目录，删除不在 valid_paths 中的 .md 文件
    """
    if not os.path.exists(DOC_OUTPUT_ROOT):
        return 0

    removed_count = 0

    # 获取 docs 的绝对路径，用于比较
    abs_doc_root = os.path.abspath(DOC_OUTPUT_ROOT)

    for root, dirs, files in os.walk(DOC_OUTPUT_ROOT):

        # [核心修改] 判断当前是否在 docs 根目录
        # 如果当前遍历的是根目录，跳过该目录下的所有文件检查
        # 这样 welcome.md, intro.md 等文件就会被保留
        if os.path.abspath(root) == abs_doc_root:
            # print(f"Skipping root directory check: {root}")
            continue

        for file in files:
            # 1. 依然保留对 category.md 的特殊保护
            if file == 'category.md':
                continue

            if file.endswith('.md'):
                abs_path = os.path.join(root, file)
                rel_path_os = os.path.relpath(abs_path, DOC_OUTPUT_ROOT)
                rel_path_key = rel_path_os.replace(os.sep, '/')

                # 2. 如果不在白名单中，说明是废弃命令，删除
                if rel_path_key not in valid_paths:
                    try:
                        os.remove(abs_path)
                        print(f"[Removed] Deprecated file: {rel_path_os}")
                        removed_count += 1
                    except Exception as e:
                        print(f"[Error] Failed to remove {abs_path}: {e}")

    return removed_count


def clean_empty_directories():
    """
    第二步：清理无效的命名空间目录
    """
    if not os.path.exists(DOC_OUTPUT_ROOT):
        return 0

    removed_dirs = 0
    abs_doc_root = os.path.abspath(DOC_OUTPUT_ROOT)

    # topdown=False 保证先处理子目录，再处理父目录
    for root, dirs, files in os.walk(DOC_OUTPUT_ROOT, topdown=False):

        # 绝对不删除 docs 根目录
        if os.path.abspath(root) == abs_doc_root:
            continue

        # 1. 检查当前目录下是否有“实际内容文件”
        current_files_set = set(files)
        real_content_files = current_files_set - SYSTEM_FILES

        # 2. 检查是否有子目录
        has_subdirs = False
        try:
            items = os.listdir(root)
            for item in items:
                if os.path.isdir(os.path.join(root, item)):
                    has_subdirs = True
                    break
        except OSError:
            continue

        # 3. 判定逻辑：既没有实际内容文件，也没有子目录 -> 删除
        if not real_content_files and not has_subdirs:
            try:
                # 先清理掉目录内的系统文件
                for sys_file in SYSTEM_FILES:
                    sys_file_path = os.path.join(root, sys_file)
                    if os.path.exists(sys_file_path):
                        os.remove(sys_file_path)

                # 删除空目录
                os.rmdir(root)
                print(
                    f"[Cleaned] Invalid Namespace: {os.path.relpath(root, BASE_DIR)}")
                removed_dirs += 1
            except Exception as e:
                print(f"[Error] Failed to remove dir {root}: {e}")

    return removed_dirs


def main():
    print("--- Starting Cleanup Process ---")

    # 1. 构建白名单
    valid_paths = get_valid_md_paths()
    print(f"Found {len(valid_paths)} valid command configurations.")

    # 2. 清理废弃的 .md 文件 (跳过 docs 根目录文件 + category.md)
    deleted_files = clean_orphan_files(valid_paths)

    # 3. 清理无效目录
    deleted_dirs = clean_empty_directories()

    print("--- Cleanup Complete ---")
    print(f"Total deprecated files removed: {deleted_files}")
    print(f"Total invalid namespaces cleaned: {deleted_dirs}")


if __name__ == "__main__":
    main()
