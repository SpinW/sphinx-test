
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
PLAIN_PRE_RE = re.compile(r'<pre(?:\s[^>]*)?>(.*?)</pre>', re.DOTALL)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
HTML_TAG_RE = re.compile(r"<[^>]+>")
HEADING_RE = re.compile(r'<h([1-6])\b[^>]*>(.*?)</h\1>', re.DOTALL | re.IGNORECASE)
PARA_RE = re.compile(r"<p\b[^>]*>(.*?)</p>", re.DOTALL | re.IGNORECASE)
LIST_RE = re.compile(r"<ul\b[^>]*>(.*?)</ul>", re.DOTALL | re.IGNORECASE)
LIST_ITEM_RE = re.compile(r"<li\b[^>]*>(.*?)</li>", re.DOTALL | re.IGNORECASE)
ANCHOR_RE = re.compile(r'<a\b[^>]*>(.*?)</a>', re.DOTALL | re.IGNORECASE)


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


ENTITY_REPLACEMENTS = (
    ("\u0026amp;", "&"),
    ("\u0026lt;", "<"),
    ("\u0026gt;", ">"),
    ("\u0026quot;", '"'),
    ("\u0026#39;", "'"),
    ("\u0026times;", "x"),
    ("\u0026reg;", "\u00ae"),
)


def unescape_html_entities(text: str) -> str:
    for entity, char in ENTITY_REPLACEMENTS:
        text = text.replace(entity, char)
    return text


def clean_matlab_html(text: str) -> str:
    text = re.sub(r"<span class=[\"'](?:string|keyword|comment)[\"']>(.*?)</span>", r"\1", text, flags=re.DOTALL)
    text = unescape_html_entities(text)
    return HTML_TAG_RE.sub("", text).strip()


