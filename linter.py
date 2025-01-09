from re import Match
from typing import Iterator

from SublimeLinter.lint import NodeLinter
from SublimeLinter.lint.linter import LintMatch


class oxlint(NodeLinter):
    defaults = {
        "selector": "source.(js|ts)"
    }

    cmd = "oxlint --jsdoc-plugin --jsx-a11y-plugin --format=unix \"$file\""

    regex = (
        r"(?P<filename>[\w\\\-]+\.\w+):"
        r"(?P<line>\d+):"
        r"(?P<col>\d+):"
        r"\s*(?P<message>[\w\s\.\-\=\"\'\?\(\)\`\:\/@]+\.?)"
        r"\s*\[(?P<warning>Warning)?(?P<error>Error)?/?"
        r"(?P<code>.+)]"
    )

    def find_errors(self, output: str) -> Iterator[LintMatch]:
        print(output)

        return super().find_errors(output)

    def split_match(self, match: Match) -> LintMatch:
        groupdict = match.groupdict()

        print(groupdict)

        return super().split_match(match)
