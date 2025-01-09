from re import Match

from SublimeLinter.lint import NodeLinter
from SublimeLinter.lint.linter import LintMatch


class oxlint(NodeLinter):
    defaults = {
        "selector": "source.js"
    }

    cmd = "oxlint --format=unix"

    regex = (
        r"(?P<filename>\w+\.\w+):"
        r"(?P<line>\d+):"
        r"(?P<col>\d+):"
        r"\s*(?P<message>[\w\s\.\-\=]+\.?)"
        r"\s*\[(?P<warning>Warning)?(?P<error>Error)?/"
        r"(?P<code>.+)]"
    )

    def split_match(self, match: Match) -> LintMatch:
        groupdict = match.groupdict()

        print(groupdict)

        return super().split_match(match)
