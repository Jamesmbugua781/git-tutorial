import os

# 1️⃣ Resolve path
def get_target_path():
    """Return the Desktop path of the current user as default."""
    return os.path.join(os.path.expanduser("~"), ".")


# 2️⃣ Traverse directory
def traverse_directory(path):
    """Yield root, dirs, files for each folder in the directory tree."""
    for root, dirs, files in os.walk(path):
        yield root, dirs, files


# 3️⃣ Count files and folders
def count_files_and_folders(path):
    total_files = 0
    total_folders = 0
    for root, dirs, files in traverse_directory(path):
        total_files += len(files)
        total_folders += len(dirs)
    return total_files, total_folders


# 4️⃣ Calculate total size
def calculate_total_size(path):
    total_size = 0
    for root, dirs, files in traverse_directory(path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                total_size += os.path.getsize(file_path)
            except OSError:
                pass
    return total_size


# 5️⃣ File type distribution
def file_type_distribution(path):
    types = {}
    for root, dirs, files in traverse_directory(path):
        for file in files:
            ext = os.path.splitext(file)[1] or "NO_EXTENSION"
            types[ext] = types.get(ext, 0) + 1
    return types


# 6️⃣ Calculate max depth
def max_folder_depth(path):
    max_depth = 0
    base_path = os.path.abspath(path)
    for root, dirs, files in traverse_directory(path):
        depth = root.replace(base_path, "").count(os.sep)
        if depth > max_depth:
            max_depth = depth
    return max_depth


# 7️⃣ Main program
def main():
    path = get_target_path()

    files, folders = count_files_and_folders(path)
    size = calculate_total_size(path)
    types = file_type_distribution(path)
    depth = max_folder_depth(path)

    print(f"Directory analyzed: {path}")
    print(f"Total files: {files}")
    print(f"Total folders: {folders}")
    print(f"Total size (KB): {size / 1024:.2f}")
    print(f"Maximum depth: {depth}")
    print("\nFile types distribution:")
    for ext, count in sorted(types.items()):
        print(f"{ext}: {count}")


if __name__ == "__main__":
    main()
