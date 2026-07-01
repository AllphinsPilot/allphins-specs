#!/usr/bin/env bash
#
# Build the markdown body for a "spec run" tracking issue.
#
# Prints the issue body to stdout. Includes only specs whose front-matter
# `status` is `reviewed` or `active` (draft specs are excluded by design).
# Each spec is a link to its file with nested pass/fail checkboxes:
#
#   ## User Management
#   - [USER-001](specs/user-management/USER-001_sign-in-with-valid-credentials.md) — A user with valid credentials can sign in
#     - [ ] pass
#     - [ ] fail
#
# Neither box ticked = not yet executed. Exits 1 (with a message on stderr)
# if no eligible specs exist, so the calling workflow fails loudly.
#
# Usage: .github/scripts/build_run_issue.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SPECS="$ROOT/specs"

# Read a single front-matter scalar (first match, between the first two `---`).
fm_value() { # <file> <key>
  awk -v key="$2" '
    /^---[[:space:]]*$/ { d++; next }
    d == 1 && index($0, key ":") == 1 {
      v = $0; sub("^" key ":[[:space:]]*", "", v); print v; exit
    }
  ' "$1"
}

# Strip one matching pair of surrounding single or double quotes.
strip_quotes() { # <value>
  local v="$1" q
  if [ ${#v} -ge 2 ]; then
    q="${v%"${v#?}"}"           # first char
    if [ "$q" = '"' ] || [ "$q" = "'" ]; then
      if [ "${v#"${v%?}"}" = "$q" ]; then  # last char == first char
        v="${v#?}"; v="${v%?}"
      fi
    fi
  fi
  printf '%s' "$v"
}

# Leaf areas: directories (relative to specs/) that directly hold a non-index spec.
leaf_areas() {
  find "$SPECS" -type f -name '*.md' ! -name index.md -print \
    | while IFS= read -r f; do d="$(dirname "$f")"; printf '%s\n' "${d#"$SPECS"/}"; done \
    | sort -u
}

# Pretty header for an area path: "book/risks" -> "Book / Risks".
area_header() { # <area-path>
  printf '%s' "$1" | awk -F/ '{
    out=""
    for (i=1;i<=NF;i++) {
      s=$i; gsub(/-/," ",s)
      n=split(s,w," "); seg=""
      for (j=1;j<=n;j++) seg=seg (j>1?" ":"") toupper(substr(w[j],1,1)) substr(w[j],2)
      out=out (i>1?" / ":"") seg
    }
    printf "%s", out
  }'
}

body=""
eligible=0

for area in $(leaf_areas); do
  section=""
  for f in "$SPECS/$area"/*.md; do
    [ -e "$f" ] || continue
    [ "$(basename "$f")" = "index.md" ] && continue
    status="$(fm_value "$f" status)"
    case "$status" in
      reviewed | active) ;;
      *) continue ;;
    esac
    fname="$(basename "$f")"
    # File is `<ID>_<slug>.md`; show the ID, link the real file.
    id="${fname%%_*}"; id="${id%.md}"
    title="$(strip_quotes "$(fm_value "$f" title)")"
    section="$section- [$id](specs/$area/$fname) — $title
  - [ ] pass
  - [ ] fail
"
    eligible=$((eligible + 1))
  done
  if [ -n "$section" ]; then
    body="$body## $(area_header "$area")
$section
"
  fi
done

if [ "$eligible" -eq 0 ]; then
  echo "No specs with status 'reviewed' or 'active' to run." >&2
  echo "Flip specs from draft to reviewed first (e.g. ./set-spec-status.local.sh reviewed)." >&2
  exit 1
fi

printf '%s\n\n%s\n' \
  "Tick **pass** or **fail** per spec. Neither ticked = not yet executed." \
  "$body"