def clean_inline_html(text: str) -> str:
    text = ANCHOR_RE.sub(lambda m: m.group(1).strip(), text)
    text = re.sub(r"</?(?:b|strong)>", "**", text, flags=re.IGNORECASE)
    text = re.sub(r"</?(?:i|em)>", "*", text, flags=re.IGNORECASE)
    text = re.sub(r"<code>(.*?)</code>", r"`\1`", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<br\s*/?>", " ", text, flags=re.IGNORECASE)
    text = HTML_TAG_RE.sub("", text)
    text = unescape_html_entities(text)
    return re.sub(r"\s+", " ", text).strip()


def list_to_markdown(match: re.Match[str]) -> str:
    items = LIST_ITEM_RE.findall(match.group(1))
    lines = [f"- {clean_inline_html(item)}" for item in items]
    return "\n" + "\n".join(lines) + "\n"


def heading_to_markdown(match: re.Match[str]) -> str:
    level = int(match.group(1))
    text = clean_inline_html(match.group(2))
    if not text:
        return ""
    # Demote the top-level tutorial heading so the page keeps a single H1.
    prefix = "#" * max(level + 1, 2)
    return f"\n\n{prefix} {text}\n\n"


def convert_pre_blocks(text: str) -> str:
    text = PRE_RE.sub(lambda m: f"\n\n```matlab\n{clean_matlab_html(m.group(1))}\n```\n\n", text)
    text = CODEOUTPUT_RE.sub(lambda m: f"\n\n```text\n{clean_matlab_html(m.group(1))}\n```\n\n", text)
    return text


def convert_tutorial_html(body: str) -> str:
    # Remove trailing MATLAB source export and other HTML comments.
    body = HTML_COMMENT_RE.sub("", body)
    # Drop the auto-generated "Contents" navigation block.
    body = re.sub(
        r"<h2[^>]*>\s*Contents\s*</h2>\s*<div>.*?</div>",
        "",
        body,
        flags=re.DOTALL | re.IGNORECASE,
    )
    # Code blocks first so their contents are not mangled by tag stripping.
    body = convert_pre_blocks(body)
    # Remaining plain <pre> blocks (e.g. the "Written by" footer).
    body = PLAIN_PRE_RE.sub(
        lambda m: f"\n\n```text\n{clean_matlab_html(m.group(1))}\n```\n\n", body
    )
    body = HEADING_RE.sub(heading_to_markdown, body)
    body = LIST_RE.sub(list_to_markdown, body)
    body = PARA_RE.sub(lambda m: f"\n\n{clean_inline_html(m.group(1))}\n\n", body)
    # Strip remaining structural tags such as <div>/<span>.
    body = re.sub(r"</?(?:div|span)[^>]*>", "", body, flags=re.IGNORECASE)
    body = HTML_TAG_RE.sub("", body)
    body = unescape_html_entities(body)
    # Remove stray leading whitespace before MyST image fences.
    body = re.sub(r"(?m)^[ \t]+(```\{image\})", r"\1", body)
    # Ensure a blank line follows the closing image fence so trailing text is
    # not parsed as directive content ("Has content, but none permitted").
    body = re.sub(r"(?m)^(```\{image\}[^\n]*\n(?::[^\n]*\n)*```)\n(?=\S)", r"\1\n\n", body)
    # Collapse excessive blank lines.
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


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


def promote_collection_headings(body: str) -> str:
    """Normalise markdown headings so they nest under the prepended page H1.

    Collection source pages take their title from front matter and start their
    body sections at deeper levels (``###`` or ``####``). After we prepend a
    ``#`` page title this creates a non-consecutive H1 -> H3/H4 jump. Shift the
    whole heading tree so the shallowest body heading becomes H2 while keeping
    the relative nesting intact.
    """

    heading_re = re.compile(r"(?m)^(#{1,6})(\s)")
    fence_re = re.compile(r"(?m)^(```|~~~).*?^\1\s*$", re.DOTALL)

    # Mask fenced code blocks so ``#`` lines inside them are not treated as
    # headings (e.g. shell comments such as ``## TEST DATA``).
    spans = [m.span() for m in fence_re.finditer(body)]

    def in_code(pos: int) -> bool:
        return any(start <= pos < end for start, end in spans)

    levels = [len(m.group(1)) for m in heading_re.finditer(body) if not in_code(m.start())]
    if not levels:
        return body

    shift = 2 - min(levels)
    if shift == 0:
        return body

    def adjust(match: re.Match[str]) -> str:
        if in_code(match.start()):
            return match.group(0)
        level = min(max(len(match.group(1)) + shift, 2), 6)
        return "#" * level + match.group(2)

    return heading_re.sub(adjust, body)


def convert_text(path: Path, target_stem: str, mapping: dict[str, str], tutorial_name: str | None = None) -> str:
    metadata, body = parse_front_matter(path.read_text())
    label = label_from_metadata(metadata, target_stem)
    title = title_from_metadata(metadata, target_stem)

    body = re.sub(r"{%\s*include\s+links\.html\s*%}", "", body)
    body = IMAGE_INCLUDE_RE.sub(image_include_to_myst, body)
    body = HTML_IMG_RE.sub(lambda m: html_img_to_myst(m, tutorial_name), body)
    if tutorial_name:
        body = convert_tutorial_html(body)
    else:
        body = convert_pre_blocks(body)
    body = re.sub(r'<div id=["\']toc["\']></div>', "", body)
    body = re.sub(r"<script\b.*?</script>", "", body, flags=re.DOTALL | re.IGNORECASE)
    body = body.replace('<h1 class="text-center">Have fun!</h1>', '# Have fun!')
    body = rewrite_links(body, mapping)
    if not tutorial_name:
        body = promote_collection_headings(body)
    body = body.strip()

    return f"({label})=\n\n# {title}\n\n{body}\n"


def convert_collections(mapping: dict[str, str]) -> None:
    for source_dir, target_dir in COLLECTIONS.items():
        target_dir.mkdir(parents=True, exist_ok=True)
        for source in sorted(source_dir.glob("*.md")):
            target = target_dir / source.name
            target.write_text(convert_text(source, source.stem, mapping))


def _tutorial_sort_key(name: str) -> tuple[int, str]:
    """Sort tutorialNN names by their numeric index when possible."""
    m = re.match(r"tutorial(\d+)", name)
    if m:
        return (int(m.group(1)), name)
    return (10**9, name)


def write_tutorials_index() -> None:
    """Generate docs/spinw/tutorials.md with a rich title+subtitle list.

    Mirrors the legacy Jekyll ``tutorials.md`` which iterated over
    ``site.tutorials`` and rendered each entry as a clickable title followed by
    its subtitle. We keep an additional hidden ``toctree`` so Sphinx's sidebar
    and prev/next navigation still works.
    """
    entries: list[tuple[str, str, str]] = []  # (slug, title, subtitle)
    for tutorial_dir in sorted(TUTORIALS.glob("tutorial*"), key=lambda p: _tutorial_sort_key(p.name)):
        sources = sorted(tutorial_dir.glob("*tutorial.md"))
        if not sources:
            continue
        metadata, _ = parse_front_matter(sources[0].read_text())
        title = metadata.get("title") or tutorial_dir.name
        subtitle = metadata.get("subtitle", "").strip()
        entries.append((tutorial_dir.name, title, subtitle))

    lines: list[str] = []
    lines.append("(tutorials)=")
    lines.append("")
    lines.append("# Tutorials")
    lines.append("")
    lines.append(
        "These tutorials can help to understand quickly how SpinW works. "
        "It is possible to download the MATLAB code of any tutorial using the "
        "`grabcode` command with the tutorial URL."
    )
    lines.append("")
    lines.append("```{toctree}")
    lines.append(":maxdepth: 1")
    lines.append(":hidden:")
    lines.append(":glob:")
    lines.append("")
    lines.append("tutorials/tutorial*")
    lines.append("```")
    lines.append("")
    for slug, title, subtitle in entries:
        if subtitle:
            lines.append(f"- [{title}](tutorials/{slug}) — {subtitle}")
        else:
            lines.append(f"- [{title}](tutorials/{slug})")
    lines.append("")

    target = ROOT / "docs" / "spinw" / "tutorials.md"
    target.write_text("\n".join(lines).rstrip() + "\n")


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
    write_tutorials_index()


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
