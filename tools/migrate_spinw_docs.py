from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD_ROOT = ROOT.parent / "spinw.github.io"

COLLECTIONS = {
    OLD_ROOT / "pages" / "_spinw": ROOT / "docs" / "spinw" / "methods",
    OLD_ROOT / "pages" / "_swfiles": ROOT / "docs" / "spinw" / "files",
    OLD_ROOT / "pages" / "_swfunc": ROOT / "docs" / "spinw" / "files" / "functions",
    OLD_ROOT / "pages" / "_swplot": ROOT / "docs" / "spinw" / "plot",
    OLD_ROOT / "pages" / "_swpref": ROOT / "docs" / "spinw" / "pref",
    OLD_ROOT / "pages" / "_swsym": ROOT / "docs" / "spinw" / "sym",
    OLD_ROOT / "pages" / "_documentation": ROOT / "docs" / "spinw" / "overview",
}

TUTORIALS = OLD_ROOT / "pages" / "_tutorials"

FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
IMAGE_INCLUDE_RE = re.compile(r'{%\s*include\s+image\.html\s+([^%]+?)%}')
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
HTML_IMG_RE = re.compile(r'<img\b[^>]*src=["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)
PRE_RE = re.compile(r'<pre class=["\'](?:codeinput|language-matlab)["\']>(.*?)</pre>', re.DOTALL)
CODEOUTPUT_RE = re.compile(r'<pre class=["\']codeoutput["\']>(.*?)</pre>', re.DOTALL)
HTML_TAG_RE = re.compile(r"<[^>]+>")


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}, text

    raw = match.group(1).strip()
    body = text[match.end() :]
    metadata: dict[str, str] = {}

    for key in ("title", "subtitle", "summary", "permalink"):
        key_match = re.search(rf"\b{key}\s*:\s*([^,\n}}]+)", raw)
        if key_match:
            metadata[key] = key_match.group(1).strip().strip('"\'')

    return metadata, body


def label_from_metadata(metadata: dict[str, str], fallback: str) -> str:
    value = metadata.get("permalink") or fallback
    return value.strip().replace("_", "-").replace("/", "-")


def title_from_metadata(metadata: dict[str, str], fallback: str) -> str:
    return metadata.get("title") or fallback.replace("_", " ").replace(".", ".")


def build_permalink_map() -> dict[str, str]:
    mapping: dict[str, str] = {}

    candidates = []
    for source_dir in COLLECTIONS:
        candidates.extend(source_dir.glob("*.md"))
    candidates.extend(OLD_ROOT.glob("*.md"))

    for path in candidates:
        metadata, _ = parse_front_matter(path.read_text())
        permalink = metadata.get("permalink")
        if permalink:
            mapping[permalink] = label_from_metadata(metadata, path.stem)

    mapping.update(
        {
            "SWclass": "spinw-class",
            "SWproperties": "class-properties",
            "installation": "installation",
            "tutorials": "tutorials",
            "spinw": "spinw",
            "swfiles": "swfiles",
            "swplot": "swplot",
            "swpref": "swpref",
            "swsym": "swsym",
        }
    )
    return mapping


def image_include_to_myst(match: re.Match[str]) -> str:
    attrs = dict(re.findall(r'(\w+)=["\']([^"\']+)["\']', match.group(1)))
    file_name = attrs.get("file", "")
    alt = attrs.get("alt", "")
    if file_name.startswith("generated/"):
        path = f"/_static/img/{file_name}"
    elif file_name:
        path = f"/_static/img/{file_name.lstrip('/')}"
    else:
        path = ""
    return f"```{{image}} {path}\n:alt: {alt}\n```"


def html_img_to_myst(match: re.Match[str], tutorial_name: str | None) -> str:
    src = match.group(1)
    alt_match = re.search(r'alt=["\']([^"\']*)["\']', match.group(0), re.IGNORECASE)
    alt = alt_match.group(1) if alt_match else ""

    if src.startswith("/img/"):
        path = "/_static/img/" + src.removeprefix("/img/")
    elif src.startswith("/") and tutorial_name:
        path = f"/_static/img/tutorials/{tutorial_name}/{src.lstrip('/')}"
    elif tutorial_name and not re.match(r"[a-z]+://", src):
        path = f"/_static/img/tutorials/{tutorial_name}/{src}"
    else:
        path = src

    return f"```{{image}} {path}\n:alt: {alt}\n```"


