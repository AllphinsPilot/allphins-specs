#!/usr/bin/env bash
#
# Build the markdown body for a "spec run" tracking issue.
#
# Prints the issue body to stdout. Includes only specs whose front-matter
# `status` is `reviewed` or `active` (draft specs are excluded by design).
# Each spec is a link to its file with nested pass/fail checkboxes:
#
#   ## Authentication
#   - [AUTH-001](specs/auth/AUTH-001.md) — A user with valid credentials can sign in
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

# Human display name for an area: the H1 of its index.md, else the slug.
area_name() { # <area>
  local idx="$SPECS/$1/index.md" h
  if [ -f "$idx" ]; then
    h="$(grep -m1 '^# ' "$idx" || true)"
    if [ -n "$h" ]; then printf '%s' "${h#\# }"; return; fi
  fi
  printf '%s' "$1"
}

# Curated area order from the root index, then any remaining areas appended.
ordered_areas() {
  local order="" a d
  if [ -f "$SPECS/index.md" ]; then
    order="$(grep -oE '\]\([a-z0-9-]+/\)' "$SPECS/index.md" \
      | sed -E 's/^\]\(([a-z0-9-]+)\/\)$/\1/')"
  fi
  local result=""
  for a in $order; do
    [ -d "$SPECS/$a" ] && result="$result $a"
  done
  for d in "$SPECS"/*/; do
    a="$(basename "$d")"
    case " $result " in *" $a "*) ;; *) result="$result $a" ;; esac
  done
  printf '%s' "$result"
}

body=""
eligible=0

for area in $(ordered_areas); do
  section=""
  for f in "$SPECS/$area"/*.md; do
    [ -e "$f" ] || continue
    [ "$(basename "$f")" = "index.md" ] && continue
    status="$(fm_value "$f" status)"
    case "$status" in
      reviewed | active) ;;
      *) continue ;;
    esac
    id="$(basename "$f" .md)"
    title="$(strip_quotes "$(fm_value "$f" title)")"
    section="$section- [$id](specs/$area/$id.md) — $title
  - [ ] pass
  - [ ] fail
"
    eligible=$((eligible + 1))
  done
  if [ -n "$section" ]; then
    body="$body## $(area_name "$area")
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
