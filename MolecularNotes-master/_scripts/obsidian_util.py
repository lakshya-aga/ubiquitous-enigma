import os
import re

vault_path = "./"


WIKILINK_RE = re.compile(r"\[\[([^\]]+?)\]\]")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def extract_wikilinks(text):
    """
    Extract Obsidian wikilink targets from a markdown string.

    Supports common forms:
    - [[Page]]
    - [[Page|Alias]]
    - [[Page#Heading]]
    - [[Page#Heading|Alias]]
    - [[Page^block-id]]
    """
    targets = []
    for raw in WIKILINK_RE.findall(text):
        target = raw.split("|", 1)[0].strip()
        target = target.split("#", 1)[0].strip()
        target = target.split("^", 1)[0].strip()
        if target:
            targets.append(target)
    return targets


def _strip_code_blocks(text):
    """
    Remove fenced code blocks (```...```) to avoid matching tags inside them.
    """
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


def has_obsidian_tag(text, tag):
    """
    Return True if the markdown text contains the given Obsidian tag.

    Matches:
    - inline tags: "... #topic ..."
    - hierarchical tags: "#topic/sub"
    - Type line: "Type: #topic"
    - YAML frontmatter:
      - tags: [topic, other]
      - tags: topic
      - type: topic
      - type: "#topic"

    Case-insensitive by default (Obsidian tags are generally case-insensitive).
    """
    if not tag:
        return False

    normalized = tag.lstrip("#")
    if not normalized:
        return False

    searchable = _strip_code_blocks(text)

    # Inline tag (including hierarchical tags)
    inline_re = re.compile(rf"(?<![\w/])#{re.escape(normalized)}(?:/[-\w]+)*\b", re.IGNORECASE)
    if inline_re.search(searchable):
        return True

    # Common "Type:" metadata line used in this vault
    type_re = re.compile(rf"^Type:\s*#{re.escape(normalized)}\b", re.IGNORECASE | re.MULTILINE)
    if type_re.search(searchable):
        return True

    # YAML frontmatter (best-effort parsing via regex)
    fm_match = FRONTMATTER_RE.search(searchable)
    if not fm_match:
        return False

    fm = fm_match.group(1)
    # tags: [topic, other]  OR tags: topic
    tags_re = re.compile(r"^tags:\s*(.+)$", re.IGNORECASE | re.MULTILINE)
    m = tags_re.search(fm)
    if m:
        value = m.group(1).strip().strip('"').strip("'")
        # strip surrounding [ ... ] if present
        if value.startswith("[") and value.endswith("]"):
            value = value[1:-1]
        parts = [p.strip().strip('"').strip("'").lstrip("#") for p in value.split(",") if p.strip()]
        if any(p.lower() == normalized.lower() or p.lower().startswith(normalized.lower() + "/") for p in parts):
            return True

    # type: topic  OR type: "#topic"
    type_key_re = re.compile(r"^type:\s*(.+)$", re.IGNORECASE | re.MULTILINE)
    m = type_key_re.search(fm)
    if m:
        value = m.group(1).strip().strip('"').strip("'").lstrip("#")
        if value.lower() == normalized.lower() or value.lower().startswith(normalized.lower() + "/"):
            return True

    return False


def list_files_in_directory(dir=vault_path):
    """
    Reads all files in the directory and returns a list of the file paths
    """
    file_paths = []
    for f in os.listdir(dir):
        if f.endswith(".md"):
            file_paths.append(f)
    return file_paths


def list_files_in_directory_recursive(dir=vault_path):
    """
    Reads all files in the directory and returns a list of the file paths recursively
    """
    file_paths = []
    for root, dirs, files in os.walk(dir):
        for f in files:
            if f.endswith(".md"):
                file_paths.append(f"{root}/{f}")
    return file_paths


def read_file(file_path):
    """
    Reads a file and returns the contents as a string
    """
    with open(file_path, "r", encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents


def read_file_lines(file_path):
    """
    Reads a file and returns the contents as a list of lines
    """
    with open(file_path, "r") as f:
        file_contents = f.readlines()
    return file_contents


def _iter_markdown_files(root=vault_path, exclude_dirs=None):
    exclude_dirs = set(exclude_dirs or [])
    for current_root, dirs, files in os.walk(root):
        # Skip excluded directories (in-place prune for performance)
        dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith(".")]
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(current_root, f)


def _safe_move(src_path, dst_dir):
    os.makedirs(dst_dir, exist_ok=True)
    filename = os.path.basename(src_path)
    dst_path = os.path.join(dst_dir, filename)
    if os.path.abspath(src_path) == os.path.abspath(dst_path):
        return False
    if os.path.exists(dst_path):
        print(f"SKIP (exists): {dst_path}")
        return False
    os.rename(src_path, dst_path)
    return True


