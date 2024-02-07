from __future__ import annotations

from typing import List

import requests
from bs4 import BeautifulSoup
from bs4 import Tag
from requests import Response


def main() -> None:
    url: str = "https://learn.microsoft.com/en-us/dotnet/api/system.array"

    response: Response = requests.get(url)
    if response.status_code == 200:
        soup: BeautifulSoup = BeautifulSoup(response.content, "html.parser")
        # print(soup.prettify())

        content: Tag = soup.find("div", "content")

        title_tag: Tag = content.find("h1")
        title: str = title_tag.string.replace(" Class", "")
        print(title)

        class_desc_tag: Tag = content.find("div", "summary clearFix")
        class_desc: str = "".join(map(str, class_desc_tag.p.contents))
        print(class_desc)

        remarks_tag: Tag = content.find("h2", id="remarks")
        remarks_paragraphs: List[str] = []
        tag: Tag
        for tag in remarks_tag.find_all_next():
            if tag.name == "p":
                remarks_paragraphs.append("".join(tag.strings))
            elif tag.name in ("h2", "h3"):
                break
        remarks: str = "\n".join(remarks_paragraphs)
        print(remarks)

    # https://learn.microsoft.com/en-us/dotnet/api/system.array.binarysearch#system-array-binarysearch(system-array-system-int32-system-int32-system-object-system-collections-icomparer)


if __name__ == "__main__":
    main()