def clean_matlab_html(text: str) -> str:
    text = re.sub(r"<span class=[\"'](?:string|keyword|comment)[\"']>(.*?)</span>", r"\1", text, flags=re.DOTALL)
    text = text.replace("&times;", "x").replace("&reg;", "®").replace("&amp;", "&")
    return HTML_TAG_RE.sub("", text).strip()


def convert_pre_blocks(text: str) -> str:
    text = PRE_RE.sub(lambda m: f"```matlab\n{clean_matlab_html(m.group(1))}\n```", text)
    text = CODEOUTPUT_RE.sub(lambda m: f"```text\n{clean_matlab_html(m.group(1))}\n```", text)
    return text


def rewrite_link_target(target: str, mapping: dict[str, str]) -> str:
    if re.match(r"(?:[a-z]+:|#)", target) or target.startswith("mailto:"):
        return target

    if target.startswith("/"):
        normalized = target.strip("/")
        if "#" in normalized:
            page, anchor = normalized.split("#", 1)
            label = mapping.get(page, page.replace("_", "-").lower())
            return f"#{label}-{anchor.replace('_', '-').lower()}"
        return mapping.get(normalized, target)

    if target in mapping:
        return f"#{mapping[target]}"

    return target


def rewrite_links(text: str, mapping: dict[str, str]) -> str:
    def replace(match: re.Match[str]) -> str:
        label = match.group(1)
        target = match.group(2)
        return f"[{label}]({rewrite_link_target(target, mapping)})"

    return LINK_RE.sub(replace, text)


def convert_text(path: Path, target_stem: str, mapping: dict[str, str], tutorial_name: str | None = None) -> str:
    metadata, body = parse_front_matter(path.read_text())
    label = label_from_metadata(metadata, target_stem)
    title = title_from_metadata(metadata, target_stem)

    body = re.sub(r"{%\s*include\s+links\.html\s*%}", "", body)
    body = IMAGE_INCLUDE_RE.sub(image_include_to_myst, body)
    body = HTML_IMG_RE.sub(lambda m: html_img_to_myst(m, tutorial_name), body)
    body = convert_pre_blocks(body)
    body = re.sub(r'<div id=["\']toc["\']></div>', "", body)
    body = re.sub(r"<script\b.*?</script>", "", body, flags=re.DOTALL | re.IGNORECASE)
    body = body.replace('<h1 class="text-center">Have fun!</h1>', '# Have fun!')
    body = rewrite_links(body, mapping)
    body = body.strip()

    return f"({label})=\n\n# {title}\n\n{body}\n"


def convert_collections(mapping: dict[str, str]) -> None:
    for source_dir, target_dir in COLLECTIONS.items():
        target_dir.mkdir(parents=True, exist_ok=True)
        for source in sorted(source_dir.glob("*.md")):
            target = target_dir / source.name
            target.write_text(convert_text(source, source.stem, mapping))


def convert_tutorials(mapping: dict[str, str]) -> None:
    target_dir = ROOT / "docs" / "spinw" / "tutorials"
    target_dir.mkdir(parents=True, exist_ok=True)
    for tutorial_dir in sorted(TUTORIALS.glob("tutorial*")):
        sources = sorted(tutorial_dir.glob("*tutorial.md"))
        if not sources:
            continue
        source = sources[0]
        target = target_dir / f"{tutorial_dir.name}.md"
        target.write_text(convert_text(source, tutorial_dir.name, mapping, tutorial_dir.name))


def main() -> None:
    parser = argparse.ArgumentParser(description="Migrate SpinW Jekyll Markdown to MyST Markdown.")
    parser.add_argument("--collections", action="store_true", help="Convert reference and overview collections.")
    parser.add_argument("--tutorials", action="store_true", help="Convert tutorial pages.")
    args = parser.parse_args()

    mapping = build_permalink_map()

    if args.collections:
        convert_collections(mapping)
    if args.tutorials:
        convert_tutorials(mapping)
    if not args.collections and not args.tutorials:
        parser.error("choose at least one of --collections or --tutorials")


if __name__ == "__main__":
    main()