def move_selector_to_folder(selector, folder):
    """
    Backwards-compatible helper.

    Historically `selector` was a literal substring like "Type: #topic".
    Now it also accepts a tag selector like "#topic" and will move notes
    recursively across the vault (excluding system folders).
    """
    tag = None
    m = re.search(r"#([A-Za-z0-9_-]+)", selector or "")
    if m:
        tag = "#" + m.group(1)

    exclude_dirs = {
        "_scripts",
        "_templates",
        "_attachments",
        ".git",
        folder,
    }

    moved_any = False
    for path in _iter_markdown_files(vault_path, exclude_dirs=exclude_dirs):
        try:
            file_contents = read_file(path)
        except UnicodeDecodeError:
            # Skip non-UTF8 notes; they likely won't contain tags we care about.
            continue

        match = False
        if tag and has_obsidian_tag(file_contents, tag):
            match = True
        elif selector and selector in file_contents:
            match = True

        if match:
            note_name = os.path.splitext(os.path.basename(path))[0]
            print(f"{note_name} --> {folder}")
            if _safe_move(path, os.path.join(vault_path, folder)):
                moved_any = True

    return moved_any


def create_authors():
    dirname = f"{vault_path}Sources"
    files = list_files_in_directory(dirname)
    for f in files:
        lines = read_file_lines(f"{dirname}/{f}")
        for line in lines:
            if "Author:" in line:
                author_string = line.split(":")[1].strip()
                for author_tag in extract_wikilinks(author_string):
                    # check if author_tag is in Authors/ or in the main folder
                    # if not, create a new file in Authors/ containing the string "Type: #author"
                    if (
                        f"{author_tag}.md"
                        in list_files_in_directory(f"{vault_path}Authors")
                        or f"{author_tag}.md" in list_files_in_directory()
                    ):
                        continue
                    else:
                        print(f"Creating new author: {author_tag}")
                        with open(
                            f"{vault_path}Authors/" + author_tag + ".md", "w"
                        ) as f:
                            f.write(f"Type: #author")


def create_topics():
    dirname = vault_path
    files = list_files_in_directory(dirname)
    for f in files:
        lines = read_file_lines(f"{dirname}{f}")
        for line in lines:
            if "Topics:" in line:
                cat_string = line.split(":")[1].strip()
                for cat_tag in extract_wikilinks(cat_string):
                    # check if cat_tag is in Authors/ or in the main folder
                    # if not, create a new file in Authors/ containing the string "Type: #author"
                    if (
                        f"{cat_tag}.md"
                        in list_files_in_directory(f"{vault_path}Topics")
                        or f"{cat_tag}.md" in list_files_in_directory()
                    ):
                        continue
                    else:
                        print(f"Creating new topic: {cat_tag}")
                        with open(f"{vault_path}Topics/" + cat_tag + ".md", "w") as f:
                            f.write(f"Type: #topic")


def notes_to_review():
    """
    Find all files in the main directory that need attention (non atoms, orphans, todos).
    """
    print("\nPlease review the following files")
    print("=================================")
    files = list_files_in_directory()
    for f in files:
        file_contents = read_file(vault_path + f)
        if (
            "#atom" not in file_contents
            and "#todo" not in file_contents
            and f != "__OBSIDIAN_META__.md"
        ):
            print(f.replace(".md", ""))

    todos = []
    mentioned = set()
    not_linked_to = []
    not_linking = []

    all_files = list_files_in_directory_recursive()

    for f in all_files:
        file_contents = read_file(vault_path + f)
        # print(f)
        if "#todo" in file_contents:
            todos.append(f.replace(".md", "").replace(vault_path, "").strip("/"))
        # Find words in [[...]] and add to mentioned
        links = extract_wikilinks(file_contents)
        if len(links) == 0:
            # These notes don't link to anything
            not_linking.append(f.split("/")[-1].replace(".md", ""))
        else:
            for word in links:
                mentioned.add(word)

    # Find notes that are not mentioned in any other file
    for f in all_files:
        note = f.split("/")[-1].replace(".md", "")
        if note not in mentioned:
            not_linked_to.append(note)

    orphans = [
        note
        for note in set(not_linked_to).intersection(set(not_linking))
        if note + ".md" not in os.listdir("_templates") and "__" not in note
    ]

    if len(todos) > 0:
        print("\nTodos")
        print("=====")
        for note in todos:
            print(note)

    if len(orphans) > 0:
        print("\nOrphans")
        print("=======")
        for note in orphans:
            print(note)


if __name__ == "__main__":
    print("\nCleaning up Obsidian")
    print("=====================")
    move_selector_to_folder("Type: #topic", "Topics")
    move_selector_to_folder("Type: #author", "Authors")
    move_selector_to_folder("Type: #molecule", "Molecules")
    move_selector_to_folder(f"Type: #source", "Sources")

    create_authors()
    create_topics()
    notes_to_review()
