import os

# Entry point for the make.fun epitaph bounty.
# Writes a single famous-last-words epitaph line to entry.txt in the
# output directory (default 'out' when MAKEFUN_OUTPUT_DIR is unset).

LINE = "It runs on a live server. Please call me back.\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    content = LINE

    # Validate: must be 1..150 characters and not blank-only, not purely whitespace.
    if not (1 <= len(content) <= 150 and content.strip()):
        raise ValueError("entry content failed validation")

    # Create the output directory if it does not exist.
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")

    # Write the line (with its trailing newline) as UTF-8.
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(path)
    print(len(content))


if __name__ == "__main__":
    main()
