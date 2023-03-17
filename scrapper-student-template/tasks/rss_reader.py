from argparse import ArgumentParser
from typing import List, Optional, Sequence
import requests
import xml.etree.ElementTree as ET
import json


class UnhandledException(Exception):
    pass


def rss_parser(
    xml: str,
    limit: Optional[int] = None,
    json_output: bool = False,
) -> List[str]:
    """
    RSS parser.

    Args:
        xml: XML document as a string.
        limit: Number of the news to return. if None, returns all news.
        json_output: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as a separate lines.

    Examples:
        >>> xml = '<rss><channel><title>Some RSS Channel</title><link>https://some.rss.com</link><description>Some RSS Channel</description></channel></rss>'
        >>> rss_parser(xml)
        ["Feed: Some RSS Channel",
        "Link: https://some.rss.com"]
        >>> print("\\n".join(rss_parser(xml)))
        Feed: Some RSS Channel
        Link: https://some.rss.com
    """
    root = ET.fromstring(xml)
    items = root.findall("./channel/item")
    if limit is not None:
        items = items[:limit]

    result = []
    for item in items:
        title = item.findtext("title")
        link = item.findtext("link")
        description = item.findtext("description")
        result.append(f"Title: {title}")
        result.append(f"Link: {link}")
        if description:
            result.append(f"Description: {description}")
        result.append("")

    if json_output:
        output_dict = {
            "feed": root.findtext("./channel/title"),
            "link": root.findtext("./channel/link"),
            "description": root.findtext("./channel/description"),
            "items": [{"title": item.findtext("title"), "link": item.findtext("link"), "description": item.findtext("description")} for item in items]
        }
        return [json.dumps(output_dict)]

    return result


def main(argv: Optional[Sequence] = None):
    """
    The main function of your task.
    """
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)
    xml = requests.get(args.source).text
    try:
        print("\n".join(rss_parser(xml, args.limit, args.json)))
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()
